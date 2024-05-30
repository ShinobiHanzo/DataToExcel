from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        json_file = request.files['json_file']
        if json_file:
            try:
                df = pd.read_json(json_file)
                output_file_path = 'output.xlsx'
                df.to_excel(output_file_path, index=False)
                return f'Data successfully written to {output_file_path}'
            except Exception as e:
                return f'Error processing data: {str(e)}'
        else:
            return 'No file selected.'

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
