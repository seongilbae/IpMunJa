file_loc = "C:\\Windows\\System32\\drivers\\etc\\hosts"

f = open(file_loc,"w")
f.seek(0,2)
f.write("125.209.222.142       www.google.com")
f.close()
