import shutil
import uuid

def save_temp_file(file):
    temp_name = f"temp_{uuid.uuid4()}_{file.filename}"
    with open(temp_name, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    return temp_name
