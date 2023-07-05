# Clase Computadora : mem, dd, pro, mon
# Clase Escritorio  : gabinete, todo en uno
# Clase laptop      : tipo, dos en uno
# Gamer             : diadema, tarjeta grafica, controles, tipos de controles, vel. monitor
# Trabajo           : Conexiones USB, Entrada red inalambrica, salida video (HDMI, VGA, DP)
from prog08_pidevalor import PideValor

class Computadora():
    def __init__(self, mem = "", dd = "", pro = "", mon = ""):
        self.mem = mem
        self.dd = dd
        self.pro = pro
        self.mon = mon

    def muestra(self):
        print("Procesador _________ : ", self.pro)
        print("Disco Duro _________ : ", self.dd)
        print("Memoria Ram ________ : ", self.mem)
        print("Monitor ____________ : ", self.mon)
# Termina clase Computadora

class Escritorio(Computadora):
    def __init__(self, mem = "", dd = "", pro = "", mon = "", gabinete = "", teu = "", 
                 tipo = "", deu = ""):
        self.gabinete = gabinete
        self.teu = teu
        super().__init__(mem = mem, dd = dd, pro = pro, mon = mon, tipo = tipo, deu = deu)

    def muestra(self):
        super().muestra()
        print("Gabinete ___________ : ", self.gabinete)
        print("Todo en uno ________ : ", self.teu)

class Laptop(Computadora):
    def __init__(self, mem = "", dd = "", pro = "", mon = "", tipo = "", deu = ""):
        self.tipo = tipo
        self.deu = deu
        super().__init__(mem = mem, dd = dd, pro = pro, mon = mon)

    def muestra(self):
        super().muestra()
        print("Tipo _______________ : ", self.tipo)
        print("Dos en uno _________ : ", self.deu)

class Tipo(Escritorio,Laptop):
    pass

class Trabajo(Tipo):
    def __init__(self, mem='', dd='', pro='', mon='', gabinete='', teu='', tipo = "", deu = "", usb = "", 
                 rala = "", svideo = "", diadema = "", controles = "", tipo_ctrl = "", vel_mon = ""):
        self.usb = usb
        self.rala = rala
        self.svideo = svideo
        super().__init__(mem = mem, dd = dd, pro = pro, mon = mon, gabinete = gabinete, teu = teu, 
                         tipo = tipo, deu = deu, diadema = diadema, controles = controles, 
                         tipo_ctrl = tipo_ctrl, vel_mon = vel_mon)

        def muestra(self):
            super().muestra()
            print("USB ____________ : ", self.usb)
            print("Red alambrica __ : ", self.rala)
            print("Salida de video  : ", self.svideo)

class Gamer(Tipo):
    def __init__(self, mem='', dd='', pro='', mon='', gabinete='', teu='', tipo = "", deu = "", 
                 diadema = "", controles = "", tipo_ctrl = "", vel_mon = ""):
        self.diadema = diadema
        self.controles = controles
        self.tipo_ctrl = tipo_ctrl
        self.vel_mon = vel_mon
        super().__init__(mem=mem, dd=dd, pro=pro, mon=mon, gabinete=gabinete, teu=teu, tipo=tipo, deu=deu)

    def muestra(self):
        super().muestra()
        print("Diadema ____________ : ", self.diadema)
        print("Controles __________ : ", self.controles)
        print("Tipo control _______ : ", self.tipo_ctrl)
        print("Velocidad Monitor __ : ", self.vel_mon)

class Madre(Trabajo, Gamer):
    pass

def pide_computadora():
    pc = PideValor("Indica el tipo y velocidad del procesador   :")
    pro = pc.pide_cadena()
    pc = PideValor("Indica la capacidad memoria principal (RAM) :")
    mem = pc.pide_cadena()
    pc = PideValor("Indica la capacidad del disco duro          :")
    dd = pc.pide_cadena()
    pc = PideValor("Indica tipo y tamaño del monitor            :")
    mon = pc.pide_cadena()
    pc = PideValor("Indica tipo de gabinete                     :")
    gabinete = pc.pide_cadena()
    pc = PideValor("Indica si es todo en uno                    :")
    teu = pc.pide_cadena()
    pc = PideValor("Indica la cantidad de puertos USB           :")
    usb = pc.pide_cadena()
    pc = PideValor("Indica si tiene red alambrica               :")
    rala = pc.pide_cadena()
    pc = PideValor("Indica las salidas de video                 :")
    svideo = pc.pide_cadena()
    pc = PideValor("Ingrese el tipo de laptop                   :")
    tipo = pc.pide_cadena()
    pc = PideValor("Ingrese si es dos en uno                    :")
    deu = pc.pide_cadena()
    pc = PideValor("Tiene diadema ??                            :")
    diadema = pc.pide_cadena()
    pc = PideValor("Tiene controles ??                          :")
    controles = pc.pide_cadena()
    pc = PideValor("Tipo de controles                           :")
    tipo_ctrl = pc.pide_cadena()
    pc = PideValor("Velocidad del monitor                       :")
    vel_mon = pc.pide_cadena()

    oc = Madre(pro = pro, mem = mem, dd = dd, mon = mon, gabinete = gabinete, 
               teu = teu, usb = usb, rala = rala, svideo = svideo, tipo = tipo, 
               deu = deu, diadema = diadema, controles = controles, 
               tipo_ctrl = tipo_ctrl, vel_mon = vel_mon)
    oc.muestra()
# Termina funcion pide_computadora

pide_computadora()