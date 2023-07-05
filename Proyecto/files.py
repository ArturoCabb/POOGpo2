class Archivo():
    def buscar(self, valor, tipo,v):
        file = open("videos.csv", "r")
        lines = file.readlines()
        file.close()
        if str(tipo) == "P":
            ids = {}
            for l in lines:
                fields = l.split(",")
                id = fields[0]
                titulo = fields[1]
                genero = fields[2]
                duracion = fields[3]
                calificacion = fields[4]
                audencia = fields[5]
                temporada = fields[6]
                episodio = fields[7]
                titulo_episodio = fields[8]
                tema = fields[9]
                ids[id] = [id,titulo, genero, duracion, calificacion, audencia, temporada, 
                           episodio, titulo_episodio, tema]
        if v in ids == False:
            print("Ya existe")
        else: 
            Archivo().grabar(valor)

        if str(tipo) == "CID":
            for l in lines:
                fields = l.split(",")
                if fields[0] == v:
                    return fields
                else:
                    print(str(v) + " No está en el registro")

    def grabar(self, valor):
        file = open("videos.csv", "a+")
        lines = file.readlines()
        file.writelines(valor)

class Listados():
    def general(self, numero, texto = "" ,n1 = 0, n2 = 0):
        file = open("videos.csv", "r")
        line = file.readline()
        lines = file.readlines()
        file.close()
        if numero == 3:
            print(" ID  " + "        Titulo      " + "    Genero     " + 
                  "Duración  " + " Calificación " + "   Audencia    " + "Temporada" 
                  + " Episodio " + "   Título del Episodio     " + "Tema" + "\n")
            x = line.find(texto)
            z = line[:x]
            x = z.find(",")
            zz = line[x:]
            y = z.find(",")
            texto = line[x:y+x]
            for l in lines:
                fields = l.split(",")
                if fields[1] == texto:
                    print(fields[0] + "     " + fields[1] + "     " + fields[2] + "   " + fields[3] + "     " + 
                          fields[4] + "    " + "    "+ fields[6] + "   " + "   " + "   " + fields[8] + 
                          "    " + fields[9] + "\n")

        if numero == 4:
            print(" ID  " + "        Titulo      " + "    Genero     " + 
                  "Duración  " + " Calificación " + "   Audencia    " + "Temporada" 
                  + " Episodio " + "   Título del Episodio     " + "Tema" + "\n")
            x = line.find(texto)
            z = line[:x]
            x = z.find(",")
            zz = line[x:]
            x = z.find(",")
            zz = line[x:]
            y = z.find(",")
            texto = line[x:y+x]
            for l in lines:
                fields = l.split(",")
                if fields[1] == texto:
                    print(fields[0] + "     " + fields[1] + "     " + fields[2] + "   " + fields[3] + "     " + 
                          fields[4] + "    " + "    "+ fields[6] + "   " + "   " + "   " + fields[8] + 
                          "    " + fields[9] + "\n")

        if numero == 5:
            print(" ID  " + "        Titulo      " + "    Genero     " + 
                  "Duración  " + " Calificación " + "   Audencia    " + "Temporada" 
                  + " Episodio " + "   Título del Episodio     " + "Tema" + "\n")
            for l in lines:
                fields = l.split(",")
                print(fields[0] + "     " + fields[1] + "     " + fields[2] + "   " + fields[3] + "     " + 
                      fields[4] + "    " + "    "+ fields[6] + "   " + "   " + "   " + fields[8] + 
                      "    " + fields[9] + "\n")

        if numero == 6:
            print(" ID  " + "        Titulo      " + "    Genero     " + 
                  "Duración  " + " Calificación " + "   Audencia    " + "Temporada" 
                  + " Episodio " + "   Título del Episodio     " + "Tema" + "\n")

            for l in lines:
                fields = l.split(",")
                if l[0] == "P":
                    print(fields[0] + "     " + fields[1] + "     " + fields[2] + "   " + fields[3] + "     " + 
                          fields[4] + "    " + "    "+ fields[6] + "   " + "   " + "   " + fields[8] + 
                          "    " + fields[9] + "\n")

        if numero == 7:
            print(" ID  " + "        Titulo      " + "    Genero     " + 
                  "Duración  " + " Calificación " + "   Audencia    " + "Temporada" 
                  + " Episodio " + "   Título del Episodio     " + "Tema" + "\n")

            for l in lines:
                if l[0] == "S":
                    fields = l.split(",")
                    print(fields[0] + "     " + fields[1] + "     " + fields[2] + "   " + fields[3] + "     " + 
                          fields[4] + "    " + "    "+ fields[6] + "   " + "   " + "   " + fields[8] + 
                          "    " + fields[9] + "\n")

        if numero == 8:
            print(" ID  " + "        Titulo      " + "    Genero     " + 
                  "Duración  " + " Calificación " + "   Audencia    " + "Temporada" 
                  + " Episodio " + "   Título del Episodio     " + "Tema" + "\n")

            for l in lines:
                if l[0] == "D":
                    fields = l.split(",")
                    print(fields[0] + "     " + fields[1] + "     " + fields[2] + "   " + fields[3] + "     " + 
                          fields[4] + "    " + "    "+ fields[6] + "   " + "   " + "   " + fields[8] + 
                          "    " + fields[9] + "\n")

        if numero == 9:
            ids = {}
            print(" ID  " + "        Titulo      " + "    Genero     " + 
                  "Duración  " + " Calificación " + "   Audencia    " + "Temporada" 
                  + " Episodio " + "   Título del Episodio     " + "Tema" + "\n")

            for l in lines:
                fields = l.split(",")
                if int(fields[4]) >= n1 and int(fields[4]) <= n2:
                    print(fields[0] + "     " + fields[1] + "     " + fields[2] + "   " + fields[3] + "     " + 
                          fields[4] + "    " + "    "+ fields[6] + "   " + "   " + "   " + fields[8] + 
                          "    " + fields[9] + "\n")

