# Simulador de la máquina Enigma  

---

### Construído con Python, Flask y CSS

---

Simulador de la máquina Enigma de comunicación encriptada. Empleada por el Ejército (Wehrmatch) y la armada alemana entre 1930 y 1945.

Su mecanismo electromecánico se basa en la técnica de cifrado "César"

Para mayor información sobre Enigma: 

https://en.wikipedia.org/wiki/Enigma_machine

https://www.youtube.com/watch?v=L8N829w3je4


---

### Versión implementada 

- La aplicación simula el modelo Enigma I con 3 rotores y un reflector fijo
- La combinación de rotores, así como el reflector, pueden elegirse de un total de 5 rotores y 2 reflectores históricos:

```sh

Rotores disponibles:

I: ABCDEFGHIJKLMNOPQRSTUVWXYZ - EKMFLGDQVZNTOWYHXUSPAIBRCJ  
II: ABCDEFGHIJKLMNOPQRSTUVWXYZ  - AJDKSIRUXBLHWTMCQGZNPYFVOE
III: ABCDEFGHIJKLMNOPQRSTUVWXYZ  - BDFHJLCPRTXVZNYEIWGAKMUSQO
IV: ABCDEFGHIJKLMNOPQRSTUVWXYZ  - ESOVPZJAYQUIRHXLNFTGKDCMWB
V: ABCDEFGHIJKLMNOPQRSTUVWXYZ  - VZBRGITYUPSDNHLXAWMJQOFECK


Reflectores disponibles:

B: YRUHQSLDPXNGOKMIEBFZCWVJAT
C: FVPJIAOYEDRZXWGCTKUQSBNMHL
```

### Alfabeto

- La Enigma usaba el alfabeto latino de 26 caracteres empleados en el idioma alemán sin el caracter especial **Eszett** o ß 

---

### Encriptar un mensaje

- Seleccionar una configuración de Enigma (combinación de 3 rotores y reflector)
- Seleccionar la posición inicial (letra del alfabeto) de cada rotor
- Escribir el mensaje usando únicamente las 26 letras del alfabeto y sin espacios entre palabras 

---

### Desencriptar un mensaje

- Seleccionar la misma configuración usada al encriptar
- Seleccionar las mismas posiciones iniciales de los rotores usadas al encriptar
- Escribir el mensaje encriptado

### Ejemplo

Configuración: Rotor 1 = I, Rotor 2 = II, Rotor 3 = III y reflector = B
Posiciones iniciales de los rotores: 'A', 'A' y 'A'

```sh
Mensaje: "GUTENMORGEN"
Mensaje encriptado: "OXODLZPTRBP"
```

### Live Demo
Prueba la enigma aquí:  

https://b4r4th30nspa.pythonanywhere.com/

