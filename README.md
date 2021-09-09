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

[![](https://mermaid.ink/img/eyJjb2RlIjoic2VxdWVuY2VEaWFncmFtXG4gICAgcGFydGljaXBhbnQgQWxlcnRpZnlcbiAgICBBbGVydGlmeSAtPj4gQml0ZmluZXg6IFJlcXVlc3QgQml0Y29pbiBwcmljZVxuICAgIEJpdGZpbmV4IC0-PiBBbGVydGlmeTogQml0Y29pbiBwcmljZVxuICAgIEFsZXJ0aWZ5IC0-PiBUd2lsaW86IFJlcXVlc3Qgc2VuZGluZyBvZiBTTVNcbiAgICBUd2lsaW8gLT4-IENlbGxwaG9uZTogU01TXG4gICAgVHdpbGlvIC0-PiBBbGVydGlmeTogQ29uZmlybWF0aW9uIGhhc2giLCJtZXJtYWlkIjp7InRoZW1lIjoiZGVmYXVsdCJ9LCJ1cGRhdGVFZGl0b3IiOmZhbHNlLCJhdXRvU3luYyI6dHJ1ZSwidXBkYXRlRGlhZ3JhbSI6ZmFsc2V9)](https://mermaid-js.github.io/mermaid-live-editor/edit/##eyJjb2RlIjoic2VxdWVuY2VEaWFncmFtXG4gICAgcGFydGljaXBhbnQgQWxlcnRpZnlcbiAgICBBbGVydGlmeSAtPj4gQml0ZmluZXg6IFJlcXVlc3QgQml0Y29pbiBwcmljZVxuICAgIEJpdGZpbmV4IC0-PiBBbGVydGlmeTogUkJpdGNvaW4gcHJpY2VcbiAgICBBbGVydGlmeSAtPj4gVHdpbGlvOiBSZXF1ZXN0IHNlbmRpbmcgb2YgU01TXG4gICAgVHdpbGlvIC0-PiBDZWxscGhvbmU6IFNNU1xuICAgIFR3aWxpbyAtPj4gQWxlcnRpZnk6IENvbmZpcm1hdGlvbiBoYXNoIiwibWVybWFpZCI6IntcbiAgXCJ0aGVtZVwiOiBcImRlZmF1bHRcIlxufSIsInVwZGF0ZUVkaXRvciI6ZmFsc2UsImF1dG9TeW5jIjp0cnVlLCJ1cGRhdGVEaWFncmFtIjpmYWxzZX0)

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

[![](https://mermaid.ink/img/eyJjb2RlIjoic2VxdWVuY2VEaWFncmFtXG4gICAgcGFydGljaXBhbnQgQWxlcnRpZnlcbiAgICBBbGVydGlmeSAtPj4gYy1saWdodG5pbmc6IFBpbmdcbiAgICBjLWxpZ2h0bmluZyAtPj4gQWxlcnRpZnk6IFBvbmdcbiAgICBBbGVydGlmeSAtPj4gVHdpbGlvOiBSZXF1ZXN0IHNlbmRpbmcgb2YgU01TXG4gICAgVHdpbGlvIC0-PiBDZWxscGhvbmU6IFNNU1xuICAgIFR3aWxpbyAtPj4gQWxlcnRpZnk6IENvbmZpcm1hdGlvbiBoYXNoIiwibWVybWFpZCI6eyJ0aGVtZSI6ImRlZmF1bHQifSwidXBkYXRlRWRpdG9yIjpmYWxzZSwiYXV0b1N5bmMiOnRydWUsInVwZGF0ZURpYWdyYW0iOmZhbHNlfQ)
