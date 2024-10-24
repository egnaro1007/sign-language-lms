CREATE TABLE language (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    code VARCHAR(10) NOT NULL UNIQUE,
    language VARCHAR(255) NOT NULL
);

CREATE TABLE shuffle_sentence (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    sentence TEXT NOT NULL,
    language_id INT,
    FOREIGN KEY (language_id) REFERENCES language(id) ON DELETE SET NULL
);

CREATE TABLE shuffle_subsequence (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    sentence_id INT NOT NULL,
    sequence_id INT NOT NULL,
    text TEXT NOT NULL,
    FOREIGN KEY (sentence_id) REFERENCES shuffle_sentence(id) ON DELETE CASCADE
);

