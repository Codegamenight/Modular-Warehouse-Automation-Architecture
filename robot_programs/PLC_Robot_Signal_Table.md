# PLC - Robot Handshake Signal Table

| Signal Name      | PLC Address | Robot IO | Direction | Description |
|------------------|-------------|-----------|-----------|-------------|
| PLC_Request      | Q0.0        | DI[1]     | PLC -> Robot | Start robot cycle |
| Robot_Busy       | I0.0         | DO[1]     | Robot -> PLC | Robot executing task |
| Robot_Done       | I0.1         | DO[2]     | Robot -> PLC | Task completed |
| Robot_Fault      | I0.2         | DO[3]     | Robot -> PLC | Fault state |
| PLC_Reset        | Q0.1        | DI[2]     | PLC -> Robot | Reset faults |
