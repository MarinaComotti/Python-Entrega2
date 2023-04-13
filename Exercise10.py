def merge_structures(nombres, notas_1, notas_2):
    """ 
        Funcion que toma los nombres y las notas y crea un diccionario a partir de reunir dicha informacion.
    
        Args:
          nombres (str): string que contiene los nombres de todos los estudiantes.
          notas_1 (list): lista de enteros con la primera nota de cada estudiante.
          notas_2(list): lista de enteros con la segunda notas de cada estudiante.
        Returns:
          students_dict (dict): diccionario con el nombre de cada alumno como clave y una tupla con sus 2 notas como valor. 
    """
      
    names = [n.strip()[1:-1] for n in nombres.split(",")]  
    final_names = [name.title() for name in names]  
    
    zip_list= zip(final_names, notas_1, notas_2) 

    students_dict = dict((tuple[0], (tuple[1], tuple[2])) for tuple in zip_list )
 
    return students_dict


def compute_averages(students_notes):
    """ Retorna un diccionario con el nombre de cada estudiante y el promedio de sus notas. """

    students_average = {}
    for student in students_notes:
        students_average[student] = sum(students_notes[student]) / len (students_notes[student])

    return students_average


def compute_total_average(students_average):
    """ Esta funcion calcula y retorna el promedio de todas las notas promedio de todos los estudiantes """

    total_notes = len(students_average)  

    total_sum = sum(students_average[student] for student in students_average) 

    average = total_sum / total_notes

    return average




def highest_note_student(students_average):
    """ Funcion que retorna el nombre del estudiante con la nota promedio mas alta """
    
    highest = max(students_average, key=lambda student: students_average[student])
    return highest



def lowest_note_student(students_average):
    """ Funcion que retorna el nombre del estudiante con la nota promedio mas baja"""

    lowest = min(students_average, key=lambda student: students_average[student])
    return lowest 



def print_info(students_notes, students_average, total_average, highest_student, lowest_student):
    """ Imprime toda la informacion procesada y calculada en las otras funciones de este programa. """

    print('-'*26)
    print(' ')
    print('Informacion de los nombres de los estudiantes con sus respectivas notas: ')
    print(' ')
    print("{:<22}{}".format("Nombre:", "Notas:"))
    for name, notes in students_notes.items():
        print("{:<22}{}".format(name, notes))

    print(' ')
    print('-'*26)
    print(' ')
    print('Informacion de la nota promedio de cada estudiante: ')
    print(' ')
    print("{:<22}{}".format("Nombre:", "Promedio:"))
    for name, average in students_average.items():
        print("{:<22}{}".format(name, average))
    print(' ')
    print('-'*26)
    print(' ')
    print(f'Promedio general del curso: {total_average:.2f}')
    print(f'Nombre del estudiante con la nota promedio mas alta: {highest_student}')
    print(f'Nombre del estudiante con la nota promedio mas baja: {lowest_student}')
    print(' ')
    print('-'*26)
      

NOMBRES = ''' 'Agustin', 'Alan', 'Andrés', 'Ariadna', 'Bautista', 'CAROLINA', 'CESAR', 
'David','Diego', 'Dolores', 'DYLAN', 'ELIANA', 'Emanuel', 'Fabián', 'Facundo', 
'Francsica', 'FEDERICO', 'Fernanda', 'GONZALO', 'Gregorio', 'Ignacio', 'Jonathan', 
'Joaquina', 'Jorge','JOSE', 'Javier', 'Joaquín' , 'Julian', 'Julieta', 'Luciana',
'LAUTARO', 'Leonel', 'Luisa', 'Luis', 'Marcos', 'María', 'MATEO', 'Matias', 
'Nicolás', 'Nancy', 'Noelia', 'Pablo', 'Priscila', 'Sabrina', 'Tomás', 'Ulises',
'Yanina' '''

NOTAS_1 = [81, 60, 72, 24, 15, 91, 12, 70, 29, 42, 16, 3, 35, 67, 10, 57, 11, 69,
12, 77, 13, 86, 48, 65, 51, 41, 87, 43, 10, 87, 91, 15, 44,
85, 73, 37, 42, 95, 18, 7, 74, 60, 9, 65, 93, 63, 74]

NOTAS_2 = [30, 95, 28, 84, 84, 43, 66, 51, 4, 11, 58, 10, 13, 34, 96, 71, 86, 37,
64, 13, 8, 87, 14, 14, 49, 27, 55, 69, 77, 59, 57, 40, 96, 24, 30, 73,
95, 19, 47, 15, 31, 39, 15, 74, 33, 57, 10]

students_notes = merge_structures(NOMBRES, NOTAS_1, NOTAS_2)

students_average = compute_averages(students_notes)


total_average = compute_total_average(students_average)

highest_student = highest_note_student(students_average)

lowest_student = lowest_note_student(students_average)

print_info(students_notes, students_average, total_average, highest_student, lowest_student)