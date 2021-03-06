########################## This file is part of BimaNLP. ############################
"""
    BimaNLP
    ~~~~~

    Is an open source Python library for Natural Language Processing aimed
    mainly for Indonesian Language.

    This library has dependency with another really great open source library such:
        > Sklearn v0.16.0(http://scikit-learn.org/stable/)
        > NLTK 3.0(http://www.nltk.org/)
        > NumPy v1.9(http://www.numpy.org/)
        > SciPy(http://www.scipy.org/)

    Copyright (C) 2015 by Aulia Normansyah a.k.a drr3d and other contributors.
    
    :license: GNU General Public License (GPL) 2.0,
              visit http://www.gnu.org/licenses/gpl-2.0.html for more details.
"""

from numpy import exp

from langutil.tokenizer import tokenize
from langutil.stemmer import ChaosStemmer
from langutil.tagger.sequentigram import NGramTag
from langutil.chunker.chunk import TagChunker
from langmodel.modeler.markov import NGramModels
from utils.loader import Loader

import langmodel.ngram as ngram

def TextTokenizer(sen):
    # Materi Syntatic proses:text tokenizing
    # http://blog.pantaw.com/syntatic-proses-text-tokenizing/
    stopwords= ['kah','lah','pun','jah','jeh','mu','ku','ke','di','tapi','saya','kamu','mereka','dia', \
          'kita','adalah','dan','jika','kalau','sama','yang', \
          'sekarang','nanti','besok','kemarin','kemaren','nya','na',\
          'at','apa','ini','itu','juga','ketika','namun',\
          'sebab','oleh','malah','memang']
        
    tok = tokenize()
    kata = tok.WordTokenize(sen,removepunct=False)
    if kata:
        print "kalimat setelah di tokenize: ", kata, "\n"
    return kata

def NgramModel(sen):
    # Materi Syntatic proses:N-Gram
    # http://blog.pantaw.com/syntatic-proses-n-grams/
    kata = TextTokenizer(sen)
    kata = ngram.ngrams(kata,n=2,njump=3)
    
    print "Jumlah sample: ", len(kata)
    for z in kata:
        print ' '.join(z)
    print "\n"

def stemm(toksen):
    # Materi Syntatic proses: Text Stemmer bahasa Indonesia dengan Python
    # http://blog.pantaw.com/syntatic-proses-text-stemmer-bahasa-indonesia-dengan-python/
    morph = ChaosStemmer('C:\\BimaNLP\\dataset\\', 'tb_katadasar.txt')
    
    for z in words:
        morph.stemm(z)
        #menyeimbangkan,menyerukan,mengatakan,berkelanjutan,pembelajaran,pengepulannya
        #print "Dirty guess word is: ",morph.getFoundGuessWord()
        #print "Detected Affix is: ", morph.getFoundSuffix(),"\n"
        print "Root kata untuk kata: ", z ," -> adalah: ", morph.getRootWord()
        print "Filtered guess word adalah:", morph.getFilteredGuessWord(),"\n"

def chunk(sent):
    # Proses chunking harus selalu didahuli dengan proses tagging text
    tagger = NGramTag('C:\\BimaNLP\\dataset\\',r'tb_tagged_katadasar.txt')
    chunk = TagChunker()

    print chunk.treePrint(chunk.tagChunk(tagger.tag(sent)))
    #print chunk.tagTokenExtractor(tagger.tag(sent))
    #print chunk.tagChunk(tagger.tag(sent))
    #print chunk.tagTokenizer(chunk.tagChunk(tagger.tag(sent)))

    #tagger.tag(sent,tagregex=True)
    #print tagger.tag(sent)

    # Delete specific tag
    #print delTag(sent,'XX')
    
    # Ekstrak specific tag
    print chunk.treeExtractor(chunk.tagChunk(tagger.tag(sent)),lambda t: t.label() == 'PRED')
    
def NGramLangModel():
    cl = Loader('C:\\BimaNLP\\dataset\\')
    f = cl.loadLarge('test_kota.txt',lazy_load=True)#tb_berita_onlinemedia, tb_kota_bywiki
    w = cl.processRaw(f,to_lower=True)
    r = cl.rawForLangmodel(w,punct_remove=True,to_token=True)
                           
    dataset=[['saya','suka','kamu'],
         ['kamu','suka','saya'],
         ['saya','tidak','suka','jika','kamu','pergi','dengan','dia']
         ]

    
    lms = NGramModels(ngram=2)
    # njump parameter belum bisa digunakan untuk modkn optimizer
    models = lms.train(dataset, optimizer='modkn',\
                       separate=False, njump=0, verbose=True)

    print "##########################################################"
    
if __name__ == "__main__":
    kata1 = 'memakan nasi goreng dipinggir empang, memang !! sungguh  nikmat sekali.'
    kata2 = 'penghasilannya hanya cukup untuk memenuhi keseluruhan kebutuhan kedua buah hati kesayangannya'
    kata3 = 'ketiga burung kecil itu saling siul-menyiul bersahut-sahutan di pagi hari'
    kata4 = "harganya"
    kata5 = "rancangan busana dan aksesori dari perancang muda indonesia ternyata diperhitungkan di tingkat internasional"

    ## Stemming hanya membutuhkan textTokenize
    #words = TextTokenizer(kata4.lower())
    #stemm(words)

    #NgramModel(kata1.lower())
    #NGramLangModel()

    chunk(kata5)
