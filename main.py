import SPRT_functions as SPRT


term1=SPRT.PRT(model='5685',numer='1114')
term2=SPRT.PRT(model='aaa')

term1.metoda1()
term2.metoda1()

term1.R0=102

print(term1.R0)