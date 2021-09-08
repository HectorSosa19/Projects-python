#Hector Jose Sosa Castro ,Matricula:2019-7889
import matplotlib.pyplot as plt 
fig=plt.figure()
ax=fig.add_subplot(111)
programas=['Python','Java','Java Script','C#','PHP']
estadisticas=[10,9,8,7,6]
grafica=range(1,len(estadisticas)+1)
ax.bar(grafica,estadisticas,width=0.5,color="Blue")
ax.set_xticks(grafica)
ax.set_xticklabels(programas)
ax.set_ylabel('Estadisticas de programas')
plt.show()