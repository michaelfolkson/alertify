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

[![](https://mermaid.ink/img/eyJjb2RlIjoic2VxdWVuY2VEaWFncmFtXG4gICAgcGFydGljaXBhbnQgQWxlcnRpZnlcbiAgICBBbGVydGlmeSAtPj4gbGlnaHRuaW5nZDogUmVxdWVzdCBjaGVjayBvbiBjaGFubmVsIGNoZWF0IGF0dGVtcHRcbiAgICBsaWdodG5pbmdkIC0-PiBiaXRjb2luZDogUmVxdWVzdCB0cmFuc2FjdGlvbiBkYXRhIG9mIHJldm9rZWQgc3RhdGVzXG4gICAgYml0Y29pbmQgLT4-IGxpZ2h0bmluZ2Q6IFJldHVybiB0cmFuc2FjdGlvbiBkYXRhXG4gICAgbGlnaHRuaW5nZCAtPj4gQWxlcnRpZnk6IENoZWF0IGF0dGVtcHQgZGV0ZWN0ZWRcbiAgICBBbGVydGlmeSAtPj4gVHdpbGlvOiBSZXF1ZXN0IHNlbmRpbmcgb2YgU01TXG4gICAgVHdpbGlvIC0-PiBDZWxscGhvbmU6IFNNUyB3YXJuaW5nXG4gICAgVHdpbGlvIC0-PiBBbGVydGlmeTogQ29uZmlybWF0aW9uIGhhc2giLCJtZXJtYWlkIjp7InRoZW1lIjoiZGVmYXVsdCJ9LCJ1cGRhdGVFZGl0b3IiOnRydWUsImF1dG9TeW5jIjp0cnVlLCJ1cGRhdGVEaWFncmFtIjp0cnVlfQ)
