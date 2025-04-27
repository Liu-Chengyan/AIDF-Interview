# Second Part: Simple Data Pipeline Automation

# Files Overview

- `pipeline.py`
  - Reads the scraped news data from `company.json`.
  - Cleans the text fields (title, date, summary) by removing unnecessary whitespaces.
  - Handles missing summaries by replacing them with the title if necessary.
  - Validates that each news item has required fields (`company`, `title`, `date`).
  - Inserts or updates the cleaned news records into a MongoDB database (`WSJ.latest_news` collection).


- `scheduled_pipeline.py`
  - Imports the pipeline function from `pipeline.py`.
  - Schedules the pipeline to run automatically every 6 hours using the `schedule` library.
  - Runs an infinite loop to keep checking and executing the scheduled task.
