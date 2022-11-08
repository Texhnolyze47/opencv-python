import cv2
def contornos_objeto():
    # Se carga la imagen
    image = cv2.imread("resources/contorno.jpg")

    # se le da un tratamiento de color a la imagen
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # contornos de canny
    edged = cv2.Canny(gray, 30, 200)
    cv2.waitKey(0)

    # Se buscan los contornos
    contours, hierarchy = cv2.findContours(edged,
                                           cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    return contours
