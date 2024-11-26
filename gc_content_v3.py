def gc_content (sequence):
    """poner como documentar un programa"""
    sequence = sequence.rstrip("\n")
    sequence = sequence.upper()
    count_G =  sequence.count("G")
    count_A = sequence.count("A")
    count_C = sequence.count("C")
    count_T = sequence.count("T")
    GC_content = count_C + count_G
    GC_content = GC_content / len(sequence)
    GC_content = round(GC_content * 100, 2)
    return GC_content
    pass

fasta_file = "levadura.fasta"

output_file = fasta_file.split('.')[0]
output_file = output_file + "_gc_content.txt"

sequence = str ()
######## No modificar ############
with open (fasta_file) as file :
    for line in file:
        if line.startswith('>'):
            pass
        else:
            line = line.rstrip('\n')
            sequence += line

print (sequence)
print (gc_content(sequence))
gc_content = gc_content(sequence)

file1 = open (output_file, "w")
file1.write(f" El contenido de GC es:{gc_content} %\n")
file1.close()