import sys 

ev_file = open("example_vec.txt", "w")

date = sys.argv[0]

ev_file.write("#!/bin/csh \n")

ev_file.write("set dir = ./test/ \n")
ev_file.write("set dhir = /Users/brownscholar/Desktop/BridgeUp_Year2/atlantic-data/dh:geo/\n")
ev_file.write("set dendir = /Users/brownscholar/Desktop/BridgeUp_Year2/atlantic-data/density/ \n")
ev_file.write("set auxdir = /Users/brownscholar/Desktop/BridgeUp_Year2/atlantic-data/aux/ \n")
ev_file.write("set outdir = /Users/brownscholar/Desktop/BridgeUp_Year2/atlantic-data/omega/ \n")
ev_file.write("set fileinfo = {$dir}info_pr.dat \n")
ev_file.write("set filedh =  {$dhdir}/dh_" + str(date) + ".gr \n")
ev_file.write("set filest =  {$dendir}/density_" + str(date) + ".gr \n")
ev_file.write("set filestm = {$auxdir}/st0/" + str(date) + "_st0.dat\n")
ev_file.write("set filequ =  {$outdir}/u/" + str(date) + "_qu.gr\n")
ev_file.write("set fileqv =  {$outdir}/v/" + str(date) + "_qv.gr\n")
ev_file.write("set fileqdi = {$auxdir}/qdi/" + str(date) + "_qdi.gr\n")

ev_file.write("./vectorq.exe << !\n")
ev_file.write("'$fileinfo'	#>>>>>Escribe info file info.dat:\n")
ev_file.write("'$filedh'	#>>>>>Escribe fichero de altura Dinamica:\n")
ev_file.write("'$filest'	#>>>>>Escribe fichero de densidad:\n")
ev_file.write("'$filestm'	#>>>>>Escribe fichero de densidad promedio:\n") 
ev_file.write("'$filequ'	#>>>>>Escribe fichero Qu:\n")
ev_file.write("'$fileqv'	#>>>>>Escribe fichero Qv:\n")
ev_file.write("'$fileqdi'	#>>>>>Escribe fichero Qdi:\n")

ev_file.close()
