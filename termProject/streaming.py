import os,sys#리눅스 명령어를 파이썬 내에서 실행시켜주는 프로그램 import
#동영상 스트리밍을 위한 리눅스 명령어를 문자열에 저장 
Streaming ="./test-launch '( rpicamsrc preview=false bitrate=2000000 keyframe-interval=15 ! video/x-h264, framerate=15/1 ! h264parse ! rtph264pay name=pay0 pt=96 )'stream ready at rtsp://127.0.0.1:8554/test"

os.system(Streaming)#리눅스 명령어 실행 