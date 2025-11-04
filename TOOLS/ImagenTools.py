from PIL import Image, ImageDraw, ImageFont, ImageEnhance
import os
from PLUGINS.plugins_tools import EQUIVALENCIAS_FORMATOS

class Imagen_Tools:
    def __init__(self):
        pass

    @staticmethod
    def transformar_IMG_ext(origen, destino, extension):
        if not os.path.isfile(origen):
            print(f"❌ Error: El archivo origen '{origen}' no existe.")
            return False
        if not extension or not isinstance(extension, str):
            print(f"❌ Error: La extensión '{extension}' no es válida.")
            return False
        try:
            imagen = Image.open(origen)
            formato = EQUIVALENCIAS_FORMATOS.get(extension.lower(), extension.upper())

            if formato in ["JPEG", "JPG"]:
                if imagen.mode in ("RGBA", "LA") or (imagen.mode == "P" and "transparency" in imagen.info):
                    imagen = imagen.convert("RGB")

            ruta_salida = f"{destino}.{extension.lower()}"
            imagen.save(ruta_salida, format=formato)
            print(f"✅ {origen} convertida a {ruta_salida}")
            return True
        except Exception as e:
            print(f"❌ Error al convertir {origen}: {e}")
            return False

    @staticmethod
    def configurarIMG_enCarpetas(carpeta_origen, carpeta_destino, extension_salida, ancho=None, alto=None):
        if not os.path.exists(carpeta_origen) or not os.path.isdir(carpeta_origen):
            print(f"❌ Error: La carpeta origen '{carpeta_origen}' no existe o no es un directorio.")
            return False
        if not extension_salida or not isinstance(extension_salida, str):
            print(f"❌ Error: La extensión de salida '{extension_salida}' no es válida.")
            return False
        if ancho is not None and (not isinstance(ancho, int) or ancho <= 0):
            print(f"❌ Error: El ancho '{ancho}' debe ser un entero positivo.")
            return False
        if alto is not None and (not isinstance(alto, int) or alto <= 0):
            print(f"❌ Error: El alto '{alto}' debe ser un entero positivo.")
            return False

        if not os.path.exists(carpeta_destino):
            try:
                os.makedirs(carpeta_destino)
            except Exception as e:
                print(f"❌ Error al crear carpeta destino '{carpeta_destino}': {e}")
                return False

        extensiones_soportadas = [ext.lower() for ext in Image.registered_extensions().keys()]
        formato = EQUIVALENCIAS_FORMATOS.get(extension_salida.lower(), extension_salida.upper())

        procesadas = 0
        errores = 0
        
        for archivo in os.listdir(carpeta_origen):
            if any(archivo.lower().endswith(ext) for ext in extensiones_soportadas):
                ruta_origen = os.path.join(carpeta_origen, archivo)
                try:
                    imagen = Image.open(ruta_origen)
                    
                    if formato == "JPEG":
                        if imagen.mode in ("RGBA", "LA") or (imagen.mode == "P" and "transparency" in imagen.info):
                            imagen = imagen.convert("RGB")

                    if ancho is not None and alto is not None:
                        imagen = imagen.resize((ancho, alto), Image.Resampling.LANCZOS)

                    nombre_sin_ext = os.path.splitext(archivo)[0]
                    ruta_destino = os.path.join(carpeta_destino, f"{nombre_sin_ext}.{extension_salida.lower()}")

                    imagen.save(ruta_destino, format=formato)
                    print(f"✅ {archivo} → {extension_salida.upper()}")
                    procesadas += 1
                except Exception as e:
                    print(f"❌ Error procesando {archivo}: {e}")
                    errores += 1
        
        print(f"\n📊 Resumen: {procesadas} procesadas, {errores} errores")
        return procesadas > 0

    @staticmethod
    def redimensionar_img(img_origen, img_destino, ancho, alto):
        if not os.path.isfile(img_origen):
            print(f"❌ Error: La imagen origen '{img_origen}' no existe.")
            return False
        if not isinstance(ancho, int) or ancho <= 0:
            print(f"❌ Error: El ancho '{ancho}' debe ser un entero positivo.")
            return False
        if not isinstance(alto, int) or alto <= 0:
            print(f"❌ Error: El alto '{alto}' debe ser un entero positivo.")
            return False

        try:
            imagen = Image.open(img_origen)
            imagen_tratada = imagen.resize((ancho, alto), Image.Resampling.LANCZOS)
            imagen_tratada.save(img_destino)
            print(f"✅ Imagen redimensionada: {img_destino}")
            return True
        except Exception as e:
            print(f"❌ Error al redimensionar imagen: {e}")
            return False

    @staticmethod
    def convertir_aICO(imagen, resultado):
        if not os.path.isfile(imagen):
            print(f"❌ Error: La imagen '{imagen}' no existe.")
            return False
        try:
            img = Image.open(imagen)
            img = img.convert("RGBA")
            
            # Crear múltiples tamaños para el ICO (requerido para buena calidad)
            sizes = [(16, 16), (32, 32), (48, 48), (64, 64), (128, 128), (256, 256)]
            icono = Image.new("RGBA", (256, 256), (0, 0, 0, 0))
            
            # Redimensionar manteniendo relación de aspecto
            img.thumbnail((256, 256), Image.Resampling.LANCZOS)
            icono.paste(img, ((256 - img.size[0]) // 2, (256 - img.size[1]) // 2))
            
            ruta_salida = f"{resultado}.ico"
            icono.save(ruta_salida, format='ICO', sizes=sizes)
            print(f"✅ Icono creado: {ruta_salida}")
            return True
        except Exception as e:
            print(f"❌ Error al convertir a ICO: {e}")
            return False

    @staticmethod
    def mostrar_metaDATOS(imagen):
        from PIL import ExifTags
        if not os.path.isfile(imagen):
            print(f"❌ Error: La imagen '{imagen}' no existe.")
            return False
        try:
            img = Image.open(imagen)
            print("\n📊 INFORMACIÓN BÁSICA")
            print("=" * 40)
            print(f"📁 Archivo: {os.path.basename(imagen)}")
            print(f"📐 Formato: {img.format}")
            print(f"📏 Tamaño: {img.size[0]} x {img.size[1]} píxeles")
            print(f"🎨 Modo de color: {img.mode}")
            if "dpi" in img.info:
                dpi_x, dpi_y = img.info["dpi"]
                print(f"📐 DPI: {dpi_x} x {dpi_y}")
            
            print("\n📋 METADATOS EXIF")
            print("=" * 40)
            exif = img.getexif()
            if not exif:
                print("ℹ️ No hay metadatos EXIF en la imagen")
            else:
                for tag, value in exif.items():
                    nombre = ExifTags.TAGS.get(tag, tag)
                    if tag == 296:
                        unidades = {1: "sin unidad", 2: "pulgadas", 3: "centímetros"}
                        value = unidades.get(value, value)
                    print(f"  {nombre}: {value}")
            
            print("\n✅ Metadatos mostrados correctamente")
            return True
        except Exception as e:
            print(f"❌ Error al mostrar metadatos: {e}")
            return False

    @staticmethod
    def agregar_marca_agua(imagen, salida, texto="Tu marca de agua", posicion=(10, 10), tamaño_fuente=20):
        if not os.path.isfile(imagen):
            print(f"❌ Error: La imagen '{imagen}' no existe.")
            return False
        if not isinstance(texto, str):
            print(f"❌ Error: El texto debe ser una cadena de caracteres.")
            return False
        if (not isinstance(posicion, tuple) or len(posicion) != 2 or
                not all(isinstance(coord, int) for coord in posicion)):
            print(f"❌ Error: La posición debe ser una tupla de dos enteros.")
            return False
        if not isinstance(tamaño_fuente, int) or tamaño_fuente <= 0:
            print(f"❌ Error: El tamaño de fuente debe ser un entero positivo.")
            return False
        try:
            img = Image.open(imagen).convert("RGBA")
            capa = Image.new("RGBA", img.size, (255, 255, 255, 0))
            draw = ImageDraw.Draw(capa)
            
            # Intentar usar fuentes del sistema
            fuentes_posibles = [
                "arial.ttf", 
                "Arial.ttf",
                "/usr/share/fonts/truetype/freefont/FreeMono.ttf",
                "C:/Windows/Fonts/arial.ttf"
            ]
            
            fuente = None
            for fuente_path in fuentes_posibles:
                try:
                    fuente = ImageFont.truetype(fuente_path, tamaño_fuente)
                    break
                except IOError:
                    continue
            
            if fuente is None:
                fuente = ImageFont.load_default()
                print("⚠️ Usando fuente por defecto (arial.ttf no encontrada)")
            
            # Calcular tamaño del texto para posición automática
            bbox = draw.textbbox((0, 0), texto, font=fuente)
            texto_ancho = bbox[2] - bbox[0]
            texto_alto = bbox[3] - bbox[1]
            
            # Ajustar posición si se sale de la imagen
            x, y = posicion
            if x + texto_ancho > img.size[0]:
                x = img.size[0] - texto_ancho - 10
            if y + texto_alto > img.size[1]:
                y = img.size[1] - texto_alto - 10
            
            # Dibujar texto con sombra para mejor legibilidad
            draw.text((x+1, y+1), texto, font=fuente, fill=(0, 0, 0, 100))
            draw.text((x, y), texto, font=fuente, fill=(255, 255, 255, 180))
            
            img_final = Image.alpha_composite(img, capa)
            img_final.save(salida)
            print(f"✅ Marca de agua agregada: {salida}")
            return True
        except Exception as e:
            print(f"❌ Error al agregar marca de agua: {e}")
            return False

    # NUEVAS FUNCIONES AGREGADAS

    @staticmethod
    def rotar_imagen(imagen, salida, angulo):
        """Rota una imagen el ángulo especificado"""
        if not os.path.isfile(imagen):
            print(f"❌ Error: La imagen '{imagen}' no existe.")
            return False
        try:
            img = Image.open(imagen)
            img_rotada = img.rotate(angulo, expand=True)
            img_rotada.save(salida)
            print(f"✅ Imagen rotada {angulo}°: {salida}")
            return True
        except Exception as e:
            print(f"❌ Error al rotar imagen: {e}")
            return False

    @staticmethod
    def voltear_imagen(imagen, salida, direccion):
        """Voltea una imagen horizontal o verticalmente"""
        if not os.path.isfile(imagen):
            print(f"❌ Error: La imagen '{imagen}' no existe.")
            return False
        try:
            img = Image.open(imagen)
            if direccion == "horizontal":
                img_volteada = img.transpose(Image.FLIP_LEFT_RIGHT)
            elif direccion == "vertical":
                img_volteada = img.transpose(Image.FLIP_TOP_BOTTOM)
            else:
                print("❌ Error: Dirección debe ser 'horizontal' o 'vertical'")
                return False
            
            img_volteada.save(salida)
            print(f"✅ Imagen volteada ({direccion}): {salida}")
            return True
        except Exception as e:
            print(f"❌ Error al voltear imagen: {e}")
            return False

    @staticmethod
    def filtro_blanco_negro(imagen, salida):
        """Convierte una imagen a blanco y negro"""
        if not os.path.isfile(imagen):
            print(f"❌ Error: La imagen '{imagen}' no existe.")
            return False
        try:
            img = Image.open(imagen)
            img_bn = img.convert("L")
            img_bn.save(salida)
            print(f"✅ Filtro blanco y negro aplicado: {salida}")
            return True
        except Exception as e:
            print(f"❌ Error al aplicar filtro: {e}")
            return False

    @staticmethod
    def recortar_imagen(imagen, salida, coordenadas):
        """Recorta una imagen según las coordenadas especificadas"""
        if not os.path.isfile(imagen):
            print(f"❌ Error: La imagen '{imagen}' no existe.")
            return False
        try:
            img = Image.open(imagen)
            img_recortada = img.crop(coordenadas)
            img_recortada.save(salida)
            print(f"✅ Imagen recortada: {salida}")
            return True
        except Exception as e:
            print(f"❌ Error al recortar imagen: {e}")
            return False

    @staticmethod
    def ajustar_brillo(imagen, salida, factor):
        """Ajusta el brillo de una imagen"""
        if not os.path.isfile(imagen):
            print(f"❌ Error: La imagen '{imagen}' no existe.")
            return False
        try:
            img = Image.open(imagen)
            enhancer = ImageEnhance.Brightness(img)
            img_mejorada = enhancer.enhance(factor)
            img_mejorada.save(salida)
            print(f"✅ Brillo ajustado (factor: {factor}): {salida}")
            return True
        except Exception as e:
            print(f"❌ Error al ajustar brillo: {e}")
            return False

    @property
    def SOPORTE_IMG(self):
        formatos = ['BMP', 'DIB', 'EPS', 'GIF', 'ICO', 'PCX', 'PNG', 'PPM', 'SGI', 'TGA', 'XBM', 'JPEG', 'TIFF', 'WebP', 'JPEG 2000']
        return f"🎨 Formatos soportados: {', '.join(formatos)}"