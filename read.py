import cv2 as cv

#scales video down by a given scale factor
def resizeFrame(frame, scale):

    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width,height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

 

capture = cv.VideoCapture('photos/rick.mkv')

while True:
    isTrue, frame = capture.read()

    resized_frame = resizeFrame(frame, 2)

    cv.imshow('Video', resized_frame)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()
