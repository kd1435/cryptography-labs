""" 
2. Vigenere šifro raktas prasideda raidėmis = SAU. Iššifruokite šifrą 

KAEIO OHINR ĮHĮIČ RĮSĖU ĮZKYG 
IAUUY GETRĮ HEOGG EIKĄL ELŪĮE 
ŪČZCS IČGHC YTUIE ĖCZOZ NCŪAĮ 
OULYK RVYHĮ BECŲE SULKĮ CSIŪČ 
SHRIĮ ZICĄR UĘEKH REGEČ ĮEĮOE 
GCAEĄ OĘLRE GĮKDS ŽRKTK IĮROY 
EĖČZL CĮGKG SCKAV RFHYL UČGLY 
BACĮC VKUĄĮ VKNAS LCOAE ĖŽSOO 
GGEIS MYACC GĖGZM ŽĄAHR JSYIA 
UNCĮE ŠČHKS TŲUOĮ CSČAU OCTYA 
ELHSA OULGA IGLIV RLČŽŽ KIĮOU 
YTRUV ŽLHLE VAYĮE UUVCE ALRKF 
CLTRĮ CJKYT AKVMJ KKSKŪ KZFVŲ 
IUIOO HRAŪE SFALR HVJAN KHEŽD 
BĄĮCL KURJS KKEAN CYTUŪ GHGSA 
ASSKY SRŠFL IKGŽH YIGRN MBIJZ 
NVPIP ŽUODZ ŽFELC VEKĮS CŠČKK 
CSULR UCCŠČ ĘEĖŪE ĮCPŲC VECUO 
CTYPE IHTAĖ BĘLRE ĄGVĖB BUUŪH 
KAGĮS YYKGŽ CSLAU NCGIY RMYCV 
ĖĄNDF OJGLŽ ĘA

"""


from collections import defaultdict

abc = 'AĄBCČDEĘĖFGHIĮYJKLMNOPRSŠTUŲŪVZŽ' # the alphabet
n   = len (abc) # number of letters in the alphabet

# makes text uppercase and filters out non-letters
def prepare (text):
    text = text.upper()
    new_text = ''
    for a in text:
        if a in abc:
            new_text += a
    return new_text

# converts a letter a from abc to a number from 0 to n - 1
def letter2number (a):
    return abc.index(a)

# converts a number d from 0 to n - 1 to a letter from abc
def number2letter (d):
    return abc [d]

# encrypts the given plaintext using Vigenere cipher with the given key
# the key is given as a word
def encryptVigenere (plaintext, key):
    plaintext = prepare (plaintext)
    key = prepare (key)
    
    # converts the key to a list of numbers
    keys = []
    key_length = len(key)
    for i in range (key_length):
        keys.append (letter2number (key [i]))

    # encrypts
    cyphertext = ""
    plaintext_length = len (plaintext)
    for i in range (plaintext_length):
        cyphertext += number2letter ((letter2number (plaintext [i]) + keys [i % key_length]) % n)
    return cyphertext

#print (encryptVigenere ('mountain', 'earth'))

# performs the Friedman's test on the given text with the given shift
def friedman_test (text, shift):
    text = prepare (text)
    text_length = len (text)
    equal_letters_count = 0
    for i in range (shift, text_length):
        if text [i] == text [i - shift] :
            equal_letters_count += 1
    return  1. * equal_letters_count / (text_length - shift)

#print (friedman_test ('ABDBSBSBSBBBCN', 2))

# splits the given text into d parts
def split (text, d):
    text = prepare (text)
    split_text = [''] * d # the list of d empty strings
    text_length = len (text)
    for i in range (text_length):
        split_text [i % d] += text [i]
    return split_text    
    
#print (split ('ABABABABABAB', 2))

# orders the letters of the given text according to their frequency of appearance in it (most frequent first)
def order_by_frequency (text):
    text = prepare (text)
    
    # counts the frequencies of letters
    frequencies = defaultdict (int)
    for w in text:
        frequencies [w] += 1                   

    # sorts the letters most frequent first and puts them in the string ordered_letters
    ordered_letters = ""
    for w in sorted (frequencies, key=frequencies.get, reverse=True):
        ordered_letters += w
    return ordered_letters

#print (order_by_frequency ('TRRYYYIIU'))

