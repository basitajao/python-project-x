CREATE TABLE Property (
    Property_ID        INT AUTO_INCREMENT PRIMARY KEY,
    Property_Name      VARCHAR(255) NOT NULL,
    Street_Number      VARCHAR(20),
    Street_Name        VARCHAR(100),
    City               VARCHAR(100),
    State              VARCHAR(100),
    Property_Type      VARCHAR(50),
    Total_Units        INT,
    Property_Valuation DECIMAL(15, 2)
);

CREATE TABLE Unit (
    Unit_ID          INT AUTO_INCREMENT PRIMARY KEY,
    Property_ID      INT NOT NULL,
    Unit_Number      VARCHAR(20) NOT NULL,
    Unit_Type        VARCHAR(50),
    Base_Rent        DECIMAL(12, 2),
    Occupancy_Status VARCHAR(20) DEFAULT 'Available',
    CONSTRAINT fk_unit_property
        FOREIGN KEY (Property_ID) REFERENCES Property(Property_ID)
        ON DELETE CASCADE ON UPDATE CASCADE,
    CONSTRAINT chk_occupancy_status
        CHECK (Occupancy_Status IN ('Available', 'Occupied', 'Maintenance'))
);

CREATE TABLE Unit_Features (
    Feature_ID   INT AUTO_INCREMENT PRIMARY KEY,
    Unit_ID      INT NOT NULL,
    Feature_Name VARCHAR(50) NOT NULL,
    CONSTRAINT fk_feature_unit
        FOREIGN KEY (Unit_ID) REFERENCES Unit(Unit_ID)
        ON DELETE CASCADE ON UPDATE CASCADE,
    CONSTRAINT chk_feature_name
        CHECK (Feature_Name IN ('WiFi', 'AC', 'Ensuite', 'Balcony'))
);

CREATE TABLE Resident (
    Resident_ID   INT AUTO_INCREMENT PRIMARY KEY,
    First_Name    VARCHAR(100),
    Last_Name     VARCHAR(100),
    Email         VARCHAR(255) UNIQUE,
    Phone_Number  VARCHAR(20),
    University_ID VARCHAR(50),
    Check_In_Date DATE,
    Rent_History  TEXT
);

CREATE TABLE Investor (
    Investor_ID  INT AUTO_INCREMENT PRIMARY KEY,
    First_Name   VARCHAR(100),
    Last_Name    VARCHAR(100),
    Contact_Info TEXT,
    KYC_Status   VARCHAR(20) DEFAULT 'Pending',
    CONSTRAINT chk_kyc_status
        CHECK (KYC_Status IN ('Verified', 'Pending'))
);

CREATE TABLE Investment_Plan (
    Plan_ID                 INT AUTO_INCREMENT PRIMARY KEY,
    Property_ID             INT NOT NULL,
    Plan_Title              VARCHAR(255),
    Risk_Level              VARCHAR(10),
    Expected_ROI_Percentage DECIMAL(5, 2),
    Duration_Months         INT,
    Minimum_Buy_In          DECIMAL(15, 2),
    CONSTRAINT fk_plan_property
        FOREIGN KEY (Property_ID) REFERENCES Property(Property_ID)
        ON DELETE RESTRICT ON UPDATE CASCADE,
    CONSTRAINT chk_risk_level
        CHECK (Risk_Level IN ('Low', 'Medium', 'High'))
);

CREATE TABLE Investment_Transaction (
    Transaction_ID   INT AUTO_INCREMENT PRIMARY KEY,
    Investor_ID      INT NOT NULL,
    Plan_ID          INT NOT NULL,
    Amount_Invested  DECIMAL(15, 2) NOT NULL,
    Transaction_Date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    Payment_Method   VARCHAR(50),
    CONSTRAINT fk_transaction_investor
        FOREIGN KEY (Investor_ID) REFERENCES Investor(Investor_ID)
        ON DELETE RESTRICT ON UPDATE CASCADE,
    CONSTRAINT fk_transaction_plan
        FOREIGN KEY (Plan_ID) REFERENCES Investment_Plan(Plan_ID)
        ON DELETE RESTRICT ON UPDATE CASCADE
);

CREATE TABLE Employee (
    Employee_ID  INT AUTO_INCREMENT PRIMARY KEY,
    First_Name   VARCHAR(100),
    Last_Name    VARCHAR(100),
    Job_Title    VARCHAR(100),
    Access_Level INT,
    Hire_Date    DATE
);

CREATE TABLE Maintenance_Log (
    Log_ID           INT AUTO_INCREMENT PRIMARY KEY,
    Property_ID      INT NOT NULL,
    Task_Description TEXT,
    Maintenance_Cost DECIMAL(12, 2),
    Completion_Date  DATE,
    CONSTRAINT fk_log_property
        FOREIGN KEY (Property_ID) REFERENCES Property(Property_ID)
        ON DELETE RESTRICT ON UPDATE CASCADE
);

CREATE VIEW Investor_Portfolio_Value AS
SELECT
    Investor_ID,
    CONCAT(First_Name, ' ', Last_Name)     AS Investor_Name,
    COALESCE(SUM(Amount_Invested), 0.00)   AS Total_Portfolio_Value
FROM Investor
LEFT JOIN Investment_Transaction USING (Investor_ID)
GROUP BY Investor_ID, First_Name, Last_Name;

