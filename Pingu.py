import os
import sys
import platform
from colorama import init, Fore, Style
# Agregar la carpeta tools al path para imports
current_dir = os.path.dirname(os.path.abspath(__file__))
tools_dir = os.path.join(current_dir, 'tools')
if tools_dir not in sys.path:
    sys.path.append(tools_dir)

try:
    from TOOLS.ImagenTools import Imagen_Tools as img
    from PLUGINS.plugins_tools import ayuda, mas
except ImportError as e:
    print(f"❌ Error importando módulos: {e}")
    print("📂 Directorio actual:", os.getcwd())
    if os.path.exists('tools'):
        print("📂 Archivos en tools:", os.listdir('tools'))
    input("Presione Enter para salir...")
    sys.exit(1)


# Inicializar colorama para compatibilidad con Windows
init(autoreset=True)

# Configuración de colores
COLOR_TITULO = Fore.CYAN + Style.BRIGHT
COLOR_MENU = Fore.GREEN
COLOR_ERROR = Fore.RED + Style.BRIGHT
COLOR_EXITO = Fore.GREEN + Style.BRIGHT
COLOR_ADVERTENCIA = Fore.YELLOW
COLOR_INFO = Fore.BLUE
COLOR_INPUT = Fore.MAGENTA
COLOR_DESTACADO = Fore.YELLOW + Style.BRIGHT

# Variable global para la carpeta conectada
carpeta_conectada = None

# Banner de la aplicación
name = """
 ____ ___ _   _  ____ _   _ 
|  _ \_ _| \ | |/ ___| | | |
| |_) | ||  \| | |  _| | | |
|  __/| || |\  | |_| | |_| |
|_|  |___|_| \_|\____|\___/ 
 
"""

def resolver_ruta(ruta_usuario):
    """
    Resuelve la ruta de un archivo/carpeta considerando la carpeta conectada.
    Si la ruta es relativa o solo un nombre, busca en la carpeta conectada.
    Si es una ruta absoluta, la usa directamente.
    """
    global carpeta_conectada
    
    # Si no hay ruta, retornar None
    if not ruta_usuario:
        return None
    
    # Si es una ruta absoluta y existe, usarla directamente
    if os.path.isabs(ruta_usuario):
        return ruta_usuario
    
    # Si existe en el directorio actual, usarla
    if os.path.exists(ruta_usuario):
        return os.path.abspath(ruta_usuario)
    
    # Si hay carpeta conectada, buscar ahí
    if carpeta_conectada:
        ruta_en_carpeta = os.path.join(carpeta_conectada, ruta_usuario)
        if os.path.exists(ruta_en_carpeta):
            return ruta_en_carpeta
        # Retornar la ruta aunque no exista (para archivos de salida)
        return ruta_en_carpeta
    
    # Si no hay carpeta conectada, usar ruta relativa al directorio actual
    return os.path.abspath(ruta_usuario)

def listar_imagenes_carpeta():
    """Muestra lista numerada de imágenes en la carpeta conectada"""
    global carpeta_conectada
    
    if not carpeta_conectada:
        return []
    
    extensiones_imagen = ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.webp', '.ico']
    imagenes = []
    
    try:
        for archivo in os.listdir(carpeta_conectada):
            if any(archivo.lower().endswith(ext) for ext in extensiones_imagen):
                imagenes.append(archivo)
        
        if imagenes:
            print(COLOR_INFO + "\n📸 Imágenes disponibles en carpeta conectada:")
            for idx, img_name in enumerate(sorted(imagenes), 1):
                print(COLOR_MENU + f"  {idx}. {img_name}")
            print(COLOR_INFO + "💡 Puedes usar el nombre o el número\n")
        
        return sorted(imagenes)
    except Exception as e:
        print(COLOR_ERROR + f"Error al listar imágenes: {e}")
        return []

def limpiar_consola():
    """Limpia la consola de forma compatible con diferentes sistemas"""
    os.system('cls' if os.name == 'nt' else 'clear')

