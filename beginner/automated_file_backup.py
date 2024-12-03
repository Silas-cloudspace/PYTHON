# pip install schedule

import os
import shutil
import datetime
import schedule
import time

source_dir = "C:/Users/sdinp/Downloads/automated_backups"
destination_dir = "C:/Users/sdinp/Desktop/Backups"

def copy_folder_to_directory(source, dest):
    print(f"Checking source directory at {datetime.datetime.now()}")
    if not os.path.exists(source):
        print(f"Source directory does not exist: {source}")
        return

    today = datetime.date.today()
    dest_dir = os.path.join(dest, str(today))
    
    try:
        shutil.copytree(source, dest_dir)
        print(f"Folder copied to: {dest_dir}")
    except FileExistsError:
        print(f"Folder already exists in: {dest}")
    except Exception as e:
        print(f"An error occurred: {e}")

def scheduled_task():
    print(f"Scheduled task triggered at {datetime.datetime.now()}")
    copy_folder_to_directory(source_dir, destination_dir)

schedule.every().day.at("07:18").do(scheduled_task)

print(f"Scheduler started. Waiting for task...")
while True:
    schedule.run_pending()
    time.sleep(60)
      
