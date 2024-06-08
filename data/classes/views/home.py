import customtkinter
from data.classes.views.views import ParentView
import pandas as pd

class View(ParentView):
    def __init__(self, master=None, state_manager=None, *args, **kwargs):
        super().__init__(master, state_manager,title="Home", *args, **kwargs)
       
        
    def header_content(self):
        self.master["padx"] = "10"
        self.master["pady"] = "10"
        # create a button to navigate to the upload view
        back_button = customtkinter.CTkButton(self.master, text="⬅", command=lambda: self.state_manager.get_state("load_view")(name="upload"))
        # grid it in the top left corner
        back_button.grid(row=0, column=0, padx=10, pady=10, sticky='w')
        return [back_button]
    
    def content(self):
        self.analyse_data()
        # Add any widgets or components here
        label = customtkinter.CTkLabel(self.master, text="Home")
        label.grid(row=1, column=0, padx=10, pady=10)
        
        
        # create four buttons each button navigate to a different view
        feeders_button = customtkinter.CTkButton(self.master, text="Feeders", command=lambda: self.state_manager.get_state("load_view")(name="feeders"))
        feeders_button.grid(row=2, column=0, padx=10, pady=10)
        nozzles_button = customtkinter.CTkButton(self.master, text="Nozzles", command=lambda: self.state_manager.get_state("load_view")(name="nozzles"))
        nozzles_button.grid(row=3, column=0, padx=10, pady=10)
        spindle_button = customtkinter.CTkButton(self.master,text="Spindles", command=lambda: self.state_manager.get_state("load_view")(name="spindles"))
        spindle_button.grid(row=2, column=0, padx=10, pady=10)
        
        return [label, spindle_button, nozzles_button, feeders_button]
        
        
    def analyse_data(self):
        if not self.state_manager.get_state("do_analysis"):
            return
        # get the file data from the state manager
        file_data = self.state_manager.get_state("file_data")
        
        # check if the file data is available
        if file_data is not None:
            # perform some analysis on the data
            # start with spindles
            spindles_data = []
            while True:
                try:
                    spindle_rate = float(str(file_data.values[len(spindles_data)][9]).replace(",", "."))
                    spindles_data.append({
                        "number": len(spindles_data) + 1,
                        "failures_rate": spindle_rate,
                        "is_failure": spindle_rate > 1,
                        "state": False,
                        "state_label": "in process 🛠️" if spindle_rate > 1 else "Normal ✔️",
                        "is_inspected": False,
                        "questions": [],
                    })

                except IndexError:
                    break
            # set the data in the state manager
            self.state_manager.set_state("spindles_data", spindles_data)
            
            # then nozzles
            nozzles_data = []
            while True:
                try:
                    nozzle_rate = float(str(file_data.values[len(nozzles_data)][10]).replace(",", "."))
                    nozzles_data.append({
                        "number": len(nozzles_data) + 1,
                        "failures_rate": nozzle_rate,
                        "is_failure": nozzle_rate > 1,
                        "questions": [],
                        "state": "in process 🛠️" if nozzle_rate > 1 else "Normal ✔️"
                    })

                except IndexError:
                    break
            # set the data in the state manager
            self.state_manager.set_state("nozzles_data", nozzles_data)
        else:
            print("No data available")
        
        # set the analysis flag to False
        self.state_manager.set_state("do_analysis", False)    
    


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
        end_row = start_row
        end_col = start_col
        
        # Find the end row
        while end_row < df.shape[0] and pd.notna(df.iat[end_row, start_col]):
            end_row += 1
        
        # Find the end column
        while end_col < df.shape[1] and pd.notna(df.iat[start_row, end_col]):
            end_col += 1
        
        table = df.iloc[start_row:end_row, start_col:end_col]
        table.columns = table.iloc[0]  # Set the first row as header
        table = table.drop(start_row)  # Drop the header row
        
        return table

    
    def read_sheets(self,file_path, sheet_numbers):
        """
        Read specified sheets from an Excel file and convert each to a DataFrame.
        """
        xls = pd.ExcelFile(file_path)
        tables = {}
        
        for sheet_num in sheet_numbers:
            sheet_name = xls.sheet_names[sheet_num - 1]
            df = pd.read_excel(file_path, sheet_name=sheet_name, header=None)
            
            start_row, start_col = self.detect_table_start(df)
            if start_row is not None and start_col is not None:
                table = self.extract_table(df, start_row, start_col)
                tables[sheet_name] = table
            else:
                print(f"Table not found in sheet {sheet_name}")
        
        return tables
    
    