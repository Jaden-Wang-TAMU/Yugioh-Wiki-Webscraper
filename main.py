from os import name
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
 
import tkinter as tk
import tkinter.font as tkFont
 
import requests
from io import BytesIO
from PIL import ImageTk
from PIL import Image as PILImage
from tkinter import * 
 
ogWindow=tk.Tk()
global fontStyle
global smallerfontStyle
fontStyle = tkFont.Font(family="Lucida Grande", size=17, weight="bold")
smallerfontStyle = tkFont.Font(family="Lucida Grande", size=14)
title = tk.Label(text="Yugioh Wiki Database", font=fontStyle)
title.pack()
 
labelName = tk.Label(text="Would you like to search by card name?\nThis feature uses db.yugioh-card.com, which is blocked on the school wifi.", font=smallerfontStyle)
labelName.pack()
 
def searchByName():
    global smallerfontStyle
    global fontStyle
    window = tk.Tk()
    title = tk.Label(window, text="Yugioh Search by Name", font=fontStyle)
    title.pack()
    name_input = tk.Label(window, text="Enter the name of a Yugioh Card:\n*case sensitive*", font=smallerfontStyle)
    name_input.pack()
    name_entry = tk.Entry(window)
    name_entry.pack()
 
    def search():
        name = name_entry.get()
        if(name!=""):
            driver = webdriver.Chrome(ChromeDriverManager().install())
            url = 'https://yugioh.fandom.com/wiki/'+str(name)
            driver.get(url)
            testBody=driver.find_elements_by_xpath("//tbody")
            if len(testBody)!=0:
                body=driver.find_element_by_xpath("//tbody")
                rows=body.find_elements_by_xpath("//tr[@class='cardtablerow']")
                laughCheck=rows[5].find_element_by_xpath("//td[@class='cardtablerowdata']")
                isLaugh=laughCheck.find_elements_by_xpath("//a[@title='LAUGH']")
                if isLaugh:
                    newWindow=tk.Toplevel()
                    response = requests.get("https://static.wikia.nocookie.net/yugioh/images/e/e1/CharismaToken-VJMP-JP-C.png/revision/latest?cb=20130220164651")
                    img = ImageTk.PhotoImage(PILImage.open(BytesIO(response.content)))
                    myImgList=[]
                    myImgList.append(img)
                    panel = tk.Label(newWindow, image=myImgList[0])
                    panel.pack(side="top", fill="none", expand="no")
                    print("made image")
                    descr = tk.Label(newWindow, text="Name: Charisma Token\nCard Type: Monster\nAttribute: LAUGH\nTypes: Charisma/Token\nLevel: 5\nText: If you use this card as a Token, you should consider using other Token Cards instead.\nLimitation text: This card cannot be in a Deck.", font=smallerfontStyle)
                    descr.pack()
                    print("made description")
                    driver.close()
                    print("close")
                    newWindow.mainloop()
                else:
                    cardType=rows[11]
                    # monster uses 12th row, spell uses 
                    trueType=cardType.find_element_by_xpath("//td[@class='cardtablerowdata']")
                    monsterType=trueType.find_elements_by_xpath("//a[@title='Monster Card']")
                    spellType=trueType.find_elements_by_xpath("//a[@title='Spell Card']")
                    trapType=trueType.find_elements_by_xpath("//a[@title='Trap Card']")
                    monster=False
                    spell=False
                    trap=False
                    monGrand=None
                    spellGrand=None
                    trapGrand=None
                    if len(monsterType)!=0:
                        mon=monsterType[0]
                        # print(mon.text)
                        monParent=mon.find_element_by_xpath("..")
                        # print(monParent)
                        # print()
                        monGrand=monParent.find_element_by_xpath("..")
                        print("got monster grandparent")
                    if len(spellType)!=0:
                        spe=spellType[0]
                        # print(spe.text)
                        speParent=spe.find_element_by_xpath("..")
                        # print(speParent)
                        # print()
                        spellGrand=speParent.find_element_by_xpath("..")
                        print("got spell grandparent")
                    if len(trapType)!=0:
                        tra=trapType[0]
                        # print(tra.text)
                        traParent=tra.find_element_by_xpath("..")
                        # print(traParent)
                        # print()
                        trapGrand=traParent.find_element_by_xpath("..")
                        print("got trap grandparent")
                    monNum=25
                    spellNum=25
                    trapNum=25
                    numCounter=0
                    for r in rows:
                        if monGrand!=None and r==monGrand:
                            monNum=numCounter
                        if spellGrand!=None and r==spellGrand:
                            spellNum=numCounter
                        if trapGrand!=None and r==trapGrand:
                            trapNum=numCounter
                    if monNum<spellNum and monNum<trapNum:
                        monster=True
                        print("This is a monster")
                    if spellNum<monNum and spellNum<trapNum:
                        spell=True
                        print('This is a spell')
                    if trapNum<monNum and trapNum<spellNum:
                        trap=True
                        print("This is a trap")
                    if monster:
                        newWindow=tk.Toplevel()
                        attribute=rows[11].find_element_by_xpath("//td[@class='cardtablerowdata']")
                        fire=attribute.find_elements_by_xpath("//a[@title='FIRE']")
                        water=attribute.find_elements_by_xpath("//a[@title='WATER']")
                        earth=attribute.find_elements_by_xpath("//a[@title='EARTH']")
                        wind=attribute.find_elements_by_xpath("//a[@title='WIND']")
                        light=attribute.find_elements_by_xpath("//a[@title='LIGHT']")
                        dark=attribute.find_elements_by_xpath("//a[@title='DARK']")
                        divine=attribute.find_elements_by_xpath("//a[@title='DIVINE']")
                        trueAttribute=""
                        if len(fire)!=0:
                            trueAttribute="Fire"
                        if len(water)!=0:
                            trueAttribute="Water"
                        if len(earth)!=0:
                            trueAttribute="Earth"
                        if len(wind)!=0:
                            trueAttribute="Wind"
                        if len(light)!=0:
                            trueAttribute="Light"
                        if len(dark)!=0:
                            trueAttribute="Dark"
                        if len(divine)!=0:
                            trueAttribute="Divine"
                        monsterType=rows[12].find_element_by_xpath("//td[@class='cardtablerowdata']")
                        aqua=monsterType.find_elements_by_xpath("//a[@title='Aqua']")
                        beast=monsterType.find_elements_by_xpath("//a[@title='Beast']")
                        beastWarrior=monsterType.find_elements_by_xpath("//a[@title='Beast-Warrior']")
                        cyberse=monsterType.find_elements_by_xpath("//a[@title='Cyberse']")
                        dinosaur=monsterType.find_elements_by_xpath("//a[@title='Dinosaur']")
                        divineBeast=monsterType.find_elements_by_xpath("//a[@title='Divine-Beast']")
                        dragon=monsterType.find_elements_by_xpath("//a[@title='Dragon']")
                        fairy=monsterType.find_elements_by_xpath("//a[@title='Fairy']")
                        fiend=monsterType.find_elements_by_xpath("//a[@title='Fiend']")
                        fish=monsterType.find_elements_by_xpath("//a[@title='Fish']")
                        insect=monsterType.find_elements_by_xpath("//a[@title='Insect']")
                        machine=monsterType.find_elements_by_xpath("//a[@title='Machine']")
                        plant=monsterType.find_elements_by_xpath("//a[@title='Plant']")
                        psychic=monsterType.find_elements_by_xpath("//a[@title='Psychic']")
                        pyro=monsterType.find_elements_by_xpath("//a[@title='Pyro']")
                        reptile=monsterType.find_elements_by_xpath("//a[@title='Reptile']")
                        rock=monsterType.find_elements_by_xpath("//a[@title='Rock']")
                        seaSerpent=monsterType.find_elements_by_xpath("//a[@title='Sea Serpent']")
                        spellcaster=monsterType.find_elements_by_xpath("//a[@title='Spellcaster']")
                        thunder=monsterType.find_elements_by_xpath("//a[@title='Thunder']")
                        warrior=monsterType.find_elements_by_xpath("//a[@title='Warrior']")
                        wingedBeast=monsterType.find_elements_by_xpath("//a[@title='Winged Beast']")
                        wyrm=monsterType.find_elements_by_xpath("//a[@title='Wyrm']")
                        zombie=monsterType.find_elements_by_xpath("//a[@title='Zombie']")
                        effect=monsterType.find_elements_by_xpath("//a[@title='Effect Monster']")
                        normal=monsterType.find_elements_by_xpath("//a[@title='Normal Monster']")
                        token=monsterType.find_elements_by_xpath("//a[@title='Token Monster']")
                        spirit=monsterType.find_elements_by_xpath("//a[@title='Spirit monster']")
                        truerType=""
                        truerCondition=""
                        isToken=False
                        if len(aqua)!=0:
                            truerType="Aqua"
                        if len(beast)!=0:
                            truerType="Beast"
                        if len(beastWarrior)!=0:
                            truerType="Beast-Warrior"
                        if len(cyberse)!=0:
                            truerType="Cyberse"
                        if len(dinosaur)!=0:
                            truerType="Dinosaur"
                        if len(divineBeast)!=0:
                            truerType="Divine Beast"
                        if len(dragon)!=0:
                            truerType="Dragon"
                        if len(fairy)!=0:
                            truerType="Fairy"
                        if len(fiend)!=0:
                            truerType="Fiend"
                        if len(fish)!=0:
                            truerType="Fish"
                        if len(insect)!=0:
                            truerType="Insect"
                        if len(machine)!=0:
                            truerType="Machine"
                        if len(plant)!=0:
                            truerType="Plant"
                        if len(psychic)!=0:
                            truerType="Psychic"
                        if len(pyro)!=0:
                            truerType="Pyro"
                        if len(reptile)!=0:
                            truerType="Reptile"
                        if len(rock)!=0:
                            truerType="Rock"
                        if len(seaSerpent)!=0:
                            truerType="Sea Serpent"
                        if len(spellcaster)!=0:
                            truerType="Spellcaster"
                        if len(thunder)!=0:
                            truerType="Thunder"
                        if len(warrior)!=0:
                            truerType="Warrior"
                        if len(wingedBeast)!=0:
                            truerType="Winged Beast"
                        if len(wyrm)!=0:
                            truerType="Wyrm"
                        if len(zombie)!=0:
                            truerType="Zombie"
                        if len(effect)!=0:
                            truerCondition="Effect Monster"
                        if len(normal)!=0:
                            truerCondition="Normal Monster"
                        if len(token)!=0:
                            truerCondition="Token"
                            isToken=True                    
                        if len(spirit)!=0:
                            truerCondition="Spirit Monster"
                        extraDeck=""
                        fusion=monsterType.find_elements_by_xpath("//a[@title='Fusion Monster']")
                        synchro=monsterType.find_elements_by_xpath("//a[@title='Synchro Monster']")
                        xyz=monsterType.find_elements_by_xpath("//a[@title='Xyz Monster']")
                        pendulum=monsterType.find_elements_by_xpath("//a[@title='Pendulum Monster']")
                        link=monsterType.find_elements_by_xpath("//a[@title='Link Monster']")
                        ritualM=monsterType.find_elements_by_xpath("//a[@title='Ritual Monster']")
                        tuner=monsterType.find_elements_by_xpath("//a[@title='Tuner monster']")
                        toon=monsterType.find_elements_by_xpath("//a[@title='Toon monster']")
                        if len(fusion)!=0:
                            extraDeck="Fusion"
                        elif len(synchro)!=0:
                            extraDeck="Synchro"
                        elif len(xyz)!=0:
                            extraDeck="Xyz"
                        elif len(link)!=0:
                            extraDeck="Link"
                        else:
                            extraDeck="None"
                        if len(ritualM)!=0:
                            truerCondition="Ritual/Effect Monster"
                        if len(tuner)!=0:
                            truerCondition="Tuner/Effect Monster"
                        if len(toon)!=0:
                            truerCondition="Toon/Effect Monster"
                        pendCard=""
                        if len(pendulum)!=0:
                            pendCard="Yes"
                        else:
                            pendCard="No"
                        levelCondition=""
                        
                        if extraDeck=="Xyz":
                            rank=rows[13].find_element_by_xpath("//td[@class='cardtablerowdata']")
                            rank1=rank.find_elements_by_xpath("//a[@title='Rank 1 Monster Cards']")
                            rank2=rank.find_elements_by_xpath("//a[@title='Rank 2 Monster Cards']")
                            rank3=rank.find_elements_by_xpath("//a[@title='Rank 3 Monster Cards']")
                            rank4=rank.find_elements_by_xpath("//a[@title='Rank 4 Monster Cards']")
                            rank5=rank.find_elements_by_xpath("//a[@title='Rank 5 Monster Cards']")
                            rank6=rank.find_elements_by_xpath("//a[@title='Rank 6 Monster Cards']")
                            rank7=rank.find_elements_by_xpath("//a[@title='Rank 7 Monster Cards']")
                            rank8=rank.find_elements_by_xpath("//a[@title='Rank 8 Monster Cards']")
                            rank9=rank.find_elements_by_xpath("//a[@title='Rank 9 Monster Cards']")
                            rank10=rank.find_elements_by_xpath("//a[@title='Rank 10 Monster Cards']")
                            rank11=rank.find_elements_by_xpath("//a[@title='Rank 11 Monster Cards']")
                            rank12=rank.find_elements_by_xpath("//a[@title='Rank 12 Monster Cards']")
                            rank13=rank.find_elements_by_xpath("//a[@title='Rank 13 Monster Cards']")
                            rank0=rank.find_elements_by_xpath("//a[@title='Rank 0 Monster Cards']")
                            trueRank=""
                            if len(rank1)!=0:
                                trueRank="Rank: 1"
                            if len(rank2)!=0:
                                trueRank="Rank: 2"
                            if len(rank3)!=0:
                                trueRank="Rank: 3"
                            if len(rank4)!=0:
                                trueRank="Rank: 4"
                            if len(rank5)!=0:
                                trueRank="Rank: 5"
                            if len(rank6)!=0:
                                trueRank="Rank: 6"
                            if len(rank7)!=0:
                                trueRank="Rank: 7"
                            if len(rank8)!=0:
                                trueRank="Rank: 8"
                            if len(rank9)!=0:
                                trueRank="Rank: 9"
                            if len(rank10)!=0:
                                trueRank="Rank: 10"
                            if len(rank11)!=0:
                                trueRank="Rank: 11"
                            if len(rank12)!=0:
                                trueRank="Rank: 12"
                            if len(rank13)!=0:
                                trueRank="Rank: 13"
                            if len(rank0)!=0:
                                trueRank="Rank: 0"
                            levelCondition="\n"+trueRank
                        elif extraDeck=="Link":
                            rate=rows[14].find_element_by_xpath("//td[@class='cardtablerowdata']")
                            rate1=rate.find_elements_by_xpath("//a[@title='Link 1 Monster Cards']")
                            rate2=rate.find_elements_by_xpath("//a[@title='Link 2 Monster Cards']")
                            rate3=rate.find_elements_by_xpath("//a[@title='Link 3 Monster Cards']")
                            rate4=rate.find_elements_by_xpath("//a[@title='Link 4 Monster Cards']")
                            rate5=rate.find_elements_by_xpath("//a[@title='Link 5 Monster Cards']")
                            rate6=rate.find_elements_by_xpath("//a[@title='Link 6 Monster Cards']")
                            num=0
                            if len(rate1)!=0:
                                num=1
                            if len(rate2)!=0:
                                num=2
                            if len(rate3)!=0:
                                num=3
                            if len(rate4)!=0:
                                num=4
                            if len(rate5)!=0:
                                num=5
                            if len(rate6)!=0:
                                num=6
                            levelCondition="\n Link: "+str(num)+"\nArrows: \n"
                            arrows=rows[13].find_element_by_xpath("//td[@class='cardtablerowdata']")
                            tl=arrows.find_elements_by_xpath("//a[@title='Top-Left Link Arrow Monster Cards']")
                            t=arrows.find_elements_by_xpath("//a[@title='Top Link Arrow Monster Cards']")
                            tr=arrows.find_elements_by_xpath("//a[@title='Top-Right Link Arrow Monster Cards']")
                            r=arrows.find_elements_by_xpath("//a[@title='Right Link Arrow Monster Cards']")
                            br=arrows.find_elements_by_xpath("//a[@title='Bottom-Right Link Arrow Monster Cards']")
                            b=arrows.find_elements_by_xpath("//a[@title='Bottom Link Arrow Monster Cards']")
                            bl=arrows.find_elements_by_xpath("//a[@title='Bottom-Left Link Arrow Monster Cards']")
                            l=arrows.find_elements_by_xpath("//a[@title='Left Link Arrow Monster Cards']")
                            if len(tl)!=0:
                                levelCondition+="Top-Left, "
                            if len(t)!=0:
                                levelCondition+="Top, "
                            if len(tr)!=0:
                                levelCondition+="Top-Right, "
                            if len(r)!=0:
                                levelCondition+="Right, "
                            if len(br)!=0:
                                levelCondition+="Bottom-Right, "
                            if len(b)!=0:
                                levelCondition+="Bottom, "
                            if len(bl)!=0:
                                levelCondition+="Bottom-Left, "
                            if len(l)!=0:
                                levelCondition+="Left, "
                            levelCondition[:-1]
                        else:
                            level=rows[13].find_element_by_xpath("//td[@class='cardtablerowdata']")
                            level1=level.find_elements_by_xpath("//a[@title='Level 1 Monster Cards']")
                            level2=level.find_elements_by_xpath("//a[@title='Level 2 Monster Cards']")
                            level3=level.find_elements_by_xpath("//a[@title='Level 3 Monster Cards']")
                            level4=level.find_elements_by_xpath("//a[@title='Level 4 Monster Cards']")
                            level5=level.find_elements_by_xpath("//a[@title='Level 5 Monster Cards']")
                            level6=level.find_elements_by_xpath("//a[@title='Level 6 Monster Cards']")
                            level7=level.find_elements_by_xpath("//a[@title='Level 7 Monster Cards']")
                            level8=level.find_elements_by_xpath("//a[@title='Level 8 Monster Cards']")
                            level9=level.find_elements_by_xpath("//a[@title='Level 9 Monster Cards']")
                            level10=level.find_elements_by_xpath("//a[@title='Level 10 Monster Cards']")
                            level11=level.find_elements_by_xpath("//a[@title='Level 11 Monster Cards']")
                            level12=level.find_elements_by_xpath("//a[@title='Level 12 Monster Cards']")
                            level0=level.find_elements_by_xpath("//a[@title='Level 0 Monster Cards']")
                            trueLevel=""
                            if len(level1)!=0:
                                trueLevel="Level: 1"
                            if len(level2)!=0:
                                trueLevel="Level: 2"
                            if len(level3)!=0:
                                trueLevel="Level: 3"
                            if len(level4)!=0:
                                trueLevel="Level: 4"
                            if len(level5)!=0:
                                trueLevel="Level: 5"
                            if len(level6)!=0:
                                trueLevel="Level: 6"
                            if len(level7)!=0:
                                trueLevel="Level: 7"
                            if len(level8)!=0:
                                trueLevel="Level: 8"
                            if len(level9)!=0:
                                trueLevel="Level: 9"
                            if len(level10)!=0:
                                trueLevel="Level: 10"
                            if len(level11)!=0:
                                trueLevel="Level: 11"
                            if len(level12)!=0:
                                trueLevel="Level: 12"
                            if len(level0)!=0:
                                trueLevel="Level: 0"
                            levelCondition="\n"+trueLevel
                        
                        if pendCard=="Yes":
                            scale=rows[14].find_element_by_xpath("//td[@class='cardtablerowdata']")
                            scale1=scale.find_elements_by_xpath("//a[@title='Pendulum Scale 1 Monster Cards']")
                            scale2=scale.find_elements_by_xpath("//a[@title='Pendulum Scale 2 Monster Cards']")
                            scale3=scale.find_elements_by_xpath("//a[@title='Pendulum Scale 3 Monster Cards']")
                            scale4=scale.find_elements_by_xpath("//a[@title='Pendulum Scale 4 Monster Cards']")
                            scale5=scale.find_elements_by_xpath("//a[@title='Pendulum Scale 5 Monster Cards']")
                            scale6=scale.find_elements_by_xpath("//a[@title='Pendulum Scale 6 Monster Cards']")
                            scale7=scale.find_elements_by_xpath("//a[@title='Pendulum Scale 7 Monster Cards']")
                            scale8=scale.find_elements_by_xpath("//a[@title='Pendulum Scale 8 Monster Cards']")
                            scale9=scale.find_elements_by_xpath("//a[@title='Pendulum Scale 9 Monster Cards']")
                            scale10=scale.find_elements_by_xpath("//a[@title='Pendulum Scale 10 Monster Cards']")
                            scale11=scale.find_elements_by_xpath("//a[@title='Pendulum Scale 11 Monster Cards']")
                            scale12=scale.find_elements_by_xpath("//a[@title='Pendulum Scale 12 Monster Cards']")
                            scale13=scale.find_elements_by_xpath("//a[@title='Pendulum Scale 13 Monster Cards']")
                            scale0=scale.find_elements_by_xpath("//a[@title='Pendulum Scale 0 Monster Cards']")
                            pendScale=""
                            if len(scale1)!=0:
                                pendScale="1"
                            if len(scale2)!=0:
                                pendScale="2"
                            if len(scale3)!=0:
                                pendScale="3"
                            if len(scale4)!=0:
                                pendScale="4"
                            if len(scale5)!=0:
                                pendScale="5"
                            if len(scale6)!=0:
                                pendScale="6"
                            if len(scale7)!=0:
                                pendScale="7"
                            if len(scale8)!=0:
                                pendScale="8"
                            if len(scale9)!=0:
                                pendScale="9"
                            if len(scale10)!=0:
                                pendScale="10"
                            if len(scale11)!=0:
                                pendScale="11"
                            if len(scale12)!=0:
                                pendScale="12"
                            if len(scale13)!=0:
                                pendScale="13"
                            if len(scale0)!=0:
                                pendScale="0"
                            levelCondition+="\nPendulum Scale: "+pendScale
                        
                        if isToken:
                            art=body.find_element_by_xpath("//img[@width=160]")
                        else:  
                            art=body.find_element_by_xpath("//img[@width=300]")
                        artLink=art.get_attribute("src")
                        response = requests.get(artLink)
                        img = ImageTk.PhotoImage(PILImage.open(BytesIO(response.content)))
                        myImgList=[]
                        myImgList.append(img)
                        panel = tk.Label(newWindow, image=myImgList[0])
                        panel.pack(side="top", fill="none", expand="no")
                        print("made image")
                        stats="" 
                        if isToken:
                            url= "https://db.ygoprodeck.com/card/?search="+str(name)
                            driver.get(url)
                            body=driver.find_element_by_xpath("//body")
                            step1=body.find_element_by_xpath("//div[@class='card-desc']")
                            newDescr=step1.find_element_by_xpath("//span[@class='card-set-desc']")
                            fullEffect="Text:\n"
                            fullText=newDescr.text
                            # print("token text: "+fullText)
                            split=fullText.split(".")
                            for x in range(len(split)):
                                print(split[x])
                                print("len: "+len(split[x]))
                                if len(split[x])<=4:
                                    split[x-1]+=split[x]
                                    split.remove(split[x])
                                    print("removed")
                            paren=False
                            for s in split:
                                beg=s[0:2] 
                                if beg==" (":
                                    fullEffect+=s[1:]+".)\n"
                                    paren=True
                                else:
                                    if paren:
                                        fullEffect+=s[2:]+".\n"
                                        paren=False
                                    else:
                                        fullEffect+=s+".\n"
                            fullEffect=fullEffect[:-3]
                            banlist="\n\nTCG Banlist Status: None\nOCG Banlist Status: None"
                            step2=body.find_element_by_xpath("//div[@class='card-atk']")
                            tokenStats=step2.find_element_by_xpath("//span[@class='card-set-atk']")
                            statString=tokenStats.text
                            statSplit=statString.split(" ")
                            stats="Attack: "+statSplit[1]+"\nDefense: "+statSplit[3]
                        else:
                            url = 'https://yugiohtopdecks.com/card/'+str(name)
                            driver.get(url)
                            newBody=driver.find_element_by_xpath("//tbody")
                            trs=newBody.find_elements_by_xpath("//tr")
                            counter=0
                            fullEffect=""
                            banlist=""
                            for x in trs:
                                tdList=x.find_elements_by_xpath("//td")
                                for i in tdList:
                                    if counter==7:
                                        stats="Attack: "+i.text
                                    if counter==9:
                                        stats+="\nDefense: "+i.text
                                    if counter==11:
                                        # print("counter: "+str(counter))
                                        # print(i.text)
                                        fullText=i.text
                                        split=fullText.split(".")
                                        paren=False
                                        for x in range(len(split)):
                                            if x!=len(split) and x!=len(split)-1:
                                                print(split[x])
                                                print("len: "+str(len(split[x])))
                                                if len(split[x])<=4:
                                                    split[x-1]+=split[x]
                                                    split.remove(split[x])
                                                    print("removed")
                                        for s in split:
                                            if s!="":
                                                beg=s[0:2] 
                                                if beg==" (":
                                                    fullEffect+=s[1:]+".)\n"
                                                    paren=True
                                                else:
                                                    if paren:
                                                        fullEffect+=s[2:]+".\n"
                                                        paren=False
                                                    else:
                                                        fullEffect+=s+".\n"
                                        fullEffect=fullEffect[:-2]+"."
                                    if counter==12:
                                        banlist="\nTCG Banlist Status: "+i.text
                                    if counter==14:
                                        banlist+="\nOCG Banlist Status: "+i.text
                                        break
                                    counter+=1
                                    # counter=11 Text, counter=12 TCG Banlist, counter=14 OCG Banlist
                                break
                            # information=trs[5]
                            # texts=information.find_elements_by_xpath("//td")
                            # newText=texts[1].text
                            # print("new Info:\n"+newText)
                        if pendCard!="Yes":
                            fullEffect="Monster Effect:\n"+fullEffect
                        descr = tk.Label(newWindow, text="Name: "+name+"\nAttribute: "+trueAttribute+"\nType: "+truerType+"\nAdditional Types: "+truerCondition+"\nExtra Deck Status: "+extraDeck+"\nPendulum Monster: "+pendCard+levelCondition+"\n"+fullEffect+"\n"+stats+banlist, font=fontStyle)
                        descr.pack()
                        print("made description")
                        driver.close()
                        print("quit")
                        newWindow.mainloop()
                if spell:
                    norm=body.find_elements_by_xpath("//a[@title='Normal Spell Card']")
                    cont=body.find_elements_by_xpath("//a[@title='Continuous Spell Card']")
                    equip=body.find_elements_by_xpath("//a[@title='Equip Spell Card']")
                    quick=body.find_elements_by_xpath("//a[@title='Quick-Play Spell Card']")
                    field=body.find_elements_by_xpath("//a[@title='Field Spell Card']")
                    ritual=body.find_elements_by_xpath("//a[@title='Ritual Spell Card']")
                    trueProperty=""
                    if len(norm)!=0:
                        trueProperty="Normal"
                    if len(cont)!=0:
                        trueProperty="Continuous"
                    if len(equip)!=0:
                        trueProperty="Equip"
                    if len(quick)!=0:
                        trueProperty="Quick-Play"
                    if len(field)!=0:
                        trueProperty="Field"
                    if len(ritual)!=0:
                        trueProperty="Ritual"
                    
                    newWindow=tk.Toplevel()
                    art=body.find_element_by_xpath("//img[@width=300]")
                    artLink=art.get_attribute("src")
                    response = requests.get(artLink)
                    img = ImageTk.PhotoImage(PILImage.open(BytesIO(response.content)))
                    myImgList=[]
                    myImgList.append(img)
                    panel = tk.Label(newWindow, image=myImgList[0])
                    panel.pack(side="top", fill="none", expand="no")
                    print("made image")

                    url = 'https://yugiohtopdecks.com/card/'+str(name)
                    driver.get(url)
                    newBody=driver.find_element_by_xpath("//tbody")
                    trs=newBody.find_elements_by_xpath("//tr")
                    counter=0
                    fullEffect=""
                    banlist=""
                    for x in trs:
                        tdList=x.find_elements_by_xpath("//td")
                        for i in tdList:
                            if counter==3:
                                print(i.text)
                                fullText=i.text
                                split=fullText.split(".")
                                paren=False
                                for x in range(len(split)):
                                    if x!=len(split) and x!=len(split)-1:
                                        print(split[x])
                                        print("len: "+str(len(split[x])))
                                        if len(split[x])<=4:
                                            split[x-1]+=split[x]
                                            split.remove(split[x])
                                            print("removed")
                                for s in split:
                                    if s!="":
                                        beg=s[0:2] 
                                        if beg==" (":
                                            fullEffect+=s[1:]+".)\n"
                                            paren=True
                                        else:
                                            if paren:
                                                fullEffect+=s[2:]+".\n"
                                                paren=False
                                            else:
                                                fullEffect+=s+".\n"
                                fullEffect=fullEffect[:-2]+"."
                            if counter==4:
                                banlist="\nTCG Banlist Status: "+i.text
                            if counter==6:
                                banlist+="\nOCG Banlist Status: "+i.text
                                break
                            counter+=1
                            # counter=11 Text, counter=12 TCG Banlist, counter=14 OCG Banlist
                        break
                    
                    
                    descr = tk.Label(newWindow, text="Name: "+name+"\nType: "+trueProperty+" Spell\nEffect:\n"+fullEffect+"\n"+banlist, font=fontStyle)
                    descr.pack()
                    print("made description")
                    driver.close()
                    print("quit")
                    newWindow.mainloop()
                if trap:
                    cardProperty=rows[12].find_element_by_xpath("//td[@class='cardtablerowdata']")
                    
                    norm=cardProperty.find_elements_by_xpath("//a[@title='Normal Trap Card']")
                    cont=cardProperty.find_elements_by_xpath("//a[@title='Continuous Trap Card']")
                    equip=cardProperty.find_elements_by_xpath("//a[@title='Equip Trap Card']")
                    counter=cardProperty.find_elements_by_xpath("//a[@title='Counter Trap Card']")
                    field=cardProperty.find_elements_by_xpath("//a[@title='Field Trap Card']")
                    trueProperty=""
                    if len(norm)!=0:
                        trueProperty="Normal"
                    if len(cont)!=0:
                        trueProperty="Continuous"
                    if len(equip)!=0:
                        trueProperty="Equip"
                    if len(counter)!=0:
                        trueProperty="Counter"
                    if len(field)!=0:
                        trueProperty="Field"

                    newWindow=tk.Toplevel()
                    art=body.find_element_by_xpath("//img[@width=300]")
                    artLink=art.get_attribute("src")
                    response = requests.get(artLink)
                    img = ImageTk.PhotoImage(PILImage.open(BytesIO(response.content)))
                    myImgList=[]
                    myImgList.append(img)
                    panel = tk.Label(newWindow, image=myImgList[0])
                    panel.pack(side="top", fill="none", expand="no")
                    print("made image")

                    url = 'https://yugiohtopdecks.com/card/'+str(name)
                    driver.get(url)
                    newBody=driver.find_element_by_xpath("//tbody")
                    trs=newBody.find_elements_by_xpath("//tr")
                    counter=0
                    fullEffect=""
                    banlist=""
                    for x in trs:
                        tdList=x.find_elements_by_xpath("//td")
                        for i in tdList:
                            if counter==3:
                                print(i.text)
                                fullText=i.text
                                split=fullText.split(".")
                                paren=False
                                for x in range(len(split)):
                                    if x!=len(split) and x!=len(split)-1:
                                        print(split[x])
                                        print("len: "+str(len(split[x])))
                                        if len(split[x])<=4:
                                            split[x-1]+=split[x]
                                            split.remove(split[x])
                                            print("removed")
                                for s in split:
                                    if s!="":
                                        beg=s[0:2] 
                                        if beg==" (":
                                            fullEffect+=s[1:]+".)\n"
                                            paren=True
                                        else:
                                            if paren:
                                                fullEffect+=s[2:]+".\n"
                                                paren=False
                                            else:
                                                fullEffect+=s+".\n"
                                fullEffect=fullEffect[:-2]+"."
                            if counter==4:
                                banlist="\nTCG Banlist Status: "+i.text
                            if counter==6:
                                banlist+="\nOCG Banlist Status: "+i.text
                                break
                            counter+=1
                            # counter=11 Text, counter=12 TCG Banlist, counter=14 OCG Banlist
                        break

                    descr = tk.Label(newWindow, text="Name: "+name+"\nType: "+trueProperty+" Trap\nEffect:\n"+fullEffect+"\n"+banlist, font=fontStyle)
                    descr.pack()
                    print("made description")
                    driver.close()
                    print("quit")
                    newWindow.mainloop()
            else:
                newWindow=tk.Toplevel()
                descr = tk.Label(newWindow, text=name+" is not a valid Yugioh Card Name.", font=fontStyle)
                descr.pack()
                print("made description")
                driver.close()
                print("quit")
                newWindow.mainloop()
   
    B = tk.Button(window, text ="Search", command = search, bg='green')
    B.pack()
    
    patient = tk.Label(window, text="Please be patient. This could take some time.\n\nSome handshakes will fail before this finishes.\n\nPlease do not interact with the pop up window.\n\nIf the program freezes after the second link is openned, please close the webpage and click the Search button again.\n\nThe second website is slow when scraping for newly searched cards.", font=fontStyle)
    patient.pack()
   
    window.mainloop()
 
