alphabet = 'a b c d e f g h i j k l m n o p q r s t u v w x y z'.split()
specials = '. / ` ( * + ! " , -'.split()

text = 'vujgvmCfb tj ufscfu ouib z/vhm jdjuFyqm jt fscfuu uibo jdju/jnqm fTjnqm tj scfuuf ' \
       'ibou fy/dpnqm yDpnqmf jt cfuufs boui dbufe/dpnqmj uGmb tj fuufsc ouib oftufe/ bstfTq jt ' \
       'uufscf uibo otf/ef uzSfbebcjmj vout/dp djbmTqf dbtft (ubsfo djbmtqf hifopv up csfbl ifu t/svmf ipvhiBmu ' \
       'zqsbdujdbmju fbutc uz/qvsj Fsspst tipvme wfsof qbtt foumz/tjm omfttV mjdjumzfyq odfe/tjmf Jo fui dfgb ' \
       'pg hvjuz-bncj gvtfsf fui ubujpoufnq up ftt/hv Uifsf vmetip fc pof.. boe sbcmzqsfgf zpom pof pvt..pcwj xbz ' \
       'pu pe ju/ Bmuipvhi uibu bzx bzn puo cf wjpvtpc bu jstug ttvomf sfzpv( i/Evud xOp tj scfuuf ibou /ofwfs ' \
       'uipvhiBm fsofw jt fopgu cfuufs boui iu++sjh x/op gJ ifu nfoubujpojnqmf tj eibs pu mbjo-fyq tju( b bec ' \
       '/jefb Jg fui foubujpojnqmfn jt fbtz up bjo-fyqm ju znb cf b hppe jefb/ bnftqbdftO bsf pof ipoljoh ' \
       'sfbuh efbj .. fu(tm pe psfn gp tf"uip'

result = ''
for symbol in text:
    if symbol.isalpha():       # Проверка на букву
        if symbol.isupper():     # Проверка на регистр
            result += ''.join(alphabet[alphabet.index(symbol.lower()) - 1]).upper()
        else:
            result += ''.join(alphabet[alphabet.index(symbol.lower()) - 1])

    elif not symbol.isalpha() and symbol != ' ':     # Проверка на знак
        result += ''.join(specials[specials.index(symbol) - 1])
    else:
        result += ''.join(symbol)

moved_result = ''
x = 0
for word in result.split():
    moved_word = list(word)

    for _ in range(3 + x):
        moved_word.insert(0, moved_word[-1])
        moved_word.pop(-1)

    moved_result += ''.join(moved_word) + ' '

    if moved_word[-1] == '.' or moved_word[-1] == '!':
        x += 1
        print(moved_result)
        moved_result = ''

    moved_word = []
