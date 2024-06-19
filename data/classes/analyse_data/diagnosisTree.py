# feeder solutions
import data.classes.analyse_data.solutions.feeder.feeder_solution_1 as feeder_solution_1
import data.classes.analyse_data.solutions.feeder.feeder_solution_2 as feeder_solution_2
import data.classes.analyse_data.solutions.feeder.feeder_solution_3 as feeder_solution_3
import data.classes.analyse_data.solutions.feeder.feeder_solution_4 as feeder_solution_4
import data.classes.analyse_data.solutions.feeder.feeder_solution_5 as feeder_solution_5
import data.classes.analyse_data.solutions.feeder.feeder_solution_6 as feeder_solution_6
import data.classes.analyse_data.solutions.feeder.feeder_solution_7 as feeder_solution_7
import data.classes.analyse_data.solutions.feeder.feeder_solution_8 as feeder_solution_8

# nozzle solutions
import data.classes.analyse_data.solutions.nozzle.nozzle_solution_1 as nozzle_solution_1
import data.classes.analyse_data.solutions.nozzle.nozzle_solution_2 as nozzle_solution_2
import data.classes.analyse_data.solutions.nozzle.nozzle_solution_3 as nozzle_solution_3
import data.classes.analyse_data.solutions.nozzle.nozzle_solution_4 as nozzle_solution_4
import data.classes.analyse_data.solutions.nozzle.nozzle_solution_5 as nozzle_solution_5
import data.classes.analyse_data.solutions.nozzle.nozzle_solution_6 as nozzle_solution_6

# spindle solutions
import data.classes.analyse_data.solutions.spindle.spindle_solution_1 as spindle_solution_1
import data.classes.analyse_data.solutions.spindle.spindle_solution_2 as spindle_solution_2
import data.classes.analyse_data.solutions.spindle.spindle_solution_3 as spindle_solution_3
import data.classes.analyse_data.solutions.spindle.spindle_solution_4 as spindle_solution_4
import data.classes.analyse_data.solutions.spindle.spindle_solution_5 as spindle_solution_5
import data.classes.analyse_data.solutions.spindle.spindle_solution_6 as spindle_solution_6
import data.classes.analyse_data.solutions.spindle.spindle_solution_7 as spindle_solution_7
import data.classes.analyse_data.solutions.spindle.spindle_solution_8 as spindle_solution_8


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
                "Components Purged": [
                    nozzle_solution_1.SolutionContent(),
                    nozzle_solution_2.SolutionContent(),
                    nozzle_solution_3.SolutionContent(),
                    nozzle_solution_4.SolutionContent(),
                    nozzle_solution_5.SolutionContent(),
                    nozzle_solution_6.SolutionContent(),
                ],
                "Part Sense Failures": [
                    nozzle_solution_1.SolutionContent(),
                    nozzle_solution_2.SolutionContent(),
                    nozzle_solution_3.SolutionContent(),
                    nozzle_solution_4.SolutionContent(),
                    nozzle_solution_5.SolutionContent(),
                    nozzle_solution_6.SolutionContent(),
                ],
                "Mispicks": [
                    nozzle_solution_1.SolutionContent(),
                    nozzle_solution_2.SolutionContent(),
                    nozzle_solution_3.SolutionContent(),
                    nozzle_solution_4.SolutionContent(),
                    nozzle_solution_5.SolutionContent(),
                    nozzle_solution_6.SolutionContent(),
                ],
                "Rejected": [
                    nozzle_solution_1.SolutionContent(),
                    nozzle_solution_2.SolutionContent(),
                    nozzle_solution_3.SolutionContent(),
                    nozzle_solution_4.SolutionContent(),
                    nozzle_solution_5.SolutionContent(),
                    nozzle_solution_6.SolutionContent(),
                ],
                # Add other nozzle failure types and their solutions here...
            },
            "spindle": {
                "Components Purged": [
                    spindle_solution_1.SolutionContent(),
                    spindle_solution_2.SolutionContent(),
                    spindle_solution_3.SolutionContent(),
                    spindle_solution_4.SolutionContent(),
                    spindle_solution_5.SolutionContent(),
                    spindle_solution_6.SolutionContent(),
                    spindle_solution_7.SolutionContent(),
                    spindle_solution_8.SolutionContent(),
                ],
                "Part Sense Failures": [
                    spindle_solution_1.SolutionContent(),
                    spindle_solution_2.SolutionContent(),
                    spindle_solution_3.SolutionContent(),
                    spindle_solution_4.SolutionContent(),
                    spindle_solution_5.SolutionContent(),
                    spindle_solution_6.SolutionContent(),
                    spindle_solution_7.SolutionContent(),
                    spindle_solution_8.SolutionContent(),
                ],
                "Mispicks": [
                    spindle_solution_1.SolutionContent(),
                    spindle_solution_2.SolutionContent(),
                    spindle_solution_3.SolutionContent(),
                    spindle_solution_4.SolutionContent(),
                    spindle_solution_5.SolutionContent(),
                    spindle_solution_6.SolutionContent(),
                    spindle_solution_7.SolutionContent(),
                    spindle_solution_8.SolutionContent(),
                ],
                "Pick Attempts From Empty Feeders": [
                    spindle_solution_1.SolutionContent(),
                    spindle_solution_2.SolutionContent(),
                    spindle_solution_3.SolutionContent(),
                    spindle_solution_4.SolutionContent(),
                    spindle_solution_5.SolutionContent(),
                    spindle_solution_6.SolutionContent(),
                    spindle_solution_7.SolutionContent(),
                    spindle_solution_8.SolutionContent(),
                ],
                "Rejected": [
                    spindle_solution_1.SolutionContent(),
                    spindle_solution_2.SolutionContent(),
                    spindle_solution_3.SolutionContent(),
                    spindle_solution_4.SolutionContent(),
                    spindle_solution_5.SolutionContent(),
                    spindle_solution_6.SolutionContent(),
                    spindle_solution_7.SolutionContent(),
                    spindle_solution_8.SolutionContent(),
                ],
                
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