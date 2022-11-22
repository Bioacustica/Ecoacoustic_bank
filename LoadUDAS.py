import pandas as pd
from mapping import Base
from mapping import engine
from sqlalchemy.orm import Session
import LoadMasterTable as LMT
from flask import Flask, request, jsonify

session = Session(engine)

app = Flask(__name__)

@app.route('/LoadMasterTables', methods = ['POST'])
def upload_file():
    file = request.files['file']
    file.save("MasterTables_v1.xlsx")
    LMT.LoadMasterTables(info_path = 'MasterTables_v1.xlsx',
                         mapping = Base.classes,
                         engine = engine)
    return "done"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=7001)

