from subprocess import Popen,PIPE,call 
import os
import ntpath
import sys

"""
	@param : imgf --> image format for frames 
"""
def filePath(path,imgf):
    
    	c = 'find '+path+' -name "*'+imgf+'" > temp.txt '
	#print(c)
	a = os.system(c)
	
	f = open('temp.txt','r')
	lst = []

	for line in f:
		lst.append(line)
	lst.sort()
    	f.close()

	#print(lst)

	return lst

"""
	@param : video_file_path --> Path of video file to process 
"""

def processing(video_file_path):	
	filename = ntpath.basename(video_file_path)
	os.system('mkdir tmpframes')
	os.system('mkdir result')
	os.system('mkdir tmpframes/txt')

	#Converting video into frames	
	a = 'ffmpeg -i '+video_file_path+' tmpframes/frame%06d.png'
	os.system(a)

	#Storing the path of frames of video file into text file
	imgf = ".png"			
	temp = filePath('tmpframes/',imgf)
	print(temp)
	#Writing absolute path of frames of video to a text file
	f=open('tmpframes/video_frames_path.txt','w')
    	for j in temp:
            f.write(j)
    	f.close()
	
	#Applying yolo darknet on frames of input video
	b =  './darknet detector test cfg/coco.data cfg/yolo.cfg yolo.weights < temp.txt'
	os.system(b)	
	
	fname, ext = os.path.splitext(filename)

	#Zip all the generated text files into a single file --> framestxt_video_upload_file.zip
	c = 'zip -r tmpframes/framestxt_'+fname+'.zip  tmpframes/txt/'
	os.system(c)
	
	#(Result) Zip file moved into result directory
	d = 'mv tmpframes/framestxt_'+fname+'.zip result/'+fname+'_framestxt.zip'
	os.system(d)	
	
	e = 'rm tmpframes/txt/*.txt'
	os.system(e)
	
	#Stitching output frames back into video
	f = 'ffmpeg -f image2 -i tmpframes/frame%06d.png tmpframes/result.mp4'
	os.system(f)
	
	#(Result) Output video moved into result directory
	g = 'mv tmpframes/result.mp4 result/'+filename
	os.system(g)
	
	h = 'rm tmpframes/*.png'
	#os.system(h)
	
	i = 'rm tmpframes/video_frames_path.txt'
        os.system(i)

path = sys.argv[1]
processing(path)
