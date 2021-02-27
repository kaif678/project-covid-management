import matplotlib.pyplot as plt
import pandas as pd 
import numpy as np

def main_menu():
       print("*****************")
       print("Read Data From File in Different Way") 
       print("I. Read complete csv file") 
       print ( " 2 . Reading complete file without index" ) 
       print("====================")
       print ( "Data VIsualIzatIon" ) 
       print (" 3. Line Chart" ) 
       print (" 4 . Bar Plot" ) 
       print ( " 5 . Pie chart" ) 
       print (" 6. Scatter chart" ) 
       print("====================")
       print("Apply Data Manipulation in the records of CSV file") 
       print("7. Sorting the data as per your choice") 
       print("8. Read Top and Bottom Records from file as per requirement") 
       print("9. Make the copy of CSV file")
       print("10. Read  the specific columns")
       print("*****************")
       
main_menu()

def ReadCSV ( ) : 
       print("Reading Data from CSV file") 
       df=pd.read_csv("/Internal storage/Android/covid19.csv") 
       print (df)
       
def no_index(): 
        print('Reading Data fran CSV elle without Index value ') 
        df=pd . readcsv ("/Internal storage/Android/covid19.csv" , index_col=0) 
        print(df) 

def new_column_name(): 
       print('Adding new column name to existing Data') 
       df=pd.read_csv("/Internal storage/Android/covid19.csv" ,index_col=0 , skiprows=1,names=["State Name,Total"])
       print (df) 
def line_plot( ) : 
       df.readcsv ( "/Internal storage/Android/covid19.csv") 
       st=df['State'] 
       cnf=df['Confirmed']
       rc=df['Recovered'] 
       dth=df['Deaths']
       ac=df['Active']
       
       print("Select Specific Line Chai:t as given below:") 
       pi:lnt("press I to print the data for State vs Confirmed Cases") 
       print("press 2 to print the data for State vs Recovered Cases") 
       print("press 3 to print the data for State vs Death Cases") 
       print("press 4 to print the data for State vs Active Cases") 
       print("press 5 to merge all the data i.n one Line chart") 

op=int(input('Enter your choice:'))

if op==1: 
      plt.ylabel ( " Confirmed cases " ) 
      plt.title (" State wise Confirmed Cases" ) 
      plt.plot (st , cnf) 
      plt.show() 
               
elif op==2 : 
        plt.ylabel( " Recovered cases " ) 
        plt.title(" State wise Recovered Cases" ) 
        plt.plot( st ,rc) 
        plt.show() 
               
elif op==3: 
        plt.ylabel ( " Death cases " )
        plt.title("State wise Death Cases")
        plt.plot (st ,dth) 
        plt.show() 

elif op==4: 
        plt.ylabel("Active cases") 
        plt. title (" State wise Acts.ve Cases" ) 
        plt .plot (st , ac) 
        plt.show() 
elif op==5 : 
        plt . ylabel ( " Number of cases " )
        plt .plot (st ,cnf , label=" State wise Conflrined Cases " )
        plt .plot (st ,rc, label=" State wise Recovered Cases" ) 
        plt .plot ( st , dth , label=" State wise Death" ) 
        plt . plot ( st , ac , label= " State wise Active Cases " ) 
        plt .legend ( ) 
        plt.show()

else: 
       print("Enter valid input")
              
def bar_plot ( ) : 
       df=pd.read_csv("/Internal storage/Android/covid19.csv") 
       st=df['State'] 
       cnf=df [' Confirmed ' ] 
       rc=df [' Recovered ' ] 
       dth=df ['Death'] 
       ac=df['Active']
       plt.xlabel("state") 
       plt . xticks(rotations= ' vertical' )
       print("Select Specific Bar Chart as given below:") 
       print("press 1 to print the data for State vs Confirmed Cases")
       print("press 2 to pi:int the data for State vs Recovered Cases") 
       print("phelps 3 to print the data for State vs Death") 
       print("press 4 to print the data for State vs Acts.ve Cases") 
       print("press 5 to print all the data in finn of stack bar chart") 
       print("press 6 to print all the data i.n four of multi bar chart") 

