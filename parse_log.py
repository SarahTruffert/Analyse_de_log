from datetime import datetime


# Récupérer les horaires en compréhension de liste: 
def open_file(path):
    lines = []
    with open(path) as file:
        lines = [line.strip() for line in file]
        file.close()
        return lines

#print(open_file('planning.log'))


#Récupérer plage horaire + convertir en minutes :
# chn_date = "09:37",
# chn_date2 = "10:40"
def convertir_minutes(chn_date, chn_date2):
    date = datetime.strptime(chn_date, "%H:%M")
    date2 = datetime.strptime(chn_date2, "%H:%M")
    return(((date2-date).seconds)//60)


# Additionner les matières si aparaissent +sieurs fois
# if matiere == matiere :
# matiere = matiere =+ 1
#     print(matiere)


#Calculer les mins en % :
def percentage(temps_total_activite,tout_total,temps_total_formation):
    # activite = "Break"
    tout_total = 100
    temps_total_activite = 65 
    temps_total_formation = 970
    percentage = (temps_total_activite * tout_total) / temps_total_formation
    return percentage

#print(percentage(65,100,970))


# Ranger le tout dans un dico:
# matiere = input("Rentrez une matière : ")
# out_put = {matiere: total_heure}

# Par ordre alphabétique .sort du dico :
def tri_dico(dico):
    return sorted(dico.items(), key=lambda t: t[0])

#print(tri_dico({'Dictionaries': 15, 'Break': 65, 'Exercices': 340}))


# Retourner selon "expected_output.txt"
# return (f'{activite}                      {temps_total_activite} minutes {round(pourcentage)}%')