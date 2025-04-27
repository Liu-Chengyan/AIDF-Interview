import schedule
import time
from pipeline import run_pipeline

# Schedule the pipeline to run every hour
schedule.every(6).hours.do(run_pipeline)

print("Scheduled task started: The news pipeline will run 6 hours.")

# Run the scheduler loop
while True:
    schedule.run_pending()
    time.sleep(1)