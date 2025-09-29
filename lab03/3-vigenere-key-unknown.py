""" 
3. Vigenere šifro raktas nežinomas. Iššifruokite šifrą 

EAZŪU BBŲSI NRUIM ŠBENO MDVAP 
TZFIL KJČIT OĮISI URČBU TRIFK 
ZĘPVR SHŠKŠ FIĮHA BFŲMY IMDOF 
MKIĖB MBIAE EĖDĖC ŪČZIU ĄRIEB 
IŽBSB MLDKV MCŠIĘ DAZOT IEDRI 
ŽBAZI NDARZ ŽDĘĮT EFĖŲG MZŪRA 
ĮKEĄA CDAČŲ AEFEO MBENO JŠEDG 
SMŽTL BDŠVI AĮTMV OĄIIŠ VAŽAO 
MČADĮ IŪBĘH BAIŠR ĄIIŠĄ ADCEZ 
ŽAZLJ ĮLUBL PMZAK BAIVU YRSFŠ 
EŪBAD KIĮHR MFIBS SĘŠND SPZVN 
ĮEOČY IŽŪZE ŽŲLRR OAIBR PFIUR 
BNZĘP BBJIA SKBŲC MNDČN ECEYR 
LHŠNŠ KSĘBI MYSĘŠ NLKLZ ŽIĘŠA 
HĘAEĘ UECEY ĘIKRĖ ŲGACŠ UZBNZ 
ŽIIBK ZVNAD AČĘJĘ ŲEŪEO ŽBEFI 
PIIAH ĘBIĘI EŽAŠĮ UDMŠŠ GJMEK 
ŽČGMC AĄRRM DUCBR ŽBAŽE IICNE 
GDJŠE ŲLKUL ŽŠLĮB IMĄKS FEKIB 
ŠZAJI KJIAS ŪKRĘI KVBUJ AIBRP 
CŠNŪĘ OJĮTI IPFĄI ŽJOFŠ RVŪNH 
UNĘHA FŠDII ĖGŠEŪ JIŠŪT EYČZA 
SMIDJ OSĄII FŠTBR UBŠAE HABIB 
ĮEEHŠ NLRMM CPIEA OŠNDB ADDJA 
ĮSBIF IFDĖĮ IBDAI CUOĖI MEUHJ 
RMEKD KKICB MJTIA JĄRTĄ EOCHA 
CMILR UBIŽŪ GDUVN MAACO JIKRA 
HTŠĮN ICIZŪ SHŠSŪ RFMŽD BSTMB 
SŠŲĖC DODRP RŠAEŠ EŪŠNŪ ĘIFŽU 
CBMŠK IIKJŽ ŠRCJU ČDEVZ JMESĄ 
BNHĮJ ŠHAFŠ SVBNB AĮČGN NŠREP 
JECNŠ YOĄMS EŠLZG GODOČ ŠNŠRT 
ZĖRŠF IEFOŽ BOFŪA ZŠAĖŠ OCBED 
ASIFT ŪBIŽŲ ŲĘADE YUŪEL ODOSŠ 
DAEAĘ VOŪYČ ZIKIĮ EHOSE FKZII 
TFEGŠ AEDĄŽ ŪAZŠA ĖTKIB SHIČŠ 
RUMŽT RIIDL ŲFBRG MLŠĮA HČOŪG 
LARAŽ JSĘUR EGKCŠ ŲŠIAG ĄAZRČ 
ZIUĄŪ RHFAB RSĘBI RIŪFD ACEEZ 
CTĘŲA ZŪTĘŲ ĖLOBE NOĘŠL ŽRBMŠ 
SŠRIF EBŲRU ĖŠNDL BŠDKI BPZČT 
IĖSME SZŪTM VOŽKD ĖOBDL ĮĖINŪ 
BŲHBU ĄKTŽĄ AŽRŠZ ĘĮDKO FŪUBB 
EŪELO DOFĄI ŽJECO SM

"""

# TODO: Fix typization

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

