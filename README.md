# Person_Detection_Using_Yolov2

## I have used darknet framework for doing person detection on video. The code is written in python.

##Thanks to Yolo[https://pjreddie.com/darknet/yolo/]

To run the project do `python processing.py test_video_path`. 

Before running the above python script follow the steps mentioned below.

1. Go in the project directory.

2. If you have GPU, please make sure to enable GPU flag and give respective cuda path in MakeFile.Otherwise, simply disable the GPU flag. It runs way faster on GPU.

3. Type following commands
	`make clean`
	`make all`

4. The above commands will create darknet binary

5. Now you can run the processing.py as mentioned above.

6. OUTPUT :The result video with persons detected and corresponding text files containing co-ordinates of each frame would be in zip file.

Please contact me if you have any doubts.

Email Id : devalshah190@gmail.com

