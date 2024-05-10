import os

class StateManager:
    def __init__(self):
        self.state = {
            "path": os.getcwd(),
            "title": "App",
            "file_data": None,
            "current_view_widget": []
            
        }

    def set_state(self, key, value):
        self.state[key] = value

    def get_state(self, key):
        return self.state.get(key)

    def remove_state(self, key):
        if key in self.state:
            del self.state[key]

    def clear_state(self):
        self.state = {
            "path": os.getcwd(),
            "title": "App",
            "file_data": None,
            "current_view_widget": []
        }
        
