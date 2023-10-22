from rxconfig import config

import reflex as rx

class State(rx.State):
    pass

@rx.page(route='/', title='AOF Web')
def index() -> rx.Component:
    return rx.fragment(
        
        rx.box(
            rx.flex(
                rx.center(
                    rx.link(rx.image(src="/aof.png", width="80px", padding="7px"), href="http://localhost:3000/")
                ),
                rx.spacer(),
                rx.center(
                    rx.breadcrumb(
                        rx.breadcrumb_item(
                            rx.breadcrumb_link("MALWARE", href="/malware"),
                        ),
                        rx.breadcrumb_item(
                            rx.breadcrumb_link("SOFTWARE LIBRE", href="/softwarelibre"),
                        ),
                        rx.breadcrumb_item(
                            rx.breadcrumb_link("ANTIMALWARE", href="/antimalware"),
                        ),

                        separator=" | ",
                        font_size="16px"
                    ),
                ),
                rx.spacer(),
                rx.color_mode_button(rx.color_mode_icon(), background_color="#F49248", is_dark=True),
            ),

            background_color="#F49248",
            width="100%",
        ),
        
        rx.center(
            rx.vstack(
                rx.heading("Web creada para la actividad 2 de Aplicaciones Ofimaticas.",
                size="lg",
                padding="35px",
                padding_bottom="5px"
                ),
                rx.text("En esta pagina podras encontrar varios tipos de malware, antimalwares y antivirus, aparte de que es y algunos programas de software libre.",
                padding="35px",
                padding_top="5px",
                text_size="15px"
                ),

                rx.image(src="/insti.png", width="55%", margin_button="20px"),

                rx.box(
                    rx.text("Es posible que en algunos dispositivos no se vea correctamente. Versión responsive en camino.", color="dark", _as="strong"),
                    background_color="#E74D42",
                    border_radius="lg",
                    padding="10px",
                    margin_top="20px"
                )
            ),
        ),

        rx.box(
            rx.flex(
                rx.text("Página creada por: ", rx.link("Juan Rodríguez", href="https://instagram.com/la__cucheria?igshid=OGQ5ZDc2ODk2ZA==", button=True, is_external=True)),
                rx.spacer(),
                rx.image(src="/by-nc-nd.png", width="90px"),
            ),
            background_color="#F49248",
            margin_top="200px",
            bottom="0",
            padding="2em",
            width="100%",
        ),
    )

