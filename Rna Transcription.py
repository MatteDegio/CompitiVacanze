def to_rna(dna_strand):
    lettere = { 'G':'C', 'C':'G', 'T':'A','A':'U'}
    rna = ''
    for k in dna_strand:
        if k not in lettere:
            return ''
        else:
            rna += lettere[k]
    return rna