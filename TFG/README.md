# Demo Network Environment

```flux
import "http"
import "json"
import "influxdata/influxdb/secrets"
option task = { 
  name: "Send Critical Email",
  every: 10m,
}

SENDGRID_APIKEY = secrets.get(key: "SENDGRID_APIKEY")

numberOfCrits = from(bucket: "requests_scores")
    |> range(start: -10m)
    |> filter(fn: (r) => r._measurement == "weblogs" and r._value >= 80)
    |> count()

numberOfCrits
    |> map(
        fn: (r) => if r._value > 0 then
            {r with _value: http.post(
                url: "https://api.sendgrid.com/v3/mail/send",
                headers: {"Content-Type": "application/json", "Authorization": "Bearer ${SENDGRID_APIKEY}"},
                data: json.encode(
                    v: {
                        "personalizations": [
                            {
                                "to": [
                                    {
                                        "email": "uo276341@uniovi.es"
                                    }
                                ]
                            }
                        ],
                        "from": {
                            "email": "antonio.paya@thenextpangea.com"
                        },
                        "subject": "IDS critical alert",
                        "content": [
                            {
                                "type": "text/plain",
                                "value": "El IDS ha detectado una peticion de anomaly score ${r._value} identificada como critica."
                            }
                        ]
                    }
                )
            )}
        else
            {r with _value: 0},
    )
```
