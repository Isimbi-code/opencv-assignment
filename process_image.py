import cv2



image = cv2.imread('assign.png')


x, y, w, h = 60, 75, 250, 180  


cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)  


text = "RAH972U"
font = cv2.FONT_HERSHEY_SIMPLEX
font_scale = 1
font_thickness = 2
text_color = (0, 255, 0)  
text_size = cv2.getTextSize(text, font, font_scale, font_thickness)[0]
text_x = x
text_y = y - 10  

cv2.putText(image, text, (text_x, text_y), font, font_scale, text_color, font_thickness)


cv2.imwrite('assign_result.png', image)


'assign_result.png'
