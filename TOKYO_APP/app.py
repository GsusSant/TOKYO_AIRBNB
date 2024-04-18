# --------------------LIBRERÍAS----------------------------#
import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
import streamlit as st
import streamlit.components.v1 as components
import numpy as np
import pandas as pd
import warnings
from PIL import Image 
import base64


# --------------------CONFIGURACIÓN DE LA PÁGINA----------------------------#
st.set_page_config(
    page_title="--",
    page_icon="---",
    layout="wide", #centered, wire
    initial_sidebar_state="expanded" #auto, collapsed, expanded
)

# ---------------------FONDO----------------------#


def get_base64(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

def get_base64(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

def set_background(png_file, background_size='auto', background_position='left'):
    bin_str = get_base64(png_file)
    page_bg_img = f'''
    <style>
    .main {{
        background-image: url("data:image/png;base64,{bin_str}");
        background-size: {background_size};
        background-position: {background_position};
        background-attachment: local;
        width: 100%;
        height: 100%;
    }}
    </style>
    <div class="main"></div>
    '''
    st.markdown(page_bg_img, unsafe_allow_html=True)

set_background("img/photo_5821122691741106634_y.jpg", background_size='70% 70%', background_position='left')


logo0 = 'https://www.japan-guide.com/thumb/destination_tokyo.jpg'
logo2 = 'img\ktem.png'
im2='img\kgeisha.png'
im='img\ksamu.png'
nube = 'img\wordcloud.png'
# --------------------COSAS QUE VAMOS A USAR EN TODA LA APP----------------------------#
@st.cache_data()
def load_data():
    df = pd.read_csv("TOKYO_AIRBNB\TOKYO_APP\data\dairbnb_tokyo.csv")
    return df

# --------------------CARGA DATOS----------------------------#
df= load_data()

# --------------------HEADER----------------------------#
# st.title("Bienvenido a Tokyo")
# st.write('**Sumérgete en la Cultura y la Elegancia Japonesa**')
# st.image([im], width=500)

# --------------------SIDEBAR----------------------------#
col1, col2 = st.sidebar.columns(2)

# Agregar la imagen a la primera columna
col2.image(im2, width=120)

# Agregar el título a la segunda columna
col1.title("INDICE")
st.sidebar.write("-------------")

page_options = ["EXPOSICIÓN", "ANÁLISIS",'MAPAS', 'RESEÑAS']
page = st.sidebar.radio("Seleccione la página:", page_options, index=0, key='current_page')
# ---------------------BODY----------------------#

# PÁGINA 1-------------------------------------
if page == "EXPOSICIÓN":
    st.markdown("<h1 style='text-align: center;'>BIENVENIDO A TOKYO</h1>", unsafe_allow_html=True)
    #st.write('**Sumérgete en la Cultura y la Elegancia Japonesa**')
    
    
    col1, col2 = st.columns([1, 2])

# En la primera columna, mostramos el texto
    with col1:
        st.image(im, width=400)

    # En la segunda columna, mostramos la imagen
    with col2:
        st.markdown("""
                **¡Bienvenido a Tokyo, la apasionante capital de Japón que fusiona la rica historia con la modernidad más vibrante! Desde los rascacielos iluminados por neón hasta los antiguos templos y jardines, Tokyo ofrece una experiencia única que encantará a cada visitante.**
                """)

        st.markdown("""
            Explora los diversos barrios de Tokyo, desde el dinámico Shibuya, famoso por su cruce peatonal y su energía electrificante, hasta el tranquilo y tradicional barrio de Yanaka, donde puedes sumergirte en la auténtica cultura japonesa.

Disfruta de la deliciosa gastronomía de Tokyo, desde los exquisitos platos de sushi y ramen hasta los dulces wagashi y los tentadores yakitoris. Descubre los mercados callejeros locales y los restaurantes ocultos donde podrás probar los sabores únicos de la cocina japonesa.

Sumérgete en la cultura y la historia de Tokyo visitando sus antiguos templos y santuarios, como el majestuoso Senso-ji en Asakusa y el tranquilo templo Meiji en Shibuya. También puedes explorar los museos de clase mundial, como el Museo Nacional de Tokio y el Museo de Arte Mori.

Ya sea que estés aquí para explorar la bulliciosa vida urbana, disfrutar de la tranquilidad de los jardines japoneses o sumergirte en la fascinante cultura del país, Tokyo te espera con los brazos abiertos para ofrecerte una experiencia inolvidable.

¡Descubre todo lo que Tokyo tiene para ofrecer y haz de tu estancia una aventura inolvidable en la capital japonesa!*
            """)
        st.markdown("""
Nuestra página web te ofrece una amplia selección de alojamientos en Tokyo para que puedas disfrutar al máximo de tu estancia en esta fascinante ciudad. Desde acogedores apartamentos en el corazón de Shibuya hasta elegantes casas tradicionales en barrios históricos, tenemos opciones para todos los gustos y presupuestos. Nuestro completo conjunto de datos incluye información detallada sobre cada propiedad, desde el nombre y la descripción hasta las comodidades disponibles y las reseñas de otros huéspedes. Explora nuestra plataforma y encuentra el alojamiento perfecto para tu próxima aventura en Tokyo. ¡Empieza a planificar tu viaje hoy mismo y descubre todo lo que esta increíble ciudad tiene para ofrecer!
                """  )      
    
    
    st.write('------')                    
    st.markdown('### **VISUALIZAMOS EL CONJUNTO DE DATOS:**')
    st.dataframe(df.head())


    
    
# PÁGINA 2-------------------------------------
elif page == "ANÁLISIS":
    
    
    
    st.markdown("<h1 style='text-align: center;'>CONOZCAMOS LOS BARRIOS</h1>", unsafe_allow_html=True)
    st.image(logo0, width=1000)
    column1, column2 = st.columns(2)

    with column1:
        st.write("""
        En esta metrópolis vibrante, cada distrito o "ku" tiene su propio encanto y carácter distintivo.

        Comencemos nuestro viaje explorando los históricos barrios de Sumida Ku y Kita Ku, donde encontrarás una mezcla única de tradición y modernidad. Luego, sumérgete en la bulliciosa vida nocturna de Shibuya Ku y la relajada atmósfera de Suginami Ku.

        No te pierdas los encantadores rincones de Setagaya Ku y Adachi Ku, ni la serenidad de Higashimurayama Shi y Katsushika Ku. Descubre la belleza costera de Shinagawa Ku y la vida urbana dinámica de Shinjuku Ku.

        Explora los elegantes barrios de Meguro Ku y Taito Ku, y sumérgete en la cultura pop de Nakano Ku y Koto Ku. Aventúrate en los espacios verdes de Hino Shi y Mitaka Shi, y maravíllate con los rascacielos de Ota Ku y Toshima Ku.
        """)

    with column2:
        st.write("""
        Recorre los encantadores pueblos de Akishima Shi y Bunkyo Ku, y descubre la historia en Hachioji Shi y Itabashi Ku. Sumérgete en la tranquilidad de Edogawa Ku y Arakawa Ku, y disfruta de la vida familiar en Nerima Ku y Machida Shi.

        Explora la naturaleza en Tama Shi y Kodaira Shi, y sumérgete en la sofisticación de Minato Ku y Komae Shi. Disfruta de la vida suburbana en Chofu Shi y Fuchu Shi, y explora el bullicio de Chuo Ku y Chiyoda Ku.

        Descubre la historia en Fussa Shi y Nishitokyo Shi, y disfruta de la belleza natural en Akiruno Shi y Koganei Shi. Explora la vida estudiantil en Kunitachi Shi y el encanto rural de Ome Shi.

        Aventúrate en los encantadores pueblos de Kokubunji Shi y Hamura Shi, y disfruta de la vida relajada en Tachikawa Shi y Musashino Shi. Maravíllate con la belleza natural de Musashimurayama Shi y Okutama Machi, y descubre la serenidad en Hinohara Mura.
        """)
        
    st.write('------')    
 
    st.write('## **EXPLORAREMOS CUÁLES SON LOS PRECIOS POR NOCHE DEPENDIENDO DEL BARRIO**')
    st.write('### Antes de ello, haremos la conversión de moneda: 1 jpy = 0.0061 euro ')

    with open("html\preciomedio_barrio.html", "r", encoding="utf-8") as f:
        html_code = f.read()

    st.components.v1.html(html_code, width=1000, height=600)
    
    
    
    
    
    
    st.write('## **EXPLORAREMOS NÚMERO DE ALOJAMIENTOS POR BARRIO**')
        
    with open("html\kalojamiento_barrio.html", "r", encoding="utf-8") as f:
        html_code = f.read()

    st.components.v1.html(html_code, width=1000, height=600)



    st.write('## **¿CUÁL ES LA DISTRIBUCIÓN DE PRECIO?**')

    with open("html\distribucion_precio.html", "r", encoding="utf-8") as f:
        html_code = f.read()

    st.components.v1.html(html_code, width=1000, height=600)
    
    
    st.write('## **¿CUÁL ES EL PRECIO SEGÚN EL TIPO DE HABITACIÓN?**')

    with open("html\grafico_boxplot.html", "r", encoding="utf-8") as f:
        html_code = f.read()

    st.components.v1.html(html_code, width=1000, height=600)
    
    
    
    
    
    with open("html\precio_habitacion.html", "r", encoding="utf-8") as f:
        html_code = f.read()

    st.components.v1.html(html_code, width=1000, height=600)
        
        
    st.write('## **DISTRIBUCIÓN DE PERSONAS SEGUN EL TIPO DE ALOJAMIENTO**')

    with open("html\personas_alojamiento.html", "r", encoding="utf-8") as f:
        html_code = f.read()

    st.components.v1.html(html_code, width=1000, height=600)





    st.write('## **PUNTUACIÓN DE LOS ALOJAMIENTOS DISTRIBUIDO POR BARRIO**')

    with open("html\puntuacion_barrio.html", "r", encoding="utf-8") as f:
        html_code = f.read()

    st.components.v1.html(html_code, width=1000, height=600)



    with open("html\puntuacion_localizacion.html", "r", encoding="utf-8") as f:
        html_code = f.read()

    st.components.v1.html(html_code, width=1000, height=600)

        
    
    



# PÁGINA 3-------------------------------------
elif page == "MAPAS":    
    
    st.markdown('### **VISUALIZAMOS EL MAPA DE TOKYO CON LA MEDIA DE PRECIOS POR BARRIO:**')
    
    with open("html\mapa_precio.html", "r", encoding="utf-8") as f:
        html_code = f.read()

    st.components.v1.html(html_code, width=1000, height=600)
    
    
    
    
    with open("html\ktokyo_map.html", "r", encoding="utf-8") as f:
        html_code = f.read()

    st.components.v1.html(html_code, width=1000, height=600)
    
    
    
        
        
        
        

# PÁGINA 4-------------------------------------
elif page == 'RESEÑAS':
    st.markdown("<h1 style='text-align: center;'>¿QUÉ HAY DE LAS RESEÑAS?</h1>", unsafe_allow_html=True)

    st.markdown("""Cuando se trata de encontrar el alojamiento perfecto en Tokyo, los viajeros a menudo recurren a las reviews y comentarios de otros huéspedes para tomar decisiones informadas. Estas reviews proporcionan una visión única sobre la calidad de los alojamientos, desde la comodidad de las habitaciones hasta la hospitalidad del personal y la conveniencia de la ubicación.

En esta charla, exploraremos la importancia de las reviews y comentarios de alojamientos en Tokyo. Analizaremos cómo estas opiniones pueden influir en las decisiones de los viajeros y cómo los propietarios de alojamientos pueden aprovechar esta retroalimentación para mejorar la experiencia de sus huéspedes.

Además, examinaremos algunas tendencias destacadas en las reviews y comentarios de alojamientos en Tokyo, incluyendo los aspectos más valorados por los viajeros y los desafíos que enfrentan los propietarios al gestionar y responder a estas opiniones.

¡Acompáñanos en este viaje para descubrir el papel fundamental que juegan las reviews y comentarios de alojamientos en Tokyo en la experiencia del viajero moderno!
    
    """)
        
    with open("html\grafico_reviews_por_mes.html", "r", encoding="utf-8") as f:
        html_code = f.read()

    st.components.v1.html(html_code, width=1000, height=600)
    
    
    with open("html\grafico_relacion_disponibilidad_puntuacion.html", "r", encoding="utf-8") as f:
        html_code = f.read()

    st.components.v1.html(html_code, width=1000, height=600)
    


    with open("html\grafico_relacion_precio_puntuacion.html", "r", encoding="utf-8") as f:
        html_code = f.read()

    st.components.v1.html(html_code, width=1000, height=600)

# --------------------TABS----------------------------#
tab2, = st.tabs(
    [ "Nube de palabras"]
)

# --------------------CORRELACION----------------------------#
# with tab1:
#     st.image(correlacion, width=1200)



# --------------------NUBE DE PALABRAS----------------------------#
with tab2:
    st.header("NUBE DE PALABRAS")
    st.markdown("""En esta sección, exploraremos una visualización fascinante de las reseñas de nuestros usuarios: la nube de palabras. Esta representación gráfica única nos permite visualizar de manera rápida y efectiva las palabras más frecuentes y relevantes que aparecen en las reseñas de nuestros productos o servicios.

La nube de palabras se crea a partir de un análisis de texto, donde cada palabra se representa en proporción a su frecuencia de aparición en las reseñas. Las palabras más frecuentes aparecen más grandes y con colores más llamativos, mientras que las menos comunes son más pequeñas y más tenues. Esta representación nos ofrece una instantánea visual de los temas más destacados y las opiniones predominantes entre nuestros usuarios.""")

    st.image(nube, width=1200)


