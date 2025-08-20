# ¿Qué es Numpy?

Es una libreria de Python que se usa para la resolución de problemas científicos y matemáticos complejos.

Esta libreria proporciona un objeto de arreglo mutidimensional que permite:
* Trabajar con listas de numeros muy grandes llamadas arreglos o array y que pueden tener varias dimensiones como tablas o cubos de datos.
* Hacer cálculos matemáticos de forma muy rápida
* Realizar operaciones básicas como sumar, restar, multiplicar
* Organizar y ordenar información
* Hacer estadística básica como promedios y sumas
* Trabajar con matrices
* Generar números aleatorios para simulaciones.

Es como tener una calculadora científica súper avanzada integrada en Python, pero que puede trabajar con millones de números a la vez de forma muy eficiente.

La escencia de Numpy es el objecto N-dimensional array.

El objeto ndarray encapsula arrays N dimensionales con datos homogeneos, es decir todos los elementos de un array deben ser del mismo tipo de dato, como numeros o textos, pero nunca mezclarse. 

Entonces un ndarray debe contener numeros unicamente. Y otro ndarray puede contener texto unicamente. Pero nunca mezclarse.

Diferencias entre los objetos de Numpy y lo objetos comunes de Python.

|Numpy|Python|
|-|-|
|Los ndarray tienen un tamaño determinado en el momento de su creacion, si se requiere cambiar el tamño del ndarray, es necesario crear un nuevo ndarray y eliminar el anterior|Crece dinamicamente|
|Los elementos deben ser del mismo tipo de dato|Puede tener elementos con diferentes tipos de datos|
|Optimiza las operaciones matematicas|Menos eficientes|
|Convierte todas las entradas como listas, diccionarios etc a objetos numpy para optimizar las operaciones|Usado como entradas de Numpy|

## Facilidad y rapidez

Numpy, permite escribir codigo simple y natural e internamente usa código C, el cual ejecuta operaciones mucho mas rápido que Python, siendo que C ya esta optimizado y compilado.

## Vectorización en NumPy y la velocidad de C

El módulo **NumPy** en Python te permite escribir código que es a la vez simple y natural, mientras que internamente aprovecha la velocidad del lenguaje **C**. A diferencia de Python, que es un lenguaje interpretado, C está optimizado y compilado, lo que le permite ejecutar operaciones de forma mucho más rápida.

La clave de este rendimiento es la **vectorización**, un concepto central en NumPy. La vectorización te permite aplicar operaciones a todos los elementos de un array sin necesidad de usar bucles explícitos (como `for` o `while`). Esto no solo hace que el código sea más legible y conciso, sino que también aprovecha al máximo las optimizaciones de C para realizar los cálculos de manera masiva y eficiente.

-----

### Ejemplo de código

Considera la diferencia entre multiplicar una lista en Python y un array de NumPy:

**Código de Python con bucle (no vectorizado):**

```python
numeros = [1, 2, 3, 4, 5]
resultado = []
for numero in numeros:
    resultado.append(numero * 2)
```

**Código de NumPy con vectorización:**

```python
import numpy as np

numeros = np.array([1, 2, 3, 4, 5])
resultado = numeros * 2  # ¡Multiplica automáticamente todos los elementos!
```

Como puedes ver en el ejemplo de NumPy, la operación `* 2` se aplica de forma automática a cada elemento del array, lo que hace el código más limpio y significativamente más rápido para grandes volúmenes de datos.

-----

### Broadcasting: Operaciones entre arrays de diferentes tamaños

Además de la vectorización, NumPy introduce el concepto de **broadcasting**. Esta funcionalidad permite que las operaciones se apliquen de forma automática elemento por elemento, incluso cuando los arrays tienen diferentes tamaños. NumPy "estira" el array más pequeño para que coincida con la forma del más grande, permitiendo que la operación se realice sin problemas.

El **broadcasting** es otra forma en que NumPy simplifica el código y lo hace más eficiente para la manipulación de arrays de distintas dimensiones.

Numpy puede ser usado bajo el paradigma de programacion orientada a objetos.

Por ejemplo *ndarray* es una clase que posee numerosos métodos y atributos.

Por lo tanto Numpy permite programar como POO y como función.

Método 1: Como programación orientada a objetos
```python
import numpy as np
arr = np.array([1, 2, 3, 4, 5])
promedio = arr.mean()  # Usando el método del objeto
```

Método 2: Como función:
```python
import numpy as np
arr = np.array([1, 2, 3, 4, 5])
promedio = np.mean(arr)  # Usando la función de NumPy
```

Ambos hacen exactamente lo mismo - calcular el promedio - pero puedes elegir el estilo que más te guste.
¿Por qué es importante esta flexibilidad?

Diferentes programadores prefieren diferentes estilos
Puedes adaptar tu código según la situación
Es más fácil aprender porque no te fuerza a un solo método

El resultado: NumPy se volvió el "idioma universal"
Como NumPy es tan flexible y fácil de usar, todas las demás bibliotecas científicas de Python decidieron adoptarlo. Es como si NumPy fuera el "inglés" del mundo de la ciencia de datos en Python.
Ejemplos de quién usa NumPy:

Pandas (análisis de datos)
Matplotlib (gráficos)
Scikit-learn (machine learning)
OpenCV (visión por computadora)
Y muchas más...

En resumen: NumPy se volvió tan popular porque es flexible y fácil de usar, por eso todo el ecosistema científico de Python lo adoptó como estándar.

[Notebook para crear el primer objeto NumPy](https://colab.research.google.com/drive/12N5lv2tJdNs6vs2p7V92SrCxg32wltTr?usp=sharing)
