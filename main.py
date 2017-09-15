import os
import argparse
import down
import keyword
parser=argparse.ArgumentParser()
parser.add_argument("-m",action="store",dest="mode",type=str,help="select id to download papers by arxiv id, keyword to search papers by keywords")
parser.add_argument("-n",action="store",dest="id",type=str,help="this is the argument of arxiv id")
parser.add_argument("-w",action="store",dest="kwyword",type=str,help="this is the argument of keywords, please connected with plus symbol(+)")
result=parser.parse_args()
if result.mode=="id":
    down.paperDown(result.id)
elif result.mode=="keyword":
    keywords=result.keyword.split("+")
    keyword.paperSearch(keywords)
else:
    print("Eriri: Insupportable mode")
