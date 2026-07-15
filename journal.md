Started with BOM.

Not exact with costing, but the parts I will need.
Made a notepad file for that.

So initially BOM includes:

* Seeed Studio XIAO ESP32-S3
* LoRa SX1278 Ra-02 Ai-Thinker

Then antenna for LoRa. I first thought of a direct-connect U.FL antenna, but it wasn't available.

So I thought of adding an SMA to U.FL pigtail cable and then an SMA antenna. It also gives a good look, like a pager with an antenna. Matches with my design.

Then eInk display.

So I thought of using a raw 2.7-inch eInk panel and then designing the FFC connector to it.

But as I'm a pro noobie in hardware, I planned to use a module with SPI interface embedded with 8 outputs.

So I fixed on the Waveshare 2.7-inch eInk display module with SPI interface.

Battery most prob 3.7V LiPo.

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
[https://drive.google.com/drive/folders/1kfr5PdgTjcCPfoEB2-ydQZeznJoeSycp?usp=sharing](here)

![Screenshot from 2026-06-08 15-09-42.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MjkyNzMsInB1ciI6ImJsb2JfaWQifX0=--359be13a1591eba478baae5423fea3f8d7d9e69a/Screenshot from 2026-06-08 15-09-42.png)


### Recording Links

- https://public.lapse-hackclub.link/timelapses/QDs2V-pR2Pm_/timelapse-QDs2V-pR2Pm_.mp4



# JUNE 7 - JUNE 26 
> **I couldn't recall exact timestampes**

## Session - 2
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

**In this lapse there is some blank and freeze screen Idk why maybe Lapse issue.
**


## Session - 3 
Citing Time Lapse ~ 3 hrs - 

So as starting I ran a DRC check as most of wiring/ tracing was done.
>For General Info:
I used *0.25 mm , 0.75 mm & 1.0 mm* tracing according to power need.
Now there was some Silkscreen overlaping for switches fixed that

Then Its time for edge cut, Now I want no extra space in board neither the super edgy corner so I made like stairs step like design on one side and rounded corners.
 
 Then I started Enclosure designing, so I started sketchin' the front face like buttons,display etc in krita u can see this in lapse, also taking some inspo from Pinterest.


# Till JULY 4 
Citing Time Lapse(s) ~ 11.5 hours + ~2 hours
Link-1 Link-2
 > This is mostly CAD/Enclosure/Assembly 

## Session 1 
 
After completing the sketch of front face of buttons, colors etc

I ignited CAD and start sketching the Enclosure boundary
> **Context** : For repeated thing in Lapse that may be misinterpreted as Inflation but In fact It first that time I'm using CAD for this extent , previously I only designed a cookie cutter. :hehehehehe:

I started making enclosure by sketch then eclosure boundary then pad it and using *thickness* carved out space. 

And:
  - Add a Kicad plugin in workbench and imposted PCB 3d model and for size purpose fit , It didn't fit by length so i have edit the case. 
  
  - For more Good looking I also add Lora Chip 3d model from web in assembly and removed horizontal header pin for display because of space and connection issue, infact the pin is like this **[Image of pin]** so I wil just solder the wire directly to TH And reimport PCB model.
  
  
  -  Imported E ink display, I researched and changed the display from 2.7 to 2.3 inch cz I didn't account for size of overall pc while designing

  - Now for supprt of PCb and display strudity i will not use screw support cz of space constraints therefore i added a wall-slab with screw groove and will use sillicon pad at end of screww to just press the both PCB and screen into position. U may seem litle google search her , was bout Freecad doubt & display sizings.

 - Sketch out display size on front of case and then chamfer it for edgy looks.
 - Imported navigation push buttons adn arrange them as best fit and Aesthetics.
 - Traced a border outline , actually i changed it few times like once I missed then correct face,once I left like empty space in b/w button so ihave also remove the area unused in b/w button so it can fit.
- Then pocket out the area , now it was time to support the buttons thought I will glue them to frame but as it will be pressed hard repteadly I desinged a frame like rising from base and then going slab like above the buttons but only halfway , for another halfway i made another one same ,not symetrically but yeah then holes above it to push the button in place by using screws. I made it in two part to little liberty while building the screw hole can be repositing at least to some magnitude.
  

**session changed**
 
 I started making 
power button for so as intially in sketch I designed it was two circle of different size on will ortae axialy. I go for same though had some issu in sketching it. then i added h vertical center to center bar and make it slanting in side of small circle for btter grip.

- Then placesd in it in correct plce on front face of enclosure
- carved out a place holder of 1.5 mm in front face to hold button and in big angle to button can slige to n fro. then pocket out a arc hole to lead a pillar like pad from front part of button on upper side and then extrude a side way tapered increasing to fix magnet there
- Imported hall sensor and 
- sketched a support three way like a helmet for hall sensor.



#  antoher lapse
In this i tried to make a gript of manget face holder but drpeed as it was alr too litte area

## button design times
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
 then I colored all the feaces .
# Lapse- cititing



