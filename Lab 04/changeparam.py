def change_param(x):
    x = "Goodbye"

x="hello"
change_param(x)
print x

#hello
#the output hello comes about because the print x command uses the variable defined
#in the main body of the script, only the varibles in the function change_param(x)
#will use the x="goodbye" and since the only line that produces out put is the
#print x in the main body the only output we see is hello.
