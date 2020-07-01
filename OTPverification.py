import random

import nexmo

otp = "your        OTP           is ...." + str(random.randint(0, 9)) + "   " + str(random.randint(0, 9)) + "   " + str(
    random.randint(0, 9)) + "   " + str(random.randint(0, 9))
otp2 = "    .........    I     repeat " + otp
client = nexmo.Client(
    application_id='',
    private_key='private.key',
)
ncco = [{
    'action': 'talk',
    'voiceName': 'Joey',
    'text': otp + otp2
}]

response = client.create_call({
    'to': [{
        'type': 'phone',
        'number': '918851408462'
    }],
    'from': {
        'type': 'phone',
        'number': '918851408462'
    },
    'ncco': ncco
})
