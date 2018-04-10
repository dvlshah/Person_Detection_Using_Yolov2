from subprocess import Popen, PIPE
import processing 
import time
import os
from collections import deque

while True:
	#3 seconds delay to check any new file is uploaded or not
	time.sleep(3)	
	
	extensions = [
		'.webm','.mkv','.flv','.vob','.avi','.mov',
		'.wmv','.yuv','.rm','.mp4','.m4v','.mpg','.mpeg',
		'.m2v','.m4v','.3gp','.flv'
	]

	#f_flag = 0
	processed_files = []
	opened_file = []
	video_files = []
	
	for file in os.listdir("/mnt/tasec/result/"):
		for ext in extensions:
                        if file.endswith(ext):
               			processed_files.append(file)
	
	#print(" P : ",processed_files)
	
	#Maintaining a list of video files that are not processed
	for file in os.listdir("/mnt/tasec/upload/"):
		for ext in extensions: 
			if file.endswith(ext):
				if file in processed_files:
					continue
				else:
					video_files.append(os.path.join("/mnt/tasec/upload/", file))
				
	#print("UP : ",video_files)
	
	if len(video_files)!=0:
		path  = "/mnt/tasec/upload/"
	
		for i in extensions:
	
			format_vid = ' '+i+' '

			first = ['lsof +D '+path]
			second = ['awk "{print $9}"']
			third = ['grep '+format_vid]

			p1 = Popen(first,stdout=PIPE,stderr=PIPE,shell=True)
			p2 = Popen(second,stdin=p1.stdout, stdout=PIPE,stderr=PIPE,shell=True)
			p3 = Popen(third,stdin=p2.stdout,stdout=PIPE,stderr=PIPE,shell=True)
		
			output,error = p3.communicate()
			#print("Output",output)
			
			if output:		
				s = output.split('/')
				opened_file.append(s[-1])
				time.sleep(10)
			#print("OP : ",opened_file)
			
		for path in video_files:
			if path not in opened_file:
				#print("Processing on video : ",path)
				processing.processing(path)		
			else:
				continue
			
	else:
		#print("All video files are processed")	
		time.sleep(2)
		continue
