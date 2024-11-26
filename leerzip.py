import gzip

sequence_file = " ../carpeta1/uniprotkb_accession_P51801_2024_11_14.tsv"
with gzip.open(sequence_file, "rt") as file:
    for line in file:
        print(line)