@rx.page(route='/malware', title='AOF Web -> Malware')
def malware():
    return rx.fragment(

        rx.box(
            rx.flex(
                rx.center(
                    rx.link(rx.image(src="/aof.png", width="80px", padding="7px"), href="http://localhost:3000/")
                ),
                rx.spacer(),
                rx.center(
                    rx.breadcrumb(
                        rx.breadcrumb_item(
                            rx.breadcrumb_link("MALWARE", href="/malware"),
                        ),
                        rx.breadcrumb_item(
                            rx.breadcrumb_link("SOFTWARE LIBRE", href="/softwarelibre"),
                        ),
                        rx.breadcrumb_item(
                            rx.breadcrumb_link("ANTIMALWARE", href="/antimalware"),
                        ),

                        separator=" | ",
                        font_size="16px"
                    ),
                ),
                rx.spacer(),
                rx.color_mode_button(rx.color_mode_icon(), background_color="#F49248", is_dark=True),
            ),

            background_color="#F49248",
            width="100%",
        ),

        rx.fragment(
            rx.heading("Malware", size="2xl", margin_top="30px", margin_botton="35px", margin_left="35px"),
            rx.text("El malware es un tipo de software con intenciones maliciosas, estás pueden ser desde el robo de tu información hasta la perdida de tus archivos. Vistos que el mal que pueden hacer es tan variado, estos se clasifican en algunas categorías combinables.", margin_left="55px", margin_right="55px", text_align="justify"),

            rx.heading("Spyware", size="lg", margin_top="30px", margin_botton="35px", margin_left="35px"),
            rx.text("Este tiene como objetivo robarte información, para posteriormente venderla, o en el peor de los casos robar datos sensibles para chantajear al dueño de estos.", margin_left="75px", margin_right="75px", text_align="justify"),
            rx.heading("Ransomware", size="lg", margin_top="15px", margin_botton="35px", margin_left="55px"),
            rx.text("Uno de los malware de moda. Se caracteriza por cifrar tus archivos, dejando solo los indispensables para que no se colapse el dispositivo, ya que la intención de este es pedirte un rescate por tus archivos. Aunque no suelen darte la clave para descifrar tus archivos, en caso de que te sobre en par de bitcoins, puedes probar suerte. Un ejemplo podria ser ", rx.link("CryptoLocker.", href="https://es.wikipedia.org/wiki/CryptoLocker", color="rgb(107,99,246)", button=True, is_external=True), margin_left="75px", margin_right="75px", text_align="justify"),
            rx.heading("Troyanos", size="lg", margin_top="15px", margin_botton="35px", margin_left="55px"),
            rx.text("Un tipo de malware cuyo nombre suele resonar bastante. Estos al momento de ejecutarse brindan al atacante acceso a tu sistema. Uno de los muchos ejemplos pordria ser ", rx.link("Qbot malware.", href="https://www.malwarebytes.com/blog/detections/backdoor-qbot", color="rgb(107,99,246)", button=True, is_external=True), margin_left="75px", margin_right="75px", text_align="justify"),
            rx.heading("Gusanos", size="lg", margin_top="15px", margin_botton="35px", margin_left="55px"),
            rx.text("Personalmente, estos son los que más temo, ya que puede ser molesto deshacerse de ellos. Estos una vez instalados en un dispositivo se duplican en otro dispositivo, ya sea alojándose en un archivo o se desplazan por la red de tu casa. Un buen ejemplo podria ser", rx.link("SQL Slammer", href="https://es.wikipedia.org/wiki/SQL_Slammer", button=True, is_external=True), margin_left="75px", margin_right="75px", text_align="justify"),
            rx.heading("Virus", size="lg", margin_top="15px", margin_botton="35px", margin_left="55px"),
            rx.text("Vendría a asignarse a los movimientos malintencionados y ocultos que realiza un software.", margin_left="75px", margin_right="75px", text_align="justify"),
            rx.heading("Bots", size="lg", margin_top="15px", margin_botton="35px", margin_left="55px"),
            rx.text("Más que un tipo de malware es una especie de estado en la que cae tu ordenador al ser controlado por un atacante. Lo más seguro es que tu dispositivo no sea el único afectado, lo más probable es que forme parte de una botnet. Estas sirven, entre muchas cosas, para hacer ataques DDOs o usar la botnet para minar criptomonedas.", margin_left="75px", margin_right="75px", text_align="justify"),
            rx.heading("Keyloggers", size="lg", margin_top="15px", margin_botton="35px", margin_left="55px"),
            rx.text("Un tipo de malware muy peligroso. Este analiza lo que tecleas, de tal forma que en caso de que escribas alguna contraseña al iniciar sesión, el atacante sabrá tu contraseña, aparte de cualquier dato adicional que hayas tecleado.", margin_left="75px", margin_right="75px", text_align="justify"),
            rx.heading("Secuestradores de navegadores", size="lg", margin_top="15px", margin_botton="35px", margin_left="55px"),
            rx.text("Este tipo de malware se volvió conocido por una reciente noticia relacionada con el juego Minecraft. Un lanzador pirata realmente famoso y conocido de este juego, al ser analizado en profundidad resulto que en segundo plano robaba las contraseñas y usuarios guardados en el navegador.", margin_left="75px", margin_right="75px", text_align="justify"),

            rx.text("En esta selección hemos recolectado algunos tipos de malware. Pero estando en un sector en constante evolución, lo más probable es que se sigan creando nuevas maneras de atacar a los usuarios.", margin_left="40px", margin_right="55px", margin_top="55px", text_align="justify"),
        ),
        rx.center(
            rx.box(
                element="iframe",
                src="https://cybermap.kaspersky.com/es/widget/dynamic/dark",
                width="65%",
                height="600px",
                margin_top="55px"
            ),
        ),
        rx.center(
            rx.text("Gracias a Kaspersky por la infomación. 😊")
        ),


        rx.breadcrumb(
            rx.breadcrumb_item(
                rx.breadcrumb_link(rx.button("AntiMalwares ->", color_scheme='orange', color="black", size="sm"), href="/antimalware", margin_right="5px")
            ),
            float="right",
            margin_top="45px"
        ),

        rx.box(
            rx.flex(
                rx.text("Página creada por: ", rx.link("Juan Rodríguez", href="https://instagram.com/la__cucheria?igshid=OGQ5ZDc2ODk2ZA==", button=True, is_external=True)),
                rx.spacer(),
                rx.image(src="/by-nc-nd.png", width="90px"),
            ),
            background_color="#F49248",
            margin_top="90px",
            padding="2em",
            width="100%",
        ),
    )

