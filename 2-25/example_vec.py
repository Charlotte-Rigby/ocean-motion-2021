import sys 

date = sys.argv[1]

ev_file = open("vectorq.exec", "w")

ev_file.write("#!/bin/csh" + "\n")

ev_file.write("set dir = ./test/" + "\n")
ev_file.write("set dhdir = /Users/brownscholar/Desktop/BridgeUp_Year2/atlantic-data/geo" + "\n")
ev_file.write("set dendir = /Users/brownscholar/Desktop/BridgeUp_Year2/atlantic-data/density"+ "\n")
ev_file.write("set auxdir = /Users/brownscholar/Desktop/BridgeUp_Year2/atlantic-data/aux"+ "\n")
ev_file.write("set outdir = /Users/brownscholar/Desktop/BridgeUp_Year2/atlantic-data/omega"+ "\n")
ev_file.write("set fileinfo = {$dir}info_pr.dat" + "\n")
ev_file.write("set filedh =  {$dhdir}/geo" + date + ".gr" + "\n")
ev_file.write("set filest =  {$dendir}/density" + date + ".gr" + "\n")
ev_file.write("set filestm = {$auxdir}/st0/" + date + "_st0.dat\n")
ev_file.write("set filequ =  {$outdir}/u/" + date + "_qu.gr\n")
ev_file.write("set fileqv =  {$outdir}/v/" + date + "_qv.gr\n")
ev_file.write("set fileqdi = {$auxdir}/qdi/" + date + "_qdi.gr\n")

ev_file.write("./vectorq.exe << !\n")
ev_file.write("'$fileinfo'	#>>>>>Escribe info file info.dat:\n")
ev_file.write("'$filedh'	#>>>>>Escribe fichero de altura Dinamica:\n")
ev_file.write("'$filest'	#>>>>>Escribe fichero de densidad:\n")
ev_file.write("'$filestm'	#>>>>>Escribe fichero de densidad promedio:\n") 
ev_file.write("'$filequ'	#>>>>>Escribe fichero Qu:\n")
ev_file.write("'$fileqv'	#>>>>>Escribe fichero Qv:\n")
ev_file.write("'$fileqdi'	#>>>>>Escribe fichero Qdi:\n")

ev_file.close()

eo_file = open("omegeainv.exec", "w")

eo_file.write("#!/bin/csh\n")

eo_file.write("set dir = ./test/\n")
eo_file.write("set fileinfo = {$dir}info_pr.dat\n")
eo_file.write("set outdir = /Users/brownscholar/Desktop/BridgeUp_Year2/atlantic-data/omega\n")
eo_file.write("set auxdir = /Users/brownscholar/Desktop/BridgeUp_Year2/atlantic-data/aux\n") 
eo_file.write("set filestm = {$auxdir}/st0/" + date + "_st0.dat\n")
eo_file.write("set fileqdi = {$auxdir}/qdi/" + date + "_qdi.gr\n")
eo_file.write("set filew =  {$outdir}w/" + date + "_ww.gr\n")

eo_file.write("./omegainv.exe << !\n")
eo_file.write("'$fileinfo' 	#>>>>>Escribe info file info.dat:\n")
eo_file.write("'$fileqdi' 	#>>>>>Escribe fichero de Div Q:\n")
eo_file.write("'$filestm'   	#>>>>>Escribe fichero de densidad promedio:\n")
eo_file.write("'ominput.dat'  #>>>>>Escribe fichero parametros (ominput.dat):\n")
eo_file.write("'$filew'	#>>>>>Escribe fichero Salida W:\n")

eo_file.close()
