#include <stdio.h>
#include <string.h>
#include "linkedqueue.c"
void generateBinary(int n) 
{ 
    char *str1, *str2;
    // Create an empty queue of strings 
    struct node *rear,*front; 
    str1 = (char *)malloc(20);
    str2=  (char *)malloc(20);
    rear = front =NULL;
    // Enqueue the first binary number 
    rear = insertqueue(rear, "1");
    front= rear; 
    while (n--) 
    { 
        
  
		// print the front of queue 
        strcpy(str1,frontelement(front)); 
        
        printf("%s\n", str1); 
  
        strcpy(str2,str1);  // Store s1 before changing it 
    
       // Add "0" to end of str1 and insert in queue  
          strcat(str1,"0");
         // printf("%s\n", str1);
          rear= insertqueue(rear, str1); 
          
        // Add "1" to str2 and insert in queue . Note that str2 contains the previous front 
         strcat(str2,"1");
        // printf("%s\n", str1);
         rear  =insertqueue(rear, str2); 
         deletequeue(&front);
    } 
} 

void main()
{
   int n = 10; 
    
   generateBinary(n); // this function will generate binary sequence till 5 
    
} 