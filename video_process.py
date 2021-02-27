import cv2

def video_process(video):

    cap = cv2.VideoCapture(video)
    frametime = 100 # To control the video playback speed
    data_points_x = []
    data_points_y = []

    try:
        while(1):

            # Take each frame
            _, frame = cap.read()
            
            # print(frame.shape)
            width = int(frame.shape[1] * 0.3)
            height = int(frame.shape[0] * 0.3)
        
            frame = cv2.resize(frame, (width, height), interpolation = cv2.INTER_AREA)
            
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            ret,thresh = cv2.threshold(gray, 127, 255,cv2.THRESH_BINARY_INV)

            contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)        
        
        
            for c in contours:
                
                # compute the center of the contour
                M = cv2.moments(c)
                cX = int(M["m10"] / M["m00"])
                cY = int(M["m01"] / M["m00"])
    
                # draw the contour and center of the shape on the image
                cv2.drawContours(frame, [c], -1, (0, 255, 0), 2)
                cv2.circle(frame, (cX, cY), 4, (255, 0, 0), -1)
                
                #Collect coordinates
                data_points_x.append(cX)
                data_points_y.append(height - cY)

            cv2.imshow('frame', frame)

            k = cv2.waitKey(frametime) & 0xFF
            if k == 27:
                break
    
    except:
        pass   

        cap.release()
        cv2.destroyAllWindows()
    
    print(data_points_x, data_points_y)
    return data_points_x, data_points_y
