#!/usr/bin/python3
#coder: kodo no kami
#obs: o recomendado é pegar a url da area "videos" do canal, no caso os videos vão estar
#     em ordem descrescente do ultimo para o primeiro

from urllib.request import urlopen,Request
import re
import numpy as np
import matplotlib.pyplot as mpl
import sys

canal = sys.argv[1]
useragent = "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0"

resposta = urlopen(Request(canal,headers={"User-Agent": useragent})).read()

filtrado = re.findall(r',"title":{"accessibility":{"accessibilityData":{"label":"(.*?)"}}',resposta.decode(),re.DOTALL)

views_array = []

for separado in filtrado:	
	views = re.match(r".*\ ([\d\.]+)\ visualiza",separado)
	num = re.sub(r"\.","",views.group(1))
	views_array.insert(0,int(num))

views_array_n = np.array(views_array)
fs = np.linspace(0,1,len(views_array_n))

print("\n\nviews: {}".format(views_array_n))

mediana = np.mean(views_array_n)
maximo = views_array_n.max()
minimo = views_array_n.min()

mpl.figure()
mpl.subplot(2,1,1)
mpl.title("VIEWS YOUTUBE")
mpl.plot(fs,views_array_n,"-o")
mpl.subplot(2,1,2)
mpl.axis("off")
mpl.text(0.02,0.8,"quantidade analisada: {}".format(len(views_array_n)))
mpl.text(0.02,0.6,"views maxima: {}".format(maximo))
mpl.text(0.02,0.4,"views minima: {}".format(minimo))
mpl.text(0.02,0.2,"views mediana: {}".format(int(mediana)))
mpl.show()

