lastDomain = []
print("\n......Working")
url = open('url.txt', "r", errors='ignore').readlines()
for i in url:
    if '?' and '=' in i and i.startswith('h'):
        try:
            currentDomain = i.split('/')[2].strip()

            if currentDomain in lastDomain:
              continue #Don't save to output file
            else:
              lastDomain.append(currentDomain)
              save = open("valid.txt", 'a')
              save.write(f"{i}")
        except:
            continue
    
    else:
        continue  

input("Finished......")
