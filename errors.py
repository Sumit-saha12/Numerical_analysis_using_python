

#RELATIVE_ERROR
#RELATIVE_PERCENTAGE_ERROR
#ABSOLUTE ERROR

def absolute_error(Vt,Va):
  Ea = abs(Vt-Va)
  print('ABSOLUTE ERROR IS =',Ea)


def relative_error(Vt,Va):
  Er = (abs(Vt-Va))/Vt
  print('RELATIVE ERROR IS =',Er)


def relative_percentage_error(Vt,Va):
  Ep = ((abs(Vt-Va))/Vt)*100
  print('RELATIVE PERCENTAGE ERROR IS =',Ep)



Vt=float(input('ENTER TRUE VALUE: '))
Va=float(input('ENTER APPROXIMATE VALUE: '))

absolute_error(Vt,Va)
relative_error(Vt,Va)
relative_percentage_error(Vt,Va)