from math import sin, cos, tan, radians

ang = float(input('Digite o angulo: '))

ang_rad = radians(ang)

s = sin(ang_rad)
c = cos(ang_rad)
t = tan(ang_rad)


print(f'O angulo digitado foi {ang:.2f}, então:\n'
      f'Seu seno é {s:.2f};\n'
      f'O Seu cosseno é {c:.2f};\n'
      f'E a sua tangênte é {t:.2f}')