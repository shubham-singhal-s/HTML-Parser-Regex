import re
string = ''
for _ in range(int(input())):
    string+=input()

string = re.sub('(<!--.*?-->)','',string,flags = re.MULTILINE|re.DOTALL)
xi = re.finditer(r'(?P<emp>(?<=\<)([^\>])+(?= \/\>))|(?P<start>(?<=\<)[^\/]([^\>])*(?! \/>))|(?P<end>(?<=\<\/)([^\>])+(?=\>))',string)
for x in xi:
    if x.group('start')!=None:
        print('{0: <6}'.format('Start')+':',x.group('start').split()[0])
        jj = ' '.join(x.group('start').split()[1:])
        for i in re.finditer(r'[\'\"]?\s?(?P<tag>[^\'\"\s]+)=[\'\"](?P<val>[^\'\"]+)|[\'\"]?\s?(?P<tag_emp>.+)(?!=)\s',jj):
            if i.group('tag') and i.group('tag')!='"'and i.group('tag')!="'":
                print('-> '+i.group('tag')+' > '+str(i.group('val')))
            if i.group('tag_emp'):
                print('-> '+i.group('tag_emp')+' > None')

        #print('Start :',x[1].split()[0])
    if x.group('end')!=None:
        print('{0: <6}'.format('End')+':',x.group('end'))
    if x.group('emp')!=None:
        print('{0: <6}'.format('Empty')+':',x.group('emp').split()[0])
        jj = ' '.join(x.group('emp').split()[1:])
        for i in re.finditer(r'[\'\"]?\s?(?P<tag>[^\'\"\s]+)=[\'\"](?P<val>[^\'\"]+)|[\'\"]?\s?(?P<tag_emp>.+)(?!=)\s',jj):
            if i.group('tag') and i.group('tag')!='"'and i.group('tag')!="'":
                print('-> '+i.group('tag')+' > '+str(i.group('val')))
            if i.group('tag_emp') and i.group('tag_emp')!='"'and i.group('tag_emp')!="'":
                print('-> '+i.group('tag_emp')+' > None')
