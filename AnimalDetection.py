import cv2
import numpy as np
# Load Yolo
net = cv2.dnn.readNet(r"YOLO Datasets\yolov.weights", r"YOLO Datasets\yolov.cfg")
classes = []
with open(r"YOLO Datasets\coco.names", "r") as f:
    classes = [line.strip() for line in f.readlines()]
layer_names = net.getLayerNames()
try:
    output_layers = [layer_names[i[0] - 1] for i in net.getUnconnectedOutLayers()]
except:
    output_layers = [layer_names[i - 1] for i in net.getUnconnectedOutLayers()]



def detection(img):
    class_ids = []
    confidences = []
    boxes = []
    height, width, channels = img.shape
        # Detecting objects
    blob = cv2.dnn.blobFromImage(img, 0.00392, (416, 416), (0, 0, 0), True, crop=False)
    net.setInput(blob)
    outs = net.forward(output_layers)
    for out in outs:
        for detection in out:
            scores = detection[5:]
            class_id = np.argmax(scores)
            confidence = scores[class_id]
            if confidence > 0.5:
                # Object detected
                center_x = int(detection[0] * width)
                center_y = int(detection[1] * height)
                w = int(detection[2] * width)
                h = int(detection[3] * height)

                    # Rectangle coordinates
                x = int(center_x - w / 2)
                y = int(center_y - h / 2)

                boxes.append([x, y, w, h])
                confidences.append(float(confidence))
                class_ids.append(class_id)

    indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)
    font = cv2.FONT_HERSHEY_SIMPLEX

    is_animal_found = False

    for i in range(len(boxes)):
        if i in indexes:
            x, y, w, h = boxes[i]
            label = str(classes[class_ids[i]]) 
            if label in ['bird','cat','dog','horse','sheep','cow','elephant','bear','zebra','giraffe']:

                print("Animal: ",label.capitalize())

                is_animal_found = True

                cv2.rectangle(img, (x, y), (x + w, y + h), (0,255,0), 1)
                (text_width, text_height) = cv2.getTextSize(label, font, fontScale=1.0, thickness=1)[0]
                box_coords = ((x,y), (x + text_width - 3, y - text_height - 2))
                cv2.putText(img, label.capitalize(), (x, y -10), font, 0.6, (0,0,255), 2)

    return img,is_animal_found

