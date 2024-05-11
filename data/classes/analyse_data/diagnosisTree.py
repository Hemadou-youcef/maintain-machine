import os
import pandas as pd

class DiagnosisTree:
    def __init__(self, part_name):
        self.part_name = part_name
        self.questionsList()
        
    def getQuestion(self, node):
        return self.questions[node][1]
    
    def getQuestionType(self, node):
        return self.questions[node][2]
    
    def getTotalNumberOfQuestions(self):
        return len(self.questions)
        
    def questionsList(self):
        try:
            # current_dir = os.path.dirname(os.path.abspath(__file__))
            current_dir = 'D:/youcef-hemadou/PROGRAMMING/PYTHON/PROJECTS/00001-MAINTAIN-MACHINE/data/assets/csv_data/questions'
            # check part name
            if self.part_name == 'spindle':
                # if self.check_file_exists(f"{current_dir}/spindle_questions.csv"):
                #     file_data = pd.read_csv(f"{current_dir}/spindle_questions.csv",header=None,sep=",")
                #     self.questions = []
                #     # csv file has no fixed number of columns
                #     # so it's like a list of if statements
                #     # first column has the question and the second column has the type of the question and the third is the answer
                #     # if the next line is empty then it's the else in the previous question if the answer is no
                #     # if the next line is not empty then it's the next question if the answer is yes
                #     # here an example structure of the file
                #     # question1, YesNo
                #     # ,question1-1, YesNo
                #     # ,,question1-1-1, YesNo, change the spindle because it's broken
                #     # question2, YesNo
                #     # ,question2-1, YesNo
                #     # question3, YesNo, change the spindle because it's broken
                #     # question4, YesNo, change the spindle because it's broken
                #     # question5, YesNo

                #     for i in range(0, len(file_data)):
                #         # check if the first column is not empty
                #         if str(file_data.values[i][0]) != 'nan':
                #             # check if there is an answer
                #             if len(file_data.values[i]) == 3:
                #                 self.questions.append([file_data.values[i][0],file_data.values[i][1],file_data.values[i][2]])
                #             else:
                #                 self.questions.append([file_data.values[i][0],file_data.values[i][1],None])
                #         else:
                #             # find the first column that is not empty
                #             for j in len(file_data.values[i]):
                #                 if str(file_data.values[i][j]) != 'nan':
                #                     # check if there is an answer
                #                     if len(file_data.values[i]) 

                self.questions = [
                    [1,"question1", "YesNo",None],
                    [1,"question1-1", "YesNo",None],
                    [1,"question1-1-1", "YesNo", "change the spindle because it's broken"],
                    [2,"question2", "YesNo",None],
                    [2,"question2-1", "YesNo",None],
                    [3,"question3", "YesNo", "change the spindle because it's broken"],
                    [4,"question4", "YesNo", "change the spindle because it's broken"],
                    [5,"question5", "YesNo", "change the spindle because it's broken"],
                ]
                                    
            elif self.part_name == 'nozzle':
                pass


        except:
            print("Error")

    def getNextMainQuestion(self, node):
        # loop through the questions and find the index of questions that have node + 1 as the first element if not found return None
        for i in range(0, len(self.questions)):
            if self.questions[i][0] == node + 1:
                return i
        return None

        
    def getResult(self,node, answer):
        # result of this function is a list of 3 elements
        # the first element is the question answer
        # the second element is the next question index
        # the third element is a boolean to tell that the question loop is stopped or not
        try:
            # get the next main question 
            next_main_question = self.getNextMainQuestion(node)
            # check the type of question
            if self.questions[node][2] == 'YesNo':
                # is there an answer
                if answer == "Yes":
                    return [self.questions[node][3],next_main_question,False]
                elif answer == "No":
                    if self.questions[node][0] == self.questions[node + 1][0]:
                        return [None,node+1,False]
                    return [self.questions[node][3],None,True]
        except:
            return None

    def getResultt(self, node, answer):
        try:
            # check the type of question
            if self.questions[node][1] == 'YesNo':
                if answer == "Yes":
                    return [self.questions[node][2]]
                elif answer == "No":
                    return node+1
            elif self.questions[node][1] == 'Input':
                # GET LIST OF IFS EACH ONE HAS 2 ELEMENTS THE FIRST ONE IS THE CONDITION AND THE SECOND ONE IS THE RESULT
                for i in range(0, len(self.diagnosis_tree[node][1]), 2):
                    typeOfOperator = self.diagnosis_tree[node][1][i].split('/')[0]
                    otherValues = self.diagnosis_tree[node][1][i].split('/')[1:]
                    if typeOfOperator == 'BETWEEN':
                        if float(otherValues[0]) <= float(answer) <= float(otherValues[1]):
                            return self.diagnosis_tree[node][1][i+1]
                    elif typeOfOperator == 'LESS':
                        if float(answer) < float(otherValues[0]):
                            return self.diagnosis_tree[node][1][i+1]
                    elif typeOfOperator == 'LESSOREQUAL':
                        if float(answer) <= float(otherValues[0]):
                            return self.diagnosis_tree[node][1][i+1]
                    elif typeOfOperator == 'GREATER':
                        if float(answer) > float(otherValues[0]):
                            return self.diagnosis_tree[node][1][i+1]
                    elif typeOfOperator == 'GREATEROREQUAL':
                        if float(answer) >= float(otherValues[0]):
                            return self.diagnosis_tree[node][1][i+1]
                    elif typeOfOperator == 'EQUAL':
                        if float(answer) == float(otherValues[0]):
                            return self.diagnosis_tree[node][1][i+1]
                    elif typeOfOperator == 'DIFFERENT':
                        if float(answer) != float(otherValues[0]):
                            return self.diagnosis_tree[node][1][i+1]
                    
            else:
                return self.diagnosis_tree[node][1][1]
        except:
            return None

    
    def check_file_exists(self,filepath):
        try:
            with open(filepath, 'r') as file:
                return True
        except FileNotFoundError:
            return False
        