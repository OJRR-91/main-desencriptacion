salida = ""
keywords={}
letras_dic={}
keymo="el veloz murciélago hindú comía feliz cardillo y kiwi cuando la cigüeña tocaba el saxofón detrás del palenque de paja"
key = "El veloz murciélago hindú comía feliz cardillo y kiwi cuando la cigüeña tocaba el saxofón detrás del palenque de paja"
#inbox = "cx kuyxnkfu úrj hcxujxqx hxlx jc qbx qj cx pdáx qj odókjlud ju hrjócx jc yjcdü árlskacxod mkuqt sdábx újckü sxlqkccd z ikík srxuqd cx skovjex pdsxóx jc nxñdúfu qjplwn qjc hxcjuérj qj hxgx qj cdn wuojcjn sdu xrpdlküxskfu qjc áxlknsxc qjc jgjlskpd qj cx uxskfu sdu jc úku qj ljsrhjlxl cx hcxüx qj cdn ukedn"
"""
inbox= "ñj céoti sóñ gúñiñ mhoéüti yñ júz \
éjpé yñ sóñoólñ jñifóé mñjñzgúéj \
ñj pkiúph w yójmñ eoéimúzmh yñ ézkz \
ñzgr mhi ói oóyh w ghoch éiúpéj \
lñzgúé gñpñohzé yñ zéifoñ w yñ ohlh \
jéz eéómñz yñ eóoúé jhz hahz yñ péj \
ñj jhlh yñ fóllúé ñj gñooúljñ jhlh \
oélúhzh xé ézhjéyh jhz éjoñyñyhoñz \
moóñj xé yñzxñmxh ghyhz jhz oñléuhz \
yñchot mhoyñohz yñchot áézghoñz \
w zhi úimhigéljñz zóz póñogñz w yéuhz \
eóñogñz méüéyhoñz éopéyhz yñ xúñoohz \
ñj cñjhü póomúvjéfh xúiyb mhpké eñjúü \
méoyújjh w qúnú móéiyh jé múfdñué ghmélé \
ñj zéíheti yñgorz yñj áéjñisóñ yñ áéaé \
eóñohi yñzgohüéyhz jhz yóohz mhjpújjhz \
yúñohi móñigé yñ jhz prz loéchz áñoohz \
mhph yñ méloúghz w yñ mhoyñoújjhz"
"""
inbox= "úhwod wáleófóe xdá iweádá ymá ñeóáñwá wáñü kdlqw \
wáleófóe úde wvwyúxd xü kdlqw wáñm wáñewxxüoü \
g ñóeóñük üuhxwá xdá üáñedá ü xd xwvdá \
wx iówkñd ow xü kdlqw íóeü wk wx lówxd g lükñü \
úhwod wáleófóe xdá iweádá ymá ñeóáñwá wáñü kdlqw \
gd xü jhóáw g ü iwlwá wxxü ñüyfóak yw jhóád \
wk xüá kdlqwá wx iwxdu yhelóaxüíd qókop ldysü \
rwxóu lüeoóxxd g bóéó lhükod xü lóítwnü ñdlüfü \
wx áüzdrck owñemá owx úüxwkjhw ow úüvü ldyd \
aáñü xü ñhiw wkñew yóá feüudá xü fwáa ñükñüá \
iwlwá füvd wx lówxd ókrókóñd \
wxxü yw jhóád ü iwlwá gd ñüyfóak xü jhwesü \
lcyd kd qüfwe üyüod áhá íeükowá dvdá róvdá"
key_list= key.split()
for i in key_list:
    keywords[key_list.index(i)+1]=len(i) #carga diccionaria
inbox_list= inbox.split()
key_index= 1
cont= 0
for i in inbox_list:
    if key_index < 21:
        if len(i)==keywords[key_index]:
            key_index+=1
        else:
            key_index=1
        cont += 1
start_position= cont - len(key_list) #posicion inicial de la llave
key1= key.replace(" ","") #cadena de la llave sin espacios
inbox_key= "".join(inbox_list[start_position:cont]) #cadena sin espacios encriptada
for i in range(0,(len(key1))):
    letras_dic[inbox_key[i]] = key1[i]
for letter in range(0,(len(inbox))):
    letra = inbox[letter]
    if chr(32) != letra:
        salida += (letras_dic[letra])
    else:
        salida += (" ")
print (salida.replace(key.lower(),' '))