FUNCTION_BLOCK FB_AlarmManager
VAR_INPUT
    FaultInput : BOOL;
END_VAR

VAR_OUTPUT
    AlarmActive : BOOL;
    AlarmCode   : INT;
END_VAR

IF FaultInput THEN
    AlarmActive := TRUE;
    AlarmCode := 1001; // Example fault code
ELSE
    AlarmActive := FALSE;
    AlarmCode := 0;
END_IF;
