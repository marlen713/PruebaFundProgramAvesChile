import requests
from templete_html import generar_template_html

# AQUI DECLARO UNA FUNCION PARA QUE OBTENGA LOS DATOS DE LA API Y LAS DEVUELVE EN FORMATO JSON
def obtener_datos():
    url = 'https://aves.ninjas.cl/api/birds'
    response = requests.get(url)
    return response.json()




#Este código esta llamando a una función llamada "obtener_datos()" que posiblemente obtiene alguna información sobre aves. 
#La función "obtener_datos()" podría estar leyendo datos de un archivo, haciendo una solicitud a una API, o realizando alguna 
#otra operación para obtener información sobre aves. Una vez que se obtiene la información, se guarda en la variable "datos_aves".
datos_aves = obtener_datos()

#Generara el string de la plantilla. Esta función genera una plantilla de código HTML utilizando los datos de aves proporcionados. 
#La plantilla HTML creada mostrará información sobre las aves, como su nombre, especie, tamaño, hábitat, etc. 
plantilla_str = generar_template_html(datos_aves)

#Genera en un archivo.html creado en la funcion generar_template_html
with open('aves_de_chile.html', 'w') as f:
        f.write(plantilla_str)

print("Archivo HTML generado exitosamente: aves_de_chile.html")