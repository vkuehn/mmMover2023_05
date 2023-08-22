"""
A tool to write camera calibration to config.
"""
import argparse
import codecs
import json
import os
import sys

import cv2
import numpy as np

from pathlib import Path

def live_calibrate(device_id, CHECKERBOARD, n_matches_needed):
    """ Find calibration parameters as the user moves a checkerboard in front of the camera """
    print("Looking for %s checkerboard" % (CHECKERBOARD,))

    # termination criteria
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)

    # Arrays to store object points and image points from all the images.
    imgpoints = []  # 2d points in image plane.
    objpoints = []  # 3d point in real world space

    # Defining the world coordinates for 3D points
    objp = np.zeros((1, CHECKERBOARD[0] * CHECKERBOARD[1], 3), np.float32)
    objp[0, :, :2] = np.mgrid[0:CHECKERBOARD[0], 0:CHECKERBOARD[1]].T.reshape(-1, 2)
    prev_img_shape = None

    cap = cv2.VideoCapture(device_id)
    while len(objpoints) < n_matches_needed:
        ret, frame = cap.read()

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        ret, corners = cv2.findChessboardCorners(gray, CHECKERBOARD,
                                                 cv2.CALIB_CB_ADAPTIVE_THRESH + cv2.CALIB_CB_FAST_CHECK + cv2.CALIB_CB_NORMALIZE_IMAGE)

        if ret:
            objpoints.append(objp)
            corners2 = cv2.cornerSubPix(gray, corners, (11, 11), (-1, -1), criteria)
            imgpoints.append(corners2)

    return cv2.calibrateCamera(objpoints, imgpoints, gray.shape[::-1], None, None)


def load_calibration(PATH_CALIBRATION):
    mtx = ""
    dist = ""
    if os.path.exists(PATH_CALIBRATION):
        obj_text = codecs.open(PATH_CALIBRATION, 'r', encoding='utf-8').read()
        j_camera_config = json.loads(obj_text)
        mtx = np.array(j_camera_config['camera_matrix'])
        dist = np.array(j_camera_config['dist_coeff'])
    else:
        print("can't find " + PATH_CALIBRATION)
        sys.exit(1)
    return [mtx, dist]


def save_calibration(PATH_CALIBRATION, mtx, dist):
    data = {'camera_matrix': np.asarray(mtx).tolist(), 'dist_coeff': np.asarray(dist).tolist()}
    json.dump(data, codecs.open(PATH_CALIBRATION, 'w', encoding='utf-8'), separators=(',', ':'), sort_keys=True,indent=4)


def calibrate():
    """
    Calibrate the live camera and optionally do a live display of the results
    """
    parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("--device", type=int, default=0)
    parser.add_argument("--height", type=int, default=7)
    parser.add_argument("--width", type=int, default=7)
    parser.add_argument("--count", type=int, default=10)
    parser.add_argument("--view", action="store_true")
    args = parser.parse_args()

    # Defining the dimensions of checkerboard
    CHECKERBOARD = (args.height, args.width)
    PATH_CALIBRATION = str(Path.home()) + "/.config/camera_calibration.json"

    print("try finding " + str(args.count) + " checkerboards in camera stream")
    ret, mtx, dist, rvecs, tvecs = live_calibrate(args.device, CHECKERBOARD, args.count)

    print("Camera matrix : \n")
    print(mtx)
    print("dist : \n")
    print(dist)
    print("save results to " + PATH_CALIBRATION)
    save_calibration(PATH_CALIBRATION, mtx, dist)
    mtx_new, dist_new = load_calibration(PATH_CALIBRATION)
    if not np.array_equal(mtx, mtx_new):
        print("MTX not saved properly")
    else:
        print("MTX saved properly")
    if not np.array_equal(dist, dist_new):
        print("Dist not saved properly")
    else:
        print("Dist saved properly")

if __name__ == "__main__":
    calibrate()