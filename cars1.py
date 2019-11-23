import pandas as pd

#Corresponding .csv file into a data frame named cars using pandas
cars = pd.read_csv('cars.csv')

#Display the first five  with odd-numbered columns.
B= cars.iloc [:5, 0::2]

#Display the row contains the ‘Model’ of Mazda RX4’
C= cars.iloc [:1]

#Displays the cylinders (‘cyl’) of the car model ‘Camaro Z28’
D= cars.loc [[23], ['Model', 'cyl']]

#Displays cylinders (‘cyl’) gear type (‘gear’) of the car models 
#‘Mazda RX4 Wag’, ‘Ford Pantera L’ and ‘Honda Civic’.
E = cars.loc [[1,18,28], ['Model','cyl','gear']]
