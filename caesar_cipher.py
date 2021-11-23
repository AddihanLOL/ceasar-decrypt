class caesar_cypher:
    def __init__(self):
        pass

    def decipher(self, text, key):
        letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
        #           1    2    3    4    5    6    7    8    9    10   11   12   13   14   15   16   17   18   19   20   21   22   23   24   25   26
        text = text.lower()


        words = []
        
        
        for x in text.split():
            for i in range(len(x)):
                if x[i] == "_":
                    return "[-] -> Please avoid '_' in your given text! "
                else:
                    if x[i] in ["ä", "ö", "ü", "ß", ".", ",", ":"]:
                        words.append(x[i])
                    else:
                        xi_value = letters.index(x[i])
                        xi_value = int(xi_value) + 1

                        diff = int(xi_value) - int(key) 
                        if diff <= 0:
                            diff = diff + 26

                        diff = diff - 1

                        words.append(letters[diff])
            words.append("_")
        
        results = "".join(words).replace("_", " ")


        return results

    
    def find_key(self, text):        
        pre = ""
        double_letter = ["hallo", "kann", "dann", "denn", "wann", "dass", "wenn", "können", "kennen"]

        for i in text.split():
            for x in range(len(i)):
                
                if i[x] == pre:
                    print(f"[+] -> Double letter found! {i}")

                    for y in range(26):
                        decifered = self.decipher(i, y + 1)
                        decifered = decifered[:len(decifered)-1]
                        if decifered in double_letter:
                            key = int(y) + 1
                            return self.decipher(text, key)

                else:
                    pre = i[x]
            
        return "[-] -> No double letter found!"
    
    
    
    def encipher(self, text, key):
        letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
        #           1    2    3    4    5    6    7    8    9    10   11   12   13   14   15   16   17   18   19   20   21   22   23   24   25   26
        text = text.lower()

        words = []

        for x in text.split():
            for i in range(len(x)):
                if x[i] == "_":
                    return "[-] -> Please avoid '_' in your given text! "
                else:
                    if x[i] in ["ä", "ö", "ü", "ß", ".", ",", ":"]:
                        words.append(x[i])
                    else:
                        xi_value = letters.index(x[i])
                        xi_value = int(xi_value) + 1

                        diff = int(xi_value) + int(key)
                        if diff > 26:
                            diff = diff - 26

                        diff = diff - 1

                        words.append(letters[diff])
            words.append("_")

        results = "".join(words).replace("_", " ")

        return results





if __name__ == "__main__":
    cc = caesar_cypher()
    #print(cc.find_key("Dlpa kyhbzzlu pu klu bulymvyzjoalu Lpuvlklu lpulz avahs hbz kly Tvkl nlrvttlulu Hbzshlbmlyz klz dlzaspjolu Zwpyhshytz kly Nhshepz slbjoala builhjoala lpul rslpul nlsil Zvuul. Bt zpl rylpza pu lpuly Luamlyubun cvu bunlmhloy hjoabukulbugpn Tpsspvulu Tlpslu lpu hizvsba builklbalukly, rslpuly ishbnybluly Wshula, klzzlu cvt Hmmlu zahttlukl Ipvmvytlu zv lyzahbuspjo wyptpapc zpuk, khzz zpl Kpnpahsboylu uvjo pttly müy lpul budhoyzjolpuspjo avssl Lympukbun ohsalu."))
    #print(cc.decipher("jre qnf yvrfg vfg qbbs", 13))
    #print(cc.encipher("wer das liest ist doof", 13))
    pass
