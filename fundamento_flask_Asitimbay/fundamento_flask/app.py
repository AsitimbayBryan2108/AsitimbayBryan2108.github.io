from flask import Flask, render_template

app = Flask(__name__)
app.config['STATIC_FOLDER'] = 'static'

@app.route('/')
def index():
    data = {
        'nombre': 'Bryan Anthony Asitimbay Sagñay',
        'fecha_nacimiento': '21 de agosto de 2003',
        'direccion': 'Av 25 De Julio, Guayaquil, Ecuador',
        'telefono': '0952164358',
        'email': 'asitimbaybryan@gmail.com',
        'experiencia': [
            {
                'empresa': 'Lactalis Ecuador',
                'puesto': 'Asistente de Sistemas',
                'periodo': 'Febrero 2020 - Marzo 2020',
                'descripcion': 'Mantenimiento'
            }
        ],
        'educacion': [
            {
                'anio': '2016',
                'colegio': 'Unidad Educativa Letras Y Vida',
                'titulo': 'Técnico en Servicios Informáticos'
            },
            {
                'anio': '2021',
                'universidad': 'Universidad de Guayaquil',
                'titulo': 'Ingeniería en Sistemas de la Información',
                'semestre': 'Cursando 4to Semestre'
            }
        ],
    'habilidades': [
        {
            'nombre': 'Inglés',
            'descripcion': 'Intermedio'
        },
        {
            'nombre': 'Lenguajes',
            'descripcion': 'HTML, Java y Python',
            'enlaces': [
                {
                    'nombre': 'HTML',
                    'enlace': 'https://github.com/AsitimbayBryan2108/HTML_y_Css/tree/main/Practicas'
                },
                {
                    'nombre': 'Java',
                    'enlace': 'https://github.com/AsitimbayBryan2108/Java/tree/main/Trabajos_Java'
                },
                {
                    'nombre': 'Python',
                    'enlace': 'https://github.com/AsitimbayBryan2108/Python/tree/main/Code'
                }
            ]
        },
        {
            'nombre': 'Gestión de bases de datos',
            'descripcion': 'PostgreSQL',
            'enlaces': [
                {
                    'nombre': 'PostgreSQL',
                    'enlace': 'https://github.com/AsitimbayBryan2108/PostgreSQL/tree/main/Programas%20Base%20de%20datos'
                }
            ]
        }
    ]
,
        'proyectos': [
            {
                'nombre': 'Proyecto Energia',
                'descripcion': 'Es un programa que realiza un seguimiento del consumo de energía de diferentes plantas generadoras en diferentes ciudades de Ecuador.',
                'imagen': 'images/Proyecto_PythonMenu.png',
                'enlace': 'https://github.com/AsitimbayBryan2108/Portafolio-Fundamentos-de-la-Programacion/tree/main/Proyecto_energia'
            },
            {
                'nombre': 'Proyecto Biblioteca',
                'descripcion': 'Es un programa que realiza un seguimiento a un libro, también muestra su código y precio.',
                'imagen': 'images/Proyecto_JavaBibliotecaMenu.png',
                'enlace': 'https://github.com/AsitimbayBryan2108/ProyectoBiblioteca/tree/main/ProyectoBiblioteca/Biblioteca'
            },
            {
                'nombre': 'Proyecto Solutions S.A',
                'descripcion': 'En este proyecto se creó una interfaz donde podemos designar técnicos, realizar cotizaciones, generar turnos y registrar clientes.',
                'imagen': 'images/Proyecto_JavaSolutionsMenu.png',
                'enlace': 'https://github.com/AsitimbayBryan2108/Proyecto_AntecendetesyRoles/tree/main/AntecedentesRolesEmpresa/AntecedentesRolesEmpresa'
            },
            {
                'nombre': 'Proyecto Chat',
                'descripcion': 'El proyecto de chat es una aplicación que permite la comunicación entre usuarios a través de mensajes de texto.',
                'imagen': 'images/Proyecto_JavaChatMenu.png',
                'enlace': 'https://github.com/AsitimbayBryan2108/Proyecto_Chat/tree/main/ChatWhatsapp'
            }
        ]
    }

    return render_template('index.html', data=data)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
