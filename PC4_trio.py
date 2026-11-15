# python -m venv .venv
# pip install Streamlit
# pip install streamlit_option_menu
# pip install streamlit.components.v1
# python -m streamlit hello
# python -m streamlit run PC4_trio.py

import streamlit as st
from streamlit_option_menu import option_menu
import streamlit.components.v1 as components

### Opción 2: Menú horizontal
opciones_2 = option_menu(
    menu_title="¡Conoce más de nosotras!", 
    options=['Presentación', 'Experiencia', 'Gráficos'], 
    icons=['chat-heart','mortarboard-fill', 'bar-chart-line-fill'], 
    menu_icon="caret-down-square-fill", default_index=0, orientation="horizontal")

if opciones_2 == 'Presentación':
    st.markdown("<h1 style='text-align: center; font-size: 50 px; color: black'>BIENVENIDOS AL MUNDO CODIFICADOR</h1>", unsafe_allow_html=True)

    # Alumno a = MATISSE
    col1, col2 = st.columns(2)
    
    col1.image("m_FOTO.jpg", caption='Matisse', width=300)

    texto = """
    ¡Hola, qué tal! Soy Matisse Huillca y tengo 20 años, y 
    actualmente me encuentro en la carrera de Publicidad de 
    la Facultad de Ciencias y Artes de las Comunicaciones 
    en la Pontificia Universidad Católica del Perú. En mis 
    tiempos libres prefiero diseñar posts por Canva y me 
    gusta mucho leer novelas o libros de género romance. 
    Asimismo, soy fan de películas de ficción como la saga 
    de Los Juegos del Hambre y la serie de Stranger Things. 
    """
    col2.markdown(f"<div style='text-align: justify; font-size: 15px;'>{texto}</div>", unsafe_allow_html=True)

    # Alumno b = jackeline
    col1, col2 = st.columns(2)
    
    texto_2 = """
    ¡Hola! Soy Jackeline Uscamayta, tengo 20 años. Soy 
    estudiante de Publicidad, amante de las películas de 
    terror y de toda situación paranormal. Tengo una colección 
    de barbies y espero en el futuro tener una colección de 
    sus casas. Mi comida favorita es el Ají de Gallina pero 
    el que prepara mi abuelita. En mis tiempos libres, disfruto 
    cocinar y probar nuevas recetas, grabo y edito videos. Por 
    último, uno de mis sueños es formar parte de una película de 
    terror, puede ser como actriz o parte de la dirección de arte.
    """
    col1.markdown(f"<div style='text-align: justify; font-size: 15px;'>{texto_2}</div>", unsafe_allow_html=True)
    
    col2.image("j_Foto.jpg", caption='Jackeline', width=300)

    # Alumno c = Andrea
    col1, col2 = st.columns(2)
    
    col1.image("a_foto_perfil.jpg", caption='Andrea', width=300)
    
    texto_3 = """
    ¡Holaaa! Me llamo Andrea y me dicen Andrea. Tal cual. 
    Estudio la carrera de Publicidad y soy una persona que 
    suele estar alegre (me río con facilidad). Me encanta 
    pasar tiempo con mis amigos y mi familia, compartir 
    momentos y disfrutar de las pequeñas cosas. Me gusta 
    la comida que sea rica, aunque no tolero tanto la comida 
    picante. Este año estoy aprendiendo muchas cosas nuevas, 
    descubriendo habilidades e intereses que no sabía que tenía. 
    Y eso es algo que me parece muy bonito. Siento que todavía 
    tengo mucho por explorar, aprender y experimentar, y eso 
    es lo que hace que esta etapa sea tan interesante para mí. 
    Por cierto, soy fan de BTS y últimamente estoy con el mood 
    de Where You From. ¡Tenía que mencionarlo!
    """
    col2.markdown(f"<div style='text-align: justify; font-size: 15px;'>{texto_3}</div>", unsafe_allow_html=True)
    
