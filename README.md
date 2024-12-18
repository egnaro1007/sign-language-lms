# Hệ Thống Quản Lý Học Ngôn Ngữ Ký Hiệu (LMS)
Dự án trang web hỗ trợ học ngôn ngữ ký hiệu dành cho người khiếm thính, cung cấp các tính năng học tập tương tác như flashcard học tập, bài tập thực hành và luyện tập sử dụng model nhận dạng thủ ngữ.

## 🛠️ Công Nghệ Sử Dụng 
- Frontend: SvelteKit. Framework hiện đại giúp phát triển giao diện nhanh và hiệu quả.
- SCSS: Hỗ trợ viết CSS dễ bảo trì và mở rộng.
- Axios: Giao tiếp API giữa frontend và backend.
- Backend:Django. Framework mạnh mẽ để phát triển backend và xây dựng API.
- Cơ Sở Dữ Liệu: SQLite (phát triển): Cơ sở dữ liệu nhẹ cho môi trường phát triển.
- PostgreSQL (sản phẩm): Cơ sở dữ liệu mạnh mẽ cho triển khai thực tế.

## 🚀 Cài Đặt Dự Án
### Frontend
- Chuyển đến thư mục:  
`cd front-end`  
- Cài đặt các thư viện cần thiết:  
`npm install`  
- Chạy server:  
`npm run dev`  
- Truy cập frontend tại cổng 5173

### Backend (dữ liệu bài học)
- Chuyển đến thư mục:  
`cd videototext-back-end`  
- Tạo và kích hoạt môi trường ảo:  
`python -m venv venv`  
`source venv/bin/activate` (Linux/Mac) hoặc `venv\Scripts\activate` (Windows)  
- Cài đặt các thư viện cần thiết:  
`pip install -r requirements.txt`  
- Chạy server:  
`python manage.py runserver`  
- Truy cập tại cổng 8000

### Backend (nhận dạng thủ ngữ)
- Chuyển đến thư mục:  
`cd videototext-back-end`  
- Tạo và kích hoạt môi trường ảo:  
`python -m venv venv`  
`source venv/bin/activate` (Linux/Mac) hoặc `venv\Scripts\activate` (Windows)  
- Cài đặt các thư viện cần thiết:  
`pip install -r requirements.txt`  
- Chạy server:  
`uvicorn main:app --port 8001`  
- Truy cập tại cổng 8001

## 📸 Hình Ảnh Minh Họa
![image](images/image1.png)
![image](images/image2.png)
![image](images/image3.png)
![image](images/image4.png)
