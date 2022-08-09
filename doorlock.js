#!/usr/bin/env node

// ^^ above command tells shell to use Node.JS ^^ 

var BLYNK_TEMPLATE_ID = 'TMPLISLOZuxh'
var BLYNK_DEVICE_NAME = 'Door1' 
var BLYNK_AUTH_TOKEN = 'JMWyTq4EIyRiUv0aUTmnU7SIuhlzWIrE'
var SERVER_ADDR = 'https://sgp1.blynk.cloud/'

//*** SMARTPHONE DOORLOCK ***//

// ************* PARAMETERS *************** //
// 
// unlockedState and lockedState
// These params are in microseconds (ms)
// The servo pulse determines the degree 
// at which the horn is positioned. in this
// case, i get about 100 degrees of rotation
// from 1ms-2.2ms pulse width. i will have to change
// these when the amazon one arrives
// 
// motorPin
// The GPIO pin the signal wire on the servo
// is connected to i think it is white cable or orange
// depending on the servo
//
// buttonPin
// The GPIO pin the signal wire on the push button
// is connected to
//
// ledPin
// The Gpio pin the signal wire on the led
// is connected to. 
//
// blynkToken
// The token which was generated for the blynk website/app application
// project
//
// **************************************** //
var unlockedState = 1000; // was 1000
var lockedState = 1800; // was 2200
// difference of 800 is approx. 90 deg 


// DELTE THIS IS NOTHING FIXES
disconnect = function (reconnect) {
    console.log('Disconnect blynk');
    if (typeof reconnect === 'undefined') {
        reconnect = true;
    }

    var self = this;
    this.conn.disconnect();
    if (this.timerHb) {
        clearInterval(this.timerHb);
        this.timerHb = null;
    }
    this.emit('disconnect');
    //cleanup to avoid multiplying listeners
    this.conn.removeAllListeners();

    //starting reconnect procedure if not already in connecting loop and reconnect is true
    if (reconnect && !self.timerConn) {
        console.log("REARMING DISCONNECT");
        setTimeout(function () { self.connect() }, 5000);
    }
}
// INSIDE HERE 



var motorPin = 14;
var buttonPin = 4
var ledPinGreen = 17
var ledPinRed = 11 

var blynkToken = 'JMWyTq4EIyRiUv0aUTmnU7SIuhlzWIrE';



// *** Start code *** //

var locked = true

//Setup servo
var Gpio = require('pigpio').Gpio,
  motor = new Gpio(motorPin, {mode: Gpio.OUTPUT}),
  button = new Gpio(buttonPin, {
    mode: Gpio.INPUT,
    pullUpDown: Gpio.PUD_DOWN,
    edge: Gpio.FALLING_EDGE
  }),
  ledGreen = new Gpio(ledPinGreen, {mode: Gpio.OUTPUT});
  ledRed = new Gpio(ledPinRed, {mode: Gpio.OUTPUT});

//Setup blynk
var Blynk = require('blynk-library');
var blynk = new Blynk.Blynk(blynkToken, options = { 
connector : new Blynk.TcpClient()
});

// the ssl one which does not connect:
// 
// var blynk = new Blynk.Blynk(blynkToken);
//
//
// The TCP version which disconnects: 
//
// var blynk = new Blynk.Blynk(blynkToken, options = { 
// connector : new Blynk.TcpClient()
// });


var v0 = new blynk.VirtualPin(0);

console.log("locking door")
lockDoor()

button.on('interrupt', function (level) {
        console.log("level: " + level + " locked: " + locked)
        if (level == 0) {
                if (locked) {
                        unlockDoor()
                } else {
                        lockDoor()
                }
        }
});

v0.on('write', function(param) {
        console.log('V0:', param);
        if (param[0] === '0') { //unlocked
                unlockDoor()
                console.log("Door is unlocking...") // the web app will display unlocked
        } else if (param[0] === '1') { //locked
                lockDoor()
                console.log("Door is locking...") // the web app will display locked
        } else {
                blynk.notify("Door lock button was pressed with unknown parameter");
        }
});

//blynk.on('connect', function() { console.log("Blynk ready?"); });
//blynk.on('disconnect', function() { console.log("DISCONNECT"); });

function lockDoor() {
        motor.servoWrite(lockedState);
        ledRed.digitalWrite(0);
        ledGreen.digitalWrite(1);
        locked = true

        //notify
        blynk.notify("Door has been locked!");
  
        //After 1.5 seconds, the door lock servo turns off to avoid stall current
        setTimeout(function(){motor.servoWrite(0)}, 1500)

}

function unlockDoor() {
        motor.servoWrite(unlockedState);
        ledGreen.digitalWrite(0);
        ledRed.digitalWrite(1);
        locked = false

        //notify
        blynk.notify("Door has been unlocked!"); 

        //After 1.5 seconds, the door lock servo turns off to avoid stall current
        setTimeout(function(){motor.servoWrite(0)}, 1500)

}