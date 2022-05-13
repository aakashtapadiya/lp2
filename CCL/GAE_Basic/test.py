import webapp2

class MainPage(webapp2.RequestHandler):
    def get(self):
        #hello world
        # self.response.write("Hello World")
        
        #name depart seat 5 times
        # name = 'xyz'
        # seat = 'ddd'
        # dept = 'Information Technology'
        # for i in range (1,6):
        #     self.response.write(name + " " + seat + " " + dept + "<br />")
        #     self.response.write(name)
        #     self.response.write(seat)
        #     self.response.write(dept)
        #     self.response.write('<br />')

        #using while loop
        # seat = 'xdd'
        # dept = 'Information Technology'
        # i=0
        # while i<10 :
        #     self.response.write("Seat No: " + seat + " Department: " + dept + "<br />")
        #     self.response.write(seat)
        #     self.response.write(dept)
        #     self.response.write('<br />')
        #     i+=1        

        #table of n
        # num = 5
        # for i in range (1,11):
        #     self.response.write(num) 
        #     self.response.write(' x ')
        #     self.response.write(i)
        #     self.response.write(' = ')
        #     self.response.write(num*i)
        #     self.response.write('<br />')

        #fibonacci1
        # a=1
        # b=1
        # for i in range(0, 10):
        #     if(i==0):
        #         self.response.out.write(0)
        #         self.response.out.write("<br>")
        #     elif(i==1 or i==2):
        #         self.response.out.write(1)
        #         self.response.out.write("<br>")
        #     else:
        #         c=a+b
        #         self.response.out.write(c)
        #         self.response.out.write("<br>")
        #         a=b
        #         b=c
        
        #fibonacci2
        # def recur_fibo(n):
        #         if n <= 1:
        #              return n
        #         else:
        #             return(recur_fibo(n-1) + recur_fibo(n-2))

        #   nterms = 8
        #   if nterms <= 0:
        #         self.response.write("Plese enter a positive integer")
        #   else:
        #         self.response.write("Fibonacci sequence:")
        #         for i in range(nterms):
        #              self.response.write(recur_fibo(i))



app = webapp2.WSGIApplication({('/', MainPage),}, debug=True)    


