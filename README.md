# CreateSTL
 ## Creates an STL file / Создает файл формата STL  

 ### How does it work?   
   1. The input file is a txt format file that contains a table with elevation values.  
      Columns are separated by tabs.  
   2. Checking the number of rows and columns.(>=2)  
   3. The length of the rows must be equal.  
   4. Calculation of coefficients for normalization by X.  
   5. Creating triangles in STL format.    
   6. Creating an STL file.  
   
 ### Как это работает?  
   1. На вход подается файл формата txt, в котором содержится таблица со значениями высот.  
      Столбцы разделены табуляцией.
   2. Проверка количества строк и столбцов.(>=2)  
      Длина строк должна быть равной.  
   3. Создание пар треугольников между двумя соседними строками.  
   4. Вычисления коэффициентов для нормировки по X.  
   5. Создание треугольников в формате STL.  
   6. Формирование STL файла.  
