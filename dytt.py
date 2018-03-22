#-*-coding:utf-8-*-
import re
import requests
import time
def dytt():
        ff=open('E:\\PYTOHN\\worm\\爬电影天堂\\dy_ftp.txt','w')
        target_url1='http://www.ygdy8.net/html/gndy/dyzz/index.html'
        target_result=requests.get(target_url1)
        target_result.encoding='gb18030'
        k=300
        for i in range(1,100):
                target_url2='http://www.ygdy8.net/html/gndy/dyzz/list_23_'+str(i)+'.html'
                target_result2=requests.get(target_url2)
                target_result2.encoding='gb18030'
                target_list=re.findall('<a href="(.*?)" class="ulink">',target_result2.text)
                for j in target_list:
                        #print (j+'/n')
                        target_url3='http://www.ygdy8.net/'+j
                        target_result3=requests.get(target_url3)
                        target_result3.encoding='gb18030'
                        #target_find=re.findall('<a href="#" target="_self" thunderpid="21319" thundertype="" thunderrestitle="(.*?)"',target_result3.text)
                        target_find=re.findall('<td style="WORD-WRAP: break-word" bgcolor="#fdfddf"><a href="(.*?)">ftp://ygdy8:ygdy8.*?</a></td>',target_result3.text) 
                         
                        ff.write(target_find[0]+'\n')
                        time.sleep(2)
                        print(k)
                        k=k-1
                        if (k==0):
                                break
                if (k==0):
                        break
dytt()