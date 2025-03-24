from flask import Flask, render_template, request, jsonify

#GPIO
import RPi.GPIO as GPIO
GPIO_PIN_LED = 27
GPIO_PIN_BUTTON = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(GPIO_PIN_LED, GPIO.OUT)
GPIO.setup(GPIO_PIN_BUTTON, GPIO.IN, pull_up_down=GPIO.PUD_UP)

#Flask
app = Flask(__name__)

#Flask page d'accueil
@app.route('/')
def index():
    return render_template('index.html')
 
 #Flask allumer eteindre DEL
@app.route('/del', methods=['POST'])
def allumer_eteindre_del():
        isLed1On = request.json['isLed1On']
        if isLed1On:
            GPIO.output(GPIO_PIN_LED, GPIO.HIGH)
        else:
            GPIO.output(GPIO_PIN_LED, GPIO.LOW)
        return jsonify({'message': 'LED state updated successfully'})

#Flask lire bouton
@app.route('/bouton', methods=['GET'])
def lire_bouton():
    isButton1On = True if GPIO.input(GPIO_PIN_BUTTON) else False
    return jsonify({'isButton1On': isButton1On})

if __name__ == '__main__':
    app.run(host='0.0.0.0')
