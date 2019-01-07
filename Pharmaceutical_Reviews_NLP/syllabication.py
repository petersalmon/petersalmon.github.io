# A function that takes a list of drug names and returns a list of the number of syllabuls of each name

def count_syllables(word):
    
    def words_in_string(word_list, a_string):
        return set(word_list).intersection(a_string.split())
    
    import string
    letters = list(string.ascii_lowercase)
    
    vowels = ['a', 'e', 'i', 'o', 'u', 'y']
   
    consonants = []
    for letter in letters:
        if not words_in_string(vowels, letter):
            consonants.append(letter) 
    
    # list of rules that are encoded in the function:
    
    # if hyphens, '-', present, begin after the last hyphen
    
    if '-' in word:      
        pos = word.rfind("-")
        pos += 1
        
        if word[:4] == 'tri-':
            new_word = 'tri'
            
        elif word[:5] == 'mono-':
            new_word = 'mo-no'
            
        elif word[:6] == 'ortho-':
            new_word = 'or-tho'
            
        elif word[:8] == 'orthori-':
            new_word = 'or-tho-ri'
            
        elif word[:5] == 'depo-':
            new_word = 'de-po'
        
        else:
            new_word = word[:pos-1]
        
    else: 
        pos = 0
        new_word = ''
        
    # Break after 'tri', 'mono', or 'ortho'; usually included in the beginning of a name
    
    if word[pos:pos+3] == 'tri':
        if pos == 0:
            new_word = new_word + 'tri'
        else:
            new_word = new_word + '-tri'
        pos = pos+3
        
    if word[pos:pos+4] == 'mono':
        if pos == 0:
            new_word = new_word + 'mo-no'
        else:
            new_word = new_word + '-mo-no'
        pos = pos+4
        
    if word[pos:pos+5] == 'ortho':
        if pos == 0:
            new_word = new_word + 'or-tho'
        else:
            new_word = new_word + '-or-tho'
        pos = pos+5
    
    # Break after the letter following the first vowel
    
    while len(word[pos:]) > 4:
        vowel_indices = [word[pos:].find(vowel) for vowel in vowels]

        if min(vowel_indices) >= 0:
            first_vowel = min(index for index in vowel_indices if index > 0)
        else:
            first_vowel = min(index for index in vowel_indices if index > -1)

        if pos == 0:
            new_word = new_word + word[pos:(pos+first_vowel+2)]
        else:
            new_word = new_word + '-' + word[pos:(pos+first_vowel+2)]
    
        pos = pos+first_vowel+2
        
    # If last word has pattern cvcv, split after first vowel
      
    if (len(word[pos:]) == 4) and (word[pos:][0] in consonants) and (word[pos:][1] in vowels) and (word[pos:][2] in consonants) and (word[pos:][3] in vowels):
        last_word = word[pos:]
        new_word = new_word + '-' + last_word[:2] + '-' + last_word[2:]
        
    # If last word has pattern vcvc, split after first consonant
      
    elif (len(word[pos:]) == 4) and (word[pos:][0] in vowels) and (word[pos:][1] in consonants) and (word[pos:][2] in vowels) and (word[pos:][3] in consonants):
        last_word = word[pos:]
        new_word = new_word + '-' + last_word[:2] + '-' + last_word[2:]
        
    # If last word has pattern vccv, split between the consonants
      
    elif (len(word[pos:]) == 4) and (word[pos:][0] in vowels) and (word[pos:][1] in consonants) and (word[pos:][2] in consonants) and (word[pos:][3] in vowels):
        last_word = word[pos:]
        new_word = new_word + '-' + last_word[:2] + '-' + last_word[2:]
        
    else:
        new_word = new_word + '-' + word[pos:]
    
    # Cleaning and returning 'new_word'
    
    if new_word[0] == '-':      # if '-' is first, remove it 
        new_word = new_word[1:]
        
    if (new_word[-1] == 'o') and (new_word[-2] == 'l'):      # if last 2 letters are 'lo', split it 
        new_word = new_word[:-1] + '-' + new_word[-1]
        
    if (new_word[-1] == 'a') and (new_word[-2] == 'i'):      # if last 2 letters are 'ia', split it 
        new_word = new_word[:-1] + '-' + new_word[-1]
     
    # Splitting word on hyphens

    new_word = new_word.split('-')
    
    new_word_len = len(new_word)
    
    #return(new_word)
    return(new_word_len)