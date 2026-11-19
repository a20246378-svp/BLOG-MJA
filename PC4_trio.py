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
    
    col1.image("m_FOTO.png", caption='Matisse', width=300)

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

    st.markdown("<h1 style='text-align: center; font-size: 50 px; color: black'> CAMINANDO ENTRE CÓDIGOS 👩‍💻</h1>", unsafe_allow_html=True)

    # Alumno a = MATISSE
    texto_4 = """
    Mi experiencia en el curso de Pensamiento Computacional 
    fue bastante retadora, ya que exigía memorizar diversos 
    códigos, comprender su función específica y dominar la 
    estructura correcta de cada uno para lograr que se 
    ejecutaran sin errores. Al principio me resultó complicado 
    identificar qué instrucción utilizar según el contexto del 
    problema y, sobre todo, cómo conectarlas de forma lógica 
    para que trabajaran en conjunto. Sin embargo, superar esa 
    curva de aprendizaje no solo me permitió articular distintas 
    piezas de código para consolidar soluciones funcionales 
    en cada ejercicio, sino que también me brindó una base 
    sólida para comprender mejor el área de la programación 
    y las bases de datos, conocimientos clave en los que podría 
    especializarme y aplicar en un futuro ámbito profesional 
    o laboral.  
    """
    st.markdown(f"<div style='text-align: justify; font-size: 18px;'>{texto_4}</div>", unsafe_allow_html=True)
    
    # VIDEO 1 = MATISSE (FORMATO DRIVE)
    st.subheader("🎥 Tomando decisiones con los booleanos")

    col1, col2, col3 = st.columns([1, 2, 1])

    with col2:  
        st.link_button("🎥 Expresiones booleanas",
                       "https://drive.google.com/file/d/1mf-Uk0OcTrBx4EoDLcyjpgaTlafH6mj-/view?usp=sharing",
                       use_container_width=True
            )

    # VIDEO 2 = MATISSE 
    st.subheader("🎥 Condicionando ando")

    col1, col2, col3 = st.columns([1, 2, 1])

    with col2:  
        st.link_button("🎥 Expresiones condicionales",
                       "https://drive.google.com/file/d/14Ul4UGiC8wEPiM2Ey6pneKI_xCuE1bzt/view?usp=sharing",
                       use_container_width=True
            )
    # Alumno b = JACKELINE
    texto_5 = """
    Cuando investigué sobre este curso, me sorprendió al 
    saber que íbamos a trabajar con Python, al principio 
    no sabía que era, porque nunca en mi vida lo había 
    utilizado. A pesar de ello, me sentía entusiasmada 
    por aprender algo nuevo y así fué. Me gustó mucho 
    aprender las funciones y métodos de Python y cómo 
    combinarlos. A medida que avanzábamos, se volvía más 
    dificultoso. Aún así, seguí estudiando e intentado 
    tomar todos los apuntes posibles en las horas prácticas 
    para entender los temas. Para terminar, estoy teniendo 
    algunas dificultades en cuanto al proyecto final, más 
    que todo en construir una buena estructura de lo que 
    queremos hacer. Aún así, considero que se va a resolver 
    porque con mi grupo estamos intentando hacerlo, tal vez 
    probando y fallando, pero así aprendemos. 
    """
    st.markdown(f"<div style='text-align: justify; font-size: 18px;'>{texto_5}</div>", unsafe_allow_html=True)
        
    # VIDEO 1 = JACKELINE (FORMATO DRIVE)
    st.subheader("🎥 Organizando datos")
    
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:  
        st.link_button("🎥 Strings y listas",
                       "https://drive.google.com/file/d/1Y3dkjkqpairW2EuSyoOUc-5QKneCC7wM/view?usp=sharing",
                       use_container_width=True
             )
    
    # VIDEO 2 = JACKELINE (FORMATO DRIVE)
    st.subheader("🎥 Condicionando ando")
    
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:  
        st.link_button("🎥 Estructuras condicionales",
                       "https://drive.google.com/file/d/1mRUM22csNqH5qnMhEiOXL6ZKQ-XwEV2U/view?usp=sharing",
                       use_container_width=True
             )
    
    # Alumno c = ANDREA 
    texto_6 = """
    Aquí escribe tu experiencia aprendiendo a programar. 
    ¿Cómo te sentiste al principio? 
    ¿Qué te ha enseñado la programación? 
    ¿Qué te gusta de programar? 
    ¿Qué te gustaría hacer con la programación en el futuro?
    """
    st.markdown(f"<div style='text-align: justify; font-size: 18px;'>{texto_6}</div>", unsafe_allow_html=True)
        
    # VIDEO 1 = ANDREA
    st.subheader("🎥 Tomando decisiones con los booleanos")
    
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:  
        st.link_button("🎥 Expresiones booleanas",
                       "https://drive.google.com/file/d/1EtGHLgeBIEuN4wGS7iDvculiR2zuD72Z/view?usp=drivesdk",
                       use_container_width=True
            )

    # VIDEO 2 = ANDREA
    st.subheader("🎥 Condicionando ando")
    
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:  
        st.link_button("🎥 Estructuras condicionales",
                       "https://drive.google.com/file/d/1P5cZvA5TR3FBQH_ggYLUFgxkKalkuNz_/view?usp=drivesdk",
                       use_container_width=True
            )

