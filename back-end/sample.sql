INSERT INTO shuffle_sentence (sentence, language_id) 
VALUES ('Tôi thường dành thời gian buổi sáng để đọc sách và học tiếng Việt.', 'vi');

INSERT INTO shuffle_subsequence (sentence_id, sequence_id, text) 
VALUES 
    (1, 1, 'tôi thường dành'),
    (1, 2, 'thời gian buổi sáng'),
    (1, 3, 'để'),
    (1, 4, 'đọc sách'),
    (1, 5, 'và'),
    (1, 6, 'học tiếng việt');



INSERT INTO shuffle_sentence (sentence, language_id) 
VALUES ('Mặc dù trời mưa to, tôi vẫn quyết định đi bộ đến công ty.', 'vi');

INSERT INTO shuffle_subsequence (sentence_id, sequence_id, text) 
VALUES 
    (2, 1, 'Mặc dù'),
    (2, 2, 'trời mưa to,'),
    (2, 3, 'tôi vẫn quyết định'),
    (2, 4, 'đi bộ'),
    (2, 5, 'đến công ty.');