from celery_app import celery_task
from fastapi import Response
import inputfile

@celery_task.task
def off_target(output_file_name, summary_file_name):
  import time
  time.sleep(5)
  import subprocess
  subprocess.run(['./cas-offinder', 'input.txt', 'G', output_file_name, '--summary', summary_file_name])
  with open(output_file_name) as file:
     reading = file.read()
     reads = reading.replace('\t', ' ')
     # return reads
 
  return  'done'
 


