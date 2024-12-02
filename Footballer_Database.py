class Footballer_Database:
    def __init__(self):
        self.footballer_database = []
        
    def add_footballer(self, footballer):
        self.footballer_database.append(footballer)
        
    def remove_footballer(self, footballer):
        self.footballer_database.remove(footballer)
        
    def search_footballer_index(self, footballer):
        i = 0
        for f in self.footballer_database:
            if f == footballer:
                return i
            i += 1
            
    def pos_is_created(self, position):
        for f in self.footballer_database:
            if f.pos == position:
                return True
        return False

    def name_is_created(self, name):
        for f in self.footballer_database:
            if f.name == name:
                return True
        return False
    
