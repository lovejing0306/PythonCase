# coding=utf-8

import os
import cv2

def load_video(video_path):
    """
        读取视频并显示
    """
    # 这里输入的视频路径必须为绝对路径，否则会报错
    cap = cv2.VideoCapture(video_path)
    while(True):
        # 读取当前帧
        ret, frame = cap.read()
        if ret == True:
            # 显示当前帧
            cv2.imshow('capture', frame)
            # 退出条件
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        else:
            break
    cap.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    # 获取当前工作目录
    program_path = os.path.abspath('..')

    video_path = os.path.join(program_path, 'data/videos/1.mp4')
    load_video(video_path)