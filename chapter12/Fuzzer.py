import sys
import subprocess

diction = "abcdefghijklmnopqrstuvwxyz"
count = 0

        
def run_(cmd, ans):
    global count
    result = subprocess.call(cmd, stdout=subprocess.PIPE)
    if(result == 1 ):
        count = count + 1
        print("########TestCase%d#########" % count)
        print("Input :  %s" % ans)
        print("Result : FAILED!\n")
        return 1
    else:
        count = count + 1
        print("########TestCase%d#########" % count)
        print("Input :  %s" % ans)
        print("Result : SUCCESS!\n")
        return 0
        

        
def main():
    
    for i in list(diction):
        for j in list(diction):
            k=i+j
            ans= ''.join(k)
            if(run_("PATH FOR \\LetsFuzz.exe %s"% ans, ans)==0): #LetsFuzz file location
                return 0

main()
