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
    Al iniciar este curso, estuve entusiasmada por la noticia 
    que iba a aprender a programar por primera vez ＼(^-^)／. 
    Recordé vagamente algunas de las últimas clases de un curso 
    del colegio, en las que el profesor nos enseñó temas relacionados 
    a HTML. Por ello, estaba emocionada con la enseñanza de Python. 
    Sin embargo, durante mi proceso, sí que fue realmente retador. 
    Las clases se volvían poco a poco difíciles para mí, pero pude 
    afrontarlo de buena manera ☆. A pesar de ello, también rescato 
    ciertas cosas que me gustaron demasiado, como la función input, 
    que permite solicitar una respuesta del usuario y combinarla con 
    estructuras condicionales. Además, algo que me llamó demasiada 
    la atención fue la nube de palabras y su respecto proceso de 
    depuración para llegar a ella. ¡Fue muy lindo tot!. Admito que, 
    con las clases teóricas y prácticas, programar me ha enseñado que 
    hay diversas formas de solucionar un problema. ¡EL PENSAMIENTO 
    DIVERGENTE! Finalmente, en el futuro me gustaría seguir aprendiendo 
    de programación y aplicarlas a mi carrera, desarrollando proyectos 
    creativos e interactivos que combinen la tecnología y la 
    comunicación ＼(_ _). 
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
    graficos = ["Gráfico_Histograma", "Gráfico_Pastel", "Gráfico_barras", "Nube_de_palabras", "Mapas"] 
    grafico_seleccionado = st.selectbox('Selecciona un gráfico', graficos)

    # MATISSE 
    if grafico_seleccionado == 'Gráfico_Histograma':
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
                st.image("m_HISTOGRAMA.png", width=900)

    elif grafico_seleccionado == 'Gráfico_Pastel':
        st.subheader("🍰 Gráfico de pastel")
        texto_8 = """
        El gráfico de pastel muestra la distribución de los 
        resultados del Valencia jugando como local. La mayor 
        proporción corresponde a los partidos ganados, representando 
        un 42.1% del total de sus encuentros locales. Por otro 
        lado, los partidos empatados equivalen al 31.6%, mientras 
        que los juegos perdidos conforman el 26.3% restante. En 
        conclusión, el equipo demuestra una clara tendencia 
        favorable al jugar en su estadio, ya que logró sumar 
        puntos en la gran mayoría de sus partidos de local. 
        """
        st.markdown(f"<div style='text-align: justify; font-size: 18px;'>{texto_8}</div>", unsafe_allow_html=True)
    
        col1, col2, col3 = st.columns([1, 7, 1])
        with col2:
            st.image("m_GRAFICO_CIRCULAR.png", width=800)

    elif grafico_seleccionado == 'Gráfico_barras':
        st.subheader("📊 Gráfico de barras")
        texto_9 = """
        El gráfico de barras muestra el promedio redondeado de 
        tarjetas amarillas que recibe cada equipo al jugar en 
        condición de visitante. Se observa que todos los clubes 
        se concentran únicamente en un promedio de 2 o 3 tarjetas 
        amarillas por partido. Equipos como Alaves, Espanol, Getafe, 
        Sevilla, Sociedad, Vallecano y Villarreal registran el promedio 
        más alto con 3 tarjetas amarillas, mientras que los demás se 
        mantienen en 2, por lo que la distribución refleja un 
        comportamiento disciplinario al no registrar valores 
        fuera del rango de 3 tarjetas.
        """
        st.markdown(f"<div style='text-align: justify; font-size: 18px;'>{texto_9}</div>", unsafe_allow_html=True)
    
        col1, col2, col3 = st.columns([1, 7, 1])
        with col2:
            st.image("m_GRAFICO_BARRAS.png", width=800)

    elif grafico_seleccionado == 'Nube_de_palabras':
        st.subheader("☁️ Nube de palabras")
        texto_10 = """
        Se convirtió todo el primer capítulo del libro de Mujercitas en 
        minúsculas, debido a que se simplificaba el proceso para la eliminación 
        de los stopwords al funcionar de manera efectiva sin dejar escapar 
        conectores o palabras innecesarias que comenzaban en una oración. 
        Asimismo, se eliminaron los números, signos de puntuación estructural, 
        delimitadores de diálogo e incisos, signos de entonación y variados 
        tipos de comillas y caracteres tipográficos. La eliminación de estos 
        caracteres fue indispensable para impedir que se pegaran a las palabras 
        adyacentes y se registraran las mismas palabras como distintas (como "mamá" 
        con "mamá,"), en cambio se conservaron las tildes y las palabras para 
        respetar la ortografía y el significado. Por otro lado, el criterio para 
        seleccionar las stopwords se basó en excluir palabras de función estrictamente 
        gramatical (artículos, preposiciones, conjunciones y pronombres) y algunos 
        conectores que no aportan contenido semántico. En conjunto, estas decisiones 
        eliminaron el ruido gramatical, permitiendo que la lista de frecuencias y 
        la de palabras final resalten de forma clara los personajes y las acciones 
        concretas que realizan. Estas decisiones influyeron de manera determinante 
        en los resultados, puesto que al eliminar el contenido gramatical innecesario 
        y consolidar las frecuencias reales, se evitó que conectores vacíos dominaran 
        el conteo, logrando que la nube de palabras final resalte con la mayor escala 
        visual a los personajes como Jo, Meg, Beth, Amy y la mamá, así como los temas 
        o hechos verdaderamente representativos del capítulo elegido como navidad, 
        regalos, dinero, trabajo y familia, y a los temas verdaderamente representativos 
        del capítulo como navidad, regalos, dinero y trabajo. 
        """
        st.markdown(f"<div style='text-align: justify; font-size: 18px;'>{texto_10}</div>", unsafe_allow_html=True)
    
        col1, col2, col3 = st.columns([1, 7, 1])
        with col2:
            st.image("m_NUBE.png", width=800)
    
    else:
        st.subheader("🌎 Mapa")
        texto_11 = """
        La estructuración de la ventana emergente se diseñó bajo un enfoque visual 
        limpio, jerárquico y centrado, usando etiquetas fundamentales para organizar 
        la información de los pilotos como la etiqueta i que se implementó para 
        colocar los nombres de ambos pilotos en cursiva, otorgándoles un estilo 
        diferenciado y estético dentro de la tarjeta de presentación, asimismo el 
        h1 para destacar los nombres de los pilotos como un título principal de mayor 
        tamaño, lo cual permite que se resalte de inmediato al abrir la ventana emergente 
        y facilitando la identificación rápida del perfil del piloto. Además, la 
        etiqueta b que se aplicó tanto para resaltar el nombre de la escudería de 
        cada piloto, dándolo peso visual frente al resto de la información complementaria, 
        y destacar la palabra "puntaje total" que permite que el lector localice de 
        manera inmediata la cifra exacta del total de puntaje obtenido de las carreras 
        por cada piloto, de manera que el valor numérico se mantiene en tipografía 
        estándar para equilibrar la lectura. Por otro lado, se utilizó un bloque con 
        alineación central (text-align: center) para mantener una simetría estética y 
        equilibrada, evitando que los elementos se dispersen alrededor del marcador 
        geográfico. Por último, se ubicó primero la fotografía del piloto con bordes 
        redondeados, permitiendo que el usuario identifique visualmente al deportista de 
        manera inmediata antes de leer los datos textuales, luego el nombre del piloto y 
        en la parte de abajo se coloca la información complementaria en líneas independientes 
        correspondiente a la escudería y el puntaje total, permitiendo que se lea la 
        información de manera secuencial. 
        """
        st.markdown(f"<div style='text-align: justify; font-size: 18px;'>{texto_11}</div>", unsafe_allow_html=True)
            
        with open("m_mapa_base.html", "r", encoding="utf-8") as mapa:
                html_content = mapa.read()
    
        components.html(html_content,height=600)

    # JACKELINE 
    if grafico_seleccionado == 'Gráfico_Histograma':
        st.subheader("📊 Histogramas")
        texto_12 = """
        Los goles anotados a nivel local por el equipo Villarreal son 
        variados. Si bien, hay pocos partidos en los que anota, se 
        destaca mucho los goles que anotó en más de 8 partidos que fueron 
        de 2 a 3 goles. Sin embargo, se anotaron de 5 a 6 goles en 3 
        partidos, los cuales dejan al equipo en una buena posición. A 
        comparación de los goles recibidos como visitante, ya que solo 
        llega a recibir 5 goles, lo cual es bueno, ya que debe acumular 
        más los goles anotados. Además, solo ha recibido entre 1 a 2 
        goles en ocho partidos, lo cual conviene al equipo porque su 
        resultado de goles anotados es mayor que los recibidos.
        """
        st.markdown(f"<div style='text-align: justify; font-size: 18px;'>{texto_12}</div>", unsafe_allow_html=True)

        col1, col2, col3 = st.columns([1, 7, 1])
        with col2:
                st.image("j_histograma_jacky.jpg", width=800)

    elif grafico_seleccionado == 'Gráfico_Pastel':
        st.subheader("🍰 Gráfico de pastel")
        texto_13 = """
        El equipo Villarreal tiene un porcentaje mayor de la cantidad 
        de partidos que ganó como local. Por ello, es un resultado muy 
        bueno para el equipo, porque es lo que se desea para estar en 
        una posición alta en La Liga. Además, solo se tiene un 15,8% de 
        la cantidad de partidos perdidos, cuyo resultado es bajo y por 
        ende, favorable para el equipo.
        """
        st.markdown(f"<div style='text-align: justify; font-size: 18px;'>{texto_13}</div>", unsafe_allow_html=True)
    
        col1, col2, col3 = st.columns([1, 7, 1])
        with col2:
            st.image("j_gráfico_pastel_Villarreal_local.png", width=800)

    elif grafico_seleccionado == 'Gráfico_barras':
        st.subheader("📊 Gráfico de barras")
        texto_14 = """
        Encontramos que siete equipos tienen un promedio de 3 en cuanto 
        a las tarjetas amarillas que reciben como visitantes. En cambio, 
        los demás equipos cuentan con un promedio de 2. Entonces, aquellos 
        equipos que tienen un promedio alto tienen posibilidades de obtener 
        una tarjeta roja en otros partidos.
        """
        st.markdown(f"<div style='text-align: justify; font-size: 18px;'>{texto_14}</div>", unsafe_allow_html=True)
    
        col1, col2, col3 = st.columns([1, 7, 1])
        with col2:
            st.image("j_gráfico_barras_equipos_visitantes.png", width=800)

    elif grafico_seleccionado == 'Nube_de_palabras':
        st.subheader("☁️ Nube de palabras")
        texto_15 = """
        Para comenzar, escogí el libro "El Extranjero" de Albert Camus, 
        porque me gustaría leer ese libro en mis tiempos libres. Además, 
        se me hizo sencillo encontrar el libro completo en internet. Por 
        otro lado, al realizar la limpieza del texto, escogí transformar 
        las palabras del texto a minúsculas, porque considero que se ve 
        bien estéticamente y se va a entender mejor. En cuanto a los signos, 
        eliminé los que estaban dentro del texto como el punto, comillas, 
        comas, signos de interrogación y exclamación, porque no me iba a 
        servir al momento de convertir el texto en una lista. Luego, al 
        crear una lista para eliminar los stopwords, escogí aquellas palabras 
        cortas de una sílaba que no son importantes dentro del texto y que 
        no aportan ningún significado y aquellas que son pronombres, artículos, 
        preposiciones y conjunciones. Solo quería tomar en cuenta las palabras 
        principales, al menos que tengan dos sílabas a más. Todo ello me 
        ayudó a tener frecuencias de palabras que tienen mayor relevancia 
        y puedan reflejarse mucho mejor en la nube de palabras. De esa 
        manera, se pueden reconocer aquellas palabras que son parte del 
        cuerpo del libro y lograr que los lectores de este libro puedan 
        reconocerlas al instante. Es así que los colores que escogí combinan 
        y dan mayor atractivo a las palabras.
        """
        st.markdown(f"<div style='text-align: justify; font-size: 18px;'>{texto_15}</div>", unsafe_allow_html=True)
    
        col1, col2, col3 = st.columns([1, 7, 1])
        with col2:
            st.image("j_nube_palabras_extranjero.png", width=800)
    
    else:
        st.subheader("🌎 Mapa")
        texto_16 = """
        Como lo hicimos en clase, traté de organizar los datos en el orden 
        que nos pedían y agregué algunos más en el diccionario de Datos 
        adicionales, los cuales quería que aparecieran en la tabla para que 
        después pueda utilizarlos fácilmente en la creación del mapa con 
        ventana emergente. En el diseño, coloqué sobre todo el nombre de 
        los pilotos con negrita para que se destacara más. Además, el icono 
        que usé fue del carro porque tiene mucha relación con el trabajo que 
        hacen. Elegí el color azul, porque siento que es un color fuerte que 
        se relaciona con los pilotos. En el primer mapa solo coloqué el nombre 
        y la Escudería, porque quería probar cómo salía y elegí el color 
        naranja, para que no sea mucho fuerte, se sienta cálido. Asimismo 
        elegí el ícono se "user" porque consideraba que no había mucha 
        información, a comparación del segundo porque es más complejo.
        """
        st.markdown(f"<div style='text-align: justify; font-size: 18px;'>{texto_16}</div>", unsafe_allow_html=True)
            
        with open("j_mapa_pilotos_2.html", "r", encoding="utf-8") as mapa:
                html_content = mapa.read()
    
        components.html(html_content,height=600)
