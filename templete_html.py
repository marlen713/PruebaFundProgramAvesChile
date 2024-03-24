from string import Template

def generar_template_html(data):
    
    # Definición de la plantilla HTML utilizando la clase Template
    html_template = Template("""
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Aves de Chile</title>
        <style>
            .ave {
                width: 23%;
                margin-bottom: 20px;
            }
            .ave img {
                width: 100%;
                height: auto;
            }
        </style>
    </head>
    <body>
        <h1>Aves de Chile</h1>
        <div class="aves-container">
            $lista_aves
        </div>
    </body>
    </html>
    """)


    lista_aves = ""
# AQUI VA INTERECTUANDO SOBRE LOS DATOS Y CONSTRUYE LA LISTA DE LAS AVES 
    for ave in data:
        lista_aves += """
            <div class="ave">
                <h2>{spanish} / {english}</h2>
                <img src="{image}" alt="{spanish}">
            </div>
        """.format(spanish=ave['name']['spanish'], english=ave['name']['english'], image=ave['images']['main'])
        
    return html_template.substitute(lista_aves=lista_aves)