def to_rna(dna_strand: str):
    tt = str.maketrans("ATGC", "UACG")
    return dna_strand.translate(tt)
