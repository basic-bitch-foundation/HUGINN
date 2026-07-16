# HUGINN
 Introduction
--------------------------------------------
Huginn was crow of Odin (Greek God), He was messenger of hims. Thus this will be your personal messenger, let u communicate w/ hommies in any 9 realms.

It is a LoRa ( Long Range ) powered  pocket off grid pager.

## Build

It have BOM, Custom PCB, 3D printed Enclosure, buttons and suport.
Download All files(.stp) from Enclosure printable folder and print 'em
 > It uses M2 screw everywhere
 > For part link please download .odf not .csv
 > In assembly u may see the MCU as colliding with PCB dw! it just cz I can't remove the header pins. :lollll:

 ### Instructions
 First comes the MCU U hve to castellated solder it on top of the board or can use very low height header pins

 then Display as display I gave in BOM, Have 8 pin(Goes to HAT) to 8 , I will suggest to solder 'em direct , though half height n 2.54 header can use.
 
 Stating with solder all component On PCB ,
 As most part will be connected using wire to component to SMD solder Pad.
 1. Part u need to connect like this: ( Component--> wire--> Smd pad)
 > 5 switches
 >2 LEDs
 >Battery (optional)

 2. The semi rotating switch have two part one is switch with rod dropped and a pad
 put the switch inside carv and then fix the pad on left face of rod so i can press momentary switch.
 Then, Screw it from bellow (Enough clamp so that It can't move freely but can move!)

 3. As most part have support in Enclosure but gluing it make it smooth
 4. Glue the disc motor that will send vibration through body
 5. I don't gave the outing for LED cz It was ruining the Aesthetics of E ink's calm there so Any who want to see the charging status can place it nea usb input or a small hole behind panel

## Code
This is basic firmware code u can compile and flash it in MCU using Platform.io (a extension in VS code) or using Thonny (IDE)





## How to use it:
As pager need to be quick I added three code fn!
and a local converter:
So U navigate up/down 
between
143 ( I Love u!)
505 ( SOS )
etc.
the click the send button when reciver will reciver get it wil automaticall converted in their own device
. This save the bytes of daya is trasmitting and saving time 


# Outro
Made for Hackclub <3 by Saksham (A.K.A bbb)
Feel free to contribute :heart:

