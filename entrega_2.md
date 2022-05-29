# Entrega dos

## Modelo matemático

### Variables constantes (dato)

$$
\begin{align*}
\text{CAPACIDAD: Importe maximo que puede llevar el camion.}\\
\text{DIMENSION: Cantidad total de sucursales.}\\
D_{ij}:\text{Distancia entre las sucursales i y j. Con i, j = [1, ..., DIMENSION]}\\
DEM_{i}: \text{Demanda de la sucursal i.}
\end{align*}
$$

### Variables enteras

$$
\begin{align*}
U_{i}:\text{Orden en que se visita la sucursal i.}\\
CAP_{i}: \text{Capacidad del camion en la sucursal i.}
\end{align*}
$$

### Variables bivalentes

$$
Y_{ij}:\text{Vale 1 si el camión va de la sucursal i a la sucursal j. Vale 0 si no.}\\
$$

### Restricciones

#### Salidas

$$
\sum_{j=0}^\text{DIMENSION} Y_{ij} = 1 \\\\
\text{para todo i de 1 a DIMENSION, con i ≠ j.}
$$

#### Llegadas

$$
\sum_{i=0}^\text{DIMENSION} Y_{ij} = 1 \\\\
\text{para todo j de 1 a DIMENSION, con i ≠ j.}
$$

#### Subtours

$$
U_{i} - U_{j} + DIMENSION * Y_{ij} \le DIMENSION - 1 \\\\
\text{para todo i,j de 1 a DIMENSION, con i ≠ j.}
$$

#### Capacidad

$$
\begin{align*}
CAP_{0} = 0 \\
0 \le CAP_{i} \le CAPACIDAD \\
\text{para todo i de 1 a DIMENSION.} \\
CAP_{i} = CAP_{i-1} + DEM_{i} \\
\text{para todo i de 1 a DIMENSION.}
\end{align*}
$$

#### Funcional

$$
Z(MIN) = \sum_{i=0}^\text{DIMENSION} \sum_{j=0}^\text{DIMENSION} Y_{ij}*D_{ij}
$$

## Ideas de resolución

El problema sigue siendo el mismo, pero ahora pasamos a tener una dimensión mucho mas grande que en la primera instancia. Se podría resolver mediante programación lineal con el modelo matemático que planteamos y alguno de los software que usamos en la materia, pero viendo la cantidad de variables que se generan no es una opción viable. Por otro lado, el algoritmo en python se podría mejorar quizás utilizando otro tipo de estructura como por ejemplo grafos, aunque creo que la mejor opción es utilizar alguna librería para resolver el problema del viajante.

## Comentarios por commit

### Commit 968cc451f6bb0848047d50ecec913779a750bd11

Tuve que hacer un rollback de la mejora que había hecho porque el algoritmo tardaba demasiado tiempo en encontrar la solución.

## Comentarios finales

Si bien creo que el algoritmo se podría mejorar, la opción mas conveniente seria utilizar alguna librería para resolver el problema del viajante y de esta forma obtener una solución optima.
