import string

def chiffrement_symetrique(msg: bytes, cle: bytes) -> bytes:

    msg_int = int.from_bytes(msg,'big')
    
    quotient = len(msg)//len(cle)
    reste = len(msg)%len(cle)
    cle_int = int.from_bytes(cle*quotient+cle[:reste],'big')

    xor = msg_int^cle_int

    taille = xor.bit_length()//8

    if xor.bit_length()%8 >= 1:
        taille += 1

    message_chiffrer = xor.to_bytes(taille,'big')
    
    return message_chiffrer


def lire_fichier(chemin: str) -> bytes:

    with open(chemin,"rb") as f:

        lines = f.read()

        return lines

def ecrire_fichier(b: bytes, chemin: str):

    with open(chemin,"wb") as f:

        f.write(b)


def chiffrement_symetrique_fichier(chemin_in: str,chemin_out: str, cle: bytes):
    
    bytes_txt = lire_fichier(chemin_in)
    txt_chiffrer = chiffrement_symetrique(bytes_txt,cle)

    ecrire_fichier(txt_chiffrer,chemin_out)




def chiffrement_cesar(decalage: int, message: str) -> str:

    alphabet = list(string.ascii_lowercase)

    chiffrement = "".join([alphabet[(alphabet.index(l)-decalage)%26] for l in message])

    return chiffrement

print(chiffrement_cesar(5,"lolita"))

#qtqnyf
#lolita