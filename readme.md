# Simulador de la máquina Enigma  

---

### Construído con Python, Flask y CSS

---

Simulador de la máquina Enigma de comunicación encriptada, empleada por la Wermacht entre 1937 y 1945, 
así como durante la guerra civil española. 

---

### Versión actual 
- La aplicación simula el modelo Enigma I (Heer) con 3 rotores y un reflector
- La combinación de rotores y reflectores puede elegirse de un total de 5 rotores y 2 reflectores históricos 

### Alfabeto

- La Enigma usaba el alfabeto latino de 26 caracteres empleados en el idioma alemán sin el caracter especial **Eszett** o ß 

---

### Encriptar un mensaje

- Seleccionar una configuración de Enigma (combinación de 3 rotores y reflector)
- Seleccionar la posición inicial (letra del alfabeto) de cada rotor
- Escribir el mensaje usando solo las 26 letras del alfabeto y sin espacios entre palabras 

---

### Desencriptar un mensaje

- Seleccionar la misma configuración usada al encriptar
- Seleccionar las mismas posiciones iniciales de los rotores usadas al encriptar
- Escribir el mensaje encriptado

### Ejemplo

Configuración: Rotor 1 = I, Rotor 2 = II, Rotor 3 = III y reflector = B
Posiciones iniciales de los rotores: 'A', 'A' y 'A'

```sh```
Mensaje: "Gutenmorgen"
Mensaje encriptado: "OXODLZPTRBP"
```

### Demo
Para una demo preliminar: 

https://b4r4th30nspa.pythonanywhere.com/

