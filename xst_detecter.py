#!/usr/bin/env python3
import socket
import sys
import requests

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'

def main(argv):
    if len(argv) <= 2:
        print(f"{bcolors.OKBLUE}Usage: {argv[0]} <host> <port>{bcolors.ENDC}")
        sys.exit(0)

    target = argv[1]
    port = int(argv[2])

    print(f"\n{bcolors.OKBLUE}Target: {target}:{port}{bcolors.ENDC}\n")

    # Test for XST (Cross-Site Tracing)
    try:
        response = requests.request("TRACE", f"http://{target}:{port}", headers={"Test": "<script>alert(1);</script>"})
        if "<script>alert(1);</script>" in response.text:
            print(f"{bcolors.FAIL}+ -- --=[Vulnerable to Cross-Site Tracing!{bcolors.ENDC}")
        else:
            print(f"{bcolors.OKGREEN}+ -- --=[Not vulnerable to Cross-Site Tracing.{bcolors.ENDC}")
    except Exception as e:
        print(f"{bcolors.WARNING}+ -- --=[Error testing XST: {e}{bcolors.ENDC}")

    # Test for Host Header Injection
    try:
        response = requests.get(f"http://{target}:{port}", headers={"Host": "http://crowdshield.com"})
        if "crowdshield" in response.text.lower():
            print(f"{bcolors.FAIL}+ -- --=[Vulnerable to Host Header Injection!{bcolors.ENDC}")
        else:
            print(f"{bcolors.OKGREEN}+ -- --=[Not vulnerable to Host Header Injection.{bcolors.ENDC}")
    except Exception as e:
        print(f"{bcolors.WARNING}+ -- --=[Error testing Host Header Injection: {e}{bcolors.ENDC}")

    # Test for Clickjacking and CFS
    try:
        response = requests.get(f"http://{target}:{port}")
        if "x-frame-options" in response.headers:
            print(f"{bcolors.OKGREEN}+ -- --=[Not vulnerable to Clickjacking/CFS.{bcolors.ENDC}")
        else:
            print(f"{bcolors.FAIL}+ -- --=[Vulnerable to Clickjacking/CFS!{bcolors.ENDC}")
    except Exception as e:
        print(f"{bcolors.WARNING}+ -- --=[Error testing Clickjacking/CFS: {e}{bcolors.ENDC}")

if __name__ == '__main__':
    main(sys.argv)
