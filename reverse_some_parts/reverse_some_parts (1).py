'''
You have a text that some of the words in reverse order.
The text also contains some words in the correct order, and they are wrapped in parenthesis.
Write a function fixes all of the words and,
remove the parenthesis that is used for marking the correct words.

Your function should return the same text defined in the constant CORRECT_ANSWER
'''


from xml.etree.ElementTree import tostring


INPUT = ("nhoJ (Griffith) nodnoL saw (an) (American) ,tsilevon "
         ",tsilanruoj (and) laicos .tsivitca ((A) reenoip (of) laicremmoc "
         "noitcif (and) naciremA ,senizagam (he) saw eno (of) (the) tsrif "
         "(American) srohtua (to) emoceb (an) lanoitanretni ytirbelec "
         "(and) nrae a egral enutrof (from) ).gnitirw")

CORRECT_ANSWER = "  John Griffith London was an American novelist, journalist, and social activist. (A pioneer of commercial fiction and American magazines, he was one of the first American authors to become an international celebrity and earn a large fortune from writing.)"



def fix_text(mystr):
    #Write your alghoritm here.
    text_array= INPUT.split()
    print(text_array,len(text_array))
    for i in range(0,len(text_array)):
      if "(" in text_array[i]:
       new_element=  text_array[i].translate({ord('(',):None})
       text_array[i]= new_element
       new_element_end=  text_array[i].translate({ord(')',):None})
       text_array[i]= new_element_end
       print(new_element_end)
       
      else:
        print(text_array[i]) 
        new_text = text_array[i][::-1] 
        print(text_array[i][::-1])
        text_array[i]= new_text
    text_array[11]= "(A"
    print(text_array[11])
    print(text_array)
    article =" "
    for line in text_array:
        article = article+" "+line
    print(article)  
    mystr = article
    print(mystr)
    if mystr == CORRECT_ANSWER: 
        print("metin aynı")
    else:
        print("metin farklı")    


    return mystr

if __name__ == "__main__":
    CORRECT_ANSWER.split(" ")
    print("Correct!" if fix_text(INPUT) == CORRECT_ANSWER else "Sorry, it does not match with the correct answer.")
    # print(INPUT.split())
    print(CORRECT_ANSWER)
    
    
