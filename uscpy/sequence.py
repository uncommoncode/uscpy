"""
Functions relating to sequences of images live here.
"""
import numpy
import cv2

def video_capture(vc):
    """
    Create an image sequence generator out of an OpenCV VideoCapture object.
    """
    has_frames = vc.isOpened()
    while has_frames:
        read_frame, frame = vc.read()
        has_frames = read_frame
        if read_frame:
            yield frame

def processor(sequence, function):
    """
    Create a generator that applies a function over an image sequence.
    """
    for frame in sequence:
        yield function(frame)

def phase_stabilize(sequence):
    """
    A generator providing a stabilized version of an image sequence.

    Args:
        sequence: the image sequence to stabalize

    This method will account for translations in the image sequence with a
    method robust to noise and some local transformations, such as cellular movement.

    Extensions to this method can provide subpixel accuracies [3].

    After trying several adhoc methods with sparse and dense optical flow, this
    method is both fast and robust to errors.

    References:
     [1] http://en.wikipedia.org/wiki/Phase_correlation
     [2] http://docs.opencv.org/trunk/modules/imgproc/doc/motion_analysis_and_object_tracking.html#phasecorrelate
     [3] V. Argyriou and T. Vlachos. "A study of sub-pixel motion estimation
          using phase correlation."
    """
    cx = 0.0
    cy = 0.0
    frame_iter = iter(sequence)
    frame = frame_iter.next()
    prev_image = numpy.float32(frame)
    yield frame
    for frame in frame_iter:
        image = numpy.float32(frame)
        # TODO: set window around phase correlation
        dp = cv2.phaseCorrelate(prev_image, image)
        cx = cx - dp[0]
        cy = cy - dp[1]
        xform = numpy.float32([[1, 0, cx], [0, 1, cy]])
        stable_image = cv2.warpAffine(frame, xform, dsize=(frame.shape[1], frame.shape[0]))
        prev_image = image
        yield stable_image
