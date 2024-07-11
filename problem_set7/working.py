import re
import sys 

def main():
     print(convert(input("Hours: ")))

def convert(s):
    pattern = r'\b(\d{1,2}:\d{2})\s*[ap]m\b'
    match = re.findall(pattern, s)
    print(match)
    pattern_1 = r'[ap]m'
    match_1 = re.findall(pattern_1,s)
    print
    string = ""
    for i in range(len(match)-1):
                print(match[i],match_1[i])
                hour , mins = match[i].split(":")
                if int(mins)>59 or int(hour)>12:
                    raise ValueError
                    sys.exit(1)
                elif match_1[i] == "pm" or match_1[i] == "PM":
                    hour = (int(hour)+12) % 24
                    if i==len(match)-1:
                        string += f"{hour}:{mins}"
                        print("in pm part without to")
                    else:
                        string += f"{hour}:{mins} to "
                        print("in pm part with to")
                else:
                    if i==len(match)-1:
                        string += f"{hour}:{mins}"
                        print("in am part without to")
                    else:
                        string += f"{hour}:{mins} to "
                        print("in am part with to")             
    return string
   



        
    

     



if __name__ == "__main__":
    main()