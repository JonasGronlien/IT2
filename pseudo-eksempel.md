## penger tjent per sang 
```pseudo
Set land to READ "Hvilket land er du fra?"
IF land EQUAL TO "Norge" 
    THEN DISPLAY "$0.44 per sang"
ELSE IF land Equal to "Sverige"
    THEN DISPLAY "$0.34 per sang"
ELSE 
    THEN DISPLAY "$0.24 per sang"
ENDIF
```
## Andel penger tjent per sang 

```pesudo 
Set streams to READ "hvor mange streams har sangen?"
IF streams is GREATER THAN "30 000 000"
    THEN DISPLAY "per sang er lik 70%"
ELSE IF streams is GREATER THAN "1 400 000"
    THEN DISPLAY "per sang lik 40%"
ELSE 
    THEN DISPLAY "per sang lik 0%"
ENDIF
```
