Title: Huginn
Aurthor: Saksham 
Description: It is a LoRa (Long-Range) off grid Pager, people can communticate in remote areas. Named upon messenger crow of Odin.
**Total Time Elapsed: 43 Hours 34 mins** without code 

>Note: SO Basically I didn't have exact duration for every sesssion, I have dates frame , duration and Lapse for it.
# June 7 - June 26 (7 sessions & 3 Lapses)
**Time Elapsed for this time frame: 9 hrs 27mins + 14hrs 30 mins + 2 hrs 57 mins = 26 hrs 54 mins**
**[Lapse Link_1](https://lapse.hackclub.com/timelapse/QDs2V-pR2Pm_)**
**[Lapse Link_2](https://lapse.hackclub.com/timelapse/tjxTxSEeeEpX)**
**[Lapse Link_3](https://lapse.hackclub.com/timelapse/QCqySz1Eb1_g)**


**I can't recall exact time/date per sessions**
#session_1
Started with BOM.

Not exact with costing, but the parts I will need.
Made a notepad file for that.

So initially BOM includes:

* Seeed Studio XIAO ESP32-S3
* LoRa SX1278 Ra-02 Ai-Thinker

Then antenna for LoRa. I first thought of a direct-connect U.FL antenna, but it wasn't available.

So I thought of adding an SMA to U.FL pigtail cable and then an SMA antenna. It also gives a good look, like a pager with an antenna. Matches with my design.

Although It can work without antenna too!

Then eInk display.

So I thought of using a raw 2.7-inch eInk panel and then designing the FFC connector to it.

But as I'm a pro noobie in hardware, I planned to use a module with SPI interface embedded with 8 outputs.
Cz FFC have like 23 pin thinnest

So I fixed on the Waveshare 2.7-inch eInk display module with SPI interface.

Battery most prob 3.7V LiPo.
![alt text](images/s1.png)

#Session_2
So at very first I went for Seeed Studio XIAO ESP32-S3 and started designing the schematic in KiCad with Conn_01x07 pins twice as per ESP32-S3 pinout, then Conn_01x08 twice for the LoRa module.

Then a single Conn_01x08 for the eInk display.

Then labeled all things and pinouts, updated the same in the notepad, then added capacitors, etc.

------------------------------ THEN HIT A PROBLEM ------------------------------

I, a dumaah, didn't account for the GPIO pins required.

And the Seeed Studio ESP32-S3 ran out of GPIOs.

So I searched for another MCU and landed at:

ESP32-S3 DevKitC-1 N8R8

Which has a whopping 45 GPIOs, but the size is big.

Then calculated the size dimensions of the pager body, etc.

It fits. :yayayay:

So for the symbol in KiCad I used Conn_02x22_Counter_Clockwise for ESP32-S3 DevKitC-1 N8R8, but it didn't work well due to many naming issues.

And I'm new to KiCad as well.

So searched for its symbol and found it in the KiCad library, but it was with different pinout and naming.

I got it, but the pins were a little disordered.

#session_3

So I edited the symbol and changed the pin names and order as per my requirement, and then added it to my project library.

[LAPSE FREEZED HERE A LITTLE]

After that I learned two things.

Dropped using local labels because of visibility and also for better understanding of the schematic, and used Global Labels.

Then wired MCU, Display, and LoRa.

Added battery and a main switch.

Then researched about the charging part and landed on MCP73831, which is a single-cell LiPo charger IC.

Added USB_C_RECEPTACLE for charging and also added Conn_01x02 for battery connection.



But here I will obviously not use all pins of USB-C. Most likely I will use the same type because I use VBUS and SHIELD with MCP73831.

Then for voltage regulator I thought of using MT3608 but switched to MCP1640, but couldn't find either one.

#Session_4


I researched a lot of regulators for 3.3V like MCP1700T, SSP9193, TPS63020.

All of them were either out of stock or not available to ship to India.

At last I found a niche sussy website selling AP2112K-3.3V.

Then using two power labels: BAT_SYS and BAT_RAW.

Fixed connections, added capacitors and resistors for charging, eInk display between battery labels, etc.

Connected regulator, charging IC, battery labels, USB-C pins, and LEDs for charging indication.

Then comes the navigation part.

For UI/UX navigation I planned for 4 buttons, but I think 5 are needed.

So added one more button for menu and used 5 buttons for:

* Up
* Down
* Left
* Right
* Menu

Connected them with MCU as required.

Now the vibration motor part.

I used an N-type MOSFET for vibration motor controlling.

I really wanted good haptics.
okay so i can upload all images so i give the drive link check out all images
 
 




#Session_5
So I started with fixing some capacitance Issue in schemtaics 
then for good structure and understanding I rearrange the schematics each working parts in seprate boxes and label them.

>  Footprint time 


As I'm new to Hardware and PCBs I didn't know that there are two types of component SMD and THT
So I change the many footprint of resistor and capacitor to THT cz SMD ones are very tiny and I wasn't sure that I could solder them or not. :confused-smash:

Then Comes Lora problem now Intially Lora is in two pats of Conn symbol.
but obv I have to assing footprint to any one
so I have to download symbol and footprint of Lora 
There fore I have to re-wire the Lora in schematics.

Then I researched (little and not continously) for other symbol's footprints. And started assinging.

Now for many things I dont want it soldered to PCB board  such as switches, Leds so I can move these parts by soldering wire on pcb on soldering pads
. Problem was there wasn't any soldering Pads of correct size neither two pads together.
So I searched for it, can't find any.
I started makin' one in footprint editor.
And used it accordingly.

Then some little search for correct usb pin so i go for a break board that can be used.
![alt text](images/s1.png) ![alt text](images/videoframe_12583.png) ![alt text](images/videoframe_21790.png) ![alt text](images/videoframe_30694.png) ![alt text](images/videoframe_35618.png) ![alt text](images/videoframe_133124.png) ![alt text](images/videoframe_183342.png) ![alt text](images/videoframe_185783.png) ![alt text](images/videoframe_210763.png) ![alt text](images/videoframe_227552.png) ![alt text](images/videoframe_273794.png) ![alt text](images/videoframe_278502.png) ![alt text](images/videoframe_341890.png) ![alt text](images/videoframe_371626.png) ![alt text](images/videoframe_381401.png) ![alt text](images/videoframe_388782.png) ![alt text](images/videoframe_478846.png) ![alt text](images/videoframe_535933.png) ![alt text](images/videoframe_550931.png) ![alt text](images/videoframe_557210.png)
**Images above are till session 5**

#Session_6

> Now here comes the assembly of footprint on PCB board
> I couldn't figure what to tell about this in Journal, U can refer to Lapse to see assembly.
> Here what I think about why It takes so long to complete the assembly 
> - It is my first PCB and hardware project so I can't figure out what to place where.
> - I didn't know that we can place component both side of the PCB
> I was facing problems with Edge cuts etc


So I started just assembly like there is DEV board and rest of component in sides
then dropped this Ideas as board was too Big.

Then this Dumahh! learned to place component on both sides and get know bout Vias. :dummahh:
so wwhat I thought that i would use header pins for devboad and plac some compo beneath it and places Lora the opposide side. Resistors on sides and soldering pads accordingly.

> Another Dumaah moment!
> I didn't account for routing, why?
> cz I didn't thought about that.
> So I have to re arrange places
> I didn't place capacitors near as possible as input line

ALso I didn't see some basic precause like no High power line near lora etc.

So I replaced capacitor to nearest to its corresponding components and started wire.
 
> You may seem some silly mistakes in lapse while wiring. As I new to KiCad so I didn't knew those. so yeah :sadge:
> Like changes the placement like 3-4 times 
**In this lapse there is some blank and freeze screen Idk why maybe Lapse issue.
**



#Session_7 


So as starting I ran a DRC check as most of wiring/ tracing was done.
>For General Info:
I used *0.25 mm , 0.75 mm & 1.0 mm* tracing according to power need.
Now there was some Silkscreen overlaping for switches fixed that

Then Its time for edge cut, Now I want no extra space in board neither the super edgy corner so I made like stairs step like design on one side and rounded corners.
 
 Then I started Enclosure designing, so I started sketchin' the front face like buttons,display etc in krita u can see this in lapse, also taking some inspo from Pinterest.
 
 a note that the usb foot print doesnt have label assing ed in footprint library it is locally assinged so whenever i updated pcb from schemtatics is renew and none label is shown so i hve to assing it again.

 ![alt text](images/videoframe_1975.png) ![alt text](images/videoframe_2743.png) ![alt text](images/videoframe_4253.png) ![alt text](images/videoframe_8511.png) ![alt text](images/videoframe_14410.png) ![alt text](images/videoframe_20830.png) ![alt text](images/videoframe_37656.png) ![alt text](images/videoframe_40441.png) ![alt text](images/videoframe_42817.png) ![alt text](images/videoframe_44340.png) ![alt text](images/videoframe_45395.png) ![alt text](images/videoframe_49905.png) ![alt text](images/videoframe_50998.png) ![alt text](images/videoframe_56633.png) ![alt text](images/videoframe_80807.png) ![alt text](images/videoframe_86633.png) ![alt text](images/videoframe_90876.png) ![alt text](images/videoframe_97800.png) ![alt text](images/videoframe_102840.png) ![alt text](images/videoframe_124216.png) ![alt text](images/videoframe_134147.png) ![alt text](images/videoframe_134466.png) ![alt text](images/videoframe_136238.png) ![alt text](images/videoframe_149896.png) ![alt text](images/videoframe_154774.png) ![alt text](images/videoframe_163205.png) ![alt text](images/videoframe_182891.png) ![alt text](images/videoframe_188394.png) ![alt text](images/videoframe_195793.png) ![alt text](images/videoframe_218212.png) ![alt text](images/videoframe_245769.png) ![alt text](images/videoframe_268215.png) ![alt text](images/videoframe_312690.png) ![alt text](images/videoframe_335648.png) ![alt text](images/videoframe_344988.png) ![alt text](images/videoframe_365425.png) ![alt text](images/videoframe_391018.png) ![alt text](images/videoframe_396044.png) ![alt text](images/videoframe_425240.png) ![alt text](images/videoframe_430915.png) ![alt text](images/videoframe_458144.png) ![alt text](images/videoframe_742331.png) ![alt text](images/videoframe_751726.png) ![alt text](images/videoframe_758518.png) ![alt text](images/videoframe_778386.png) ![alt text](images/videoframe_782961.png) ![alt text](images/videoframe_823988.png)

# Till JULY 4 (1 Lapse, 1 session)
**[Lapse Link](https://lapse.hackclub.com/timelapse/FahkMhBIB23j) Time Elapsed: 12hrs**


 > This is mostly CAD/Enclosure/Assembly 

#Session_1 
 
After completing the sketch of front face of buttons, colors etc

I ignited CAD and start sketching the Enclosure boundary
> **Context** : For repeated thing in Lapse that may be misinterpreted as Inflation but In fact It first that time I'm using CAD for this extent , previously I only designed a cookie cutter. :hehehehehe:

I started making enclosure by sketch then eclosure boundary then pad it and using *thickness* carved out space.  Althout this ^ step take too long cz i can't figure out how to hollow the box and how to meausure distance
![alt text](images/videoframe_4106.png) ![alt text](images/videoframe_20800.png) ![alt text](images/videoframe_91554.png)
And:
  - Fixed very little tracing issue in pcb then try to export it as step but it was just plain green board so LIke i have find better way to get it with 3d component too!
![alt text](images/videoframe_105729.png)
  - Added a Kicad plugin in workbench and imported PCB 3d model and for size purpose fit , It didn't fit by length so i have edit the case. 
  
  - For more Good looking I also add Lora Chip 3d model from web in assembly and removed horizontal header pin for display because of space and connection issue, infact the pin is like this **[Image of pin]** so I wil just solder the wire directly to TH And reimport PCB model.
  ![alt text](images/videoframe_117850.png) ![alt text](images/videoframe_130483.png) ![alt text](images/videoframe_147785.png) ![alt text](images/videoframe_162543.png) ![alt text](images/videoframe_175506.png)
  
  -  Imported E ink display, I researched and changed the display from 2.7 to 2.3 inch cz I didn't account for size of overall pc while designing
  -  And I desinge a [ shape suport for display but later remvoed it as it was eating volume for pcb fitting.

  - Now for supprt of PCb and display strudity i will not use screw support cz of space constraints therefore i added a wall-slab with screw groove and will use sillicon pad at end of screww to just press the both PCB and screen into position. U may seem litle google search her , was bout Freecad doubt & display sizings.

 - Sketch out display size on front of case and then chamfer it for edgy looks.
 - ![alt text](images/videoframe_342538.png)
 - ![alt text](images/videoframe_193881.png) ![alt text](images/videoframe_203382.png) ![alt text](images/videoframe_267917.png) ![alt text](images/videoframe_276917.png) ![alt text](images/videoframe_313238.png) ![alt text](images/videoframe_330867.png)
 - Imported navigation push buttons adn arrange them as best fit and Aesthetics.
 - ![alt text](images/videoframe_339996.png) ![alt text](images/videoframe_360219.png)
 - Traced a border outline , actually i changed it few times like once I missed then correct face,once I left like empty space in b/w button so ihave also remove the area unused in b/w button so it can fit.
- Then pocket out the area , now it was time to support the buttons thought I will glue them to frame but as it will be pressed hard repteadly I desinged a frame like rising from base and then going slab like above the buttons but only halfway , for another halfway i made another one same ,not symetrically but yeah then holes above it to push the button in place by using screws. I made it in two part to little liberty while building the screw hole can be repositing at least to some magnitude.
- (This actually took soo much time like idk how aling to different body for perfect alingment)
- ![alt text](images/videoframe_452849.png)
  ![alt text](images/videoframe_376594.png)![alt text](images/videoframe_416970.png)![alt text](images/videoframe_479015.png)![alt text](images/videoframe_479015.png)
![alt text](images/videoframe_515435.png)


#Session_2
 
 I started making 
power button for so as intially in sketch I designed it was two circle of different size on will ortae axialy. I go for same though had some issu in sketching it. then i added h vertical center to center bar and make it slanting in side of small circle for btter grip.

- Then placed in it in correct palce on front face of enclosure
- carved out a place holder of 1.5 mm in front face to hold button and in big angle to button can slige to n fro. then pocket out a arc hole to lead a pillar like pad from front part of button on upper side and then extrude a side way tapered increasing to fix magnet there
- Imported hall sensor and 
- sketched a support three way like a helmet for hall sensor.

(Thouth I face a lots of contraint issue in this sketch)
![alt text](images/videoframe_542839.png) ![alt text](images/videoframe_547559.png) ![alt text](images/videoframe_585211.png) ![alt text](images/videoframe_593774.png) ![alt text](images/videoframe_603661.png) ![alt text](images/videoframe_648255.png) ![alt text](images/videoframe_659562.png) ![alt text](images/videoframe_676813.png) ![alt text](images/videoframe_705977.png) ![alt text](images/videoframe_717290.png) ![alt text](images/videoframe_719074.png)

#  July 4 (1 session, 1 lapse)
**[Lapse Link](https://lapse.hackclub.com/timelapse/i13NdgKe-hXV) Time Elapsed: 2hrs 24 mins**
In this i tried to make a grip of magnet face holder but dropeed as it was alr too litte area

## button top design times
now it was time to design to design button top
So I started with first pocketing out a square for send button, I forgot bout that :dumb: so then I started button design 
so for navigatin istead of seprate button for ech side used all arrow adn spear like design to go for
sketch it , pad it, aling it to the buttons and then pocket out holder holes for then and then fit it in assembly.then fillet it from all sides
same for send button but It was of triangle shape though.
> This took a little longer to plan the design and aling and sketch as i want it to look good 
Then:
- I alr iported a 3.7 v Li-po batter but ididnt fit soI found a another one but could not find its 3D model so i statred to made one , In this stage i learne hoe to colro faces and body in FreeCAD
  
Then, Its time to make a back panel for Encosure
so I first sketch out and then pocket out a rim inisde of wall of enclosure ant hen sketh it out and pad it to full panel for sketch.

For support and fixing panel I use the same slab hole that'll use to clamp the pcb and scrren so a single screw will hold the panel, display and pcb
 then I colored all the faces .
 
 Then i made cutout for type C but I cant find real cutout dimentsion it fixed later when i imported a type c break board, but imported breakout board's pcb was dislocated so i mad eon with correct dimension and replaced it
 ![alt text](images/videoframe_5216.png) ![alt text](images/videoframe_21211.png) ![alt text](images/videoframe_30782.png) ![alt text](images/videoframe_37621.png) ![alt text](images/videoframe_40651.png) ![alt text](images/videoframe_45397.png) ![alt text](images/videoframe_60795.png) ![alt text](images/videoframe_114834.png) ![alt text](images/videoframe_120827.png) ![alt text](images/videoframe_133805.png) ![alt text](images/videoframe_135908.png)

# July 16 (1 Lapse and 1 session)
**[Lapse Link](https://lapse.hackclub.com/timelapse/NnLJkcKzMWgB) Time Elapsed: 2hrs 16 mins**


Fist thing I saw many issue
Like 
>- the frame and back panel are in same body
we need it different baody to print seprately and 

>- The screww holes was of wring diameter, as for M2 screw with self tapping I need 1.6 +- 0.05 mm bot Idk why I use 2.1 mm everywhere.

> - As I removed the supporting slab cz it was too space consumeing and not supporting firmlyso There isn't any support for Display .

>- the power button is like axial rotation but display FFC strip is blocking its way + the Momentary switch is not alinged to pressing pad

>- There isn;t any hlding an rotaing mechanishm for Pwer switch

  
How do i Solve them? :ponders:
So first I can't remove the back panel which is *PAD* in a body if dlete it it will break the body
so what i did is i use external geometry selction on fce of panel out and pocket it out

then use a shape binder of the frame in another body and make the bakc panel with correct dimension


2. For screww Holes i just openned the skect and pocket of every hole and resketch to 1.65mm of diameter and re- pocket

3. I made a two thin flecxible strip , little shorter than display height for firm grip.
4. Now comes the most time consuming part. So, First I forgot that Hall sensor require a GPIO pin to work, though I could assing one in PCB but problem was i want complete power shut off switch. But I Edit the support for Hall sensor then add a momentary switch ( actually i didn't know that this thing exists :blyat:)

Now Bout switch, 
- So first switch is made of two sketch so I have to move them seprately and pocket them out seprately
- Now I need to make a holding system for switch rotation and so i did like a pocket for M2 screww obv with self tapping dimensions that will be screwed little loose vertically so that button can rotate.
- Then comes the padd part that will press the momentary switch so delete the pad before and restart from scratch pad a long pad then the pad


A dumb problem here i added a pad on base or power button but after print how some one can get it fit inside so i have to make the same pad in another body
 so later I undo it and add and export it as another body ( though i didn't have lapse for this specific task)
 ![alt text](<images/videoframe_7864 (1).png>) ![alt text](images/videoframe_17167.png) ![alt text](images/videoframe_24598.png) ![alt text](images/videoframe_35939.png) ![alt text](images/videoframe_41954.png) ![alt text](images/videoframe_50062.png) ![alt text](images/videoframe_63869.png) ![alt text](images/videoframe_72772.png) ![alt text](images/videoframe_81347.png) ![alt text](images/videoframe_94637.png) ![alt text](images/videoframe_99857.png) ![alt text](images/videoframe_104002.png) ![alt text](images/videoframe_107897.png) ![alt text](images/videoframe_122830.png) ![alt text](images/videoframe_125037.png) 
  
