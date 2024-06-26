from datetime import datetime, timedelta

class Fecha:
    def __init__(self, dia=None, mes=None, año=None):
        if dia is None or mes is None or año is None:
            # Si no se proporcionan argumentos, tomar la fecha de hoy
            fecha_actual = datetime.now()
            self.dia = fecha_actual.day
            self.mes = fecha_actual.month
            self.año = fecha_actual.year
        else:
            self.dia = dia
            self.mes = mes
            self.año = año
    
    def __str__(self):
        return f"{self.dia:02d}/{self.mes:02d}/{self.año}"
    
    def __eq__(self, other):
        return (self.dia == other.dia) and (self.mes == other.mes) and (self.año == other.año)
    
    def __add__(self, days):
        fecha_nueva = datetime(self.año, self.mes, self.dia) + timedelta(days=days)
        return Fecha(fecha_nueva.day, fecha_nueva.month, fecha_nueva.year)
    
    def calcular_dif_fecha(self, otra_fecha):
        fecha1 = datetime(self.año, self.mes, self.dia)
        fecha2 = datetime(otra_fecha.año, otra_fecha.mes, otra_fecha.dia)
        diferencia = fecha1 - fecha2
        return abs(diferencia.days)


#Ejercicio2


from datetime import date

class Alumno:
    def __init__(self, nombre, dni, fecha_ingreso, carrera):
        self.data = {
            "Nombre": nombre,
            "DNI": dni,
            "FechaIngreso": fecha_ingreso,
            "Carrera": carrera
        }
    
    def cambiar_datos(self, **kwargs):
        for key, value in kwargs.items():
            if key in self.data:
                self.data[key] = value
            else:
                raise KeyError(f"No existe el atributo '{key}' en los datos del alumno.")
    
    def antiguedad(self):
        fecha_actual = date.today()
        fecha_ingreso = self.data["FechaIngreso"]
        tiempo_transcurrido = fecha_actual - fecha_ingreso
        return tiempo_transcurrido.days // 365  # antigüedad en años aproximada
    
    def __str__(self):
        return f"Alumno: {self.data['Nombre']} - DNI: {self.data['DNI']} - Carrera: {self.data['Carrera']}"
    
    def __eq__(self, other):
        if isinstance(other, Alumno):
            return self.data == other.data
        return False


#Ejercicio3

import random

class Alumno:
    def _init_(self, nombre, edad, promedio):
        self.nombre = nombre
        self.edad = edad
        self.promedio = promedio

    def _str_(self):
        return f"Nombre: {self.nombre}, Edad: {self.edad}, Promedio: {self.promedio}"

class Nodo:
    def _init_(self, alumno=None):
        self.alumno = alumno
        self.siguiente = None
        self.anterior = None

class ListaIterador:
    def _init_(self, cabeza):
        self.actual = cabeza

    def _iter_(self):
        return self

    def _next_(self):
        if self.actual is None:
            raise StopIteration
        else:
            nodo = self.actual
            self.actual = self.actual.siguiente
            return nodo.alumno

class ListaDoblementeEnlazada:
    def _init_(self):
        self.cabeza = None
        self.cola = None

    def esta_vacia(self):
        return self.cabeza is None

    def insertar_al_final(self, alumno):
        nuevo_nodo = Nodo(alumno)
        if self.esta_vacia():
            self.cabeza = nuevo_nodo
            self.cola = nuevo_nodo
        else:
            nuevo_nodo.anterior = self.cola
            self.cola.siguiente = nuevo_nodo
            self.cola = nuevo_nodo

    def eliminar(self, alumno):
        actual = self.cabeza
        encontrado = False
        while actual is not None and not encontrado:
            if actual.alumno == alumno:
                encontrado = True
            else:
                actual = actual.siguiente

        if actual is None:
            raise ValueError("El alumno no está en la lista")
        elif actual == self.cabeza:
            self.cabeza = actual.siguiente
            if self.cabeza is not None:
                self.cabeza.anterior = None
        elif actual == self.cola:
            self.cola = actual.anterior
            self.cola.siguiente = None
        else:
            actual.anterior.siguiente = actual.siguiente
            actual.siguiente.anterior = actual.anterior

    def _iter_(self):
        return ListaIterador(self.cabeza)

    def lista_ejemplo(self, n):
        nombres = ["Juan", "María", "Pedro", "Ana", "Luisa"]
        lista = ListaDoblementeEnlazada()
        for _ in range(n):
            nombre = random.choice(nombres)
            edad = random.randint(18, 25)
            promedio = round(random.uniform(6, 10), 2)
            alumno = Alumno(nombre, edad, promedio)
            lista.insertar_al_final(alumno)
        return lista


#Ejercicio4


class Alumno:
    def _init_(self, nombre, fecha_ingreso):
        self.nombre = nombre
        self.fecha_ingreso = fecha_ingreso  # Suponiendo que fecha_ingreso es una cadena en formato 'YYYY-MM-DD'

class Nodo:
    def _init_(self, data):
        self.data = data
        self.prev = None
        self.next = None

class ListaDoblementeEnlazada:
    def _init_(self):
        self.head = None
        self.tail = None

    def append(self, data):
        nuevo_nodo = Nodo(data)
        if self.head is None:
            self.head = nuevo_nodo
            self.tail = nuevo_nodo
        else:
            self.tail.next = nuevo_nodo
            nuevo_nodo.prev = self.tail
            self.tail = nuevo_nodo

    def display(self):
        current = self.head
        while current:
            print(f"Nombre: {current.data.nombre}, Fecha de Ingreso: {current.data.fecha_ingreso}")
            current = current.next

    def sort_by_fecha_ingreso(self):
        if self.head is None:
            return

        current = self.head.next
        while current:
            key = current
            mover = current.prev

            while mover and mover.data.fecha_ingreso > key.data.fecha_ingreso:
                mover = mover.prev

            next_node = current.next
            if key.prev:
                key.prev.next = key.next
            if key.next:
                key.next.prev = key.prev

            if mover is None:
                key.next = self.head
                self.head.prev = key
                key.prev = None
                self.head = key
            else:
                key.next = mover.next
                if mover.next:
                    mover.next.prev = key
                key.prev = mover
                mover.next = key

            current = next_node


#ejercicio5

import os

def crear_directorio_y_archivo(lista_alumnos, directorio_origen, directorio_destino):
  
    if not os.path.exists(directorio_origen):
        os.makedirs(directorio_origen)
    
    archivo_alumnos = os.path.join(directorio_origen, "alumnos.txt")
    with open(archivo_alumnos, 'w') as f:
        for alumno in lista_alumnos:
            f.write(alumno + '\n')
    
    
    os.rename(directorio_origen, directorio_destino)
    print(f"Directorio movido a {directorio_destino}")
    
    
    os.remove(os.path.join(directorio_destino, "alumnos.txt"))
    os.rmdir(directorio_destino)
    print("Archivo y directorio borrados correctamente")




  





