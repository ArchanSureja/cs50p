# input : any kind of string with :) and :( 
# output : string replace with actual emoji 

string = input()
string = string.replace(':)', '😊').replace(':(','😞')
print(string)