count_A = 0
count_C = 0
count_G = 0
count_T = 0
gc_content = 0
gene_name = ""
with open ('Bsubtilis_CDS.fna.txt') as file:
    for line in file:
        if line.startswith('>'):
            gc_content += (count_G + count_C)/(count_G + count_C+count_A + count_T)*100
            try:
                gc_content += (count_G + count_C)/(count_G + count_C+count_A + count_T)
            except ZeroDivisionError:
                gc_content = 0
            try:
                
            print(gc_content)
            # print(line.strip())
            temp = line.split()
            # print(temp)
            gene_name = temp[1].split('=')[1][:-1]
            count_A=count_C=count_G=count_G=0
            gc_content = 0
            print(gene_name)
        #if "gene=" in gene_name or "locus_tag=":
            #gene_name = gene_name.replace("gene=","").replace ("locus_tag=","")
            #print(gene_name)
        else:
            count_A += line.count("A")
            count_C += line.count("C")
            count_G += line.count("G")
            count_T += line.count("T")
            #gc_content = count_C + count_G
            #gc_content = gc_content / len(line)
            #gc_content = round(gc_content * 100, 2)
            #print(count_A)
