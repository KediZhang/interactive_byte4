import csv

def lang_csv ():
    #lang_pair = {}
    lang_list = ["zh","pt","uk","sr","fa","ca","ar","no","sh","fi","hu","id","ko","cs","ro","ms","tr","eu","eo","bg","hy","da","zh-min-nan","sk","he","min","kk","hr","lt","et","ce","sl","be","gl","er","ur","nn","az","simple","uz","la","hi","th","ka","vo","ta","cy"]
    #lang_list = ["en","ceb","sv","de","fr","nl","ru","it","es","pl","war","vi","ja"]
    with open('relation2.txt','r') as f:
        count = 1
        lang_pair = {}
        for line in f:
            newline = line[2:]
            newline = newline[:-3]
            array = newline.split("', '")
            #print (array)
            for i in range(len(array)):
                #if array[i] in lang_list:
                    for j in range(i+1,len(array)):
                    #for j in range(len(array)-1):
                        #if array[i] in lang_list and array[j+1] in lang_list:
                        if array[j] in lang_list:
                            keyname = array[i]+","+array[j]
                            if keyname in lang_pair.keys():
                                lang_pair[keyname] += 1
                                #print(lang_pair[keyname])
                            else:
                                lang_pair[keyname] = 1
            print (str(count) + "articles")
            count +=1
    with open('lang_all.csv','w') as csvfile:
        for key, value in lang_pair.items():
            csvfile.write(key+","+str(value))
            csvfile.write('\n')
        csvfile.close

lang_csv()
