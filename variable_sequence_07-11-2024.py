"""Clase Jueves 7 de noviembre #definicion de la VARIABLE SEQUENCE"""

sequence = "ABCDFGH" #  ABCFGH
print("La secuencia es:\n >",len(sequence)+3)
print(f"La secuencia es: {sequence}")  #contol + D duplica la entrada

sequence = sequence + "IJKL"
print(f"La secuencia es: {sequence}")

sequence += "MNÑOPQ"
print(f"La secuencia es: {sequence}")


print(len(sequence))

type(sequence)

sequence.lower()
sequence=sequence.lower()
print(f"La secuencia es: {sequence}")

for letter in sequence:
  print(letter)
  pass         #sirve para aplazar las iteraciones sin que sea necesario eliminar la linea que se puede usar depues


sequence[::-1]