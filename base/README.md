## Cosas por hacer
-Agregar un tipo de categoría para que el programa reconozca
 si se trata de código, traducción de un idioma a otro etc
 para así poder manipularlo adecuadamente. Por ejemplo, si se
 trata de traducir entonces el programa puede cambiar de inglés
 a españo y viceversa sin que el usuario tenga que escribir ambas.
 En el caso del código se puede mostrar con diferentes colores 
 en vez del mismo color etc.
-Poder presionar botón arriba etc para mostrar últimas habilidades
 registradas en caso de que escribir la nueva sea muy similar
 a alguna de las anteriores
-Autocompletar inicios de frases recurrentes como "Responder correctamente a"
-Tal vez permitir elegir de un selection box el tipo de habilidad. Por ejemplo
 una opción puede ser significado que contiene la frase "qué significa X en Y"
 y el usuario rellena X con lo que se quiere saber y Y con el contexto, eg:
 qué significa EBS en AWS. Esto puede permitir tambien una automatización de cosas como colocar las letras en cursiva o negrita etc Otras opciones pueden ser:
    -traducción
    --frase:traducir X del Y a Z
    ---eg:
    ----traducir peel del inglés al español
    -categorías
    --frase:Enumerar ...
    -Contenido
    --frase: Explicar contenido del X llamado Y
    ---eg:
    ----Explicar contenido del video llamado Superstructures with Daniel Schmachtenberger
-Permitir colocar algún símbolo etc en la habilidad para poder generar 
 otras habilidades automáticamente. eg:
 -Habilidad Infrastructure as a Service $$(IaaS)\nSoftware as a Service $$(SaaS)\nPlatform as a Service $$(PaaS). El símbolo $$ indica generar una pregunta de
 tipo que significa la sigla que está dentro de $$(). Habría que indicar el contexto
-Permitir agregar imagenes etc cómo en el caso del coeficiente de Gini
-Lógica sencilla para mostrar habilidades a condicionar/mantener
-Permitir cargar bulks para poder condicionar habilidades. eg
--cargar paises y capitales para desarrollar la habilidad de decir capital
  según pais (o viceversa). Designar el tipo de habilidad (esta podría ser
  algo así como intraverbal simple) para que se haga el condicionamiento
  respectivo.
-Tener plantillas para poder repasar habilidades pequeñas pero que 
 requieren de pasos previos. eg
--repasar hacer un menu en vue y element ui requiere una plantilla con
  vue instalado, element-ui instalado y las importaciones y componentes
  globales escritos. Tal vez se pueda con git. Siendo ramas diferentes
  templates distintos o commits.
-Hacer una columna de created at y de updated at tal vez en la tabla puente
-permitir hacer jerarquias manipulando nodos y ejes (de modo visual e   interactivo) de modo que rápido se puedan generar automáticamente por lo menos
 2 habilidades ante un diagrama que muestre esta jerarquia X -> Y (X padre de Y):
 decir el padre de Y
 decir un(el) hijo de X
 Esto aumenta la velocidad de escritura de habilidades
-Desarrollar/buscar algoritmo que infiera la categoría (otros, aws etc) con base
 en las palabras que se colocan en la habilidad
-Permitir opción de ver al azar (o de otras formas) temas de un tópico específico
 (como aws) tal que se vean todas antes de repetir (o de otras maneras). Esto
 sirve para tener más fortalecidas habilidades de un tópico particular.
-Permitir mostrarle al programa por ejemplo a traves de un #? o algún símbolo
 que una respuesta también puede ser una habilidad. Si por ejemplo se está viendo la feature de EC2 como elastic load balancing y la habilidad pide enumerar los tipos de elastic load balancing pero el usuario no sabe que 
 hace cada uno de los tipos entonces en la respuesta a la habilidad se puede 
 colocar por cada tipo de load balancing un #? (o el símbolo elegido) para indicarle al programa que cree una habilidad del tipo: Decir qué hace [TIPO X]
-Con base al número de habilidades ingresadas y/o repasadas se dan tokens que
 pueden ser intercambiados por ver gráficas etc
-Interfaz similar a la del dashboard de EPICA pero que haya que clickear en cada
 el-card para que aparezca la tabla, para así registrar cuales son más preferidas
 (más valoradas) y usadas como reforzadores
-Poder colocar hitos o marcas verticales en graficas temporales para poder
 ver cambios en las mismas después del hito.
 eg:
  colocar un hito cuando se permitió agregar habilidades desde el front y no
  desde el shell (a = Ability(ability=...); a.save(); a.answers_set.create(answer=...); a.topic = Topic(id=...); a.save())
-Premiar por superar ciertos promedios etc
 eg:
  premiar cuando se sobrepasa el promedio de habilidades ingresadas por dia
-Prohibir ingresar nuevas habilidades después de x número a menos que se "pague" 
 por ellas
-Para más adelante: Con lo que ingresa un usuario en el dia (o cualquier intervalo
 de tiempo) hacer pequeños robots que operen en mundos pequeños. La intención acá
 es tratar de simular el refuerzo que se obtiene cuando alguien hace más inteligente
 a otra persona a través de la información que le da. (tal vez esto se pueda hacer
 de alguna manera con teoría de la información)
