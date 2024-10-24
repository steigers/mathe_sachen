einser = ['null', 'ein', 'zwei', 'drei', 'vier', 'fünf', 'sechs', 'sieben', 'acht', 'neun']
zig = ['null', 'zehn', 'zwanzig', 'dreissig', 'vierzig', 'fünfzig', 'sechzig', 'siebzig', 'achtzig', 'neunzig']
zehn_bis_neunzehn = ['zehn', 'elf', 'zwölf', 'dreizehn', 'vierzehn', 'fünfzehn', 'sechzehn', 'siebzehn', 'achtzehn', 'neunzehn']

null_bis_999 = []  # Eine Liste von null bis neun-hundert-neun-und-neunzig
for h in range(0, 10):  # Hunderter
  for z in range(0, 10):  # Zehner
    for e in range(0, 10):  # Einser
      if z == 0:
          zehner = einser[e]
      elif z == 1:
          zehner = zehn_bis_neunzehn[e]
      else:
          if e == 0:
              zehner = zig[z]
          else:
              zehner = einser[e] + '-und-' + zig[z]
      if h == 0:
          zahl = zehner
      else:
          zahl = einser[h] + '-hundert-und-' + zehner
      null_bis_999.append(zahl)
# print(str(null_bis_999))

alles = []  # Eine Liste von null bis neun-hundert-neun-und-neunzig-tausend-neun-hundert-neun-und-neunzig
for t in range(0, 1000):  # Tausender
   for i in range(0, 1000):
      if t == 0:
          alles.append(null_bis_999[i])
      else:
          alles.append(null_bis_999[t] + '-tausend-' + null_bis_999[i])

# print(str(resultat[12000:12020]))
resultat = sorted(alles)
print(str(resultat[:5]))
print(str(resultat[-5:]))
