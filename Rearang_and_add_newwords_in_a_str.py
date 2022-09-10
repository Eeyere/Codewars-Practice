
"""
Spyder Editor

This is a temporary script file.
"""
aa=('hello world rules !')





"""
for ind, val in enumerate(ab):
    if val[0] in letters:
        ab[ind]=val[1:]+val[0]+'ay'
        """
    
    

def pig_it(text):
    tt=text.split(' ')
    letters= 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    for ind,val in enumerate(tt):
        if val[0] in letters:
            tt[ind]=val[1:]+val[0]+'ay'
    return ' '.join(tt)

print(pig_it(aa))
print(pig_it('Pig latin is cool'))

def pig_it(text):
    return ' '.join([w[1:] + w[0] + 'ay' if w.isalpha() else w for w in text.split(' ')])   


from string import punctuation
def pig_it(text):
    words = text.split(' ')
    return ' '.join(
        [
            '{}{}ay'.format(
                word[1:],
                word[0]
            ) if word not in punctuation else word for word in words
        ]
    )



def pig_it(text):
    return " ".join(x[1:] + x[0] + "ay" if x.isalnum() else x for x in text.split())