def mostrar_banner():
    """Muestra el banner de la aplicación"""
    limpiar_consola()
    print(COLOR_TITULO + name)
    print(COLOR_INFO + "=" * 60)
    print(COLOR_MENU + "     Herramienta Profesional de Procesamiento de Imágenes")
    print(COLOR_INFO + "=" * 60)
    
    # Mostrar información del sistema
    print(COLOR_DESTACADO + f"💻 Sistema: {platform.system()} {platform.release()}")
    
    # Mostrar carpeta conectada si existe
    global carpeta_conectada
    if carpeta_conectada:
        print(COLOR_EXITO + f"📁 Carpeta conectada: {carpeta_conectada}")
        # Contar imágenes
        try:
            extensiones_imagen = ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.webp', '.ico']
            imagenes = [f for f in os.listdir(carpeta_conectada) 
                       if any(f.lower().endswith(ext) for ext in extensiones_imagen)]
            print(COLOR_INFO + f"🖼️  Imágenes encontradas: {len(imagenes)}")
        except:
            pass
    print()

def menu():
    """Muestra el menú principal"""
    mostrar_banner()
    print()
    print(COLOR_MENU + "🗂️  COMANDOS PRINCIPALES:")
    print(COLOR_MENU + "-" * 40)
    print(COLOR_INFO + "  /ayuda           " + Fore.WHITE + "- Información sobre comandos")
    print(COLOR_INFO + "  /mas             " + Fore.WHITE + "- Más información sobre la aplicación")
    print(COLOR_INFO + "  /limpiar         " + Fore.WHITE + "- Limpiar la consola")
    print(COLOR_INFO + "  /salir           " + Fore.WHITE + "- Salir de la aplicación")
    print()
    
    # Mostrar estado de carpeta conectada
    global carpeta_conectada
    if carpeta_conectada:
        print(COLOR_EXITO + "  /ver             " + Fore.WHITE + "- Ver contenido de carpeta conectada")
        print(COLOR_EXITO + "  /listar          " + Fore.WHITE + "- Listar solo imágenes")
        print(COLOR_INFO + "  /desconectar     " + Fore.WHITE + "- Desconectar carpeta actual")
    else:
        print(COLOR_INFO + "  /conectar_carpeta " + Fore.WHITE + "- Conectar a una carpeta de trabajo")
    print()

def obtener_entero(mensaje, min_val=1, max_val=None, opcional=False):
    """Obtiene un valor entero validado del usuario"""
    while True:
        try:
            valor = input(COLOR_INPUT + mensaje).strip()
            if opcional and not valor:
                return None
            num = int(valor)
            if num < min_val:
                print(COLOR_ERROR + f"Error: El valor debe ser al menos {min_val}")
                continue
            if max_val and num > max_val:
                print(COLOR_ERROR + f"Error: El valor no puede ser mayor que {max_val}")
                continue
            return num
        except ValueError:
            print(COLOR_ERROR + "Error: Por favor ingrese un número entero válido")

def obtener_float(mensaje, min_val=0.1, max_val=10.0, opcional=False):
    """Obtiene un valor float validado del usuario"""
    while True:
        try:
            valor = input(COLOR_INPUT + mensaje).strip()
            if opcional and not valor:
                return None
            num = float(valor)
            if num < min_val:
                print(COLOR_ERROR + f"Error: El valor debe ser al menos {min_val}")
                continue
            if max_val and num > max_val:
                print(COLOR_ERROR + f"Error: El valor no puede ser mayor que {max_val}")
                continue
            return num
        except ValueError:
            print(COLOR_ERROR + "Error: Por favor ingrese un número válido")

def obtener_texto(mensaje, opcional=False):
    """Obtiene texto validado del usuario"""
    while True:
        texto = input(COLOR_INPUT + mensaje).strip()
        if opcional or texto:
            return texto if texto else None
        print(COLOR_ERROR + "Error: Este campo no puede estar vacío")

