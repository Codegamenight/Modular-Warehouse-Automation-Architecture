# Modular Warehouse Automation Architecture Portfolio

## Project Overview
This project implements a modular automation architecture for a robotic warehouse cell, integrating PLC control, robotics, SCADA visualization, and cloud-based remote monitoring.

## Objectives
- Standardize automation templates for multi-site deployment  
- Enable remote diagnostics and predictive maintenance  
- Demonstrate system architecture design methodology  

## System Components

### Hardware
- Yaskawa Motoman Robot (Simulated)
- PLC (Siemens / Beckhoff / Codesys)
- Conveyor System
- Vision Camera
- Safety System (PLCs, relays, light curtains)

### Software
- PLC Logic (IEC 61131-3)
- Robot Programs (Handshake Protocols)
- SCADA Visualization
- Python Middleware
- SQL Database
- OPC UA and MQTT Communication

## Folder Structure
- architecture_diagrams  
- plc_code  
- robot_programs  
- scada_screens  
- python_middleware  
- sql_schema  
- documentation  

## Key Features
- Modular PLC Function Blocks  
- Robot-PLC Handshake Interface  
- SCADA KPI Dashboard  
- Alarm and Event Logging  
- Cloud-Based Remote Monitoring  

##Finished project outlined Below.

# Modular-Warehouse-Automation-Architecture

## System Architecture

![System Architecture](architecture_diagrams/system_architecture.png)

This diagram shows PLC control, robot integration, SCADA visualization, Python middleware, and cloud monitoring architecture.

# Modular Warehouse Automation Architecture

## Overview
This project demonstrates a modular warehouse automation system integrating:

- **PLC Layer**: Siemens/Beckhoff function blocks for conveyor, robot handshake, alarms, and state machines.
- **Middleware Layer**: Python OPC UA client/server and MQTT publisher to transmit telemetry.
- **SCADA Layer**: JSON configurations for trends, alarms, and KPI dashboards.
- **Architecture**: System diagram showing data flow PLC → OPC UA → MQTT → SCADA → Cloud.

---

## Architecture Diagram
![System Architecture](architecture_diagrams/system_architecture.png)

---

## Folder Structure
- `plc_code/`: Modular PLC function blocks.
- `python_middleware/`: OPC UA client/server scripts and MQTT publisher.
- `scada_config/`: SCADA dashboard configuration files (alarms, trends, KPI).
- `docs/`: Documentation, architecture overview, test plans, and specs.

---

## Running the System

### 1. Activate Python Virtual Environment
```powershell
cd python_middleware
.\venv\Scripts\Activate.ps1