ciphertext = '''EAZŪU BBŲSI NRUIM ŠBENO MDVAP 
TZFIL KJČIT OĮISI URČBU TRIFK 
ZĘPVR SHŠKŠ FIĮHA BFŲMY IMDOF 
MKIĖB MBIAE EĖDĖC ŪČZIU ĄRIEB 
IŽBSB MLDKV MCŠIĘ DAZOT IEDRI 
ŽBAZI NDARZ ŽDĘĮT EFĖŲG MZŪRA 
ĮKEĄA CDAČŲ AEFEO MBENO JŠEDG 
SMŽTL BDŠVI AĮTMV OĄIIŠ VAŽAO 
MČADĮ IŪBĘH BAIŠR ĄIIŠĄ ADCEZ 
ŽAZLJ ĮLUBL PMZAK BAIVU YRSFŠ 
EŪBAD KIĮHR MFIBS SĘŠND SPZVN 
ĮEOČY IŽŪZE ŽŲLRR OAIBR PFIUR 
BNZĘP BBJIA SKBŲC MNDČN ECEYR 
LHŠNŠ KSĘBI MYSĘŠ NLKLZ ŽIĘŠA 
HĘAEĘ UECEY ĘIKRĖ ŲGACŠ UZBNZ 
ŽIIBK ZVNAD AČĘJĘ ŲEŪEO ŽBEFI 
PIIAH ĘBIĘI EŽAŠĮ UDMŠŠ GJMEK 
ŽČGMC AĄRRM DUCBR ŽBAŽE IICNE 
GDJŠE ŲLKUL ŽŠLĮB IMĄKS FEKIB 
ŠZAJI KJIAS ŪKRĘI KVBUJ AIBRP 
CŠNŪĘ OJĮTI IPFĄI ŽJOFŠ RVŪNH 
UNĘHA FŠDII ĖGŠEŪ JIŠŪT EYČZA 
SMIDJ OSĄII FŠTBR UBŠAE HABIB 
ĮEEHŠ NLRMM CPIEA OŠNDB ADDJA 
ĮSBIF IFDĖĮ IBDAI CUOĖI MEUHJ 
RMEKD KKICB MJTIA JĄRTĄ EOCHA 
CMILR UBIŽŪ GDUVN MAACO JIKRA 
HTŠĮN ICIZŪ SHŠSŪ RFMŽD BSTMB 
SŠŲĖC DODRP RŠAEŠ EŪŠNŪ ĘIFŽU 
CBMŠK IIKJŽ ŠRCJU ČDEVZ JMESĄ 
BNHĮJ ŠHAFŠ SVBNB AĮČGN NŠREP 
JECNŠ YOĄMS EŠLZG GODOČ ŠNŠRT 
ZĖRŠF IEFOŽ BOFŪA ZŠAĖŠ OCBED 
ASIFT ŪBIŽŲ ŲĘADE YUŪEL ODOSŠ 
DAEAĘ VOŪYČ ZIKIĮ EHOSE FKZII 
TFEGŠ AEDĄŽ ŪAZŠA ĖTKIB SHIČŠ 
RUMŽT RIIDL ŲFBRG MLŠĮA HČOŪG 
LARAŽ JSĘUR EGKCŠ ŲŠIAG ĄAZRČ 
ZIUĄŪ RHFAB RSĘBI RIŪFD ACEEZ 
CTĘŲA ZŪTĘŲ ĖLOBE NOĘŠL ŽRBMŠ 
SŠRIF EBŲRU ĖŠNDL BŠDKI BPZČT 
IĖSME SZŪTM VOŽKD ĖOBDL ĮĖINŪ 
BŲHBU ĄKTŽĄ AŽRŠZ ĘĮDKO FŪUBB 
EŪELO DOFĄI ŽJECO SM'''
key = '' # key unknown

# inverse_key = ''.join([number2letter((-letter2number(k)) % n) for k in key])
# print(encryptVigenere(ciphertext, inverse_key))

# print(friedman_test(ciphertext, 6)) 
# d = 6


# for i in range(15):
#     print(i, friedman_test(ciphertext, i))

""" 
    0 1.0
    1 0.025664527956003668
    2 0.03302752293577982
    3 0.04224058769513315
    4 0.034926470588235295
    5 0.040478380864765406
    6 0.055248618784530384
    7 0.029493087557603687
    8 0.035977859778597784
    9 0.048938134810710986
    10 0.030499075785582256
    11 0.03885291396854764
    12 0.06296296296296296
    13 0.03151065801668211
    14 0.032467532467532464
"""

d = 6 # a guess
# d: length of the key

fragments = split(ciphertext, 6)
# print(fragments)

# for fragment in fragments:
#     print(order_by_frequency(fragment))
#     print()

""" 
BRKIĮFGEDJŪĘLHYŠŲNČĖASPUCZ

AIOSETRUJNKDPŲBČLMĖĮŠVZGFĄŪ

ZMFHEIĘCĖBČDŠŪJŽGSUAOĮĄKRNL

ŠICEŽABVDMŪĘĄOFRČLĮTHYZKUŲGĖ

IANUSTOKBREJLDPĖŲŠŽĮVĘMFGČ

IEŠŽDBĄŪCAZLMĘROVŲYĮTHKČF
"""

test = 'IAŠE' # This is for most common letters in the ciphertext?


# for i in range(d):
#     print("GUESSING key letter nr.", i)
#     for k in range(n):
#         print(k, number2letter(k), guess(test, k, fragments[i]))

#     print("********************************************************")
#     print()

# for k in range(n):
#     print(k, number2letter(k), guess(test, k, fragments[3]))
# # # key[3] = G ?

# # for k in range(n):
# #     print(k, number2letter(k), guess(test, k, fragments[4]))
# # # key[4] = U ?

# for k in range(n):
#     print(k, number2letter(k), guess(test, k, fragments[5]))
# # key[5] = S ?


# solution: 