def obtener_archivo(mensaje, mostrar_lista=True):
    """
    Obtiene la ruta de un archivo validado.
    Si hay carpeta conectada, permite usar nombres relativos.
    """
    global carpeta_conectada
    
    # Mostrar lista de imágenes si hay carpeta conectada
    imagenes_disponibles = []
    if carpeta_conectada and mostrar_lista:
        imagenes_disponibles = listar_imagenes_carpeta()
    
    while True:
        ruta_input = obtener_texto(mensaje)
        
        # Si es un número y hay imágenes listadas
        if ruta_input.isdigit() and imagenes_disponibles:
            idx = int(ruta_input) - 1
            if 0 <= idx < len(imagenes_disponibles):
                ruta_input = imagenes_disponibles[idx]
                print(COLOR_EXITO + f"✅ Seleccionado: {ruta_input}")
            else:
                print(COLOR_ERROR + "Error: Número fuera de rango")
                continue
        
        # Resolver la ruta
        ruta_completa = resolver_ruta(ruta_input)
        
        if os.path.isfile(ruta_completa):
            return ruta_completa
        
        print(COLOR_ERROR + f"Error: El archivo '{ruta_input}' no se encuentra")
        if carpeta_conectada:
            print(COLOR_INFO + f"💡 Buscado en: {carpeta_conectada}")
            print(COLOR_INFO + "💡 Usa /ver o /listar para ver archivos disponibles")

def obtener_archivo_salida(mensaje):
    """
    Obtiene el nombre de un archivo de salida.
    Si hay carpeta conectada, lo guarda ahí automáticamente.
    """
    while True:
        nombre = obtener_texto(mensaje)
        ruta_completa = resolver_ruta(nombre)
        
        # Verificar si ya existe
        if os.path.exists(ruta_completa):
            sobrescribir = input(COLOR_ADVERTENCIA + 
                               f"⚠️  El archivo '{nombre}' ya existe. ¿Sobrescribir? (s/n): ").strip().lower()
            if sobrescribir != 's':
                continue
        
        if carpeta_conectada:
            print(COLOR_INFO + f"💾 Se guardará en: {ruta_completa}")
        
        return ruta_completa

def obtener_carpeta(mensaje, crear=False):
    """Obtiene la ruta de una carpeta validada"""
    while True:
        ruta = obtener_texto(mensaje)
        ruta_completa = resolver_ruta(ruta)
        
        if os.path.isdir(ruta_completa):
            return ruta_completa
        if crear and not os.path.exists(ruta_completa):
            try:
                os.makedirs(ruta_completa)
                print(COLOR_EXITO + f"✅ Carpeta creada: {ruta_completa}")
                return ruta_completa
            except Exception as e:
                print(COLOR_ERROR + f"Error al crear carpeta: {e}")
        else:
            print(COLOR_ERROR + f"Error: La carpeta '{ruta}' no existe")

def obtener_coordenadas(mensaje):
    """Obtiene coordenadas en formato tupla"""
    while True:
        try:
            print(COLOR_INPUT + mensaje)
            x = obtener_entero("Coordenada X: ")
            y = obtener_entero("Coordenada Y: ")
            return (x, y)
        except Exception as e:
            print(COLOR_ERROR + f"Error en las coordenadas: {e}")

def conectar_carpeta():
    """Conecta a una carpeta específica"""
    global carpeta_conectada
    print(COLOR_INFO + "\n" + "📂 CONECTAR CARPETA")
    print(COLOR_INFO + "-" * 30)
    
    ruta = obtener_texto("Ingresa la ruta de la carpeta: ")
    
    # Procesar el comando PG si se usa
    if ruta.upper().startswith("PG "):
        ruta = ruta[3:]
    
    # Expandir variables de entorno y rutas relativas
    ruta = os.path.expanduser(ruta)
    ruta = os.path.expandvars(ruta)
    
    if os.path.isdir(ruta):
        carpeta_conectada = os.path.abspath(ruta)
        print(COLOR_EXITO + f"✅ Carpeta conectada: {carpeta_conectada}")
        
        # Mostrar cantidad de imágenes
        try:
            extensiones_imagen = ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.webp', '.ico']
            imagenes = [f for f in os.listdir(carpeta_conectada) 
                       if any(f.lower().endswith(ext) for ext in extensiones_imagen)]
            print(COLOR_INFO + f"🖼️  Se encontraron {len(imagenes)} imágenes")
            print(COLOR_INFO + "💡 Ahora puedes usar solo el nombre de las imágenes en los comandos")
        except Exception as e:
            print(COLOR_ADVERTENCIA + f"⚠️  Error al leer carpeta: {e}")
        
        return True
    else:
        print(COLOR_ERROR + f"❌ La carpeta no existe: {ruta}")
        return False

