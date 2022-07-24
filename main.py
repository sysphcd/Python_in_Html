from datetime import datetime
from plot_demo import plot_sin



time = datetime.now()
pyscript.write('time',time.strftime("%H : %M : %S") )

pyscript.write('plot', plot_sin())