op=int (input ("Enter your choice : " ) ) 
if op==1: 
       plt . ylabel ( " Confirmed cases " ) 
       plt. title (" State wise Confirmed Cases" )
       plt . bar(st , cnf)
       plt.show()     

elif op==2 : 
         plt . ylabel ( " Recovered cases " )
         plt . title ( " State wise Recovered Cases " ) 
         plt . bar(st, rc)
         plt.show()
             
elif op==3 : 
         plt.ylabel("Death cases") 
         plt . ti.tle ( " State wise Death Cases" ) 
         plt . bar (st ,dth) 
         plt.show()
         
elif op==4 : 
         plt .ylabel ( "Active cases" ) 
         plt. title (" State wise Active Cases" ) 
         plt . bar (st , ac) 
         plt.show()
elif op==5:
         plt . ylabel ( "Number of cases" ) 
         plt .plot (st , cnf , label=" State wise Conflated Cases" ) 
         plt .plot ( st , rc , label=" State wise Recovered Cases" ) 
         plt .plot (st ,dth , label=" State wise Death" ) 
         plt .plot (st , ac , label=" State wise Acts.ve Cases" ) 
         plt .legend ( ) 
         plt.show()

else: 
       print ("Enter valid input" )    
              
def  bar_plot():
	    df=pd.read_csv("/Internal storage/Android/covid19.csv"    ) 
	    st=df[ 'State '] 
	    cnf=df [' Confirmed']
	    rc=df[' Recovered ' ] 
	    dth=df['Deaths ' ] 
	    ac=df[' Active']
	    plt . xlabel("state" ) 
	    plt . xticks (rotations= ' vertical ' ) 
	    
	    print("Select Specific Bar Chart as given below:") 
	    print("press I to print the data for State vs Confirmed Cases") 
	    print("press 2 to print the data for State vs Recovered Cases") 
	    print("press 3 to print the data for State vs Death") 
	    print("press 4 to print the data for State vs Active Cases") 
	    print("press 5 to print all the data in finn of stack bar chart") 
	    print("press 6 to print all the data in form of multi bar chart") 

op=int (input ("Enter: your choi.ce : " ) )  
if op==1:
            plt . ylabel ( " Confirmed cases " ) 
            plt . title ( " State wise Confirmed Cases" ) 
            plt.bar (st,cnf) 
            plt.show()
            
elif op==2 : 
              plt . ylabel ( " Recovered cases " ) 
              plt. title (" State wise Recovered Cases" ) 
              plt .bar(st, rc) 
              plt.show()

elif op==3: 
              plt.ylabel("Death cases") 
              plt . title (" State wise Death Cases" ) 
              plt . bar (st ,dth) 
              plt. show ( )
              
elif op==4 : 
              plt .ylabel ( "Active cases" ) 
              plt. ti.tle (" State wise Active Cases" ) 
              plt.bar(st,ac) 
       
elif op==5: 
              plt.bar(st,cnf,width=0.2,label="Statewise Confirmed  Cases") 
              plt . bar ( st , rc , width=0.2 , label=" State wise Recovered Cases " ) 
              plt . bar (st ,dth ,width=0.2 , label=" State wise Death" ) 
              plt.bar(st,ac,width=0.2,label="State wise Active Cases") 
              plt .legend ( ) 
              plt.show()

elif op==6:
         ind:np . arange (len ( st ) ) 
         width=0.25 
         plt .bar (ind,cnf ,width , label=" State wise Confirmed Cases" ) 
         plt . bar ( ind+0.25 , rc ,width , label= " State wise Recovered Cases " ) 
         plt . bar ( ind+0.50 , dth ,width , label=" State wise Death" )
         plt . bar (ind+0.75 , ac ,width , label=" State wi.se Active Cases" ) 
         plt .legend ( )
         plt. show ( ) 

else : 
       print("Enter valid input") 
                          
       
def pie_plot():
         sc=df['State']  
         cnf=df [' Confirmed ' ] 
         rc=df [' Recovered ' ] 
         dth=df ['Deaths '] 
         ac=df['Active']

print("Select Specific Pie Chart as given below:") 
print("press I to print the data for State vs Confirmed Cases") 
print("press 2 to print the data for State vs Recovered Cases") 
print('press 3 to print the data for State vs Death') 
print("press 4 to print the data for State vs Active Cases") 

