from estudiante import Estudiante
from docente import Docente 

estudiante = Estudiante("SANTIAGO", "RUBIO", 24, "0106422066", "0989774352", "CUENCA","santiago@gmail.com", "DESARROLLO DE SOFTWARE",[7,6,8,10,6])
estudiante1 = Estudiante("MARIA", "GOMEZ", 22, "0106422067", "0989774353", "CUENCA", "amria@gmail.com","DESARROLLO DE SOFTWARE",[8,7,9,10,8])
estudiante2 = Estudiante("JUAN", "PEREZ", 23, "0106422068", "0989774354", "CUENCA", "juan@gmail.com", "DESARROLLO DE SOFTWARE",[9,8,7,10,9])
estudiante3 = Estudiante("CARLOS", "LOPEZ", 21, "0106422069", "0989774355", "CUENCA", "carlos@gmail.com", "DESARROLLO DE SOFTWARE",[10,9,8,10,10])
estudiante4 = Estudiante("ANA", "MARTINEZ", 20, "0106422070", "0989774356", "CUENCA", "ana@gmail.com", "DESARROLLO DE SOFTWARE",[6,7,8,10,9])

docente = Docente("VERONICA", "CHIMBO", 35, "0106422071", "0989774357", "CUENCA", "VEROC@gmail.com", "POO", 40)
docente1 = Docente("VERONICA", "SEGARRA", 40 , "0106422072", "0989774358", "CUENCA", "veronica@gmail.com", "BASE DE DATOS", 35)
docente2 = Docente("ILIANA", "TINOCO", 39, "0106422073", "0989774359", "CUENCA", "iliana@gmail.com", "EXPRESION ORAL", 30)
docente3  = Docente("DIANA", "ROMERO", 44 , "0106422074", "0989774360", "CUENCA", "diana@gmail.com", "ESTADISTICA", 40)
docente4 = Docente("CARMEN", "TACURI", 50, "0106422075", "0989774361", "CUENCA", "carmen@gmail.com", "APPS WEB", 40)
print("Docentes:")
print("-"*50)
print(docente.calcular_salario())
print(docente,docente1,docente2,docente3,docente4,sep="\n")
print("Estudiantes:")
print("-"*50)
print(estudiante.validar_edad())
print(estudiante.__str__())