def ver_contenido_carpeta():
    """Muestra el contenido de la carpeta conectada"""
    global carpeta_conectada
    if not carpeta_conectada:
        print(COLOR_ERROR + "❌ No hay ninguna carpeta conectada. Use /conectar_carpeta primero.")
        return
    
    print(COLOR_INFO + f"\n📂 CONTENIDO DE: {carpeta_conectada}")
    print(COLOR_INFO + "=" * 60)
    
    try:
        # Obtener lista de archivos y carpetas
        contenido = os.listdir(carpeta_conectada)
        
        if not contenido:
            print(COLOR_ADVERTENCIA + "📂 La carpeta está vacía")
            return
        
        # Separar archivos y carpetas
        carpetas = []
        archivos = []
        imagenes = []
        
        for item in contenido:
            ruta_completa = os.path.join(carpeta_conectada, item)
            if os.path.isdir(ruta_completa):
                carpetas.append(item)
            else:
                archivos.append(item)
                # Verificar si es imagen por extensión
                extensiones_imagen = ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.webp', '.ico']
                if any(item.lower().endswith(ext) for ext in extensiones_imagen):
                    imagenes.append(item)
        
        # Mostrar carpetas
        if carpetas:
            print(COLOR_TITULO + "\n📂 CARPETAS:")
            for carpeta in sorted(carpetas):
                print(COLOR_INFO + f"  📁 {carpeta}")
        
        # Mostrar imágenes
        if imagenes:
            print(COLOR_TITULO + "\n🖼️  IMÁGENES:")
            try:
                from PIL import Image
                for idx, imagen in enumerate(sorted(imagenes), 1):
                    ruta_imagen = os.path.join(carpeta_conectada, imagen)
                    try:
                        img_pil = Image.open(ruta_imagen)
                        tamaño = img_pil.size
                        formato = img_pil.format
                        img_pil.close()
                        print(COLOR_EXITO + f"  {idx}. 🖼️  {imagen} - {tamaño[0]}x{tamaño[1]} - {formato}")
                    except Exception:
                        print(COLOR_EXITO + f"  {idx}. 🖼️  {imagen}")
            except ImportError:
                for idx, imagen in enumerate(sorted(imagenes), 1):
                    print(COLOR_EXITO + f"  {idx}. 🖼️  {imagen}")
        
        # Mostrar otros archivos
        otros_archivos = [archivo for archivo in archivos if archivo not in imagenes]
        if otros_archivos:
            print(COLOR_TITULO + "\n📄 OTROS ARCHIVOS:")
            for archivo in sorted(otros_archivos):
                ruta_archivo = os.path.join(carpeta_conectada, archivo)
                tamaño = os.path.getsize(ruta_archivo)
                tamaño_kb = tamaño / 1024
                print(COLOR_MENU + f"  📄 {archivo} - {tamaño_kb:.1f} KB")
        
        # Estadísticas
        print(COLOR_INFO + "\n" + "=" * 60)
        print(COLOR_TITULO + f"📊 ESTADÍSTICAS:")
        print(COLOR_INFO + f"  📂 Carpetas: {len(carpetas)}")
        print(COLOR_INFO + f"  🖼️  Imágenes: {len(imagenes)}")
        print(COLOR_INFO + f"  📄 Otros archivos: {len(otros_archivos)}")
        print(COLOR_INFO + f"  📊 Total: {len(contenido)} elementos")
        
    except PermissionError:
        print(COLOR_ERROR + f"❌ Error de permisos: No se puede acceder a la carpeta")
    except Exception as e:
        print(COLOR_ERROR + f"❌ Error al leer la carpeta: {e}")