elif  opciones_2 == 'Experiencia':

    st.markdown("<h1 style='text-align: center; font-size: 50 px; color: black'>Nombre a la sección de experiencia 💻</h1>", unsafe_allow_html=True)

    # Alumno a
    texto_4 = """
    Aquí escribe tu experiencia aprendiendo a programar. 
    ¿Cómo te sentiste al principio? 
    ¿Qué te ha enseñado la programación? 
    ¿Qué te gusta de programar? 
    ¿Qué te gustaría hacer con la programación en el futuro?
    """
    st.markdown(f"<div style='text-align: justify; font-size: 18px;'>{texto_4}</div>", unsafe_allow_html=True)
    
    # Formato YouTube
    st.subheader("🎥 Título apropiado video 1")
    st.video("https://www.youtube.com/watch?v=X_Z7d04x9-E")
    
    # Formato Google Drive
    st.subheader("🎥 Título apropiado video 2")

    col1, col2, col3 = st.columns([1, 2, 1])

    with col2:  
        st.link_button("🎥 Texto del botón",
                       "https://drive.google.com/file/d/1REvRXSu3GuGD73w8j44135MkRiezd0gP/view?usp=drive_link",
                       use_container_width=True
            )

    # Alumno b
    texto_5 = """
    Aquí escribe tu experiencia aprendiendo a programar. 
    ¿Cómo te sentiste al principio?
    ¿Qué te ha enseñado la programación?
    ¿Qué te gusta de programar? 
    ¿Qué te gustaría hacer con la programación en el futuro?
    """
    st.markdown(f"<div style='text-align: justify; font-size: 18px;'>{texto_5}</div>", unsafe_allow_html=True)
        
    # Formato YouTube
    st.subheader("🎥 Título apropiado video 1")
    st.video("https://www.youtube.com/watch?v=X_Z7d04x9-E")
        
    # Formato Google Drive
    st.subheader("🎥 Título apropiado video 2")
    
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:  
        st.link_button("🎥 Texto del botón",
                       "https://drive.google.com/file/d/1REvRXSu3GuGD73w8j44135MkRiezd0gP/view?usp=drive_link",
                       use_container_width=True
             )

    # Alumno c
    texto_6 = """
    Aquí escribe tu experiencia aprendiendo a programar. 
    ¿Cómo te sentiste al principio? 
    ¿Qué te ha enseñado la programación? 
    ¿Qué te gusta de programar? 
    ¿Qué te gustaría hacer con la programación en el futuro?
    """
    st.markdown(f"<div style='text-align: justify; font-size: 18px;'>{texto_6}</div>", unsafe_allow_html=True)
        
    # Formato YouTube
    st.subheader("🎥 Título apropiado video 1")
    st.video("https://www.youtube.com/watch?v=X_Z7d04x9-E")
        
    # Formato Google Drive
    st.subheader("🎥 Título apropiado video 2")
    
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:  
        st.link_button("🎥 Texto del botón",
                       "https://drive.google.com/file/d/1REvRXSu3GuGD73w8j44135MkRiezd0gP/view?usp=drive_link",
                       use_container_width=True
            )
            
else:

    st.markdown("<h1 style='text-align: center;font-size: 50 px; color: black'>Nombre a la sección</h1>", unsafe_allow_html=True)
    
    # Aquí todos los integrantes deben poner sus 3 gráficos y su mapa en la lista 
    # y aumentar la estructura condicional como sea necesaria
    graficos = ['Gráfico_1', 'Gráfico_2', 'Mapa_1'] 
    grafico_seleccionado = st.selectbox('Selecciona un gráfico', graficos)
    
    if grafico_seleccionado == 'Gráfico_1':
        st.subheader("📊 Gráfico 1: Lenguas aisladas")
        texto_7 = """
        Interpretación del Gráfico 1
        """
        st.markdown(f"<div style='text-align: justify; font-size: 18px;'>{texto_7}</div>", unsafe_allow_html=True)

        col1, col2, col3 = st.columns([1, 7, 1])
        with col2:
                st.image("aisladas_base_datos.png", width=800)

    elif grafico_seleccionado == 'Gráfico_2':
        st.subheader("📊 Gráfico 2: Familias lingüísticas")
        texto_8 = """
        Interpretación del Gráfico 2
        """
        st.markdown(f"<div style='text-align: justify; font-size: 18px;'>{texto_8}</div>", unsafe_allow_html=True)
    
        col1, col2, col3 = st.columns([1, 7, 1])
        with col2:
            st.image("lengua_familia_GB.png", width=800)
    
    else:
        st.subheader("🗺️ Mapa 1: Distribución geográfica")
        texto_9 = """
        Interpretación del mapa
        """
        st.markdown(f"<div style='text-align: justify; font-size: 18px;'>{texto_9}</div>", unsafe_allow_html=True)
            
        with open("mapa.html", "r", encoding="utf-8") as mapa:
                html_content = mapa.read()
    
        components.html(html_content,height=600)
    
