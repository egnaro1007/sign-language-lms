from models import BaseModel
from database import Database


class ShuffleQuestion(BaseModel):
    sub_sequences = {}
    def __init__(self):
        self.db = Database()

    def add_subsequent(self, sequence_id, text):
        if sequence_id in self.sub_sequences:
            raise ValueError("Sequence ID already exists")
        self.sub_sequences[sequence_id] = text

    def get_subsequents(self):
        return self.sub_sequences
    
    def get_complete_sentence(self):
        # Retrieve and sort the keys
        sorted_keys = sorted(self.sub_sequences.keys())
        
        # Concatenate the values in order of the sorted keys
        complete_sentence = ''.join(self.sub_sequences[key] for key in sorted_keys)
        
        return complete_sentence
    
    def load_from_database(self, id): 
        # ID does not exist
        if self.db.fetch_one("SELECT 1 FROM shuffle_sentence WHERE id = ?", (id,)) is None:
            return None   

        rows = self.db.fetch_all("SELECT * FROM shuffle_subsequence WHERE sentence_id = ?", (id,))
        self.sub_sequences = {}
        for row in rows:
            self.add_subsequent(row[2], row[3])

    def load_random_from_database(self):
        random_id = self.db.fetch_one("SELECT id FROM shuffle_sentence ORDER BY RANDOM() LIMIT 1")
        
        if random_id is not None:
            self.load_from_database(random_id[0])

    def save_to_database(self, id):
        if self.db.fetch_one("SELECT 1 FROM shuffle_sentence WHERE id = ?", (id,)) is None:
            raise ValueError("ID does not exist")
        
        pass