def desconectar_carpeta():
    """Desconecta la carpeta actual"""
    global carpeta_conectada
    if carpeta_conectada:
        print(COLOR_EXITO + f"✅ Carpeta desconectada: {carpeta_conectada}")
        carpeta_conectada = None
    else:
        print(COLOR_ADVERTENCIA + "ℹ️ No hay ninguna carpeta conectada")

def procesar_comando_marca_agua():
    """Procesa el comando de marca de agua"""
    print(COLOR_INFO + "\n" + "💧 AGREGAR MARCA DE AGUA")
    print(COLOR_INFO + "-" * 30)
    
    nombre_img = obtener_archivo("Nombre de la imagen con extensión: ")
    nombre_salida = obtener_archivo_salida("Nombre de imagen resultado (con extensión): ")
    marca_agua = obtener_texto("Ingresa la marca de agua: ")
    
    print(COLOR_INFO + "📍 Posición de la marca de agua:")
    posicion_marca = obtener_coordenadas("Ejemplo: para (20,20) ingresa:")
    
    tamaño_letra = obtener_entero("Tamaño de letra (8-100): ", 8, 100)
    
    # Confirmar operación
    print(f"\n📋 RESUMEN:")
    print(f"   Imagen: {os.path.basename(nombre_img)}")
    print(f"   Salida: {os.path.basename(nombre_salida)}")
    print(f"   Marca: {marca_agua}")
    print(f"   Posición: {posicion_marca}")
    print(f"   Tamaño letra: {tamaño_letra}")
    
    confirmar = input(COLOR_INPUT + "\n✅ ¿Continuar? (s/n) [s]: ").strip().lower()
    if confirmar != 'n':
        return img.agregar_marca_agua(nombre_img, nombre_salida, marca_agua, posicion_marca, tamaño_letra)
    return False

def procesar_comando_convertir_ico():
    """Procesa el comando de conversión a ICO"""
    print(COLOR_INFO + "\n" + "🎯 CONVERTIR A FORMATO ICO")
    print(COLOR_INFO + "-" * 30)
    
    nombre_img_to_ico = obtener_archivo("Nombre de la imagen con extensión: ")
    icono_resultado = obtener_texto("Nombre del resultado sin extensión: ")
    
    # Resolver ruta de salida
    if carpeta_conectada:
        icono_resultado = resolver_ruta(icono_resultado)
    
    return img.convertir_aICO(nombre_img_to_ico, icono_resultado)

def procesar_comando_metadatos():
    """Procesa el comando de metadatos"""
    print(COLOR_INFO + "\n" + "📊 MOSTRAR METADATOS")
    print(COLOR_INFO + "-" * 30)
    
    img_metadatos = obtener_archivo("Ingrese el nombre de la imagen con extensión: ")
    return img.mostrar_metaDATOS(img_metadatos)

def procesar_comando_redimensionar():
    """Procesa el comando de redimensionar"""
    print(COLOR_INFO + "\n" + "📏 REDIMENSIONAR IMAGEN")
    print(COLOR_INFO + "-" * 30)
    
    img_aMODIFICAR = obtener_archivo("Ingresa el nombre de la imagen con extensión: ")
    img_Modificada = obtener_archivo_salida("Nombre de la imagen resultado (con extensión): ")
    ancho_img = obtener_entero("Ancho de la imagen: ", 1)
    alto_img = obtener_entero("Alto de la imagen: ", 1)
    
    return img.redimensionar_img(img_aMODIFICAR, img_Modificada, ancho_img, alto_img)

def procesar_comando_procesar_carpeta():
    """Procesa el comando de procesar carpeta"""
    print(COLOR_INFO + "\n" + "📁 PROCESAR IMÁGENES EN CARPETA")
    print(COLOR_INFO + "-" * 30)
    
    carpeta_origen = obtener_carpeta("Ruta de la carpeta de origen: ")
    carpeta_destino = obtener_carpeta("Ruta de la carpeta de destino: ", crear=True)
    extension_salida = obtener_texto("Extensión de salida (ej: jpg, png): ")
    
    print(COLOR_INFO + "📏 Dimensiones (opcional - presione Enter para omitir):")
    ancho = obtener_entero("Ancho (0 para omitir): ", 0, opcional=True)
    alto = obtener_entero("Alto (0 para omitir): ", 0, opcional=True)
    
    ancho = ancho if ancho and ancho > 0 else None
    alto = alto if alto and alto > 0 else None
    
    return img.configurarIMG_enCarpetas(carpeta_origen, carpeta_destino, extension_salida, ancho, alto)

