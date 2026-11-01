import re,os,shutil
src='proto/elisa-chambre.html';s=open(src).read()
s=s.replace('<meta name="claude:viewport-fit-sides" content="cover">\n','')
i=s.index('</style>')+len('</style>');head,body=s[:i],s[i:]
doc=('<!doctype html>\n<html lang="en">\n<head>\n<meta charset="utf-8">\n<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">\n'
     '<meta name="description" content="Good Night Elisa – a black-and-white isometric horror loop. Prototype: the bedroom.">\n'
     '<meta name="theme-color" content="#000000">\n'+head+'\n</head>\n<body>'+body+'\n</body>\n</html>\n')
os.makedirs('site/sons',exist_ok=True)
open('site/index.html','w').write(doc)
refs=set(re.findall(r'["(]((?:sons/)?[\w\-]+\.(?:webp|js|mp3|png|jpg))["\)]',doc))|{'chambre_glb.js','elisa_glb.js','sons/musique.mp3'}
for n in re.findall(r'"(\w+)"',re.search(r'const SFX_FILES=\[([^\]]+)\]',doc).group(1)): refs.add('sons/%s.mp3'%n)
for r in sorted(refs): shutil.copy('proto/'+r,'site/'+r)
open('site/.nojekyll','w').write('')
print('site ok',len(refs))
import glob
os.makedirs('site/sons/narr',exist_ok=True)
for f in glob.glob('proto/sons/narr/*.mp3'): shutil.copy(f,'site/sons/narr/')
print('narr',len(glob.glob('site/sons/narr/*.mp3')))
