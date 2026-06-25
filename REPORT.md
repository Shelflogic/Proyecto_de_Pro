Este proyecto está pensado para organizar y gestionar la renta de equipos y personal para eventos (como escenarios, consolas de sonido, micrófonos, luces, etc). El objetivo principal es simular cómo funcionaría el negocio de una productora, controlando que los recursos alcancen y que no se superpongan las fechas entre diferentes clientes.
El programa se divide en dos partes principales:

1. Panel de Empresas (Proveedores)
Registrar inventario: Permite guardar una empresa nueva en el sistema y definir qué cantidad tiene de cada recurso en su almacén (por ejemplo: cuántos escenarios o cuántas consolas tiene para rentar).

Control de datos: Se pueden ver las empresas guardadas y borrar un inventario, pero el programa bloquea la eliminación si esa empresa ya tiene un compromiso o un evento agendado en el futuro.

2. Panel de Clientes (Reservas y Fechas)
Control de disponibilidad por fecha: Cuando un cliente quiere rentar elementos de algun enventario, elige la empresa, las cantidades y los días que va a durar su evento. El programa revisa si otra persona ya reservó con esa misma empresa en esas fechas. Si hay coincidencia, el segundo cliente solo puede rentar lo que quede libre en el almacén de la empresa para esos días.

Sugerencia automática de fechas: En caso de que el cliente pida una fecha donde la empresa ya está ocupada y no presente una completa disponibilidad, el programa analiza el calendario completo y le propone un "hueco" o intervalo libre en el futuro donde la empresa vuelva a tener todo su inventario disponible por la misma cantidad de días que el usuario quería.

Código de seguimiento único: Al inicar una reserva, el sistema genera un número de asignación único para ese evento. Con este número, el cliente puede entrar después al menú para revisar exactamente qué fue lo que rentó o cancelar la reserva por completo, lo que devuelve los equipos al almacén de inmediato para que otra persona los pueda usar.

Para la estructura del programa, decidí modelar el negocio de una productora de eventos. La razón principal de esta elección es que este tipo de empresas maneja inventarios caros y personal muy especializado, lo que hacía perfecto el reto de controlar la disponibilidad de los recursos por tiempo.
Toda la persistencia de datos la manejé separando la información en archivos JSON independientes (inventarios.json, clientes.json y lista_asignacion.json). Tomé esta decisión para que el código fuera más limpio, y fácil de leer, evitando mezclar los datos del stock de las empresas con las agendas privadas de los clientes.
Para darle realismo al programa, diseñé tres reglas lógicas obligatorias dentro del flujo de contratación:

Renta de Consola de Sonido exige Ingeniero de Sonido (Co-requisito / Inclusión):
Una consola de audio profesional es un equipo de alta gama extremadamente complejo y delicado. Tomé la decisión de bloquear el alquiler si no se incluye al menos un ingeniero, porque en la vida real un cliente común podría romper el equipo o no saber operarlo correctamente. Así la empresa asegura que su inversión está protegida por un profesional técnico.

Consola de Luces Tradicionales excluye Consola Inteligente (Exclusión Mutua):
Estas dos consolas representan tecnologías y flujos de trabajo totalmente opuestos. Las luces tradicionales usan sistemas de dimers analógicos antiguos, mientras que las inteligentes van por protocolo digital moderno (DMX). Un mismo evento no necesita rentar los dos cerebros de control a la vez; decidirse por un formato excluye la necesidad del otro, y dejar que alquilen ambos sería un gasto innecesario para el cliente y un desperdicio de stock para la empresa.

Dependencia de Luces con Efectos (Restricción Cruzada):
Las luces con efectos especiales (como cabezas móviles o estrobos) no funcionan solas; necesitan obligatoriamente una consola inteligente para ser programadas y controladas. Decidí que el programa bloquee la renta de luces con efectos si el usuario no ha seleccionado primero una consola inteligente, ya que de lo contrario el cliente se llevaría a su evento un equipo costoso que no podría ni encender, generando quejas y problemas.

El desarrollo de este proyecto me permitió enfrentarme por primera vez a problemas reales de lógica y a herramientas fundamentales que no había manejado a fondo:

1. Gestión de Datos con JSON
Antes de este proyecto no sabía cómo hacer que los datos de un programa se quedaran guardados al cerrarlo, por lo que tuve que aprender a usar el módulo json de Python para conectar mi código con archivos externos (.json). Aprendí a cargar la información usando json.load() para convertir los textos guardados en diccionarios de Python con los que mi lógica pudiera trabajar; y a actualizar y reescribir esos archivos usando json.dump(), asegurando que cada nueva empresa creada o cada evento agendado se registrara de forma permanente.

2. Manejo de Fechas y Tiempo con Datetime
Controlar los calendarios y las duraciones fue una tarea complicada. Gracias a esto, aprendí a dominar el módulo datetime.
Descubrí cómo transformar textos con formato de fecha (como "Año-Mes-Día") en objetos de tiempo reales que Python pueda entender, usando datetime.strptime().
Aprendí a realizar operaciones matemáticas con fechas, como restar la fecha de fin menos la fecha de inicio para calcular la duración exacta de un evento en días y poder buscar "huecos" libres en el calendario de las empresas.

3. Lógica de Programación y Estructuras de Datos
Tuve que aprender a organizar diccionarios anidados complejos (donde un evento tiene una empresa, y esa empresa tiene recursos y períodos de tiempo) y a diseñar algoritmos para comparar intervalos de fechas, asegurándome de que ningún recurso se rente dos veces en el mismo momento.


Durante el desarrollo del proyecto me topé con varios problemas complejos que me obligaron a investigar y a cambiar la lógica que tenía pensada al principio. Al ser de primer año, nunca había trabajado con persistencia de datos ni con el manejo formal de fechas. Al principio el programa perdía toda la información cada vez que lo cerraba, y no sabía cómo calcular la duración de los eventos leyendo las fechas como texto. Para darle solucióna este problema, dediqué tiempo a investigar la documentación de Python. Aprendí a estructurar correctamente los archivos .json para guardar diccionarios complejos y entendí cómo usar strptime para transformar los textos en objetos de tiempo con los que sí podía hacer operaciones matemáticas.
Me di cuenta de que si varios clientes hacían reservas con la misma empresa, los datos se podían mezclar. Necesitaba una manera de identificar cada contrato de forma única para que el usuario pudiera revisar o cancelar su evento específico después.
Para solucionar este problema, diseñé una función de asignación de eventos que genera de forma automática un número único para cada reserva. Este número se vincula directamente al JSON, sirviendo como una "llave" limpia para buscar o borrar los datos sin alterar los eventos de los demás.
Crear una funcion inteligente para sugerir el proximo intervalo disponible fue, sin duda, la parte más difícil del proyecto. Cuando una empresa no tenía disponibilidad, crear el algoritmo para sugerir el próximo intervalo fue complicado al principio. Intentar buscar un espacio vacío comparando fechas desordenadas directamente desde el archivo de clientes hacía que el código fallara o se saltara 
para resolverlo, decidí cambiar la estrategia: primero extraje todos los períodos ocupados de la empresa y los organicé cronológicamente dentro de una lista. Al tener la lista completamente ordenada de menor a mayor, fue mucho más fácil programar un ciclo que fuera comparando el final de un evento con el inicio del siguiente. Así logré que el sistema detectara con precisión el primer "hueco" disponible que fuera igual o mayor a los días que el cliente necesitaba.