ogBName = tk.Button(ogWindow, text ="Name Search", command = searchByName, bg='green')
ogBName.pack()
 
labelStats = tk.Label(text="Or would you like to search by card stats?\nThis feature is not blocked on the school wifi, but the school wifi slows it down significantly.", font=smallerfontStyle)
labelStats.pack()
 
def searchByStats():
    global fontStyle
    global smallerfontStyle
    newWindow = tk.Tk()
    title = tk.Label(newWindow, text="Yugioh Search by Stats", font=fontStyle)
    title.pack()
    
    monName = tk.Label(newWindow, text="Would you like to search for a monster?", font=smallerfontStyle)
    monName.pack()

    def searchingM():
        window=tk.Tk()

        instr = tk.Label(window, text="Fill in as much info as you can about the card you're looking for:\nIf you don't know a part of a card's info, just leave it blank.", font=fontStyle)
        instr.pack()

        level_input = tk.Label(window, text="Enter a level from 0-12:", font=fontStyle)
        level_input.pack()
        level_entry = tk.Entry(window)
        level_entry.pack()
    
        rank_input = tk.Label(window, text="Enter a rank from 0-13 (if applicable):", font=fontStyle)
        rank_input.pack()
        rank_entry = tk.Entry(window)
        rank_entry.pack()
    
        pend_input = tk.Label(window, text="Enter a pendulum scale from 0-13 (if applicable):", font=fontStyle)
        pend_input.pack()
        pend_entry = tk.Entry(window)
        pend_entry.pack()
    
        link_input = tk.Label(window, text="Enter a link rating from 1-6 (if applicable):", font=fontStyle)
        link_input.pack()
        link_entry = tk.Entry(window)
        link_entry.pack()

        attr_input = tk.Label(window, text="Enter an attribute (Light, Dark, Earth, Fire, Wind, Water, Divine):", font=fontStyle)
        attr_input.pack()
        attr_entry = tk.Entry(window)
        attr_entry.pack()

        type_input = tk.Label(window, text="Enter a type:\n(Aqua, Beast, Beast-Warrior, Cyberse, Dinosaur, Divine-Beast,\nDragon, Fairy, Fiend, Fish, Insect, Machine,\nPlant, Psychic, Pyro, Reptile, Rock, Sea Serpent,\nSpellcaster, Thunder, Warrior, Winged-Beast, Wyrm, and Zombie)", font=fontStyle)
        type_input.pack()
        type_entry = tk.Entry(window)
        type_entry.pack()

        atk_input = tk.Label(window, text="Enter an attack stat:", font=fontStyle)
        atk_input.pack()
        atk_entry = tk.Entry(window)
        atk_entry.pack()

        def_input = tk.Label(window, text="Enter a defense stat:", font=fontStyle)
        def_input.pack()
        def_entry = tk.Entry(window)
        def_entry.pack()

        name_input = tk.Label(window, text="Enter a word or phrase that's in your card's name (case sensitive):", font=fontStyle)
        name_input.pack()
        name_entry = tk.Entry(window)
        name_entry.pack()
    
        def searchM():
            level = level_entry.get()
            rank=rank_entry.get()
            pend = pend_entry.get()
            linkrate=link_entry.get()
            attr=attr_entry.get()
            cardType=type_entry.get()
            cardATK=atk_entry.get()
            cardDEF=def_entry.get()
            cardName=name_entry.get()
            global driver
            driver = webdriver.Chrome(ChromeDriverManager().install())
            if(pend!=""):
                url = 'https://yugioh.fandom.com/wiki/Pendulum_Scale_'+str(pend)+'_Monster_Cards'
                driver.get(url)
            elif(linkrate!=""):
                url = 'https://yugioh.fandom.com/wiki/Link_'+str(linkrate)+'_Monster_Cards'
                driver.get(url)
            elif(rank!=""):
                url = 'https://yugioh.fandom.com/wiki/Rank_'+str(rank)+'_Monster_Cards'
                driver.get(url)
            elif(cardDEF!=""):
                url = 'https://yugioh.fandom.com/wiki/'+str(cardDEF)+'_DEF_Monster_Cards'
                driver.get(url)
            elif(cardATK!=""):
                url = 'https://yugioh.fandom.com/wiki/'+str(cardATK)+'_ATK_Monster_Cards'
                driver.get(url)
            elif(cardType!=""):
                url = 'https://yugioh.fandom.com/wiki/List_of_'+cardType.lower().capitalize()+'-Type_monsters'
                driver.get(url)
            elif(level!=""):
                url = 'https://yugioh.fandom.com/wiki/Level_'+str(level)+'_Monster_Cards'
                driver.get(url)
            elif(attr!=""):
                url = 'https://yugioh.fandom.com/wiki/List_of_'+attr.upper()+'_monsters'
                driver.get(url)
            
            global allLinks
            allLinks=[]
            
            def find():
                global allLinks
                global driver
                body=driver.find_element_by_xpath("//tbody")
                newRows=body.find_elements_by_xpath("//tr")
                for x in range(len(newRows)-1):
                    print("going through 500, currently at "+str(x+1))
                    row=body.find_element_by_xpath("//tr[@data-row-number='"+str(x+1)+"']")
                    children=row.find_elements_by_xpath(".//*")
                    cardAttr=""
                    cardType2=""
                    cardAtk=""
                    cardDef=""
                    cardLevel=""
                    cardLink=""
                    actualName=""
                    for y in children:
                        par=y.find_element_by_xpath("..")
                        if par!=None and par.get_attribute("class")=="[[Attribute]] smwtype_wpg":
                            cardAttr=y.text
                        if par!=None and par.get_attribute("class")=="[[Type]] smwtype_wpg":
                            cardType2=y.text
                        if y.get_attribute("class")=="[[ATK]] smwtype_txt":
                            cardAtk=y.text
                        if y.get_attribute("class")=="[[DEF]] smwtype_txt":
                            cardDef=y.text
                        if y.get_attribute("class")=="[[Level]]/-[[Rank]] smwtype_txt":
                            cardLevel=y.text
                        if par!=None and par.get_attribute("class")=="English-name-(linked) smwtype_txt":
                            cardLink=y.get_attribute("href")
                            actualName=y.text
                    if pend!="":
                        if ((cardName=="" or cardName in actualName) and (level=="" or level==cardLevel) and (rank=="" or rank==cardLevel) and (attr=="" or attr.upper()==cardAttr) and (cardType=="" or cardType==cardType2) and (cardATK=="" or str(cardATK)==cardAtk) and (cardDEF=="" or str(cardDEF)==cardDef)):
                            print("Pend Link: "+cardLink)
                            allLinks.append(cardLink)
                    elif linkrate!="":
                        if ((cardName=="" or cardName in actualName) and (attr=="" or attr.upper()==cardAttr) and (cardType=="" or cardType.lower().capitalize()==cardType2) and (cardATK=="" or str(cardATK)==cardAtk) and (cardDEF=="" or str(cardDEF)==cardDef)):
                            print("Level/Rank/Link Link: "+cardLink)
                            allLinks.append(cardLink)
                    elif rank!="":
                        if ((cardName=="" or cardName in actualName) and (attr=="" or attr.upper()==cardAttr) and (cardType=="" or cardType.lower().capitalize()==cardType2) and (cardATK=="" or str(cardATK)==cardAtk) and (cardDEF=="" or str(cardDEF)==cardDef)):
                            print("Level/Rank/Link Link: "+cardLink)
                            allLinks.append(cardLink)
                    elif cardDEF!="":
                        if ((cardName=="" or cardName in actualName) and (level=="" or level==cardLevel) and (attr=="" or attr.upper()==cardAttr) and (cardType=="" or cardType.lower().capitalize()==cardType2) and (cardATK=="" or str(cardATK)==cardAtk) and (attr=="" or attr.upper()==cardAttr)):
                            print("DEF Link: "+cardLink)
                            allLinks.append(cardLink)
                    elif cardATK!="":
                        if ((cardName=="" or cardName in actualName) and (level=="" or level==cardLevel) and (attr=="" or attr.upper()==cardAttr) and (cardType=="" or cardType.lower().capitalize()==cardType2)):
                            print("ATK Link: "+cardLink)
                            allLinks.append(cardLink)
                    elif cardType!="":
                        if ((cardName=="" or cardName in actualName) and (level=="" or level==cardLevel) and (attr=="" or attr.upper()==cardAttr)):
                            print("Type Link: "+cardLink)
                            allLinks.append(cardLink)
                    elif level!="":
                        if ((cardName=="" or cardName in actualName) and (attr=="" or attr.upper()==cardAttr) and (cardATK=="" or str(cardATK)==cardAtk) and (cardDEF=="" or str(cardDEF)==cardDef)):
                            print("Level/Rank/Link Link: "+cardLink)
                            allLinks.append(cardLink)
                    elif attr!="":
                        if(cardName=="" or cardName in actualName):
                            print("Attr Link: "+cardLink)
                            allLinks.append(cardLink)
                    
                print("Done")

            def find2():
                global allLinks
                global driver
                body=driver.find_element_by_xpath("//tbody")
                rowCounter=0
                for x in range(49):
                    row=body.find_elements_by_xpath("//tr[@data-row-number='"+str(x+1)+"']")
                    if len(row)!=0:
                        rowCounter+=1
                print(rowCounter)
                for x in range(rowCounter):
                    print("going through 500, currently at "+str(x+1))
                    row=body.find_element_by_xpath("//tr[@data-row-number='"+str(x+1)+"']")
                    children=row.find_elements_by_xpath(".//*")
                    cardAttr=""
                    cardType2=""
                    cardAtk=""
                    cardDef=""
                    cardLevel=""
                    cardLink=""
                    actualName=""
                    for y in children:
                        par=y.find_element_by_xpath("..")
                        if par!=None and par.get_attribute("class")=="[[Attribute]] smwtype_wpg":
                            cardAttr=y.text
                        if par!=None and par.get_attribute("class")=="[[Type]] smwtype_wpg":
                            cardType2=y.text
                        if y.get_attribute("class")=="[[ATK]] smwtype_txt":
                            cardAtk=y.text
                        if y.get_attribute("class")=="[[DEF]] smwtype_txt":
                            cardDef=y.text
                        if y.get_attribute("class")=="[[Level]]/-[[Rank]] smwtype_txt":
                            cardLevel=y.text
                        if par!=None and par.get_attribute("class")=="smwtype_txt":
                            cardLink=y.get_attribute("href")
                            actualName=y.text
                    if pend!="":
                        if ((cardName=="" or cardName in actualName) and (level=="" or level==cardLevel) and (rank=="" or rank==cardLevel) and (attr=="" or attr.upper()==cardAttr) and (cardType=="" or cardType==cardType2) and (cardATK=="" or str(cardATK)==cardAtk) and (cardDEF=="" or str(cardDEF)==cardDef)):
                            print("Pend Link: "+cardLink)
                            allLinks.append(cardLink)
                    elif linkrate!="":
                        if ((cardName=="" or cardName in actualName) and (attr=="" or attr.upper()==cardAttr) and (cardType=="" or cardType.lower().capitalize()==cardType2) and (cardATK=="" or str(cardATK)==cardAtk) and (cardDEF=="" or str(cardDEF)==cardDef)):
                            print("Level/Rank/Link Link: "+cardLink)
                            allLinks.append(cardLink)
                    elif rank!="":
                        if ((cardName=="" or cardName in actualName) and (attr=="" or attr.upper()==cardAttr) and (cardType=="" or cardType.lower().capitalize()==cardType2) and (cardATK=="" or str(cardATK)==cardAtk) and (cardDEF=="" or str(cardDEF)==cardDef)):
                            print("Level/Rank/Link Link: "+cardLink)
                            allLinks.append(cardLink)
                    elif cardDEF!="":
                        if ((cardName=="" or cardName in actualName) and (level=="" or level==cardLevel) and (attr=="" or attr.upper()==cardAttr) and (cardType=="" or cardType.lower().capitalize()==cardType2) and (cardATK=="" or str(cardATK)==cardAtk) and (attr=="" or attr.upper()==cardAttr)):
                            print("DEF Link: "+cardLink)
                            allLinks.append(cardLink)
                    elif cardATK!="":
                        if ((cardName=="" or cardName in actualName) and (level=="" or level==cardLevel) and (attr=="" or attr.upper()==cardAttr) and (cardType=="" or cardType.lower().capitalize()==cardType2)):
                            print("ATK Link: "+cardLink)
                            allLinks.append(cardLink)
                    elif cardType!="":
                        if ((cardName=="" or cardName in actualName) and (level=="" or level==cardLevel) and (attr=="" or attr.upper()==cardAttr)):
                            print("Type Link: "+cardLink)
                            allLinks.append(cardLink)
                    elif level!="":
                        if ((cardName=="" or cardName in actualName) and (attr=="" or attr.upper()==cardAttr) and (cardATK=="" or str(cardATK)==cardAtk) and (cardDEF=="" or str(cardDEF)==cardDef)):
                            print("Level/Rank/Link Link: "+cardLink)
                            allLinks.append(cardLink)
                    elif attr!="":
                        if(cardName=="" or cardName in actualName):
                            print("Attr Link: "+cardLink)
                            allLinks.append(cardLink)
                    
                print("Done")
            
            span=driver.find_elements_by_xpath("//span[@class='smw-table-furtherresults']")
            if len(span)!=0:
                print('found span')
                children=span[0].find_elements_by_xpath(".//*")
                print('found children')
                child=children[0]
                link=child.get_attribute("href")
                print("link: "+link)
                driver.get(link)

                five=driver.find_element_by_xpath("//a[@title='Show 500 results per page']")
                link=five.get_attribute("href")
                print("link2: "+link)
                driver.get(link)

                five=driver.find_element_by_xpath("//a[@title='Previous 500 results']")
                link=five.get_attribute("href")
                print("link3: "+link)
                driver.get(link)
                # driver.get("https://yugioh.fandom.com/wiki/Special:Ask?limit=500&offset=0&q=%5B%5BClass+1%3A%3AOfficial%5D%5D+%5B%5BCard+type%3A%3AMonster+Card%5D%5D+%5B%5BLevel%3A%3A8%5D%5D&p=mainlabel%3D-20-2D%2Fformat%3Dtable%2Fheaders%3D-20plain%2Fsearchlabel%3D-20...-20further-20results-20%28571-20more%29%2Fclass%3D-20sortable-20wikitable-20smwtable-20card-2Dlist&po=%3FEnglish+name+%28linked%29%0A%3FJapanese+name%0A%3FPrimary+type%0A%3FSecondary+type%0A%3FAttribute%3D%5B%5BAttribute%5D%5D%0A%3FType%3D%5B%5BType%5D%5D%0A%3FATK+string%3D%5B%5BATK%5D%5D%0A%3FDEF+string%3D%5B%5BDEF%5D%5D%0A&sort=&order=asc&eq=no#search")
                # main=driver.find_element_by_xpath("//div[@class='main-container']")
                find()
                notFinished=True
                while notFinished:
                    nextFive=driver.find_elements_by_xpath("//a[@title='Next 500 results']")
                    if len(nextFive)!=0:
                        link=nextFive[0].get_attribute("href")
                        driver.get(link)
                        print("getting next 500")
                        find()
                    else:
                        notFinished=False
                print("All Done")
            else:
                find2()
                print("All Done")
            
            global myImgList
            global myNameList
            myImgList=[]
            myNameList=[]
            global counter
            counter=0
            print(len(allLinks))
            for x in allLinks:
                if x!="":
                    driver.get(x)
                    body=driver.find_element_by_xpath("//tbody")
                    art=body.find_elements_by_xpath("//img[@width=300]")
                    if len(art)!=0:
                        artLink=art[0].get_attribute("src")
                        response = requests.get(artLink)
                        img_data = response.content
                        img = ImageTk.PhotoImage(PILImage.open(BytesIO(img_data)))
                        myImgList.append(img)
                        rows=body.find_elements_by_xpath("//tr[@class='cardtablerow']")
                        attribute=rows[11].find_element_by_xpath("//td[@class='cardtablerowdata']")
                        fire=attribute.find_elements_by_xpath("//a[@title='FIRE']")
                        water=attribute.find_elements_by_xpath("//a[@title='WATER']")
                        earth=attribute.find_elements_by_xpath("//a[@title='EARTH']")
                        wind=attribute.find_elements_by_xpath("//a[@title='WIND']")
                        light=attribute.find_elements_by_xpath("//a[@title='LIGHT']")
                        dark=attribute.find_elements_by_xpath("//a[@title='DARK']")
                        divine=attribute.find_elements_by_xpath("//a[@title='DIVINE']")
                        trueAttribute=""
                        if len(fire)!=0:
                            trueAttribute="Fire"
                        if len(water)!=0:
                            trueAttribute="Water"
                        if len(earth)!=0:
                            trueAttribute="Earth"
                        if len(wind)!=0:
                            trueAttribute="Wind"
                        if len(light)!=0:
                            trueAttribute="Light"
                        if len(dark)!=0:
                            trueAttribute="Dark"
                        if len(divine)!=0:
                            trueAttribute="Divine"
                        monsterType=rows[12].find_element_by_xpath("//td[@class='cardtablerowdata']")
                        aqua=monsterType.find_elements_by_xpath("//a[@title='Aqua']")
                        beast=monsterType.find_elements_by_xpath("//a[@title='Beast']")
                        beastWarrior=monsterType.find_elements_by_xpath("//a[@title='Beast-Warrior']")
                        cyberse=monsterType.find_elements_by_xpath("//a[@title='Cyberse']")
                        dinosaur=monsterType.find_elements_by_xpath("//a[@title='Dinosaur']")
                        divineBeast=monsterType.find_elements_by_xpath("//a[@title='Divine-Beast']")
                        dragon=monsterType.find_elements_by_xpath("//a[@title='Dragon']")
                        fairy=monsterType.find_elements_by_xpath("//a[@title='Fairy']")
                        fiend=monsterType.find_elements_by_xpath("//a[@title='Fiend']")
                        fish=monsterType.find_elements_by_xpath("//a[@title='Fish']")
                        insect=monsterType.find_elements_by_xpath("//a[@title='Insect']")
                        machine=monsterType.find_elements_by_xpath("//a[@title='Machine']")
                        plant=monsterType.find_elements_by_xpath("//a[@title='Plant']")
                        psychic=monsterType.find_elements_by_xpath("//a[@title='Psychic']")
                        pyro=monsterType.find_elements_by_xpath("//a[@title='Pyro']")
                        reptile=monsterType.find_elements_by_xpath("//a[@title='Reptile']")
                        rock=monsterType.find_elements_by_xpath("//a[@title='Rock']")
                        seaSerpent=monsterType.find_elements_by_xpath("//a[@title='Sea Serpent']")
                        spellcaster=monsterType.find_elements_by_xpath("//a[@title='Spellcaster']")
                        thunder=monsterType.find_elements_by_xpath("//a[@title='Thunder']")
                        warrior=monsterType.find_elements_by_xpath("//a[@title='Warrior']")
                        wingedBeast=monsterType.find_elements_by_xpath("//a[@title='Winged Beast']")
                        wyrm=monsterType.find_elements_by_xpath("//a[@title='Wyrm']")
                        zombie=monsterType.find_elements_by_xpath("//a[@title='Zombie']")
                        effect=monsterType.find_elements_by_xpath("//a[@title='Effect Monster']")
                        normal=monsterType.find_elements_by_xpath("//a[@title='Normal Monster']")
                        token=monsterType.find_elements_by_xpath("//a[@title='Token Monster']")
                        spirit=monsterType.find_elements_by_xpath("//a[@title='Spirit monster']")
                        truerType=""
                        truerCondition=""
                        if len(aqua)!=0:
                            truerType="Aqua"
                        if len(beast)!=0:
                            truerType="Beast"
                        if len(beastWarrior)!=0:
                            truerType="Beast-Warrior"
                        if len(cyberse)!=0:
                            truerType="Cyberse"
                        if len(dinosaur)!=0:
                            truerType="Dinosaur"
                        if len(divineBeast)!=0:
                            truerType="Divine Beast"
                        if len(dragon)!=0:
                            truerType="Dragon"
                        if len(fairy)!=0:
                            truerType="Fairy"
                        if len(fiend)!=0:
                            truerType="Fiend"
                        if len(fish)!=0:
                            truerType="Fish"
                        if len(insect)!=0:
                            truerType="Insect"
                        if len(machine)!=0:
                            truerType="Machine"
                        if len(plant)!=0:
                            truerType="Plant"
                        if len(psychic)!=0:
                            truerType="Psychic"
                        if len(pyro)!=0:
                            truerType="Pyro"
                        if len(reptile)!=0:
                            truerType="Reptile"
                        if len(rock)!=0:
                            truerType="Rock"
                        if len(seaSerpent)!=0:
                            truerType="Sea Serpent"
                        if len(spellcaster)!=0:
                            truerType="Spellcaster"
                        if len(thunder)!=0:
                            truerType="Thunder"
                        if len(warrior)!=0:
                            truerType="Warrior"
                        if len(wingedBeast)!=0:
                            truerType="Winged Beast"
                        if len(wyrm)!=0:
                            truerType="Wyrm"
                        if len(zombie)!=0:
                            truerType="Zombie"
                        if len(effect)!=0:
                            truerCondition="Effect Monster"
                        if len(normal)!=0:
                            truerCondition="Normal Monster"
                        if len(token)!=0:
                            truerCondition="Token"                   
                        if len(spirit)!=0:
                            truerCondition="Spirit Monster"
                        extraDeck=""
                        fusion=monsterType.find_elements_by_xpath("//a[@title='Fusion Monster']")
                        synchro=monsterType.find_elements_by_xpath("//a[@title='Synchro Monster']")
                        xyz=monsterType.find_elements_by_xpath("//a[@title='Xyz Monster']")
                        pendulum=monsterType.find_elements_by_xpath("//a[@title='Pendulum Monster']")
                        link=monsterType.find_elements_by_xpath("//a[@title='Link Monster']")
                        ritualM=monsterType.find_elements_by_xpath("//a[@title='Ritual Monster']")
                        tuner=monsterType.find_elements_by_xpath("//a[@title='Tuner monster']")
                        toon=monsterType.find_elements_by_xpath("//a[@title='Toon monster']")
                        if len(fusion)!=0:
                            extraDeck="Fusion"
                        elif len(synchro)!=0:
                            extraDeck="Synchro"
                        elif len(xyz)!=0:
                            extraDeck="Xyz"
                        elif len(link)!=0:
                            extraDeck="Link"
                        else:
                            extraDeck="None"
                        if len(ritualM)!=0:
                            truerCondition="Ritual/Effect Monster"
                        if len(tuner)!=0:
                            truerCondition="Tuner/Effect Monster"
                        if len(toon)!=0:
                            truerCondition="Toon/Effect Monster"
                        pendCard=""
                        if len(pendulum)!=0:
                            pendCard="Yes"
                        else:
                            pendCard="No"
                        levelCondition=""
                        
                        if extraDeck=="Xyz":
                            rank=rows[13].find_element_by_xpath("//td[@class='cardtablerowdata']")
                            rank1=rank.find_elements_by_xpath("//a[@title='Rank 1 Monster Cards']")
                            rank2=rank.find_elements_by_xpath("//a[@title='Rank 2 Monster Cards']")
                            rank3=rank.find_elements_by_xpath("//a[@title='Rank 3 Monster Cards']")
                            rank4=rank.find_elements_by_xpath("//a[@title='Rank 4 Monster Cards']")
                            rank5=rank.find_elements_by_xpath("//a[@title='Rank 5 Monster Cards']")
                            rank6=rank.find_elements_by_xpath("//a[@title='Rank 6 Monster Cards']")
                            rank7=rank.find_elements_by_xpath("//a[@title='Rank 7 Monster Cards']")
                            rank8=rank.find_elements_by_xpath("//a[@title='Rank 8 Monster Cards']")
                            rank9=rank.find_elements_by_xpath("//a[@title='Rank 9 Monster Cards']")
                            rank10=rank.find_elements_by_xpath("//a[@title='Rank 10 Monster Cards']")
                            rank11=rank.find_elements_by_xpath("//a[@title='Rank 11 Monster Cards']")
                            rank12=rank.find_elements_by_xpath("//a[@title='Rank 12 Monster Cards']")
                            rank13=rank.find_elements_by_xpath("//a[@title='Rank 13 Monster Cards']")
                            rank0=rank.find_elements_by_xpath("//a[@title='Rank 0 Monster Cards']")
                            trueRank=""
                            if len(rank1)!=0:
                                trueRank="Rank: 1"
                            if len(rank2)!=0:
                                trueRank="Rank: 2"
                            if len(rank3)!=0:
                                trueRank="Rank: 3"
                            if len(rank4)!=0:
                                trueRank="Rank: 4"
                            if len(rank5)!=0:
                                trueRank="Rank: 5"
                            if len(rank6)!=0:
                                trueRank="Rank: 6"
                            if len(rank7)!=0:
                                trueRank="Rank: 7"
                            if len(rank8)!=0:
                                trueRank="Rank: 8"
                            if len(rank9)!=0:
                                trueRank="Rank: 9"
                            if len(rank10)!=0:
                                trueRank="Rank: 10"
                            if len(rank11)!=0:
                                trueRank="Rank: 11"
                            if len(rank12)!=0:
                                trueRank="Rank: 12"
                            if len(rank13)!=0:
                                trueRank="Rank: 13"
                            if len(rank0)!=0:
                                trueRank="Rank: 0"
                            levelCondition="\n"+trueRank
                        elif extraDeck=="Link":
                            rate=rows[14].find_element_by_xpath("//td[@class='cardtablerowdata']")
                            rate1=rate.find_elements_by_xpath("//a[@title='Link 1 Monster Cards']")
                            rate2=rate.find_elements_by_xpath("//a[@title='Link 2 Monster Cards']")
                            rate3=rate.find_elements_by_xpath("//a[@title='Link 3 Monster Cards']")
                            rate4=rate.find_elements_by_xpath("//a[@title='Link 4 Monster Cards']")
                            rate5=rate.find_elements_by_xpath("//a[@title='Link 5 Monster Cards']")
                            rate6=rate.find_elements_by_xpath("//a[@title='Link 6 Monster Cards']")
                            num=0
                            if len(rate1)!=0:
                                num=1
                            if len(rate2)!=0:
                                num=2
                            if len(rate3)!=0:
                                num=3
                            if len(rate4)!=0:
                                num=4
                            if len(rate5)!=0:
                                num=5
                            if len(rate6)!=0:
                                num=6
                            levelCondition="\n Link: "+str(num)+"\nArrows: \n"
                            arrows=rows[13].find_element_by_xpath("//td[@class='cardtablerowdata']")
                            tl=arrows.find_elements_by_xpath("//a[@title='Top-Left Link Arrow Monster Cards']")
                            t=arrows.find_elements_by_xpath("//a[@title='Top Link Arrow Monster Cards']")
                            tr=arrows.find_elements_by_xpath("//a[@title='Top-Right Link Arrow Monster Cards']")
                            r=arrows.find_elements_by_xpath("//a[@title='Right Link Arrow Monster Cards']")
                            br=arrows.find_elements_by_xpath("//a[@title='Bottom-Right Link Arrow Monster Cards']")
                            b=arrows.find_elements_by_xpath("//a[@title='Bottom Link Arrow Monster Cards']")
                            bl=arrows.find_elements_by_xpath("//a[@title='Bottom-Left Link Arrow Monster Cards']")
                            l=arrows.find_elements_by_xpath("//a[@title='Left Link Arrow Monster Cards']")
                            if len(tl)!=0:
                                levelCondition+="Top-Left, "
                            if len(t)!=0:
                                levelCondition+="Top, "
                            if len(tr)!=0:
                                levelCondition+="Top-Right, "
                            if len(r)!=0:
                                levelCondition+="Right, "
                            if len(br)!=0:
                                levelCondition+="Bottom-Right, "
                            if len(b)!=0:
                                levelCondition+="Bottom, "
                            if len(bl)!=0:
                                levelCondition+="Bottom-Left, "
                            if len(l)!=0:
                                levelCondition+="Left, "
                            levelCondition[:-1]
                        else:
                            level=rows[13].find_element_by_xpath("//td[@class='cardtablerowdata']")
                            level1=level.find_elements_by_xpath("//a[@title='Level 1 Monster Cards']")
                            level2=level.find_elements_by_xpath("//a[@title='Level 2 Monster Cards']")
                            level3=level.find_elements_by_xpath("//a[@title='Level 3 Monster Cards']")
                            level4=level.find_elements_by_xpath("//a[@title='Level 4 Monster Cards']")
                            level5=level.find_elements_by_xpath("//a[@title='Level 5 Monster Cards']")
                            level6=level.find_elements_by_xpath("//a[@title='Level 6 Monster Cards']")
                            level7=level.find_elements_by_xpath("//a[@title='Level 7 Monster Cards']")
                            level8=level.find_elements_by_xpath("//a[@title='Level 8 Monster Cards']")
                            level9=level.find_elements_by_xpath("//a[@title='Level 9 Monster Cards']")
                            level10=level.find_elements_by_xpath("//a[@title='Level 10 Monster Cards']")
                            level11=level.find_elements_by_xpath("//a[@title='Level 11 Monster Cards']")
                            level12=level.find_elements_by_xpath("//a[@title='Level 12 Monster Cards']")
                            level0=level.find_elements_by_xpath("//a[@title='Level 0 Monster Cards']")
                            trueLevel=""
                            if len(level1)!=0:
                                trueLevel="Level: 1"
                            if len(level2)!=0:
                                trueLevel="Level: 2"
                            if len(level3)!=0:
                                trueLevel="Level: 3"
                            if len(level4)!=0:
                                trueLevel="Level: 4"
                            if len(level5)!=0:
                                trueLevel="Level: 5"
                            if len(level6)!=0:
                                trueLevel="Level: 6"
                            if len(level7)!=0:
                                trueLevel="Level: 7"
                            if len(level8)!=0:
                                trueLevel="Level: 8"
                            if len(level9)!=0:
                                trueLevel="Level: 9"
                            if len(level10)!=0:
                                trueLevel="Level: 10"
                            if len(level11)!=0:
                                trueLevel="Level: 11"
                            if len(level12)!=0:
                                trueLevel="Level: 12"
                            if len(level0)!=0:
                                trueLevel="Level: 0"
                            levelCondition="\n"+trueLevel
                        
                        if pendCard=="Yes":
                            scale=rows[14].find_element_by_xpath("//td[@class='cardtablerowdata']")
                            scale1=scale.find_elements_by_xpath("//a[@title='Pendulum Scale 1 Monster Cards']")
                            scale2=scale.find_elements_by_xpath("//a[@title='Pendulum Scale 2 Monster Cards']")
                            scale3=scale.find_elements_by_xpath("//a[@title='Pendulum Scale 3 Monster Cards']")
                            scale4=scale.find_elements_by_xpath("//a[@title='Pendulum Scale 4 Monster Cards']")
                            scale5=scale.find_elements_by_xpath("//a[@title='Pendulum Scale 5 Monster Cards']")
                            scale6=scale.find_elements_by_xpath("//a[@title='Pendulum Scale 6 Monster Cards']")
                            scale7=scale.find_elements_by_xpath("//a[@title='Pendulum Scale 7 Monster Cards']")
                            scale8=scale.find_elements_by_xpath("//a[@title='Pendulum Scale 8 Monster Cards']")
                            scale9=scale.find_elements_by_xpath("//a[@title='Pendulum Scale 9 Monster Cards']")
                            scale10=scale.find_elements_by_xpath("//a[@title='Pendulum Scale 10 Monster Cards']")
                            scale11=scale.find_elements_by_xpath("//a[@title='Pendulum Scale 11 Monster Cards']")
                            scale12=scale.find_elements_by_xpath("//a[@title='Pendulum Scale 12 Monster Cards']")
                            scale13=scale.find_elements_by_xpath("//a[@title='Pendulum Scale 13 Monster Cards']")
                            scale0=scale.find_elements_by_xpath("//a[@title='Pendulum Scale 0 Monster Cards']")
                            pendScale=""
                            if len(scale1)!=0:
                                pendScale="1"
                            if len(scale2)!=0:
                                pendScale="2"
                            if len(scale3)!=0:
                                pendScale="3"
                            if len(scale4)!=0:
                                pendScale="4"
                            if len(scale5)!=0:
                                pendScale="5"
                            if len(scale6)!=0:
                                pendScale="6"
                            if len(scale7)!=0:
                                pendScale="7"
                            if len(scale8)!=0:
                                pendScale="8"
                            if len(scale9)!=0:
                                pendScale="9"
                            if len(scale10)!=0:
                                pendScale="10"
                            if len(scale11)!=0:
                                pendScale="11"
                            if len(scale12)!=0:
                                pendScale="12"
                            if len(scale13)!=0:
                                pendScale="13"
                            if len(scale0)!=0:
                                pendScale="0"
                            levelCondition+="\nPendulum Scale: "+pendScale

                            # descr = tk.Label(newWindow, text="Name: "+name+"\nAttribute: "+trueAttribute+"\nType: "+truerType+"\nCondition: "+truerCondition+"\nExtra Deck Status: "+extraDeck+"\nPendulum Monster: "+pendCard+levelCondition+"\n"+fullEffect+"\n"+stats+banlist, font=fontStyle)
                            
                        myName=rows[0].find_element_by_xpath("//td[@class='cardtablerowdata']")
                        myNameList.append(myName.text+"\nCard Type: "+truerType+"\nAttribute: "+trueAttribute+"\nAdditional Types: "+truerCondition+"\nExtra Deck Status: "+extraDeck+"\nPendulum Monster: "+pendCard+levelCondition)
            
            print(len(myImgList))
            if len(myImgList)!=0:
                driver.close()        
                finWindow=tk.Toplevel()
                global panel
                panel=tk.Label(finWindow, image=myImgList[0])
                panel.pack(side="top", fill="none", expand="no")
                global finName
                counter=0
                finName=tk.Label(finWindow, text="Name: "+myNameList[counter], font=fontStyle)
                finName.pack()
                my_menu=Menu(finWindow)
                finWindow.config(menu=my_menu)
                def prevScreen():
                    print("prevScreen")
                    global myImgList
                    global counter
                    global panel
                    global finName
                    if counter>0:
                        panel.destroy()
                        finName.destroy()
                        counter-=1
                        panel=tk.Label(finWindow, image=myImgList[counter])
                        panel.pack()
                        finName=tk.Label(finWindow, text="Name: "+myNameList[counter], font=fontStyle)
                        finName.pack()
                        print("newCounter: "+str(counter))

                def nextScreen():
                    print("nextScreen")
                    global myImgList
                    global counter
                    global panel
                    global finName
                    if counter<len(myImgList)-1:
                        panel.destroy()
                        finName.destroy()
                        counter+=1
                        panel=tk.Label(finWindow, image=myImgList[counter])
                        panel.pack()
                        finName=tk.Label(finWindow, text="Name: "+myNameList[counter], font=fontStyle)
                        finName.pack()
                        print("newCounter: "+str(counter))

                my_menu.add_command(label="Prev Screen", command =  prevScreen)
                my_menu.add_command(label="Next Screen", command = nextScreen)
                driver.close() 
            else:
                driver.close()        
                finWindow=tk.Toplevel()
                finName=tk.Label(finWindow, text="Sorry, no cards were found!", font=fontStyle)
                finName.pack()
                print("No cards found")
                
    
        B = tk.Button(window, text ="Search", command = searchM, bg='green')
        B.pack()

        window.mainloop()
    
    monB = tk.Button(newWindow, text ="Monster Search", command = searchingM, bg='green')
    monB.pack()

    speName = tk.Label(newWindow, text="Would you like to search for a spell?", font=smallerfontStyle)
    speName.pack()
    def searchingS():
        window=tk.Tk()

        type_input = tk.Label(window, text="Enter a type of spell card (Normal, Continuous, Equip, Quick-Play, Field, Ritual):", font=fontStyle)
        type_input.pack()
        type_entry = tk.Entry(window)
        type_entry.pack()

        name_input = tk.Label(window, text="Enter a word or phrase that's in your card's name (case sensitive):", font=fontStyle)
        name_input.pack()
        name_entry = tk.Entry(window)
        name_entry.pack()

        patient = tk.Label(window, text="Please be patient. This could take some time.\nSome handshakes will fail before this finishes.\nPlease do not interact with the pop up window.", font=fontStyle)
        patient.pack()
        
        def searchS():
            global driver
            speType = type_entry.get()
            name=name_entry.get()
            
            if(speType!=""):
                driver = webdriver.Chrome(ChromeDriverManager().install())
                url = 'https://yugioh.fandom.com/wiki/List_of_'+speType.capitalize()+'_Spell_Cards'
                driver.get(url)

            
            global allLinks
            allLinks=[]

            def find():
                global allLinks
                global driver
                body=driver.find_element_by_xpath("//tbody")
                newRows=body.find_elements_by_xpath("//tr")
                for x in range(len(newRows)-1):
                    print("going through 500, currently at "+str(x+1))
                    row=body.find_element_by_xpath("//tr[@data-row-number='"+str(x+1)+"']")
                    children=row.find_elements_by_xpath(".//*")
                    actualName=""
                    for y in children:
                        par=y.find_element_by_xpath("..")
                        if par!=None and par.get_attribute("class")=="English-name-(linked) smwtype_txt":
                            cardLink=y.get_attribute("href")
                            actualName=y.text
                    if name!="":
                        if name in actualName:
                            print("Name Link: "+cardLink)
                            allLinks.append(cardLink)
                    else:
                        allLinks.append(cardLink)
                    
                print("Done")
            
            testSpan=driver.find_elements_by_xpath("//span[@class='smw-table-furtherresults']")
            if len(testSpan)!=0:
                span=driver.find_element_by_xpath("//span[@class='smw-table-furtherresults']")
                print('found span')
                children=span.find_elements_by_xpath(".//*")
                print('found children')
                child=children[0]
                link=child.get_attribute("href")
                print("link: "+link)
                driver.get(link)

                five=driver.find_element_by_xpath("//a[@title='Show 500 results per page']")
                link=five.get_attribute("href")
                print("link2: "+link)
                driver.get(link)

                five=driver.find_element_by_xpath("//a[@title='Previous 500 results']")
                link=five.get_attribute("href")
                print("link3: "+link)
                driver.get(link)

                find()
                notFinished=True
                while notFinished:
                    nextFive=driver.find_elements_by_xpath("//a[@title='Next 500 results']")
                    if len(nextFive)!=0:
                        link=nextFive[0].get_attribute("href")
                        driver.get(link)
                        print("getting next 500")
                        find()
                    else:
                        notFinished=False
            else:
                find()

            print("All Done")
            global myImgList
            myImgList=[]
            global myNameList
            myNameList=[]
            global counter
            counter=0
            for x in allLinks:
                driver.get(x)
                body=driver.find_element_by_xpath("//tbody")
                art=body.find_elements_by_xpath("//img[@width=300]")
                if len(art)!=0:
                    artLink=art[0].get_attribute("src")
                    response = requests.get(artLink)
                    img_data = response.content
                    img = ImageTk.PhotoImage(PILImage.open(BytesIO(img_data)))
                    myImgList.append(img)
                    rows=body.find_elements_by_xpath("//tr[@class='cardtablerow']")
                    myName=rows[0].find_element_by_xpath("//td[@class='cardtablerowdata']")
                    # descr = tk.Label(newWindow, text="Name: "+name+"\nProperty: "+trueProperty+" Spell\nEffect:\n"+fullEffect+"\n"+banlist, font=fontStyle)
                    myNameList.append(myName.text+"\nType: "+speType+" Spell")
            finWindow=tk.Toplevel()
            
            print(len(myImgList))
            if myImgList!=0:
                global panel
                panel=tk.Label(finWindow, image=myImgList[0])
                panel.pack(side="top", fill="none", expand="no")
                global finName
                finName=tk.Label(finWindow, text="Name: "+myNameList[counter], font=fontStyle)
                finName.pack()
                my_menu=Menu(finWindow)
                finWindow.config(menu=my_menu)
                def prevScreen():
                    print("prevScreen")
                    global myImgList
                    global counter
                    global panel
                    global finName
                    if counter>0:
                        panel.destroy()
                        finName.destroy()
                        counter-=1
                        panel=tk.Label(finWindow, image=myImgList[counter])
                        panel.pack()
                        finName=tk.Label(finWindow, text="Name: "+myNameList[counter], font=fontStyle)
                        finName.pack()
                        print("newCounter: "+str(counter))

                def nextScreen():
                    print("nextScreen")
                    global myImgList
                    global counter
                    global panel
                    global finName
                    if counter<len(myImgList)-1:
                        panel.destroy()
                        finName.destroy()
                        counter+=1
                        panel=tk.Label(finWindow, image=myImgList[counter])
                        panel.pack()
                        finName=tk.Label(finWindow, text="Name: "+myNameList[counter], font=fontStyle)
                        finName.pack()
                        print("newCounter: "+str(counter))
                
                my_menu.add_command(label="Prev Screen", command =  prevScreen)
                my_menu.add_command(label="Next Screen", command = nextScreen)
                driver.close() 
            else:
                driver.close()        
                finWindow=tk.Toplevel()
                finName=tk.Label(finWindow, text="Sorry, no cards were found!", font=fontStyle)
                finName.pack()
                print("No cards found")
    
        B = tk.Button(window, text ="Search", command = searchS, bg='green')
        B.pack()

        window.mainloop()
    
    speB = tk.Button(newWindow, text ="Spell Search", command = searchingS, bg='green')
    speB.pack()


    traName = tk.Label(newWindow, text="Would you like to search for a trap?", font=smallerfontStyle)
    traName.pack()

    def searchingT():
        window=tk.Tk()

        type_input = tk.Label(window, text="Enter a type of trap card (Normal, Continuous, Equip, Counter, Field):", font=fontStyle)
        type_input.pack()
        type_entry = tk.Entry(window)
        type_entry.pack()

        name_input = tk.Label(window, text="Enter a word or phrase that's in your card's name (case sensitive):", font=fontStyle)
        name_input.pack()
        name_entry = tk.Entry(window)
        name_entry.pack()

        patient = tk.Label(window, text="Please be patient. This could take some time.\nSome handshakes will fail before this finishes.\nPlease do not interact with the pop up window.", font=fontStyle)
        patient.pack()
        
        def searchT():
            global driver
            traType = type_entry.get()
            name=name_entry.get()

            if(traType!=""):
                driver = webdriver.Chrome(ChromeDriverManager().install())
                url = 'https://yugioh.fandom.com/wiki/List_of_'+traType.capitalize()+'_Trap_Cards'
                driver.get(url)
            
            global allLinks
            allLinks=[]
            
            def find():
                global allLinks
                global driver
                body=driver.find_element_by_xpath("//tbody")
                newRows=body.find_elements_by_xpath("//tr")
                for x in range(len(newRows)-1):
                    print("going through 500, currently at "+str(x+1))
                    row=body.find_element_by_xpath("//tr[@data-row-number='"+str(x+1)+"']")
                    children=row.find_elements_by_xpath(".//*")
                    actualName=""
                    for y in children:
                        par=y.find_element_by_xpath("..")
                        if par!=None and par.get_attribute("class")=="English-name-(linked) smwtype_txt":
                            cardLink=y.get_attribute("href")
                            actualName=y.text
                    if name!="":
                        if name in actualName:
                            print("Name Link: "+cardLink)
                            allLinks.append(cardLink)
                    else:
                        allLinks.append(cardLink)
                    
                print("Done")
            testSpan=driver.find_elements_by_xpath("//span[@class='smw-table-furtherresults']")
            if len(testSpan)!=0:
                span=driver.find_element_by_xpath("//span[@class='smw-table-furtherresults']")
                print('found span')
                children=span.find_elements_by_xpath(".//*")
                print('found children')
                child=children[0]
                link=child.get_attribute("href")
                print("link: "+link)
                driver.get(link)

                five=driver.find_element_by_xpath("//a[@title='Show 500 results per page']")
                link=five.get_attribute("href")
                print("link2: "+link)
                driver.get(link)

                five=driver.find_element_by_xpath("//a[@title='Previous 500 results']")
                link=five.get_attribute("href")
                print("link3: "+link)
                driver.get(link)

                find()
                notFinished=True
                while notFinished:
                    nextFive=driver.find_elements_by_xpath("//a[@title='Next 500 results']")
                    if len(nextFive)!=0:
                        link=nextFive[0].get_attribute("href")
                        driver.get(link)
                        print("getting next 500")
                        find()
                    else:
                        notFinished=False
            else:
                find()
            
            print("All Done")
            global myImgList
            myImgList=[]
            global myNameList
            myNameList=[]
            global counter
            counter=0
            for x in allLinks:
                driver.get(x)
                body=driver.find_element_by_xpath("//tbody")
                art=body.find_elements_by_xpath("//img[@width=300]")
                if len(art)!=0:
                    artLink=art[0].get_attribute("src")
                    response = requests.get(artLink)
                    img_data = response.content
                    img = ImageTk.PhotoImage(PILImage.open(BytesIO(img_data)))
                    myImgList.append(img)
                    rows=body.find_elements_by_xpath("//tr[@class='cardtablerow']")
                    myName=rows[0].find_element_by_xpath("//td[@class='cardtablerowdata']")
                    myNameList.append(myName.text+"\nType: "+traType.lower().capitalize()+" Trap")
            finWindow=tk.Toplevel()
            
            
            print(len(myImgList))
            if len(myImgList)!=0:
                global panel
                panel=tk.Label(finWindow, image=myImgList[0])
                panel.pack(side="top", fill="none", expand="no")
                global finName
                counter=0
                finName=tk.Label(finWindow, text="Name: "+myNameList[counter], font=fontStyle)
                finName.pack()
                my_menu=Menu(finWindow)
                finWindow.config(menu=my_menu)
                def prevScreen():
                    print("prevScreen")
                    global myImgList
                    global counter
                    global panel
                    global finName
                    if counter>0:
                        panel.destroy()
                        finName.destroy()
                        counter-=1
                        panel=tk.Label(finWindow, image=myImgList[counter])
                        panel.pack()
                        finName=tk.Label(finWindow, text="Name: "+myNameList[counter], font=fontStyle)
                        finName.pack()
                        print("newCounter: "+str(counter))

                def nextScreen():
                    print("nextScreen")
                    global myImgList
                    global counter
                    global panel
                    global finName
                    if counter<len(myImgList)-1:
                        panel.destroy()
                        finName.destroy()
                        counter+=1
                        panel=tk.Label(finWindow, image=myImgList[counter])
                        panel.pack()
                        finName=tk.Label(finWindow, text="Name: "+myNameList[counter], font=fontStyle)
                        finName.pack()
                        print("newCounter: "+str(counter))

                my_menu.add_command(label="Prev Screen", command =  prevScreen)
                my_menu.add_command(label="Next Screen", command = nextScreen)
                driver.close()
            else:
                driver.close()        
                finWindow=tk.Toplevel()
                finName=tk.Label(finWindow, text="Sorry, no cards were found!", font=fontStyle)
                finName.pack()
                print("No cards found")


    
        B = tk.Button(window, text ="Search", command = searchT, bg='green')
        B.pack()
        
        window.mainloop()

    traB = tk.Button(newWindow, text ="Trap Search", command = searchingT, bg='green')
    traB.pack()
   
    newWindow.mainloop()
 
 
ogBStats = tk.Button(ogWindow, text ="Stats Search", command = searchByStats, bg='green')
ogBStats.pack()
 
ogWindow.mainloop()
