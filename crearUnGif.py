import imageio.v3 as iio # Importamos la librería imageio

     # Creamos una lista con los nombres de los archivos que queremos incluir en el gif/directorio completo si no quiere funcionar
filenames = [
    'D:/ProyectosPython/creaUnGif/img1.png',
    'D:/ProyectosPython/creaUnGif/img2.png',
    'D:/ProyectosPython/creaUnGif/img3.png',
    'D:/ProyectosPython/creaUnGif/img4.png'
    ]
# Creamos una lista vacía para almacenar las imágenes
images = [ ]
# Iteramos sobre la lista de nombres de archivos
for filename in filenames:
  # Leemos cada imagen y la almacenamos en la lista de imágenes
  images.append(iio.imread(filename))
""" Creamos el gif con las imágenes almacenadas en la lista esto indicando un directorio para guardarlo y le asignamos una duración de 500 milisegundos por imagen con 
  bucle infinito para que se repita constantemente"""
iio.imwrite('spidercat.gif', images, duration = 500, loop = 0)