@rx.page(route='/softwarelibre', title='AOF Web -> Antimalware')
def softwarelibre():
    return rx.fragment(

        rx.box(
            rx.flex(
                rx.center(
                    rx.link(rx.image(src="/aof.png", width="80px", padding="7px"), href="http://localhost:3000/")
                ),
                rx.spacer(),
                rx.center(
                    rx.breadcrumb(
                        rx.breadcrumb_item(
                            rx.breadcrumb_link("MALWARE", href="/malware"),
                        ),
                        rx.breadcrumb_item(
                            rx.breadcrumb_link("SOFTWARE LIBRE", href="/softwarelibre"),
                        ),
                        rx.breadcrumb_item(
                            rx.breadcrumb_link("ANTIMALWARE", href="/antimalware"),
                        ),

                        separator=" | ",
                        font_size="16px"
                    ),
                ),
                rx.spacer(),
                rx.color_mode_button(rx.color_mode_icon(), background_color="#F49248", is_dark=True),
            ),

            background_color="#F49248",
            width="100%",
        ),

        rx.fragment(
            rx.heading("Software libre", size="2xl", margin_top="30px", margin_botton="35px", margin_left="35px"),
            rx.text("El software libre se caracteriza principalmente por qué el usuario puede consultar el código fuente, aparte que suele tener disponible las cuatro libertades que se detallan más adelante en la pequeña infografía.", margin_left="55px", margin_right="55px", margin_top="20px", text_align="justify"),
            rx.text("Uno de los principales impulsores de este tipo de software es Richard Stallman. Un estaudinidense creador de GNU, el primer proyecto de código abierto, proyecto al que posteriormente se añadió Linus Torvalds creando GNU/Linux.", margin_left="55px", margin_right="55px", margin_top="20px", text_align="justify"),
            rx.center(
                rx.box(
                    element="iframe",
                    src="https://www.youtube.com/embed/8SdPLG-_wtA?si=ZlC3Q40j5LxTnkNb",
                    width="60%",
                    height="400px",
                    margin_top="55px",
                ),
            ),
            rx.text("Esto en beneficioso ya que tenemos la confianza que no contiene ningun tipo de malware, aparte que la comunidad puede realizar modificaciones para mejorar el funcionamiento.", margin_left="55px", margin_right="55px", margin_top="55px", text_align="justify"),
            rx.center(rx.image(src="/info.jpg", margin_top="45px", width="35%"),),
        ),

        rx.box(
            rx.flex(
                rx.text("Página creada por: ", rx.link("Juan Rodríguez", href="https://instagram.com/la__cucheria?igshid=OGQ5ZDc2ODk2ZA==", button=True, is_external=True)),
                rx.spacer(),
                rx.image(src="/by-nc-nd.png", width="90px"),
            ),
            background_color="#F49248",
            margin_top="90px",
            padding="2em",
            width="100%",
        ),
    )

