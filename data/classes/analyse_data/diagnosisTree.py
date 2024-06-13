# feeder solutions
import data.classes.analyse_data.solutions.feeder.feeder_solution_1 as feeder_solution_1
import data.classes.analyse_data.solutions.feeder.feeder_solution_2 as feeder_solution_2
import data.classes.analyse_data.solutions.feeder.feeder_solution_3 as feeder_solution_3
import data.classes.analyse_data.solutions.feeder.feeder_solution_4 as feeder_solution_4
import data.classes.analyse_data.solutions.feeder.feeder_solution_5 as feeder_solution_5
import data.classes.analyse_data.solutions.feeder.feeder_solution_6 as feeder_solution_6
import data.classes.analyse_data.solutions.feeder.feeder_solution_7 as feeder_solution_7
import data.classes.analyse_data.solutions.feeder.feeder_solution_8 as feeder_solution_8


class DiagnosisTree:
    def __init__(self, part_name):
        self.part_name = part_name
        self.failure_data = None
        self.solutions = {
            "feeder": {
                "Components Purged": [
                    feeder_solution_1.SolutionContent(),
                    feeder_solution_2.SolutionContent(),
                    feeder_solution_3.SolutionContent(),
                    feeder_solution_4.SolutionContent(),
                    feeder_solution_5.SolutionContent(),
                    feeder_solution_6.SolutionContent(),
                    feeder_solution_7.SolutionContent(),
                    feeder_solution_8.SolutionContent(),
                ],
                "Part Sense Failures": [
                    feeder_solution_1.SolutionContent(),
                    feeder_solution_2.SolutionContent(),
                    feeder_solution_3.SolutionContent(),
                    feeder_solution_4.SolutionContent(),
                    feeder_solution_5.SolutionContent(),
                    feeder_solution_6.SolutionContent(),
                    feeder_solution_7.SolutionContent(),
                    feeder_solution_8.SolutionContent(),
                ],
                "Mispicks": [
                    feeder_solution_1.SolutionContent(),
                    feeder_solution_2.SolutionContent(),
                    feeder_solution_3.SolutionContent(),
                    feeder_solution_4.SolutionContent(),
                    feeder_solution_5.SolutionContent(),
                    feeder_solution_6.SolutionContent(),
                    feeder_solution_7.SolutionContent(),
                    feeder_solution_8.SolutionContent(),
                ],
                "Pick Attempts From Empty Feeders": [
                    feeder_solution_1.SolutionContent(),
                    feeder_solution_2.SolutionContent(),
                    feeder_solution_3.SolutionContent(),
                    feeder_solution_4.SolutionContent(),
                    feeder_solution_5.SolutionContent(),
                    feeder_solution_6.SolutionContent(),
                    feeder_solution_7.SolutionContent(),
                    feeder_solution_8.SolutionContent(),
                ],
                "Rejected": [
                    feeder_solution_1.SolutionContent(),
                    feeder_solution_2.SolutionContent(),
                    feeder_solution_3.SolutionContent(),
                    feeder_solution_4.SolutionContent(),
                    feeder_solution_5.SolutionContent(),
                    feeder_solution_6.SolutionContent(),
                    feeder_solution_7.SolutionContent(),
                    feeder_solution_8.SolutionContent(),
                ],
                "Location Failures": [
                    feeder_solution_1.SolutionContent(),
                    feeder_solution_2.SolutionContent(),
                    feeder_solution_3.SolutionContent(),
                    feeder_solution_4.SolutionContent(),
                    feeder_solution_5.SolutionContent(),
                    feeder_solution_6.SolutionContent(),
                    feeder_solution_7.SolutionContent(),
                    feeder_solution_8.SolutionContent(),
                ],
                "Components Upside Down": [
                    feeder_solution_1.SolutionContent(),
                    feeder_solution_2.SolutionContent(),
                    feeder_solution_3.SolutionContent(),
                    feeder_solution_4.SolutionContent(),
                    feeder_solution_5.SolutionContent(),
                    feeder_solution_6.SolutionContent(),
                    feeder_solution_7.SolutionContent(),
                    feeder_solution_8.SolutionContent(),
                ],
                "VPS Part Presence Failures": [
                    feeder_solution_1.SolutionContent(),
                    feeder_solution_2.SolutionContent(),
                    feeder_solution_3.SolutionContent(),
                    feeder_solution_4.SolutionContent(),
                    feeder_solution_5.SolutionContent(),
                    feeder_solution_6.SolutionContent(),
                    feeder_solution_7.SolutionContent(),
                    feeder_solution_8.SolutionContent(),
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