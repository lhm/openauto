CREATE TABLE eu_co2 (
    id         INTEGER PRIMARY KEY, -- Identification number
    ms         TEXT,                -- Member state
    mp         TEXT,                -- Manufacturer pooling
    vfn        TEXT,                -- Vehicle family identification number
    mh         TEXT,                -- Manufacturer name, EU standard denomination
    man        TEXT,                -- Manufacturer name OEM declaration
    mms        TEXT,                -- Manufacturer name, MS registry denomination
    tan        TEXT,                -- Type approval number
    t          TEXT,                -- Type
    va         TEXT,                -- Variant
    ve         TEXT,                -- Version
    mk         TEXT,                -- Make
    cn         TEXT,                -- Commercial name
    ct         TEXT,                -- Category of the vehicle type approved
    cr         TEXT,                -- Category of the vehicle registered
    m          INTEGER,             -- Mass in running order, completed/complete vehicle (kg)
    mt         INTEGER,             -- WLTP test mass
    enedc      INTEGER,             -- Specific CO2 Emissions (NEDC), (g/km)
    ewltp      INTEGER,             -- Specific CO2 Emissions (WLTP), (g/km)
    w          INTEGER,             -- Wheel Base, (mm)
    at1        INTEGER,             -- Axle width steering axle, (mm)
    at2        INTEGER,             -- Axle width other axle, (mm)
    ft         TEXT,                -- Fuel type
    fm         TEXT,                -- Fuel mode
    ec         INTEGER,             -- Engine capacity, (cm³)
    ep         INTEGER,             -- Engine power, (KW)
    z          INTEGER,             -- Electric energy consumption, (Wh/km)
    it         TEXT,                -- Innovative technology or group of innovative technologies
    ernedc     REAL,                -- Emissions reduction through innovative technologies, (g/km)
    erwltp     REAL,                -- Emissions reduction through innovative technologies (WLTP), (g/km)
    de         REAL,                -- Deviation factor
    vf         INTEGER,             -- Verification factor
    r          INTEGER              -- Total new registrations
);
