Checks site for Bitcoin price data

Process diagram: https://v.gd/0cBnHM

```mermaid
sequenceDiagram
    participant Alertify
    Alertify ->> Bitfinex: Request Bitcoin price
    Bitfinex ->> Alertify: Bitcoin price
    Alertify ->> Twilio: Request sending of SMS
    Twilio ->> Cellphone: SMS
    Twilio ->> Alertify: Confirmation hash
```

Pinging c-lightning node

Process diagram: https://v.gd/ouBvmq

```mermaid
sequenceDiagram
    participant Alertify
    Alertify ->> c-lightning: Ping
    c-lightning ->> Alertify: Pong
    Alertify ->> Twilio: Request sending of SMS
    Twilio ->> Cellphone: SMS
    Twilio ->> Alertify: Confirmation hash
```

Receive SMS alert when there is Lightning channel cheat attempt

Process diagram: https://v.gd/3uyJKP

```mermaid
sequenceDiagram
    participant Alertify
    Alertify ->> lightningd: Request check on channel cheat attempt
    lightningd ->> bitcoind: Request transaction data of revoked states
    bitcoind ->> lightningd: Return transaction data
    lightningd ->> Alertify: Cheat attempt detected
    Alertify ->> Twilio: Request sending of SMS
    Twilio ->> Cellphone: SMS warning
    Twilio ->> Alertify: Confirmation hash
 ```