def procesar_comando_cambiar_formato():
    """Procesa el comando de cambiar formato"""
    print(COLOR_INFO + "\n" + "🔄 CAMBIAR FORMATO DE IMAGEN")
    print(COLOR_INFO + "-" * 30)
    
    img_inicio = obtener_archivo("Ruta de la imagen de inicio con extensión: ")
    img_destino = obtener_texto("Ruta de la imagen resultado sin extensión: ")
    extension_salida = obtener_texto("Extensión de salida: ")
    
    # Resolver ruta de salida
    img_destino = resolver_ruta(img_destino)
    
    return img.transformar_IMG_ext(img_inicio, img_destino, extension_salida)

def procesar_comando_rotar():
    """Procesa el comando de rotar imagen"""
    print(COLOR_INFO + "\n" + "🔄 ROTAR IMAGEN")
    print(COLOR_INFO + "-" * 30)
    
    imagen = obtener_archivo("Ruta de la imagen: ")
    angulo = obtener_entero("Ángulo de rotación (0-360): ", 0, 360)
    resultado = obtener_archivo_salida("Nombre de la imagen resultado: ")
    
    return img.rotar_imagen(imagen, resultado, angulo)

def procesar_comando_espejo():
    """Procesa el comando de voltear imagen"""
    print(COLOR_INFO + "\n" + "🪞 VOLTEAR IMAGEN (ESPEJO)")
    print(COLOR_INFO + "-" * 30)
    
    imagen = obtener_archivo("Ruta de la imagen: ")
    
    while True:
        direccion = obtener_texto("Dirección (horizontal/vertical): ").lower()
        if direccion in ['horizontal', 'vertical']:
            break
        print(COLOR_ERROR + "Error: Debe ser 'horizontal' o 'vertical'")
    
    resultado = obtener_archivo_salida("Nombre de la imagen resultado: ")
    
    return img.voltear_imagen(imagen, resultado, direccion)

def procesar_comando_filtro_bn():
    """Procesa el comando de filtro blanco y negro"""
    print(COLOR_INFO + "\n" + "⚫ APLICAR FILTRO BLANCO Y NEGRO")
    print(COLOR_INFO + "-" * 30)
    
    imagen = obtener_archivo("Ruta de la imagen: ")
    resultado = obtener_archivo_salida("Nombre de la imagen resultado: ")
    
    return img.filtro_blanco_negro(imagen, resultado)

def procesar_comando_recortar():
    """Procesa el comando de recortar imagen"""
    print(COLOR_INFO + "\n" + "✂️ RECORTAR IMAGEN")
    print(COLOR_INFO + "-" * 30)
    
    imagen = obtener_archivo("Ruta de la imagen: ")
    
    print(COLOR_INFO + "📍 Coordenadas del área a recortar:")
    izquierda = obtener_entero("Coordenada izquierda: ", 0)
    superior = obtener_entero("Coordenada superior: ", 0)
    derecha = obtener_entero("Coordenada derecha: ", izquierda + 1)
    inferior = obtener_entero("Coordenada inferior: ", superior + 1)
    
    resultado = obtener_archivo_salida("Nombre de la imagen resultado: ")
    
    return img.recortar_imagen(imagen, resultado, (izquierda, superior, derecha, inferior))

