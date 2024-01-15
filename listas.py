calificaciones = [1,2,3,4,5]
nombres = ["Moisés","Camila","Fernanda","Pablo","Tania"]
lista_variada = [True, 10.5,"abc", [0,1,1]]

print("Estudiante: ", nombres[2])
print("Calificación: ", calificaciones[-2])# 12345 y el-2 054 =calidficacion 4
print("Lista dento de otra: ", lista_variada[3][1])
print("Imprimir un rango o slices ", nombres[1:2])
print(lista_variada)

#agregar elementos a una lista
nombres.append("Anibal")
print(nombres)
#remover elementos de una lista
nombres.remove("Pablo")
print(nombres)