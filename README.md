# <h1 align=center> **PROYECTO INDIVIDUAL Nº2** </h1>

## Introduccion

El dataset consiste en un archivo excel que contiene dos tablas: hechos y victimas, y un diccionario para cada tabla.

La tabla Hechos tiene informacion de lo ocurrido en el accidente tales como: donde fue, en que calle y en que comuna, su posicion de latitud y longitud, dice cuantas victimas hay y tambien detalla el tipo de vehiculo o estado de transito que tenia el acusado y la victima, definimos acusado como aquel vehiculo que causo el daño (mas no tiene que ser la causa del accidente) en el informe lo especifica como "Vehículo que ocupaba quien resultó acusado/a del hecho, sin
implicar culpabilidad legal" y la victima evidentemente es el vehiculo de la persona que fallecio o se lastimo, tambien hay informacion de si la via era una avenida o calle o autopista.

La tabla victimas tiene informacion acerca de las victimas del accidentes como el sexo, la edad, y tambien hay un campo llamado rol que indica el rol de cada victima, puede ser conductor, peaton o pasajero acompañante.

Las dos tablas estan relacionadas mediante el campo ID que es un ID unico del accidente.

Un dato curioso es que en el informe especifica que los hechos que se catalogan como suicidio no se cuentan como victimas.

## Objetivo del Proyecto

El objetivo principal del proyecto es tener la posibilidad del analisis de los datos en totalidad, eso se logra mediante un dashboard interactivo, donde con pocos graficos que puedan variar con filtros puedan resumir un informe mucho mas largo.

El objetivo primario es hacer un EDA para sacar algunos graficos de las tablas y haciendo parte de estos analisis como el estudio de los campos de la tabla para aprovechar la limpieza y normalizacion de los datos para que sea consistente y no genere dificultades al momento de hacer el disenio del dashboard.

Luego de hacer el EDA se empieza a diseñar el dashboard, a medida de que se va avanzando en el dashboard surge la necesidad de crear nuevas tablas en el notebook del EDA.

## Herramientas y Desarrollo del proyecto

En el proyecto se utiliza mucho la libreria de pandas, porque domino mucho mejor pandas que el dax del power bi, a la hora de crear nuevas columnas que son producto del calculo de una o mas columnas que pueden estar filtradas, he decidido armar tablas complementarias que se puedan proyectar en power bi de manera sencilla.

## Dashboard

El Dashboard tiene 5 paginas ademas del inicio:

    -La primera tiene 2 mapas que grafican la distribucion de accidentes en la ciudad, separando en que comuna estan,
    para esto se tenia que crear una tabla que contuviera las localidades de cada comuna, porque el mapa de power bi de
    areas no reconoce todos los nombres "Comuna N", pero el de las localidades si.

    -La segunda consiste en varios 3 diagramas de barras que tienen informacion de la cantidad de accidentes por comuna,
    por el tipo de victima y por tipo de calle con un filtro de fechas.

    -La tercera contiene datos acerca de las victimas y los acusados, donde se puede filtrar por edad y por sexo.

    -La cuarta y quinta son los dos KPI's de la consigna, contiene un grafico donde se pueden ver detalles de los
    cammbios y el grafico del kpi donde aparece el valor seleccionado y cual fue su rendimiento.

Imagenes adjuntas del dashboard.

<p align="center">
<img src="https://github.com/samuelchacon00/PI_PT05_2/blob/master/src/inicio.png"
height=400></p>

<p align="center">
<img src="https://github.com/samuelchacon00/PI_PT05_2/blob/master/src/mapa.png"
height=400></p>

<p align="center">
<img src="https://github.com/samuelchacon00/PI_PT05_2/blob/master/src/accidentes.png"
height=400></p>

<p align="center">
<img src="https://github.com/samuelchacon00/PI_PT05_2/blob/master/src/victimas.png"
height=400></p>

<p align="center">
<img src="https://github.com/samuelchacon00/PI_PT05_2/blob/master/src/kpi_tasas.png"
height=400></p>

<p align="center">
<img src="https://github.com/samuelchacon00/PI_PT05_2/blob/master/src/kpi_motos.png"
height=400></p>

## KPI's

En la consigna hay 2 KPI's:

    - Uno conciste en reducir un 10% la tasa de mortalidad de accidentes por cada 100.000 habitantes en cada semestre.
    Para esto tuve que buscar una fuentes de datos que contenga informacion acerca del censo poblacional del 2016 hasta
    el 2021 y que estuviera dividido por comunas. Esas tablas se consiguieron en la pagina Estadistica de la ciudad(el
    link esta en el notebook del EDA y al final del README en las conclusiones, una vez armada la tabla con la poblacion se podia hacer el respectivo calculo de
    la tasa de mortalidad que es (cantidad de accidentes en zona geografica/poblacion total de dicha zona)*100.000 una
    vez calculada la tasa se crea otra columna llamada objetivo que va a ser el valor de medida del kpi, como queremos
    que baje un 10% cada semestre se debe multiplicar la tasa del semestre anterior por 0.9 y luego el grafico del power
    bi se va a encargar de graficar el resto.

    -Otro consiste en reducir un 7% la cantidad de accidentes por moto semestral, a diferencia del KPI anterior en este
    no necesitamos la informacion de la poblacion, dado que es cantidad solo se cuenta la cantidad de registros por año
    y semestre, luego solo hay que crear la columna objetivo que se calcula (cantidad de accidentes anterior*0.93)
    porque es el valor anterior reducido un 7%.

Los dos KPI's tienen sus propias tablas y cada KPI tienen 2 graficos de lineas, uno donde se le puede indicar la comuna que esta a la izquierda y el general que esta a la derecha, estas tablas se llaman "cantidad_muertes_motos.csv" y "tasas.csv".

## Conclusiones

Aunque el desarrollo del proyecto no es perfecto se logra abarcar gran parte del analisis de todos los campos de las
tablas, todas las conclusiones tecnicas estan en el [EDA](https://github.com/samuelchacon00/PI_PT05_2/blob/master/EDA.ipynb). 

    En cuanto a los siniestros viales, las medidas que se pueden tomar, es aumentar la cantidad de semaforos, y
    vigilancias en estos para poner multas y que los conductores lo piensen mejor antes de hacer una infraccion
    obviamente no todos los siniestros viales se dan por inprudencias de parte del acusado, puede haber mas causas como
    distracciones de parte de las victimas, en ese caso lo unico que se puede hacer es concientizar a las personas que
    pongan mas atencion cuando caminen y manejen en la calle aun cuando estan respetando las normas de transito, ya que
    si otra persona no lo hace puede poner en riesgo a otras personas.

## Enlaces

[Enunciado del proyecto](https://github.com/soyHenry/PI_DA/tree/Full_Time?tab=readme-ov-file)

[Dataset del censo poblacional en CABA por comunas ](https://www.estadisticaciudad.gob.ar/eyc/?p=76599)
