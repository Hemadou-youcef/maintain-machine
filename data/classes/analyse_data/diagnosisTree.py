class DiagnosisTree:
    def __init__(self):
        self.questionsList()
        self.answersList()
        self.questionsAnswsertree()
        
    def getQuestions(self):
        return [1,2,5,6]
    
    def getQuestion(self, node):
        return self.questions[node][0]
    
    def getQuestionType(self, node):
        return self.questions[node][1]
        
    def questionsList(self):
        self.questions = {
            1: ['Is the spindle broken?','YesNo'],
            2: ['Please Input the spindle calibration value:','Input'],
            3: ['Is the spindle dirty?','YesNo'],
            4: ['Is the spindle installed correctly?','YesNo'],
            5: ['Is the spindle lubricated?','YesNo'],
            6: ['Is the spindle maintained?','YesNo'],
            7: ['Is the spindle cooled?','YesNo'],
            8: ['Is the spindle ventilated?','YesNo'],
            9: ['Is the spindle powered?','YesNo'],
            10: ['Is the spindle between 1.5 and 1000?','Input'],
            11: ['Is the spindle less than 100?','Input'],
            
            
        }
    
    def getAnswers(self, node):
        return self.diagnosis_tree[node]
    
    def getAnswer(self, node):
        return self.answers[node]
        
    def answersList(self):
        self.answers = {
            1: 'PLEASE REPLACE THE SPINDLE',
            2: 'CLEAN THE SPINDLE',
            3: 'REINSTALL THE SPINDLE',
            4: 'LUBRICATE THE SPINDLE',
            5: 'CALIBRATE THE SPINDLE',
            6: 'MAINTAIN THE SPINDLE',
            7: 'COOL THE SPINDLE',
            8: 'VENTILATE THE SPINDLE',
            9: 'POWER THE SPINDLE',
        }
        
    def questionsAnswsertree(self):
        self.diagnosis_tree = {
            1: {
                1: [[10],[1]],
                2: [[3],[]]
            },
            2: {
                1: ["BETWEEN/1.5/1000",[[],[]],"LESS/100",[[],[]]]
            },
            3: {
                1: [[4],[2]],
                2: [[],[5]]
            },
            4: {
                1: [[5],[3]],
                2: [[],[5]]
            },
            5: {
                1: [[6],[4]],
                2: [[],[]]
            },
            6: {
                1: [[1],[5]],
                2: [[],[9]]
            },
            7: {
                1: [[8],[6]],
                2: [[],[]]
            },
            8: {
                1: [[9],[7]],
                2: [[],[]]
            },
            9: {
                1: [[],[]]
            },
            10: {
                1: [[11],[8]],
                2: [[],[]]
            },
        }
        

    def getResult(self, node, answer):
        try:
            # check the type of question
            if self.questions[node][1] == 'YesNo':
                if answer == "Yes":
                    return self.diagnosis_tree[node][1]
                elif answer == "No":
                    return self.diagnosis_tree[node][2]
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

    
