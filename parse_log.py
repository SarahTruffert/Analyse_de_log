from datetime import datetime
import logging

logging.basicConfig(filename="parse.log", level=logging.INFO,
 format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')

 
def open_file(path):
    """ 
        Récupérer les horaires :
    """
    lines = []
    with open(path) as file:
        lines = [line.strip() for line in file]
        file.close()
        logging.info(f'Open file : {path}')
        return lines

def minutes(path):
    """
        Supprimer l'espace pour soustraire la plage horaire
        Calculer les heures en minutes 
        Les ranger dans une liste
    """
    liste_minutes = []
    lines = open_file(path)
    for i in lines :
        if len(i) != 0 :
            var = (i[0:11]).split("-")
            date = datetime.strptime(var[1], "%H:%M")
            date2 = datetime.strptime(var[0], "%H:%M")
            liste_minutes.append(str(((date-date2).seconds)//60))
    return liste_minutes
#print(minutes('planning.log'))

def matiere(path):
    """
        Récupérer les matières :
    """
    
    liste_matieres = []
    lines = open_file(path)
    for i in lines :
        if len(i) != 0 :
            var_matiere = ((i[11:24]))
            liste_matieres.append(var_matiere + " ")
    return liste_matieres

#print(matiere('planning.log'))


def matiere_et_minutes(path):

    liste_matieres = matiere(path)
    liste_minutes = minutes(path)
    res = [i + j for i, j in zip (liste_matieres, liste_minutes)]
    print(res)

#matiere_et_minutes('planning.log')  


def percentage(temps_total_activite,tout_total,temps_total_formation):
    """
        Calcule les minutes en % :
    """
    # activite = "Break"
    # tout_total = 100
    # temps_total_activite = 65 
    # temps_total_formation = 970
    percentage = (temps_total_activite * tout_total) / temps_total_formation
    logging.info('Calcule le pourcentage')
    return percentage



# Additionner les matières si aparaissent +sieurs fois
# if matiere == matiere :
# add_matière = matiere_1 + matiere_2
# matiere = matiere =+ 1
#     print(matiere)


#print(percentage(65,100,970))




def tri_dico(dico):
    """
        retourne le dico en ordre alphabétique : 
    """
    logging.info('Tri par ordre alphabétique')
    return sorted(dico.items(), key=lambda t: t[0])

#print(tri_dico({'Dictionaries': 15, 'Break': 65, 'Exercices': 340}))

def main():
    pass


# Retourner selon "expected_output.txt"
# return (f'{activite}                      {temps_total_activite} minutes {round(pourcentage)}%')

