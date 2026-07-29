m = float(input('Digite um valor '))
cm = m * 100 #como converter metro para centimetro.
mm = m * 1000 #como converter metro para milimetro.
km = m / 1000 #como converter para quilometro.
hm = m / 100 #como converter para hectômetro.
dam = m / 10 #como converter para decâmetro.

print(f'{km:.2f}km, {hm:.2f}hm, {dam:.2f}dam, {m:.2f}m, {cm:.2f}cm, {mm:.2f}mm')
