import time
from sys import *
from os import *
#cry <for crypto tool>
#cal <for calculate tool>
#con <for convert tool>
#rec <for reconnaissance tool>
#sor <for sorting tool>
l = ("\n","#"*7,'Tool is Loading',"#"*7,"\n\n")
def sist():
      system('cls' if name == 'nt' else 'clear')
while True:
  def loding():
      for char in list(l):
          print(' '.join(char), end='', flush=True)
          time.sleep(1)
  def done():
        print("done!")
  def mm():
        print("""
    ====================================||
    ||==Themis, The Goddes of JUSTICE===||
    ||      ||==========================||
    ====================================||
    || Mit Trauer und Entscheidung      ||
    || im Herzen                        ||
    ====================================||
    ||      [1] Tools for Cryptography  ||
    ||      [2] Tools for Calculate     ||
    ||      [3] Tools for Convert       ||
    ||      [4] Tools for Reconnaissance||
    ||      [5] Tools for Sorting       ||
    ||                                  ||
    ||      [0] Quit                    ||
    ====================================//
                                     """)
  mm()
  l1 = input(">> ")
  l1 = int(l1)

  def t1(num):
    if num == 1:
      sist()
      loding()
      done()
      print("""\
          --Tool For Cryptography--

          [1]   DES Tools
          [2] 
          [3] 
          [4]   

          [99]  Back
          """)
      

      cry1 = input('>> ')
      cry1 = int(cry1)
      if cry1 == 99:
            return
      if cry1 == 1:
            pass
            
  def t2(num):
    if num == 2:
      sist()
      loding()
      done()
      def cal():
        print("""\
            --Tool For Calculate--

            [1] 
            [2] 
            [3] 
            [4] 

            [99] Back
            """)
      cal()
      cal1 = input('>> ')
      cal1 = int(cal1)
      if cal1 == 99:
            return
  def t3(num):
    if num == 3:
      loding()
      done()
      sist()
      cov1 = print("""\
          --Tool For Convert--

          [1]   Konversi Suhu
          [2]   
          [3]   
          [4]   

          [99]  Back
          """)
      con1 = (input('>> '))
      con1 = int(con1)
      if con1 == 99:
            return mm()
      elif con1==1:
            
            import convert.suhu_konversion as shkonv
            sh1 = input('''
[Q]uit
[B]ack
                    
>>''').lower()
            if sh1 == 'b':
                  sist()
                  return t3(num)
            elif sh1 == 'q':
                  sist()
                  exit()
      else : pass



  def t4(num):
    if num == 4:
      sist()
      loding()
      done()
      print("""\
          --Tool For Reconnaisance--

          [1]   
          [2]   
          [3]   
          [4]   

          [99]  Back
          """)
      rec1 = (input('>> '))
      rec1 = int(rec1)
      if rec1 == 99:
            sist()
            return


  def t5(num):
    if num == 5:
      sist()
      loding()
      done()
      print("""\
          --Tool For Sorting--

          [1] 
          [2] 
          [3] 
          [4] 

          [99] Back
          """)
      sor1 = input('>> ')
      sor1 = int(sor1)
      if sor1 == 99:
            sist()
            return


  def t0(num):
    if num == 0:
      sist()
      print("""\
          Bye, Have a Great Time :)
          """)
      exit()
  t1(l1)
  t2(l1)
  t3(l1)      
  t4(l1)
  t5(l1)
  t0(l1)