else:

    st.markdown("<h1 style='text-align: center;font-size: 50 px; color: black'>CÍRCULOS, COLUMNAS Y COORDENADAS</h1>", unsafe_allow_html=True)
    
    # Aquí todos los integrantes deben poner sus 3 gráficos y su mapa en la lista 
    # y aumentar la estructura condicional como sea necesaria
    graficos = ['Histograma_Matisse', "Histograma_Jackeline", "Histograma_Andrea", 'Pastel_Matisse', 'Pastel_Jackeline', 'Pastel_Andrea', "Wordcloud_Matisse", "Wordcloud_Jackeline", "Wordcloud_Andrea", 'Mapa_Matisse', "Mapa_Jackeline", "Mapa_Andrea"] 
    grafico_seleccionado = st.selectbox('Selecciona un gráfico', graficos)

    # MATISSE 
    if grafico_seleccionado == 'Histograma_Matisse':
        st.subheader("📊 Histogramas")
        texto_7 = """
        En el primer histograma se observa que el equipo de 
        local anotó predominantemente 1 gol por encuentro en 
        9 partidos, caso contrario, el segundo gráfico muestra 
        que como visitante el equipo mantuvo su arco en cero 
        durante 6 partidos, mientras que su valor más recurrente 
        de goles recibidos fue de 1 gol en 9 partidos. Al comparar 
        ambos gráficos, se aprecia que el equipo es muy fuerte en 
        defensa cuando juega de visitante, pues casi nunca le encajan 
        más de un gol. Asimismo, cuando juega de local demuestra una 
        efectividad constante en ataque, anotando casi siempre entre 
        1 y 3 goles. En conclusión, los resultados muestran un 
        rendimiento equilibrado entre la cantidad de goles que anota 
        de local y los pocos goles que recibe de visitante. 
        """
        st.markdown(f"<div style='text-align: justify; font-size: 18px;'>{texto_7}</div>", unsafe_allow_html=True)

        col1, col2, col3 = st.columns([1, 7, 1])
        with col2:
                st.image("m_HISTOGRAMA.png", width=800)

    elif grafico_seleccionado == 'Histograma_Jackeline':
        st.subheader("📊 Histogramas")
        texto_8 = """
        Los goles anotados a nivel local por el equipo Villarreal 
        son variados. Si bien, hay pocos partidos en los que anota, 
        se destaca mucho los goles que anotó en más de 8 partidos 
        que fueron de 2 a 3 goles. Sin embargo, se anotaron de 5 
        a 6 goles en 3 partidos, los cuales dejan al equipo en una 
        buena posición. A comparación de los goles recibidos como 
        visitante, ya que solo llega a recibir 5 goles, lo cual es 
        bueno, ya que debe acumular más los goles anotados. Además, 
        solo ha recibido entre 1 a 2 goles en ocho partidos, lo cual 
        conviene al equipo porque su resultado de goles anotados es 
        mayor que los recibidos.
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
    
