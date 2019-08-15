import difflib

a = 'Thanks for calling America Expansion'
b = 'Express'
c = 'Thanks for calling American Express'
seq = difflib.SequenceMatcher(None,a,c)
d = seq.ratio()*100
print(d)
### OUTPUT: 87.323943
