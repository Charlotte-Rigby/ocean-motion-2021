import sys 

date = sys.argv[1]

eo_file = open("example_ome.txt", "w")

eo_file.write("#!/bin/csh\n")

eo_file.write("set dir = ./test/\n")
eo_file.write("set fileinfo = {$dir}info_pr.dat\n")
eo_file.write("set outdir = /Users/brownscholar/Desktop/BridgeUp_Year2/atlantic-data/omega/\n")
eo_file.write("set auxdir = /Users/brownscholar/Desktop/BridgeUp_Year2/atlantic-data/aux/\n") 
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