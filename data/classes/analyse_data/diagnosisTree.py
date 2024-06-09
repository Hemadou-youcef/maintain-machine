import data.classes.analyse_data.solutions.first_solution as first_solution
class DiagnosisTree:
    def __init__(self, part_name):
        self.part_name = part_name
        self.failure_data = None
        self.solutions = {
            "feeder": {
                "Components Purged": [
                    first_solution.SolutionContent(),
                    first_solution.SolutionContent()
                ],
                "Part Sense Failures": [
                    first_solution.SolutionContent(),
                    first_solution.SolutionContent()
                ],
                "Mispicks": [
                    first_solution.SolutionContent(),
                    first_solution.SolutionContent()
                ],
                "Pick Attempts From Empty Feeders": [
                    first_solution.SolutionContent(),
                    first_solution.SolutionContent()
                ],
                "Rejected": [
                    first_solution.SolutionContent(),
                    first_solution.SolutionContent()
                ],
                "Location Failures": [
                    first_solution.SolutionContent(),
                    first_solution.SolutionContent()
                ],
                "Components Upside Down": [
                    first_solution.SolutionContent(),
                    first_solution.SolutionContent()
                ],
                "VPS Part Presence Failures": [
                    first_solution.SolutionContent(),
                    first_solution.SolutionContent()
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