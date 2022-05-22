#!/usr/bin/env python3                                                                                                                                 
from urllib.parse import urlparse                                                               
from urllib.parse import parse_qs                                                                                                               
import requests                                                                                                                      
import argparse                                                                                                                      
import sys                                                                                                                                             
import os                                                                                                                                  
                                                                                                                                                       
GETPARAMS = []                                                                                                                                         

def prepareUrls(args, urlFile):
    PREPARED = []
    KNOWN = []
    INPUT_URLS = []

    # Get urls from a file
    if(args.file):
        if(os.path.exists(urlFile)):
            with open(urlFile, "r") as inputFile:
                lines = inputFile.readlines()
                for line in lines:
                    line = line.replace("\n", "")
                    INPUT_URLS.append(line)
        else:
            print("[!] Provided file '" + args.f + "' doesn't exist. Exiting...")
            sys.exit(-1)

    else:
        #Get urls from stdin
        for line in sys.stdin.readlines():
            INPUT_URLS.append(line)

    # Filter duplicate urls with same parameters
    for url in INPUT_URLS:
        u = urlparse(url)
        query = parse_qs(u.query)
        
        keys = []
        values = []
        for k,v in query.items():
            keys.append(k)
            if("".join(k) not in GETPARAMS):
                GETPARAMS.append("".join(k))

            values.append("".join(v))

        unique = "".join(keys)
        exists = False
        for i in range(len(KNOWN)):
            if(unique == KNOWN[i]):
                exists = True
        if(not exists):
            KNOWN.append(unique)
            #Recreate modified url with keyword
            scheme = u.scheme
            creds = u.netloc
            path = u.path
            q = query
            
            recreated = ""
            recreated += scheme
            recreated += "://"
            recreated += creds
            recreated += path
            
            
            c = 0
            for k, v in zip(keys, values):
                if(c == 0): recreated += "?"
                else: recreated += "&"
                recreated += "".join(k)
                recreated += "="
                recreated += args.param_name

            PREPARED.append(recreated.replace("\n", ""))
    return PREPARED


def main():
    
    parser = argparse.ArgumentParser(description="URL data parser/helper tool", add_help = False)
    parser.add_argument("-f", metavar="<FILE>", dest="file", help="\t\t Specify file with URLs.")
    parser.add_argument("-p", metavar= "<PARAM>", dest="param_name", help="\t\t Specify placeholder parameter value.")
    parser.add_argument("-g", "--getvals", action="store_true", dest="getvals", help="\t\t Print all unique GET parameters.")
    parser.add_argument("-u", "--unique", action="store_true", dest="unique", help="\t\t Print only unique URLs.")
    parser.add_argument("-h", "--help", action="help", default=argparse.SUPPRESS, help="\t\t Print this help menu.")

    args = parser.parse_args()

    # Command line options check
    if(not args.getvals and not args.unique):
        print("Error. Specify at least 'g' or 'u' parameters. Exiting...")
        sys.exit(-1)
    if(not args.param_name):
        args.param_name = "PWN"
    
    # Parse data
    preparedList = prepareUrls(args, args.file)
    
    
    # Print URLS + unique GET parameters
    if(args.unique):
        if(preparedList):
            for item in preparedList:
                print(item)
    
    if(args.getvals):
        for p in GETPARAMS:
            print(p)


if(__name__ == "__main__"):
    main()