@rx.page(route='/antimalware', title='AOF Web -> Software Libre')
def antimalware():
    return rx.fragment(

        rx.box(
            rx.flex(
                rx.center(
                    rx.link(rx.image(src="/aof.png", width="80px", padding="7px"), href="http://localhost:3000/")
                ),
                rx.spacer(),
                rx.center(
                    rx.breadcrumb(
                        rx.breadcrumb_item(
                            rx.breadcrumb_link("MALWARE", href="/malware"),
                        ),
                        rx.breadcrumb_item(
                            rx.breadcrumb_link("SOFTWARE LIBRE", href="/softwarelibre"),
                        ),
                        rx.breadcrumb_item(
                            rx.breadcrumb_link("ANTIMALWARE", href="/antimalware"),
                        ),

                        separator=" | ",
                        font_size="16px"
                    ),
                ),
                rx.spacer(),
                rx.color_mode_button(rx.color_mode_icon(), background_color="#F49248", is_dark=True),
            ),

            background_color="#F49248",
            width="100%",
        ),

        rx.fragment(
            rx.center(
                rx.vstack(
                    rx.heading("Antimalware", size="2xl"),
                    rx.text("Los antimalware y los antivirus nos protegen de las amenazas. Por eso es importante al menos de vez en cuando analizar nuestro equipo. A continuación tienes una lista de los antimalware y antivirus más conocidos.", text_align="justify"),
                ),
            ),

            rx.center(rx.heading("Antivirus", size="xl"), margin_top="50px"),
            rx.center(
                rx.box(
                    rx.hstack(
                        rx.image(src="/avast.png", width="10%"),
                        rx.vstack(
                            rx.heading("Avast", size="lg", text_align="left", color="orange"),
                            rx.text("Avast es un software antivirus y suite de seguridad de la firma checa Avast Software (antes conocida como ALWIL Software), desarrollado a principios de la década de 1990.", text_align="justify"),
                            rx.link(
                                rx.button(
                                    "Descargar",
                                    bg="orange",
                                    size="md"
                                ),
                                href="https://www.avast.com/es-es/index#pc",
                                is_external=True,  
                            )
                        ),
                    ),
                    margin="30px"
                )
            ),
            rx.html("<hr>"),
            rx.center(
                rx.box(
                    rx.hstack(
                        rx.image(src="/k.png", width="10%"),
                        rx.vstack(
                            rx.heading("Kaspersky", size="lg", text_align="left", color="#00AEFF"),
                            rx.text("Kaspersky es una compañía internacional dedicada a la seguridad informática con presencia en aproximadamente 195 países del mundo.", text_align="justify"),
                            rx.link(
                                rx.button(
                                    "Descargar",
                                    bg="orange",
                                    size="md"
                                ),
                                href="https://www.kaspersky.es/downloads#compare-table",
                                is_external=True,  
                            )
                        ),
                    ),
                    margin="30px"
                )
            ),
            rx.html("<hr>"),
            rx.center(
                rx.box(
                    rx.hstack(
                        rx.image(src="/m.png", width="10%"),
                        rx.vstack(
                            rx.heading("Microsoft defender", size="lg", text_align="left"),
                            rx.text("Microsoft Defender para usuarios individuales es una aplicación de seguridad entre dispositivos que ayuda tanto a individuos como a familias a proteger sus datos y dispositivos y a estar más seguros online gracias a la protección contra malware5, las notificaciones de seguridad en tiempo real, las recomendaciones de seguridad y la supervisión de los robos de identidad.",  text_align="justify"),
                            rx.link(
                                rx.button(
                                    "Descargar",
                                    bg="orange",
                                    size="md"
                                ),
                                href="https://www.microsoft.com/es-es/microsoft-365/microsoft-defender-for-individuals",
                                is_external=True,  
                            )
                        ),
                        padding_left="150px", 
                        padding_right="150px"
                    ),
                    margin="30px"
                )
            ),
            rx.center(rx.heading("Antimalware", size="xl"), margin_top="50px"),
            rx.center(
                rx.box(
                    rx.hstack(
                        rx.image(src="/mal.png", width="10%"),
                        rx.vstack(
                            rx.heading("Malwarebytes", size="lg", text_align="left", color="blue"),
                            rx.text("Malwarebytes (anteriormente Malwarebytes Anti-Malware, abreviado como MBAM) es un software anti-malware para Microsoft Windows, macOS y Android que detecta y elimina el malware.",  text_align="justify"),
                            rx.link(
                                rx.button(
                                    "Descargar",
                                    bg="orange",
                                    size="md"
                                ),
                                href="https://es.malwarebytes.com/mwb-download/thankyou/",
                                is_external=True,  
                            )
                        ),
                    ),
                    margin="30px"
                )
            ),
        ),

        rx.breadcrumb(
            rx.breadcrumb_item(
                rx.breadcrumb_link(rx.button("Malwares ->", color_scheme='red', color="black", size="sm"), href="/malware", margin_right="5px")
            ),
            float="right",
            margin_top="45px"
        ),

        rx.box(
            rx.flex(
                rx.text("Página creada por: ", rx.link("Juan Rodríguez", href="https://instagram.com/la__cucheria?igshid=OGQ5ZDc2ODk2ZA==", button=True, is_external=True)),
                rx.spacer(),
                rx.image(src="/by-nc-nd.png", width="90px"),
            ),
            background_color="#F49248",
            margin_top="90px",
            padding="2em",
            width="100%",
        )
    )

# Add state and page to the app.
app = rx.App()
app.add_page(index)
app.add_page(malware, route="/malware")
app.add_page(softwarelibre, route="/softwarelibre")
app.add_page(antimalware, route="/antimalware")
app.compile()
