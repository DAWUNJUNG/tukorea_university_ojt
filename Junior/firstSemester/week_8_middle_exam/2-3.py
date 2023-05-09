with open("NM_207618.2.fasta", "r") as inf:
    data = inf.read().splitlines(True)
with open('dna1.txt', 'w') as outf:
    outf.writelines(data[1:])
f = open("dna1.txt", "r")
sequence = f.read()
sequence = sequence.replace(' ', '')
sequence = sequence.replace('\n', '')
sequence = sequence.replace('\r', '')
print(sequence)