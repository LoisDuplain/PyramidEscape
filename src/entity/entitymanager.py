class EntityManager:

    def __init__(self):
        self.entities = []

    def get_entities(self):
        return self.entities

    def register_entity(self, entity):
        if entity in self.entities:
            return False
        else:
            self.entities.append(entity)
            return True
