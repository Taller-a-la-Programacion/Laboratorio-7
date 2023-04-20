Laboratorio 7

## Instrucciones Generales
- El archivo **debe** llamarse **Laboratorio7.py**
- Debe realizar la siguiente función con recursión de cola


## cortarMatriz(matriz, fila, columna)

- La función debe validar que la matriz sea homegenea y tenga valores numéricos (int, float).
- Debe crear la función largoLista
- Los valores de fila y columna deben ser enteros y mayores a -1
- Además los valores de fila y columna deben ser menor o igual al total de filas y columnas de la matriz
- La función debe retornar una nueva matriz con las nuevas dimensiones solicitadas por los parámetros de filas y columnas

```python
matriz = [[2,4,6,8,10], [1,3,5,7,9], [4,8,12,16,20], [0,0,0,0,0], [5,10,5,10,5]]

>>>cortarMatriz(matriz, 2, 3)
[[2,4,6], [1,3,5]]
>>>cortarMatriz(matriz, 2, 2)
[[2,4], [1,3]]
>>>cortarMatriz(matriz, 5, 5)
[[2,4,6,8,10], [1,3,5,7,9], [4,8,12,16,20], [0,0,0,0,0], [5,10,5,10,5]]
>>>cortarMatriz(matriz, 8, 5)
'Error: los valores de la nueva matriz exceden las dimensiones actuales'
```

## cortarMatriz_v2(matriz, fila, columna, largoFila, largoColumna)

- La función debe validar que la matriz sea homegenea y tenga valores numéricos (int, float).
- Debe crear la función largoLista
- Los valores de fila, columna, largoFila y largoColumna deben ser enteros y mayores a -1
- Además los valores de fila y columna deben ser menor o igual al total de filas y columnas de la matriz
- La función debe retornar una nueva matriz con las nuevas dimensiones solicitadas por los parámetros de  largoFila y largoColumna, pero para ello los valores de fila y columna indicará a partir de donde comenzará el corte para la nueva matriz.  
  - Es decir dado una matriz de 10 x 10, 
  - fila sea 3
  - columna sea 2,
  - Entonces el punto de partida para cortar la matriz será fila 3 y columna 2 
  - Desde ese punto, obtener la cantidad de columnas y filas según los parámetros de largoFila, largoColumna

```python
matriz = [[2,4,6,8,10], [1,3,5,7,9], [4,8,12,16,20], [10,20,30,40,50], [5,10,15,20,25]]

>>>cortarMatriz_v2(matriz, 2, 3, 2, 2)
[ [16,20], [40,50] ]
>>>cortarMatriz_v2(matriz, 2, 0, 2, 2)
[ [4,8], [10,20] ]
>>>cortarMatriz_v2(matriz, 0,0,5,5)
[[2,4,6,8,10], [1,3,5,7,9], [4,8,12,16,20], [10,20,30,40,50], [5,10,15,20,25]]
>>>cortarMatriz_v2(matriz, 2, 1, 6, 6)
'Error: los valores de la nueva matriz exceden las dimensiones actuales'
```


## convertirBinADec(matriz)
- La función debe recibir un parámetro matriz y este debe estar compuesto por 1 y 0. El programa debe retornar una lista con la conversión de binario a decimal de cada uno de sus vectores.
- Usar la técnica conversión numeríca sin cambios de tipo de dato
- Crear las funciones respectivas de conversión numérica según visto en clases
- Recorrer la matriz por sus indices

```python
matriz = [ [1,0,0,0,0], [1,1,1,1,1], [0,1,0,1,0]]
matriz2 = [ [1,0], [0,0], [1,1], [1,0], [0,1], [1,1]]

>>>convertirBinADec(matriz)
[16, 31, 10]
>>>convertirBinADec(matriz2)
[2,0,3,2,1,3]
```

## convertirHexADec(matriz)
- La función debe recibir un parámetro matriz y este debe estar compuesto desde 0 hasta 9 y desde 'A' hasta 'F'. El programa debe retornar una lista con la conversión de hexadecimal a decimal de cada uno de sus vectores.
- Crear las funciones respectivas de conversión numérica según visto en clases
- Recorrer la matriz por sus indices

```python
matriz = [ [1,0,0,0,0], [1,1,1,1,1], [0,1,0,1,0]]
matriz2 = [ ['A',1,0], [0,'B',0], ['F','F',1], ['A','B',5], [2,'C',9]]

>>>convertirHexADec(matriz)
[65536, 69905, 4112]
>>>convertirHexADec(matriz2)
[2576, 176, 4081, 2741, 713]
```
