import random
que=["Current Railway Minister of India is_________\n\n(a)Mamta Banarjee (b)Ram Vilash (c)Ashwini Vaishnaw (d)Piyush Goyal\n\n",
"Which god is also known as ‘Gauri Nandan’?\n\n(a)Agni (b)Indra (c)Hanuman (d)Ganesha\n\n",
"What does not grow on tree according to a popular Hindi saying?\n\n(a)Money (b)Flowers (c)Leaves (d)Fruits\n\n",
"Which city is known as Pink City in India?\n\n(a)Banglore (b)Maysore (c)Jaipur (d)Kochi\n\n",
"How many religions are there in India?\n\n(a)6 (b)7 (c)8 (d)9\n\n",
"When is the National Hindi Diwas celebrated?\n\n(a)13 September (b)14 September (c)14 July (d)15 August\n\n",
"Which one of the following places is famous for the Great Vishnu Temple?\n\n(a)Bordubar,Indonesia (b)Bamiyan,Afghanistan (c)Panja Sahib,Pakistan (d)Ankorvat,Cambodia\n\n",
"The largest Buddhist Monastery in India is located at______\n\n(a)Sarnath, Uttar Pradesh (b)Tawang, Arunachal Pradesh (c)Dharmashala, Himachal Pradesh (d)Gangtok, Sikkim\n\n",
"Who among the following was killed during 'Operation Bluestar' of 1984?\n\n(a)Baba Santa Singh (b)Haji Mastan (c)Jarnail Singh Bhindrawale (d)Homi Jehangir Bhabha\n\n",
"Which former Indian President died as a result of a road accident?\n\n(a)Rajendra Prasad (b)Faqruddin Ali Ahmed (c)Giani Zail Singh (d)R.Venkatraman\n\n",
"Who is the founder of the political party Dravida Munnetra Kazhagam (DMK)?\n\n(a)C.N.Annadurai (b)M.Karunanidhi (c)M.G.Ramachandran (d)Jayalalitha\n\n",
"Who was the first Indian woman to win a medal in the Olympics?\n\n(a)P.T.Usha (b)Kunjarani Devi (c)Bachendri Pal (d)Karnam Maleshwari\n\n",
"Which Mughal Emperor was deported to Rangoon by the British?\n\n(a)Shah Jahan (b)Bahadur Shah II (c)Akbar Shah I (d)Bahadur Shah I\n\n",
"Who among the following is said to have witnessed the reigns of eight Delhi Sultans?\n\n(a)Minhaj-us-Siraj (b)Ziauddin Barani (c)Amir Khusro (d)Shams-i-Siraj Afif\n\n",
"The fine step-well complex of 'Agrasen ki Baoli' is located at______\n\n(a)Gwalior (b)Amritsar (c)Agra (d)New Delhi\n\n",
"Which James Bond movie was shot in the Indian city of Udaipur?\n\n(a)Diamonds Are Forever (b)License to Kill (c)Live and Let Die (d)Octupussy\n\n",
"Which city is known as the 'Silicon Valley Of India'?\n\n(a)Delhi (b)Mumbai (c)Chennai (d)Bangalore\n\n",
"Where was the BRICS summit held in 2014?\n\n(a)Brazil (b)India (c)Russia (d)China\n\n",
"Who wrote the introduction to the English translation of Rabindranath Tagore’s Gitanjali?\n\n(a)P.B. Shelley (b)Alfred Tennyson (c)W.B. Yeats (d)T.S. Elliot\n\n",
"Which of these leaders was a recipient of a gallantry award in 1987 by a state government for saving two girls from drowning?\n\n(a)Anandiben Patel (b)Vasundhara Raje Scindia (c)Uma Bharti (d)Mamata Banerjee\n\n",
"The wife of which of these famous sports persons was once captain of Indian volleyball team?\n\n(a)K.D.Jadav (b)Prakash Padukone (c)Dhyan Chand (d)Milkha Singh\n\n",
"Which of these terms can only be used for women?\n\n(a)Dirghaayu (b)Suhagan (c)Chiranjeevi (d)Sushil\n\n"
]
ans=("c","d","a","c","a","b","d","b","c","c","a","d","d","c","d","d","d","a","c","a","d","b")
prz=[1000,2000,3000,5000,10000,20000,40000,80000,160000,320000,640000,1250000,2500000,5000000,10000000,70000000]
count=0
j=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21]
print(que)
print("=================================================")
print("              Kaun Banega Crorepati")
print("=================================================\t")
print("                Prizes:\n")
print("                1)1,000")
print("                2)2,000")
print("                3)3,000")
print("                4)5,000")
print("                5)10,000")
print("                6)20,000")
print("                7)40,000")
print("                8)80,000")
print("                9)1,60,000")
print("                10)3,20,000")
print("                11)6,40,000")
print("                12)12,50,000")
print("                13)25,00,000")
print("                14)50,00,000")
print("                15)100,00,000")
print("                16)700,00,000")
print("=================================================\t")
print("                Questions:\n")
for i in range(0,16):
  p=random.choice(j)
  l=j.index(p)
  print(i+1,". ",que[p],"->Prize:",prz[i])
  o=input("Enter option you wish : ")
  if(ans[p]==o):
    print("Correct")
    count=count+prz[i]
    print("You Won : ",prz[i])
    print("Total Won : ",count,"\n")
  else:
    print("wrong")
    print("Correct Answer is : ",ans[p])
    print("Total Won : ",count,"\n")
    break
  j.pop(l)