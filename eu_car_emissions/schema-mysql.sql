CREATE TABLE euco2 (
  id       INTEGER PRIMARY KEY,  -- Identification number
  ms       VARCHAR(2),           -- Member state
  mp       VARCHAR(50),          -- Manufacturer pooling
  vfn      VARCHAR(25),          -- Vehicle family identification number
  mh       VARCHAR(50),          -- Manufacturer name, EU standard denomination
  man      VARCHAR(50),          -- Manufacturer name OEM declaration
  mms      VARCHAR(125),         -- Manufacturer name, MS registry denomination
  tan      VARCHAR(50),          -- Type approval number
  t        VARCHAR(25),          -- Type
  va       VARCHAR(25),          -- Variant
  ve       VARCHAR(35),          -- Version
  mk       VARCHAR(25),          -- Make
  cn       VARCHAR(50),          -- Commercial name
  ct       VARCHAR(5),           -- Category of the vehicle type approved
  cr       VARCHAR(5),           -- Category of the vehicle registered
  m        INTEGER,              -- Mass in running order, Completed/complete vehicle, (kg)
  mt       INTEGER,              -- WLTP test mass
  enedc    INTEGER,              -- Specific CO2 Emissions (NEDC), (g/km)
  ewltp    INTEGER,              -- Specific CO2 Emissions (WLTP), (g/km)
  w        INTEGER,              -- Wheel Base, (mm)
  at1      INTEGER,              -- Axle width steering axle, (mm)
  at2      INTEGER,              -- Axle width other axle, (mm)
  ft       VARCHAR(25),          -- Fuel type
  fm       VARCHAR(1),           -- Fuel mode
  ec       INTEGER,              -- Engine capacity, (cm³)
  ep       INTEGER,              -- Engine power,  (KW)
  z        INTEGER,              -- Electric energy consumption, (Wh/km)
  it       VARCHAR(25),          -- Innovative technology or group of innovative technologies
  ernedc   FLOAT,                -- Emissions reduction through innovative technologies, (g/km)
  erwltp   FLOAT,                -- Emissions reduction through innovative technologies (WLTP), (g/km)
  de       FLOAT,                -- Deviation factor
  vf       INTEGER,              -- Verification factor
  r        INTEGER               -- Total new registrations
);
