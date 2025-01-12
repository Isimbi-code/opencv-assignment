import cv2

image = cv2.imread('assign.jpg')

cv2.rectangle(image, (263, 188), (985, 930), (0, 255, 0), 10)

cv2.addWeighted(cv2.rectangle(image.copy(), (790, 70), (1240, 175), (0, 0, 0), -1), 0.5, image, 1 - 0.5, 0, dst=image)

cv2.putText(image, 'RAH972U', (800, 150), cv2.FONT_HERSHEY_SIMPLEX, 3, (0, 255, 0), 7)

cv2.imshow('Image', image)

cv2.waitKey(0)

cv2.imwrite('assign_result.jpg', image)

cv2.destroyAllWindows()
