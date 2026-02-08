FUNCTION_BLOCK FB_ConveyorControl
VAR_INPUT
    StartCmd   : BOOL;
    StopCmd    : BOOL;
    FaultReset : BOOL;
END_VAR

VAR_OUTPUT
    ConveyorRun : BOOL;
    FaultActive : BOOL;
END_VAR

VAR
    InternalFault : BOOL;
END_VAR

IF FaultReset THEN
    InternalFault := FALSE;
END_IF;

IF StartCmd AND NOT StopCmd AND NOT InternalFault THEN
    ConveyorRun := TRUE;
ELSIF StopCmd THEN
    ConveyorRun := FALSE;
END_IF;

// Simulated fault condition placeholder
IF ConveyorRun = TRUE AND FALSE THEN
    InternalFault := TRUE;
END_IF;

FaultActive := InternalFault;