-ELABORACIÖN DE IDEA DE MÁS ARRIBA
 Adquirir habilidades de determinar si x fruta (comida) es acida o alcalina:
 se pasa el nombre de las frutas y su nivel de ph y se forman habilidades del tipo:
 -Decir si la x (eg x=piña) es ácida o alcalina
 -Enumerar frutas alcalinas
-Poder relacionar habilidad a respuesta de una habilidad por ejemplo si la
 habilidad es "Decir que significa el 0, 1 y 2 en user_type de la tabla X"
 y su respuesta es "0 = anonimo, 1=..." entonces se puede agregar una 
 habilidad relacionada a esta respuesta diciendo "Cómo se supo que 0 = anonimo, 1=..." es la respuesta correcta
-Añadir posibilidad de agregar topic en front
-Corregir codigo que no obtiene directamente los topics en front de la tabla Topic
 sino que lo obtiene de las habilidades (por lo que si existe un tópico sin habilidad no se mostrará en front)
-Refrescar pagina de manera eficiente despues de enviar habilidad
-Establecer dificultad de condicionamiento de habilidad
-Permitir editar habilidad
-Pixel de abilities app
-Otra app (otro microservicio tal vez) que permita mostrar y comparar desempeño
 en app de habilidades etc (por ejemplo en términos de # de habilidades ingresadas al dia,
 o # de temas ingresados al dia etc) con base en lo hecho en el día presente y día(s) anterior(es) tal que por ejemplo se pueda mostrar que se hizo/comió etc a la
 par del desempeño medido en la app de habilidades
-Generación de habilidades a través de preguntas como
 -Qué Xs cumplen la(s) propiedad(es) (Y1)
 --eg
 ---Qué repositorios solo se conectan a postgres y usan JS
 ---Qué repositorios usan Typescript
 ---Cuántos Deployment objects hay en cada nodo del cluster epica-production-aks
 ---Cuáles son las estrellas más longevas
 ---Enumerar riesgos catastróficos
 -Dónde está X
 --eg
 ---Cuál es la carpeta padre del archivo feature-flipper.js
-Tokens por desempeños x
-Para las nuevas palabras, que el programa haga contingencias para
 reforzar y generalizarlas por ejemplo pedir hacer frases etc con eso
-Tal vez despues del primer repaso, no permitir repasar x habilidad
 sino hasta que haya pasado cierto tiempo
-poder linkear habilidades que se confunden. eg si el significado 
 de una palabra (habilidad A) se confunde con el significado de otra
 palabra (habilidad B) entonces linkearlas para que aparezcan más 
 cercanas en el tiempo etc.
-Si se registra que el usuario permanece un tiempo continuado en la
 plataforma, pedir calificación de motivación frente a la interacción
 con la misma (tambien puede servir un poco para detectar si la persona
 se fue y dejó la app abierta o está interactuando)
-Se pueden transformar las habilidades que responden booleanamente tal 
 que por ejemplo se complete la frase. eg: si la habilidad es "Decir sí 
 o no a la siguiente afirmación: Para Los Horcones la ciencia no solo
 provee de procedimientos sino valores también." se puede cambiar tal que
 se complete la palabra valores etc.
-Mostrar por temas cuantas habilidades hay por día. El programa, con base en esto,puede alertar al usuario que no ha ingresado habilidades de x tema o 
 x características o reforzar determinado desempeño (eg variedad de temas
 por día, o constancia en x tema(s) etc)
-Usar diccionario etc para guardar abreviaciones de palabras o frases (pueden ser autoclíticos) tal que el usuario escriba las abreviaciones
 y el programa interprete en palabras normales. eg {':=':'significado'}
 el programa interpreta ':=' del usuario como 'significado'. Otro eg 
 {'X => Y':'Si X entonces Y'} el programa interpreta 'X => Y' como
 'Si X entonces Y' en donde X y Y son variables.
-Estoy observando "procrastinación" o una secuencia de eventos
 similar para anotar las habilidades. Realizar contingencias que permitan
 mejorar esto.
-Tal vez usar computed prop para la lista de habilidades de modo que no
 se cacheen y no se computen por cada ocasión.
-Llamar al endpoint solo cuando sea necesario. Por ejemplo cuando se carga
 la app de 0s y no cuando se pasa de una pagina a otra.
-Cambiar el color de rojo a verde según se anotan más habilidades, sé repasan
 más etc
-Poner fotos para poder responder a ellas
-Colocar algo aleatorio reforzante al abrir una habilidad
-De las habilidades automaticas según tipo de habilidad se pueden generar
 unas para la habilidad de traducir de un idioma a otro:
 -Decir cómo se escribe la palabra que en español es X
 -Cómo se pronuncia la palabra Y
 -Añada un ejemplo del uso de esa palabra en una frase
-Generar combobox en select para elegir varios tópicos que se relacionan
 con una habilidad. eg:
 -diferencia entre created y mounted hooks se relaciona con el tópico 
  tecnologias de internet, Vue, React (si es que comparten la misma
  funcionalidad ambos)
-Ir guardando en lista etc las habilidades repasadas en el día. Tal vez
 para repasar de nuevo aquellas categorizadas como dificiles
-Permitir describir la emoción etc en cada repaso de habilidad
 -Eg:
 --Si fué emitida la respuesta cuando sentía (la estimulación)
   parecía estar asociada a una baja probabilidad de dicha respuesta
 --Fué rápida, cómo quisiera

 