# computes the part of the letters of test encrypted with the given key in the given ciphertext
# test - most frequent letter string, key - guessed Caesar cipher key
def guess(test, key, ciphertext): 
    test = prepare (test)
    ciphertext = prepare (ciphertext)
    
    # encrypts the given test with the given key
    encrypted_test = ''
    for r in test:
        encrypted_test += number2letter ((letter2number (r) + key) % n)

    # counts the letters of encrypted_test in the given ciphertext
    nb = 0
    for r in ciphertext:
        if r in encrypted_test: 
            nb += 1
    return 1. * nb / len(ciphertext)

#print (guess ('ABC', 2, 'ABABABASSDDHHDKKKCCCCCLKLDKSJJSJSJLL'))

ciphertext = '''KAEIO OHINR ĮHĮIČ RĮSĖU ĮZKYG 
IAUUY GETRĮ HEOGG EIKĄL ELŪĮE 
ŪČZCS IČGHC YTUIE ĖCZOZ NCŪAĮ 
OULYK RVYHĮ BECŲE SULKĮ CSIŪČ 
SHRIĮ ZICĄR UĘEKH REGEČ ĮEĮOE 
GCAEĄ OĘLRE GĮKDS ŽRKTK IĮROY 
EĖČZL CĮGKG SCKAV RFHYL UČGLY 
BACĮC VKUĄĮ VKNAS LCOAE ĖŽSOO 
GGEIS MYACC GĖGZM ŽĄAHR JSYIA 
UNCĮE ŠČHKS TŲUOĮ CSČAU OCTYA 
ELHSA OULGA IGLIV RLČŽŽ KIĮOU 
YTRUV ŽLHLE VAYĮE UUVCE ALRKF 
CLTRĮ CJKYT AKVMJ KKSKŪ KZFVŲ 
IUIOO HRAŪE SFALR HVJAN KHEŽD 
BĄĮCL KURJS KKEAN CYTUŪ GHGSA 
ASSKY SRŠFL IKGŽH YIGRN MBIJZ 
NVPIP ŽUODZ ŽFELC VEKĮS CŠČKK 
CSULR UCCŠČ ĘEĖŪE ĮCPŲC VECUO 
CTYPE IHTAĖ BĘLRE ĄGVĖB BUUŪH 
KAGĮS YYKGŽ CSLAU NCGIY RMYCV 
ĖĄNDF OJGLŽ ĘA'''
# key = 'SAU'
key = 'SAUGUS'

inverse_key = ''.join([number2letter((-letter2number(k)) % n) for k in key])
print(encryptVigenere(ciphertext, inverse_key))

# print(friedman_test(ciphertext, 6)) 
# d = 6


# for i in range(15):
#     print(friedman_test(ciphertext, i))

fragments = split(ciphertext, 6)
# print(fragments)

# for fragment in fragments:
#     print(order_by_frequency(fragment))
#     print()

test = 'IECR'


# # for k in range(n):
# #     print(k, number2letter(k), guess(test, k, fragments[3]))
# # # key[3] = G ?

# # for k in range(n):
# #     print(k, number2letter(k), guess(test, k, fragments[4]))
# # # key[4] = U ?

# for k in range(n):
#     print(k, number2letter(k), guess(test, k, fragments[5]))
# # key[5] = S ?


# solution: TAIBUVOITINORIGINALUNORSNIEKASNEŽINOJOKAIPTĄSŪSDREBUČIAIGALISTABILIZUOTIDANGAUSKŪNOORBITĄJAUSENIAIBUVOŽINOMIGRAVITORIAIĮRENGINIAISUKURIANTYSDIRBTINIUSJĖGOSIRGRAVITACIJOSLAUKUSBETNIEKASNETNEĮSIVAIZDAVOKAIPAMORFINĖKOŠĖGALIPASIEKTIREZULTATĄKURISGRAVITORIUOSEGAUNAMASPERSUDĖTINGASBRANDUOLINESREAKCIJASIRMILŽINIŠKOJETEMPERATŪROJEČIABUVOREMIAMASILEŠATELJĖDĖSNIUKAIPATKIRTISTAMKONSERVATYVIZMUIRADOSIKITŲHIPOTEZIŲPAVYZDŽIUIVIENAIŠGERIAUSIAIIŠGVILDENTŲČIVITAVITOHIPOTEZĖKURISKELBĖKADOKEANASYRADIALEKTINIOIŠSIVYSTYMOPASĖKA