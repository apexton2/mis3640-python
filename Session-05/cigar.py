def cigar_party(cigars, is_weekend):
 
return is_weekend and cigars >= 40 or 40 <= cigars <= 60


cigar_party(30, False)
cigar_party(50, False) 
cigar_party(70, True) 