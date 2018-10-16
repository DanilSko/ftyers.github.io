## MaxMatch by Danya

#testsentence = 'ホッケーにはデンジャラスプレ'
#testdictionary = 'ホッケ ーには デンジ ャラスプレ'

def maxmatch (sentence, dictionary, final_list = None):
    if final_list == None:
        final_list = []
    if len (sentence) == 0:
        return final_list
    for character_position in range (len(sentence),0, -1):
        firstword = sentence[0:character_position]
        remainder = sentence[character_position:]
        if firstword in dictionary:
            final_list.append (firstword)
            maxmatch (remainder, dictionary ,final_list)
            return (final_list)
    firstword = sentence[0]
    remainder =  sentence[1:]
    final_list.append (firstword)
    maxmatch (remainder, dictionary, final_list)
    return (final_list)
