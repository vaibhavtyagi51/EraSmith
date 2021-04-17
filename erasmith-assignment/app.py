from datetime import date, datetime, timedelta
import os, glob

delete_file = "logfiles/{filename}"

def get_seven_back_date():
    now = datetime.now()
    date_before_seven_days = datetime.now() - timedelta(days=7)
    date = date_before_seven_days.strftime("%Y%m%d")
    return int(date)

def get_log_files():
    for files in os.listdir("./logfiles"):
        try:
            file_dates = int(files.split('_')[2][:8])
            get_seven_days_data = get_seven_back_date()
            if file_dates <= get_seven_days_data:
                file_path = delete_file.format(filename=files)
                os.remove(file_path)
        except Exception as e:
            return {"error":e}


if __name__ == "__main__":
    get_log_files()

