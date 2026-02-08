FUNCTION_BLOCK FB_StateMachine
VAR_INPUT
    Start : BOOL;
    Stop  : BOOL;
END_VAR

VAR_OUTPUT
    State : INT;
END_VAR

// States: 0=Idle, 1=Running, 2=Stopped
IF Start THEN
    State := 1;
END_IF;

IF Stop THEN
    State := 2;
END_IF;

IF NOT Start AND NOT Stop THEN
    State := 0;
END_IF;
