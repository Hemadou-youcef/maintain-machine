import customtkinter
from data.classes.views.views import ParentView
import pandas as pd

class View(ParentView):
    def __init__(self, master=None, state_manager=None, *args, **kwargs):
        super().__init__(master, state_manager,title="Home", *args, **kwargs)
       
        
    def header_content(self):
        self.master["padx"] = 20
        self.master["pady"] = 20
        self.master.grid_columnconfigure(0, weight=0)
        self.master.grid_columnconfigure(1, weight=1)
        
        back_button = customtkinter.CTkButton(
            self.master, text="⬅", command=lambda: self.state_manager.get_state("load_view")(name="upload"),bg_color="transparent"
        )
        back_button.grid(row=0, column=0, padx=10, pady=10, sticky='w')
        return [back_button]
    

    def content(self):
        self.analyse_data()

        # Title Label
        label = customtkinter.CTkLabel(self.master, text="Home", font=("Arial", 24, "bold"))
        label.grid(row=1, column=0, padx=10, pady=10, columnspan=2, sticky='w')

        # Container Frame for Content
        content_frame = customtkinter.CTkFrame(self.master)
        content_frame.grid(row=2, column=0, padx=10, pady=10, sticky='nsew')
        content_frame.grid_columnconfigure(0, weight=1)

        # Button Frame on the Left
        button_frame = customtkinter.CTkFrame(content_frame)
        button_frame.grid(row=0, column=0, padx=10, pady=10, sticky='nsew')
        button_frame.grid_columnconfigure(0, weight=1)

        # Feeders Button
        feeders_button = customtkinter.CTkButton(
            button_frame, text="Feeders", command=lambda: self.navigate_to_view("feeders"), width=200, height=50
        )
        feeders_button.grid(row=0, column=0, padx=10, pady=10, sticky='ew')

        # Nozzles Button
        nozzles_button = customtkinter.CTkButton(
            button_frame, text="Nozzles", command=lambda: self.navigate_to_view("nozzles"), width=200, height=50
        )
        nozzles_button.grid(row=1, column=0, padx=10, pady=10, sticky='ew')

        # Spindle Button
        spindle_button = customtkinter.CTkButton(
            button_frame, text="Spindles", command=lambda: self.navigate_to_view("spindles"), width=200, height=50
        )
        spindle_button.grid(row=2, column=0, padx=10, pady=10, sticky='ew')

        # Text Frame on the Right
        text_frame = customtkinter.CTkFrame(self.master, width=200, height=200)
        text_frame.grid(row=2, column=1, padx=10, pady=10, sticky='nsew')
        
        text_label = customtkinter.CTkLabel(text_frame, text="Information", font=("Arial", 16))
        text_label.pack(padx=10, pady=10)

        # create a list of text to display
        # good part => is_failure = False and state = False
        # bad part => is_failure = True and state = False
        # fixed part => is_failure = True and state = True
        # so the condition is 
        # is_failure | state | Result
        # True | False | 0
        # False | False | 0
        # True | True | 1
        # False | True | 1
        # so the sum of the result is the total failure
        text = [
            f"Total Failures of Feeders: {sum([1 if not(feeder['is_failure'] == feeder['state']) else 0 for feeder in self.state_manager.get_state('parts')[0]['inspected_data']])} / {len(self.state_manager.get_state('parts')[0]['data'])}",
            f"Total Failures of Nozzles: {sum([1 if not(nozzle['is_failure'] == nozzle['state']) else 0 for nozzle in self.state_manager.get_state('parts')[2]['inspected_data']])} / {len(self.state_manager.get_state('parts')[2]['data'])}",
            f"Total Failures of Spindles: {sum([1 if not(spindle['is_failure'] == spindle['state']) else 0 for spindle in self.state_manager.get_state('parts')[1]['inspected_data']])} / {len(self.state_manager.get_state('parts')[1]['data'])}",
        ]


        info_text = customtkinter.CTkLabel(
            text_frame, 
            text="\n".join(text), justify="left",
            font=("Arial", 20)
        )
        info_text.pack(padx=10, pady=10)

        return [label, feeders_button, spindle_button, nozzles_button]
        
    def navigate_to_view(self, view_name):
        self.state_manager.get_state("load_view")(name=view_name)
        
    def analyse_data(self):
        if not self.state_manager.get_state("do_analysis"):
            return
        # get the file data from the state manager
        file_data = self.state_manager.get_state("file_data")
        
        # check if the file data is available
        if file_data is not None:
            # perform some analysis on the data
            # start with spindles
            positions = [5,7,8]
            parts = [
                {
                    "part": "feeders",
                    "position": positions[0],
                    "data": None,
                    "inspected_data":[]
                },
                {
                    "part": "spindles",
                    "position": positions[1],
                    "data": None,
                    "inspected_data":[]
                },
                {
                    "part": "nozzles",
                    "position": positions[2],
                    "data": None,
                    "inspected_data":[]
                }
            ]
            tables = self.process_sheets(file_data, positions)
            

            for sheet_num, table in tables.items():
                if sheet_num == positions[0]:
                    parts[0]["data"] = table
                    parts[0]["inspected_data"] = self.check_parts(table, "feeders")
                elif sheet_num == positions[1]:
                    parts[1]["data"] = table
                    parts[1]["inspected_data"] = self.check_parts(table, "spindles")
                elif sheet_num == positions[2]:
                    parts[2]["data"] = table
                    parts[2]["inspected_data"] = self.check_parts(table, "nozzles")

            
            self.state_manager.set_state("parts", parts)

        else:
            print("No data available")
        
        # set the analysis flag to False
        self.state_manager.set_state("do_analysis", False)    
    
    def check_parts(self,table, part_name):
        # check if column Total Failures is bigger than 2% of sum of Total Failures
        total_failure = table["Total Failures"].sum()
        inspected_data = []

        name = ""
        # loop through the table and check if the Total Failures is greater than 2% of the sum of Total Failures
        for index, row in table.iterrows():
            if part_name == "feeders":
                name = f"{row['Component']},Feeder: {' '.join(row['Feeder'].split(' ')[1:])}, Slot: ,Track: {row['Track/Pallet'].split(' ')[1]}"
            elif part_name == "spindles":
                name = f"Spindle: {row['Serial Number']}"
            elif part_name == "nozzles":
                name = f"Nozzle: {row['Nozzle']} - {index}"
            if row["Total Failures"] > 0.02 * total_failure:
                inspected_data.append({
                        "name": name,
                        "number": index,
                        "total_failure": row["Total Failures"],
                        "failures_rate": row["Total Failures"] / total_failure,
                        "is_failure": True,
                        "state": False,
                        "state_label": "in process 🛠️" if row["Total Failures"] / total_failure > 1 else "Normal ✔️",
                        "solutions": [],
                        "is_inspected": False,
                    })
            else:
                inspected_data.append({
                        "name": name,
                        "number": index,
                        "total_failure": row["Total Failures"],
                        "failures_rate": row["Total Failures"] / total_failure,
                        "is_failure": False,
                        "state": False,
                        "state_label": "Normal ✔️",
                        "solutions": [],
                        "is_inspected": False,
                    })
                
        return inspected_data
    
        

    def detect_table_start(self,df):
        """
        Detect the starting position (row and column) of the table.
        This assumes that the table starts with non-empty header cells.
        """
        for row in range(df.shape[0]):
            for col in range(df.shape[1]):
                if pd.notna(df.iat[row, col]):  # Detect the first non-NaN cell
                    return row, col
        return None, None
    
    def extract_table(self,df, start_row, start_col):
        """
        Extract the table from the dataframe starting at (start_row, start_col).
        """
        end_row = df.shape[0]
        end_col = df.shape[1]
        
        table = df.iloc[start_row:end_row, start_col:end_col]
        table = table.dropna(thresh=4)
        table = table.reset_index(drop=True)
        # set the first row as the header
        table.columns = table.iloc[0]
        table = table.drop(0)
        
        return table

    
    def process_sheets(self,xls, sheet_numbers):
        """
        Process the specified sheets from the Excel file and convert each to a DataFrame.
        """
        tables = {}
        
        for sheet_num in sheet_numbers:
            df = xls.parse(sheet_num - 1, header=None)
            
            start_row, start_col = self.detect_table_start(df)
            if start_row is not None and start_col is not None:
                table = self.extract_table(df, start_row, start_col)
                tables[sheet_num] = table
            else:
                print(f"Table not found in sheet {sheet_num}")
        
        return tables

    
    