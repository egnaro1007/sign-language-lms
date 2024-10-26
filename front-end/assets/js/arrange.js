let currentQuestion = 0;
let selectedAnswers = [];

 const sampleData = [
        {
            0: {
            1: "to",
            2: "work", 
            3: "have",
            4: "I"
            },
            1: {
            1: "I",
            2: "have",
            3: "to",
            4: "work",
            }
        },

    ];
function loadQuestion() {
        const question = questionsData[currentQuestion];
        document.querySelector('.question-text').innerText = `Arrange the sentence:`;

        const questionContainer = document.getElementById('arrange__question');
        const answersContainer = document.getElementById('arrange__answer');
        
        choicesContainer.innerHTML = '';
        answersContainer.innerHTML = '';

        question.choices.forEach((choice, index) => {
            const choiceBox = document.createElement('div');
            choiceBox.classList.add('choice-box');
            choiceBox.innerText = choice;
            choiceBox.addEventListener('click', () => selectAnswer(choice, choiceBox));

            choicesContainer.appendChild(choiceBox);
        });

        // Tạo các ô trống cho đáp án
        question.answer.forEach(() => {
            const answerBox = document.createElement('div');
            answerBox.classList.add('answer-box');
            answersContainer.appendChild(answerBox);
        });


        selectedAnswers = [];
    }

    