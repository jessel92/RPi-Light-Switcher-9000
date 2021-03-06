# Raspberry Pi Light Switcher 9000


Let me start by saying, I am **VERY** new to Python, HTML, and GitHub so please feel free to give me any advise you may have!  
This is an awesome simple project if you are just starting with python, 3D printing or Raspberry Pi's.


---
I really wanted some home automation (and I was bored),
but I live in a rented apartment in NYC and it turns out my landlord really frown upon me messing with the apartment's wiring.
:stuck_out_tongue_winking_eye:  
So I've designed a small bracket that attaches to your existing light switch plate that holds a micro servo which can turn on and off a paddle style light switch.

This is a simple Flask server that is run from your Raspberry Pi (or other single board computers) that can control that micro servo via a web interface over your local network!  
Without messing with any existing electrical work!

See my [Thingiverse](https://www.thingiverse.com/Forgedinplastic3d/about) post (I will post the actual link as soon as I put it up)for the micro servo switch plate mount.
  
If you have a standard style light switch check out this [Servo Switch Plate Mount](https://www.thingiverse.com/thing:1156995) by carjo3000  
I havent tried it but I'm sure you can make it work with some slight adjustments to the code!

The servo I used: [Keywish MG90S](https://www.amazon.com/gp/product/B071J7BGV8/ref=oh_aui_detailpage_o02_s00?ie=UTF8&psc=1)  

---
## How to use RPi Light Switch 9000

* **MAKE SURE TO CHANGE ALL OF MY IP ADDRESSES TO YOUR PI'S LOCAL ADDRESS!!**

* **Adjust the `serv_pin` variable in `app.py` to your servos GPIO pin**

* **Use the `test.py` to determine the correct ON/OFF angles for the servo.** 

* **Run `app.py`  on your pi**

* **To access the interface from any browser on your local network go to  `http://<Your Pi's IP>:5000/`**  
    *Example: `http://192.168.0.2:5000/`*
   
* **Edit the HTML and CSS in `index.html`. Share your changes!**

---
 
#### Feel free to contact me if you have any questions or if you have some advise for a newbie like me!  
I need your help, Teach me something, give me advice! 


**PLEASE CONTRIBUTE!**