op=int (input ( "Enter your choice : " ) )
          
if op==1:  
             plt. title (" State wise Confirmed Cases" )
             plt .pie (cnf , label= st,autopct=" %3d%%" ) 
#autopct attribute can be used to show the percentage of the data. 
             plt.show()

elif op==2:
                plt.pie(rc,label=st,autopct="%3d%%") 
                plt.title("State wise Recovered Cases")
                plt.bar(st,rc)
                plt.show()
elif op==3: 
                plt .pie (dth , label=st , autopct=" %3d%%" ) 
                plt. title (" State wise Death Cases" ) 
                plt. show()
elif op==4:
                plt .pie (ac , labels=st , autopct="%3d%%" ) 
                plt. ti.tle (" State wise Active Cases" ) 
                plt. show ( ) 
                
def scatter_chart ( ) : 
        df=pd . read_csv (  "/Internal storage/Android/covid19.csv") 
        st=df['State'] 
        cnf=df['Confirmed']
        rc=df[' Recovered ' ] 
        dth=df [' Deaths ' ] 
        
        ax=plt . gca ( ) 
        ax . scatter ( st , cnf , color= ' b ' , label=" State wise Confirmed Cases " ) 
        ax . scatter (st , rc , color='r' , label=" State wise Recovered Cases" ) 
        ax . scatter(st ,dth ,color= ' g ' , label=" State wise Death" ) 
        ax . scatter( st , ac , color= ' y ' , label=" State wise Active Cases " ) 
        plt . xlabel(" state" ) 
        plt .sticks (rotations= ' vertical' ) 
        plt . title ( "Complete Scatter chart" ) 
        plt .legend ( ) 
        plt.show()
 
def data_sorting(): 
       df=pd . read_csv ( "/Internal storage/Android/covid19.csv" ) 
       
       print("Press 1 to arrange the record as per the State Name")
       print("Press 2 to arrange the record as per the Confirmed Cases") 
       print("Press 3 to arrange the record as per the Recovered Cases") 
       print("Press 4 to arrange the record as per the Total Deaths") 
       print("Press 5 to ari:ange the record as per the Active Cases") 
       
       op=int (input ("Enter Your choice : " ) ) 
       if op==1 : 
            df . sort_values ( [ " State" ] , inplace=True) 
            #lnplace: nuke the changes i-n passed DataFrame 
            print ( df ) 
       elif op==2 : 
              df . sort_values ( [" Confirmed"] , inplace=True ) 
              print (df) 
       elif op==3 : 
              df . sort_values ( [" Recovered"] , inplace=True ) 
              print(df)   
       elif op==4 : 
              df . sort_values ( ["Deaths"] , inplace=True ) 
              print(df)   
       elif op==5 : 
              df . sort_values ( ["Active"] , inplace=True ) 
              print(df)
       else:
              print('Enter valid input')
                 
def top_bottom_selected_records(): 
       df=pd . read .csv ("/Internal storage/Android/covid19.csv" , index_col=0) 
       top=int(input("How many  records to display from top:")) 
       print ( " First" , top , " records " ) 
       print (df . head (top) ) 
       bottom=int(input("How many records to display from bottom:") ) 
       print ( " Last" , bottom, " records " ) 
       print (df . taiI (bottom) ) 

def duplicate ( ) : 
        print("Duplicate the file with new file") 
        df=pd . read_csv ( "/Internal storage/Android/covid19.csv") 
        df . to_csv ( "/Internal storage/Android/covid19.csv") 
        print("Data from the new file")    
        print(df)   
        
opt=int(input("enter your choice=")) 
if opt==1 : 
     ReadCSV ( ) 
elif opt==2 : 
     no_index ( ) 
elif opt==3 : 
     line_plot ( ) 
elif opt==4 : 
     bar_plot ( ) 
elif opt==5: 
      pie_plot ( ) 
elif opt==6 : 
       scatter_chart ( ) 
elif opt==7 : 
      data_sorting ( ) 
elif opt==8 : 
        top_bottom_selected_records ( ) 
elif opt==9 : 
       duplicate ( ) 
elif opt==10 :   
       specific_col()      
else:   
       print('Enter  Valid Input')           