lastDomain = []
print("\n......Working")
url = open('url.txt', "r", errors='ignore').readlines()
total = len(url)
v = []
print(f"Total Link: {total}")
for i in url:
    if '?' and '=' in i and i.startswith('h') and ".kr" not in i:
        try:
            currentDomain = i.split('/')[2].strip()

            if currentDomain in lastDomain:
              continue #Don't save to output file
            else:
              lastDomain.append(currentDomain)
              save = open("valid.txt", 'a')
              save.write(f"{i}")
              v.append("0")
        except:
            continue
    
    else:
        continue  

total_v = len(v)
print(f"valid link:{total_v}")
input("Finished......")
