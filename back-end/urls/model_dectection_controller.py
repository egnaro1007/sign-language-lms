from fastapi import APIRouter, UploadFile
import pickle
import cv2
import mediapipe as mp
import numpy as np

# Router cho việc detect ký hiệu ngôn ngữ
sign_language_detection_router = APIRouter(
    prefix="/model_detection",
    tags=["model_detection"],
)

# Load mô hình
model_dict = pickle.load(open('./model_checkpoint/model.p', 'rb'))
model = model_dict['model']

# Labels cho các ký hiệu
labels_dict = {0: 'hello', 1: 'iloveyou', 2: 'no', 3: 'yes'}

# Mediapipe khởi tạo
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
hands = mp_hands.Hands(static_image_mode=True, min_detection_confidence=0.3)


@sign_language_detection_router.post("/detect")
async def detect_sign_language(file: UploadFile):
    """
    Nhận file hình ảnh và trả về ký hiệu ngôn ngữ dự đoán
    """
    try:
        # Đọc file upload
        contents = await file.read()
        nparr = np.frombuffer(contents, np.uint8)
        frame = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

        # Chuyển ảnh sang RGB để dùng Mediapipe
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Phân tích landmarks bằng Mediapipe
        results = hands.process(frame_rgb)
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                data_aux = []
                x_ = []
                y_ = []

                for i in range(len(hand_landmarks.landmark)):
                    x = hand_landmarks.landmark[i].x
                    y = hand_landmarks.landmark[i].y

                    x_.append(x)
                    y_.append(y)

                for i in range(len(hand_landmarks.landmark)):
                    x = hand_landmarks.landmark[i].x
                    y = hand_landmarks.landmark[i].y
                    data_aux.append(x - min(x_))
                    data_aux.append(y - min(y_))

               # Dự đoán ký hiệu ngôn ngữ
            prediction = model.predict([np.asarray(data_aux)])
            predicted_character = prediction[0]  # Trả về trực tiếp nếu đã là nhãn
            return {"sign_language": predicted_character}

        else:
            return {"error": "No hand landmarks detected."}
    except Exception as e:
        return {"error": str(e)}
