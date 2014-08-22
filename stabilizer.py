"""
Image stabilization code.
"""
import argparse

import cv2

import uscpy.sequence
import uscpy.frame

parser = argparse.ArgumentParser(description="Perform image stabalization to a video")
parser.add_argument("input", help="input video path")
parser.add_argument("output", help="output video path")
args = parser.parse_args()

vc = cv2.VideoCapture(args.input)
if not vc.isOpened():
    raise Exception("Error opening video input '%s'" % args.input)

width = int(vc.get(cv2.cv.CV_CAP_PROP_FRAME_WIDTH))
height = int(vc.get(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT))
fps = vc.get(cv2.cv.CV_CAP_PROP_FPS)
fourcc = int(vc.get(cv2.cv.CV_CAP_PROP_FOURCC))
print("video-input:")
print("   width: %d\n   height: %d\n   fps: %d" % (width, height, fps))
vw = cv2.VideoWriter(args.output, cv2.cv.FOURCC('m', 'p', '4', 'v'), fps, (width, height), True)

if not vw.isOpened():
    raise Exception("Error opening video output '%s'" % args.output)

vc_sequence = uscpy.sequence.video_capture(vc)
greyscale_sequence = uscpy.sequence.processor(vc_sequence, uscpy.frame.greyscale)
stable_sequence = uscpy.sequence.phase_stabilize(greyscale_sequence)

frame_count = 0
for frame in stable_sequence:
    # save each frame to disk
    bgr_frame = cv2.cvtColor(frame, cv2.COLOR_GRAY2BGR)
    vw.write(bgr_frame)
    if (frame_count % fps) == 0:
        print("rendered-frame: %d" % frame_count)
    frame_count += 1

