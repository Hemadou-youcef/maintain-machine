class DiagnosisTree:
    def __init__(self, part_name):
        self.part_name = part_name
        self.failure_data = None
        self.solutions = {
            "feeder": {
                "Components Purged": [
                    {"name": "Feeder Solution 1", "description": "Description of feeder solution 1", "image": "/assets/images/image1.png"},
                    {"name": "Feeder Solution 2", "description": "Description of feeder solution 2", "image": "/assets/images/image2.png"},
                ],
                "Part Sense Failures": [
                    {"name": "Feeder Solution 1", "description": "Description of feeder solution 1", "image": "/assets/images/image3.png"},
                    {"name": "Feeder Solution 2", "description": "Description of feeder solution 2", "image": "/assets/images/image4.png"},
                ],
                "Mispicks": [
                    {"name": "Feeder Solution 1", "description": "Description of Feeder solution 1", "image": "/assets/images/image5.png"},
                    {"name": "Feeder Solution 2", "description": "Description of Feeder solution 2", "image": "/assets/images/image6.png"},
                ],
                "Pick Attempts From Empty Feeders": [
                    {"name": "Feeder Solution 1", "description": "Description of Feeder solution 1", "image": "/assets/images/image7.png"},
                    {"name": "Feeder Solution 2", "description": "Description of Feeder solution 2", "image": "/assets/images/image8.png"},
                ],
                "Rejected": [
                    {"name": "Feeder Solution 1", "description": "Description of Feeder solution 1", "image": "/assets/images/image9.png"},
                    {"name": "Feeder Solution 2", "description": "Description of Feeder solution 2", "image": "/assets/images/image10.png"},
                ],
                "Location Failures": [
                    {"name": "Feeder Solution 1", "description": "Description of Feeder solution 1", "image": "/assets/images/image11.png"},
                    {"name": "Feeder Solution 2", "description": "Description of Feeder solution 2", "image": "/assets/images/image12.png"},
                ],
                # Add other feeder failure types and their solutions here...
            },
            "nozzle": {
                
                # Add other nozzle failure types and their solutions here...
            },
            "spindle": {
                
                # Add other spindle failure types and their solutions here...
            }
        }

    def load_failure_data(self, df):
        self.failure_data = df

    def get_solution(self, failure_type):
        if self.part_name in self.solutions and failure_type in self.solutions[self.part_name]:
            return self.solutions[self.part_name][failure_type]
        else:
            return None