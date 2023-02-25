# from os import remove
import re
import  time
import pyautogui
import pywhatkit
text="Hola buen día. \nNos comunicamos por parte de la Universidad Politécnica de Querétaro.\nEl motivo de este mensaje para mencionarle acerca de los cursos que tenemos ofertados para este nuevo cuatrimestre Enero-Abril 2023, los cuales son Inglés, Alemán, Frances y Business English.\nA continuación; le adjunto el TEMARIO/PLAN DE ESTUDIOS que corresponde a los Cursos Enero - Abril 2023.\n\nNOTA: Sí usted ya pertenece a la comunidad estudiantil, le recuerdo que actualmente contamos con tarifas preferenciales, mismas que podrá encontrar en dicho documento.\nAsí mismo, anexo los respectivos links de registro para los CURSOS en caso de que presente algún inconveniente con los que se encuentran en el temario/plan de estudios.\n\nLINK DE CURSOS OFERTADOS 2023: \nhttps://drive.google.com/file/d/1Y5_v3Yd6RI3U9Erdat9Ide7BapC6PKXk/view?usp=share_link \n\n LINK DE REGISTRO ALEMÁN: \nhttps://forms.gle/kHk4UQGimr6uGSLo9 \nLINK REGISTRO INGLÉS: \nhttps://forms.gle/rKy7VhF3H46SHS167 \nLINK REGISTRO FRANCÉS: \nhttps://forms.gle/CcS9Mm9Ze3FZTGCA9 \nLINK REGISTRO BUSINESS ENGLISH: \nhttps://forms.gle/WraRsqTmJk7xJ8N86 \n\nSin más que agregar, que tenga un excelente día. \n¡Reciba un cordial saludo!"
# text = "¡Hola buen día!\nNos comunicamos por parte de la Universidad Politécnica de Querétaro.\nEl motivo de este mensaje para ofertarle la promoción que tenemos para el examen de TOEFL ITP que tenemos disponible para usted.  El examen tiene un costo de $1,443.00 y será aplicado en las instalaciones de la universidad, el día 15 de diciembre del 2022 y el horario es de 4:00 a 6:00 pm.\n\nA continuación; le adjuntamos el LINK de REGISTRO\nLINK DE REGISTO: https://forms.gle/rqKF8apPptZHUsjt5 \n\n¡Esperamos que aproveche está gran oportunidad!\n\nSin más que agregar, que tenga un excelente día.\n¡Reciba un cordial saludo!"
# text=("Hola muy buenos días\nNos comunicamos por parte de la Universidad Politécnica de Querétaro.\nEl motivo de este mensaje es para recordarle que su referencia de pago de inscripción de inglés vence el día de hoy. \nEn caso de que haya tenido algún problema realizando su pago, favor de comunicárnoslo para brindarle la atención necesaria. \nEn caso de que necesite más tiempo para realizar su pago, notifíquelo por este medio para reactivar su referencia.\n\nQuedamos atentos a sus preguntas y comentarios, que tenga un buen día.")

print(text)


directorio = "C:/Users/Vadose/OneDrive/Documentos/Tags/Resultados/2311/"
numDeColumnas = 1
fi = open("datos.txt", "r",  encoding='utf8')

real  = []
multiArray = []

for linea in fi:
    if linea != '\n':
        linea = re.sub("\\n","",linea)
        linea = re.sub("\\t","",linea)

        real.append(linea)
                
for numero in real:    
    
    pywhatkit.sendwhatmsg_instantly(numero,text, 15, True, 10)
    
    # pywhatkit.sendwhats_image(numero, "",text, 15, True, 10)
    # time.sleep(1)
    # pyautogui.press("enter")
    print(numero)
