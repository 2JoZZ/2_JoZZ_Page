"""Clase Martes 12 de Noviembre - Estilos y usos de texto"""

"""
Este programa toma una secuencia de DNA y calcula el contenido de GC
"""

# sequence asfdxasfdasfd
sequence =str()
gc_content =float()
count_A = 0
count_T = 0
count_G = 0
count_C = 0
sequence = "ACGTACGTACGTACGTacgtn X \n"
sequence = sequence.upper()
sequence = sequence.replace(" ","")   # elimina los espacios . Sirve para eliminar elementos que no deseamos en la linea
sequence = sequence.replace("\n","")  # elimina los saltos de linea
#sequence.strip()
for nucleotide in sequence:
  #print("--->" ,nucleotide)    #---> me permite detallar si hay algun salto en la linea en este caso la la secuencia.
  if nucleotide == "A":
    # print(nucleotide)
    count_A += 1
    pass
  elif nucleotide == "C":
    # print(nucleotide)
    count_C += 1
    pass
  elif nucleotide == "G":
    # print(nucleotide)
    count_G += 1
    pass
  elif nucleotide == "T":
    # print(nucleotide)
    count_T += 1
    pass
  else:
    print(f"Nucleotido no reconocido \n{nucleotide}")
  pass
print(f"El total de Adeninas es: {count_A}")
print(f"El total de Timinas es: {count_T}")
print(f"El total de Guaninas es: {count_G}")
print(f"El total de Citosinas es: {count_C}")

gc_content = (count_C + count_G) / len(sequence) * 100
print(f"El contenido de GC es: {round(gc_content,2)}%")
sequence.count("GC")