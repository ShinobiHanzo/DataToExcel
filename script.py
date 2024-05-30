import tkinter as tk
from tkinter import filedialog, messagebox
import pandas as pd

class JSONToExcelConverter(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("JSON to Excel Converter")

        self.input_file_path = None

        self.create_widgets()

    def create_widgets(self):
        self.label = tk.Label(self, text="Drag and drop a JSON file here:")
        self.label.pack(pady=10)

        self.drop_area = tk.Listbox(self, width=50, height=5)
        self.drop_area.pack(expand=True)

        self.drop_area.bind("<Button-1>", self.browse_file)

        self.process_button = tk.Button(self, text="Process", command=self.process_data)
        self.process_button.pack(pady=5)

    def browse_file(self, event):
        file_path = filedialog.askopenfilename(filetypes=[("JSON files", "*.json")])
        if file_path:
            self.input_file_path = file_path
            self.drop_area.delete(0, tk.END)
            self.drop_area.insert(tk.END, self.input_file_path)

            # Display preview of the data
            try:
                df = pd.read_json(self.input_file_path)
                preview = df.head().to_string(index=False)
                messagebox.showinfo("Preview", f"Data Preview:\n{preview}")
            except Exception as e:
                messagebox.showerror("Error", f"Error loading data: {str(e)}")

    def process_data(self):
        if self.input_file_path:
            output_file_path = filedialog.asksaveasfilename(defaultextension=".xlsx",
                                                             filetypes=[("Excel files", "*.xlsx")])
            if output_file_path:
                try:
                    df = pd.read_json(self.input_file_path)
                    df.to_excel(output_file_path, index=False)
                    messagebox.showinfo("Success", f"Data successfully written to {output_file_path}")
                except Exception as e:
                    messagebox.showerror("Error", f"Error processing data: {str(e)}")
        else:
            messagebox.showerror("Error", "No input file selected.")


if __name__ == "__main__":
    app = JSONToExcelConverter()
    app.mainloop()
