#VERSION QUE REPRODUCE LOS RESULTADOS DE DOS SIMULADORES EXISTENTES ('enigma08.py)
#FALTA:

#DECODIFICAR EN CADENAS DE 4 CARACTERES Y NO PERMITIR ESPACIOS (O CODIFICARLOS CON X)
#HACER REDIRECT AL REFRESCAR
#PERMITIR EL REDIRECT CON POST REQUEST CON EL CAMPO ENTRADA VACÍO (NO LO HACE)
#DOBLE PASO
#PLUGBOARD
#RING SETTINGS
#ACTIVAR LA DECODIFICACION SOLO SI SE ESCOGE LA OPCION 'ENIGMA I' DEL MENÚ
#DEFINIR CONFIGURACIÓN DE MODELOS
#HACER QUE REGRESE A DONDE ESTABA AL REFRESCAR (QUE NO SALTE)
#PROBLEMA OCASIONAL AL REFRESCAR DESCUADRA EVERYTHING!
#HOSPEDAR EN GITHUB

#abecedario
abecedario = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

#juego de rotores  
juego = {'I'  : ['EKMFLGDQVZNTOWYHXUSPAIBRCJ', 'Q'],
            'II' : ['AJDKSIRUXBLHWTMCQGZNPYFVOE' , 'E'],
            'III': ['BDFHJLCPRTXVZNYEIWGAKMUSQO' , 'V'],
            'IV' : ['ESOVPZJAYQUIRHXLNFTGKDCMWB' , 'J'],
            'V'  :  ['VZBRGITYUPSDNHLXAWMJQOFECK', 'Z']
            #'VI' : ['JPGVOUMFYQBENHZRDKASXLICTW', 'ZM'],
            #'VII': ['NZJHGRCXMYSWBOUFAIVLPEKQDT', 'ZM'],
            #'VIII': ['FKQHTLXOCBJSPDZRAMEWNIUYGV', 'ZM']
            }

#juego de reflectores (UKW):

UKW = { 'B':'YRUHQSLDPXNGOKMIEBFZCWVJAT', 
        'C': 'FVPJIAOYEDRZXWGCTKUQSBNMHL'}


class Reflector():
 
    def __init__(self, abecedario, UKW):
        self.abecedario = abecedario
        self.UKW = UKW
        
        
    def refleja(self,indice): 
        reflejo = self.UKW[indice]
        indice = self.abecedario.index(reflejo)
        return indice


class Rotor():
   
    def __init__ (self, abecedario, pareo, paso='Z', orden =1):
        self.abecedario = abecedario
        self.pareo = pareo
        self._paso = paso    
        self._ini = 0
        self.orden = orden
    
        
    def avanza(self):        
        
        if self.orden == 1:       
            self._ini = (self._ini + 1) % len(self.abecedario)

        elif self.orden == 2:  
            if trigger == True:
                self._ini = (self._ini + 1) % len(self.abecedario)
        else:
            if trigger == True:
                self._ini = (self._ini + 1) % len(self.abecedario)
     
    def paso(self):      
        if self._ini == (self.abecedario.index(self._paso) + 1) % len(self.abecedario):  
                        #Trigger debe cambiar a True en la letra siguiente a la del paso (por oposición a cambiar EN el paso), de lo contrario el resultado no es igual al de los simuladores  
            return True 
        else:
            return False                  


    def codifica(self,indice):
      
        indice =  (indice + self._ini) % len(self.abecedario)
        letra = self.pareo[indice]
        indice = (self.abecedario.index(letra) - self._ini) % len(self.abecedario)  
        return indice
        
    def decodifica(self, indice):
        indice =  (indice + self._ini) % len(self.abecedario)
        letra = self.abecedario[indice]
        indice = (self.pareo.index(letra) - self._ini) % len(self.abecedario)  
        return indice 


class Enigma():

   
    def __init__(self, abecedario, rotores, reflector, inicio='AAA'): 
        self.abecedario = abecedario
        self.rotores = rotores
        self.reflector = reflector
        self._ini = inicio
        for i, rotor in enumerate(self.rotores):    #inicializa los rotores existentes
            rotor._ini = self.abecedario.index(self._ini[i])  

        
    def codificaCadena(self, cadena):  
        cadenaCodificada = ''
        global trigger        #trigger cambia a True en el paso inmediatamente siguiente a cumplir la vuelta (método 'paso' de la clase Rotor)
        trigger = False
        
        for letra in cadena:
            indice = self.abecedario.index(letra)
            
            for rotor in self.rotores:
                rotor.avanza()
                trigger = rotor.paso()               
                #print(trigger)    
                   
                indice = rotor.codifica(indice)     #codifica una letra de la cadena (viaje de ida)
           
            indice = self.reflector.refleja(indice) #refleja el índice de salida del tercer rotor y se lo devuelve
            
            for rotor in self.rotores[::-1]:        #recorrido de vuelta desde el tercer al primer rotor
                indice = rotor.decodifica(indice)   #decodifica una letra de la cadena (viaje de vuelta)

            cadenaCodificada += self.abecedario[indice] 
        #print(cadenaCodificada)
        return cadenaCodificada  

    @property        #el setter permite cambiar la posicion inicial de Enigma (y de cada rotor) desde afuera
    def ini(self):
            return self._ini
        
    @ini.setter
    def ini(self, inicio):
        self._ini = inicio
        for i, rotor in enumerate(self.rotores):        
            rotor._ini = self.abecedario.index(self._ini[i])


    