def procesar_comando_brillo():
    """Procesa el comando de ajustar brillo"""
    print(COLOR_INFO + "\n" + "💡 AJUSTAR BRILLO")
    print(COLOR_INFO + "-" * 30)
    
    imagen = obtener_archivo("Ruta de la imagen: ")
    
    print(COLOR_INFO + "💡 Factor de brillo: 1.0 = normal, <1.0 = más oscuro, >1.0 = más brilloso")
    factor = obtener_float("Factor de brillo (0.1 - 5.0): ", 0.1, 5.0)
    
    resultado = obtener_archivo_salida("Nombre de la imagen resultado: ")
    
    return img.ajustar_brillo(imagen, resultado, factor)

def constructor():
    """Función principal del programa"""
    menu()
    home = True
    
    while home:
        try:
            print(COLOR_INPUT + "\nIngrese un comando (o presione Enter para ver el menú): ", end="")
            usuario = input().strip().lower()
            
            if usuario == "":
                menu()
            elif usuario == "/limpiar" or usuario == "/casa":
                menu()
            elif usuario == "/ayuda":
                print(COLOR_INFO + "\n" + "="*50)
                print(COLOR_TITULO + "📚 AYUDA DETALLADA DE COMANDOS")
                print(COLOR_INFO + "="*50)
                print(ayuda["comando_ayuda"])
            elif usuario == "/mas":
                print(COLOR_INFO + "\n" + "="*50)
                print(COLOR_TITULO + "📖 INFORMACIÓN ADICIONAL")
                print(COLOR_INFO + "="*50)
                print(mas["comando_mas"])
            
            # COMANDOS DE GESTIÓN DE CARPETAS
            elif usuario == "/conectar_carpeta":
                conectar_carpeta()
            elif usuario == "/ver":
                ver_contenido_carpeta()
            elif usuario == "/listar":
                listar_imagenes_carpeta()
            elif usuario == "/desconectar":
                desconectar_carpeta()
            
            # COMANDOS DE PROCESAMIENTO DE IMÁGENES
            elif usuario == "/marca_agua" or usuario == "/agregar_marca_agua":
                procesar_comando_marca_agua()
            elif usuario == "/convertir_ico" or usuario == "/convertir_aico":
                procesar_comando_convertir_ico()
            elif usuario == "/metadatos" or usuario == "/mostrar_metadatos":
                procesar_comando_metadatos()
            elif usuario == "/redimensionar" or usuario == "/redimensionar_img":
                procesar_comando_redimensionar()
            elif usuario == "/procesar_carpeta" or usuario == "/configurarimg_encarpetas":
                procesar_comando_procesar_carpeta()
            elif usuario == "/cambiar_formato" or usuario == "/transformar_img_ext":
                procesar_comando_cambiar_formato()
            elif usuario == "/soporte" or usuario == "/soporte_img":
                print(COLOR_INFO + "\n" + "🎨 FORMATOS SOPORTADOS")
                print(COLOR_INFO + "-" * 30)
                print(img.SOPORTE_IMG)
            elif usuario == "/rotar":
                procesar_comando_rotar()
            elif usuario == "/espejo":
                procesar_comando_espejo()
            elif usuario == "/filtro_bn":
                procesar_comando_filtro_bn()
            elif usuario == "/recortar":
                procesar_comando_recortar()
            elif usuario == "/brillo":
                procesar_comando_brillo()
            elif usuario == "/salir":
                print(COLOR_EXITO + "\n" + "="*50)
                print(COLOR_TITULO + "👋 ¡Gracias por usar PINGU!")
                print(COLOR_EXITO + "✅ EJECUCIÓN FINALIZADA")
                print(COLOR_EXITO + "="*50)
                home = False
            else:
                print(COLOR_ERROR + f"❌ Comando no reconocido: [{usuario}]")
                print(COLOR_INFO + "💡 Use /ayuda para ver los comandos disponibles")
                
        except KeyboardInterrupt:
            print(COLOR_EXITO + "\n\n⏹️  Ejecución interrumpida por el usuario. ¡Hasta pronto!")
            home = False
        except Exception as e:
            print(COLOR_ERROR + f"\n❌ Error inesperado: {e}")
            print(COLOR_INFO + "🔄 Reiniciando aplicación...")
            input(COLOR_INPUT + "Presione Enter para continuar...")
            menu()

if __name__ == "__main__":
    constructor()