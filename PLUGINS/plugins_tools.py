EQUIVALENCIAS_FORMATOS = {
    "jpg": "JPEG",
    "jpeg": "JPEG",
    "jpe": "JPEG",
    "jfif": "JPEG",
    "pjpeg": "JPEG",
    "pjp": "JPEG",
    "tif": "TIFF",
    "tiff": "TIFF",
    "png": "PNG",
    "bmp": "BMP",
    "dib": "BMP",
    "gif": "GIF",
    "webp": "WEBP",
    "ico": "ICO",
    "jp2": "JPEG 2000",
    "j2k": "JPEG 2000",
    "jpf": "JPEG 2000",
    "jpx": "JPEG 2000",
    "j2c": "JPEG 2000",
    "pbm": "PPM",
    "pgm": "PPM",
    "ppm": "PPM",
    "pcx": "PCX",
    "tga": "TGA",
    "xbm": "XBM",
    "eps": "EPS",
    "pdf": "PDF",
    "ps": "EPS"
}

# En el diccionario 'ayuda', actualiza la sección de UTILIDADES:
ayuda = {
    "comando_ayuda": """
📋 COMANDOS DISPONIBLES:

🖼️  PROCESAMIENTO BÁSICO:
  /marca_agua       - Agregar marca de agua a imagen
  /convertir_ico    - Convertir imagen a formato ICO
  /metadatos        - Mostrar metadatos EXIF
  /redimensionar    - Redimensionar imagen
  /cambiar_formato  - Cambiar formato de imagen
  /rotar            - Rotar imagen
  /espejo           - Voltear imagen (espejo)
  /filtro_bn        - Aplicar filtro blanco y negro
  /recortar         - Recortar imagen

📁 PROCESAMIENTO POR LOTES:
  /procesar_carpeta - Procesar múltiples imágenes en carpeta

📂 GESTIÓN DE CARPETAS:
  /conectar_carpeta - Conectar a una carpeta de trabajo
  /ver              - Ver contenido de carpeta conectada  
  /desconectar      - Desconectar carpeta actual

🔧 UTILIDADES:
  /soporte          - Mostrar formatos soportados
  /ayuda            - Mostrar esta ayuda
  /mas              - Información detallada
  /limpiar          - Limpiar consola
  /salir            - Salir de la aplicación
"""
}


mas = {
    "comando_mas": """
📖 INFORMACIÓN DETALLADA DE COMANDOS:

# ... (comandos existentes)

📂 GESTIÓN DE CARPETAS:

/conectar_carpeta
  Conecta el programa a una carpeta específica para trabajar más fácilmente
  con las imágenes. Puedes usar "PG C:\\RUTA" o cualquier ruta completa.
  Ejemplo: "PG C:\\Users\\TuUsuario\\Imágenes"

/ver
  Muestra el contenido detallado de la carpeta conectada, incluyendo:
  - Carpetas dentro de la carpeta conectada
  - Imágenes con información de tamaño y formato
  - Otros archivos
  - Estadísticas del contenido

/desconectar
  Desconecta la carpeta actual para poder conectar una nueva.
"""
}

mas = {
    "comando_mas": """
📖 INFORMACIÓN DETALLADA DE COMANDOS:

🖼️  /marca_agua
  Superpone una marca de agua sobre una imagen en una posición específica
  con transparencia y sombra para mejor legibilidad.

🎯 /convertir_ico
  Convierte una imagen cualquiera a formato .ico con múltiples resoluciones
  para uso como icono de aplicación.

📊 /metadatos
  Muestra los metadatos EXIF de una imagen, incluyendo información de cámara,
  configuración de exposición, GPS (si está disponible) y más.

📐 /redimensionar
  Redimensiona una imagen a un tamaño específico manteniendo la calidad
  usando el algoritmo LANCZOS.

🔄 /cambiar_formato
  Convierte una imagen a otro formato, manejando automáticamente la
  transparencia cuando es necesario.

🔄 /rotar
  Rota una imagen en cualquier ángulo (0-360 grados) con relleno automático.

🪞 /espejo
  Voltea una imagen horizontal o verticalmente (efecto espejo).

⚫ /filtro_bn
  Convierte una imagen a escala de grises (blanco y negro).

✂️  /recortar
  Recorta una imagen según coordenadas específicas.

📁 /procesar_carpeta
  Procesa todas las imágenes en una carpeta, permitiendo cambiar formato,
  redimensionar y organizar en carpeta de destino.

🎨 /soporte
  Lista completa de formatos de imagen soportados para abrir y guardar.
"""
}