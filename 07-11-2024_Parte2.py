sequence = "TACATaCAA"
sequence = sequence.upper()
count_A = 0
for nucleotide in sequence:
  #print(f"El nucleotido es: {nucleotide}")
  if nucleotide == "A":
    print(f"El nucleotido: {nucleotide} es A")
    count_A += 1
  else:
    print(f"El nucleotido: {nucleotide} no es A")
  pass

print(f"El total de Adenindas es: {count_A}")
print("Y corresponde al:", round(count_A/len(sequence) *100, 2),"%")