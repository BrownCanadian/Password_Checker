import requests
import hashlib  



def request_api(query):
    url = 'https://api.pwnedpasswords.com/range/'+ query
    red = requests.get(url)
    # print(red)
    if red.status_code !=200:
        raise RuntimeError("ERROR, CHECK THE QUERY")
    # print(red)
    return red

def get_pass_leak(hashes, hash_to_check):
    hashes = (line.split(':') for line in hashes.text.splitlines())
    c = 0
    for h, count in hashes:
        # print("COUNT IS: ",count)
        if h == hash_to_check:
            # print('Check: ',count)
            c = count
        
    return c
    
def check_api(password):
    #check if pass exists in check_api
    
    sha1_pass = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()

    first_5 = sha1_pass[:5]
    rest = sha1_pass[5:]
    # print(first_5,rest)
    response = request_api(first_5)
    # print("LAST: ",get_pass_leak(response, rest))
    return get_pass_leak(response, rest)

def main(tupil):

    for password in tupil:
        # print(password)
        count = check_api(password)
        # print(count)
        if count :
            print("THE PASSWORD: ", password, "WAS FOUND",count, "TIMES")
        else:
            print("PASS NOT FOUND")
    return("done")




main(("kushank121600",))
