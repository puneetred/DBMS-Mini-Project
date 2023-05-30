DROP DATABASE blood_bank_management;

CREATE DATABASE blood_bank_management;

USE blood_bank_management;

CREATE TABLE donors (
  donor_id INT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(50) NOT NULL,
  blood_group VARCHAR(5) NOT NULL,
  date_of_birth DATE,
  gender VARCHAR(10),
  contact_number VARCHAR(15),
  email VARCHAR(50),
  address VARCHAR(100),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

CREATE TABLE recipients (
  recipient_id INT AUTO_INCREMENT PRIMARY KEY,
  name VARCHARc50) NOT NULL,
  blood_group VARCHAR(5) NOT NULL,
  age INT,
  gender VARCHAR(10),
  contact_number VARCHAR(15),
  email VARCHAR(50),
  address VARCHAR(100),
  medical_history TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

CREATE TABLE blood_inventory (
  blood_id INT AUTO_INCREMENT PRIMARY KEY,
  blood_group VARCHAR(5) NOT NULL,
  quantity INT NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

CREATE TABLE donations (
  donation_id INT AUTO_INCREMENT PRIMARY KEY,
  donor_id INT,
  blood_group VARCHAR(5),
  donation_date DATE,
  FOREIGN KEY (donor_id) REFERENCES donors(donor_id),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

CREATE TABLE transfusions (
  transfusion_id INT AUTO_INCREMENT PRIMARY KEY,
  recipient_id INT,
  blood_group VARCHAR(5),
  transfusion_date DATE,
  FOREIGN KEY (recipient_id) REFERENCES recipients(recipient_id),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- Trigger for updating blood inventory after a new donation
DELIMITER //
CREATE TRIGGER after_donation_insert
AFTER INSERT ON donations
FOR EACH ROW
BEGIN
    -- Update the blood_inventory table by increasing the quantity for the corresponding blood group
    UPDATE blood_inventory
    SET quantity = quantity + 1
    WHERE blood_group = NEW.blood_group;
END//
DELIMITER ;

-- Trigger for updating blood inventory after a new transfusion
DELIMITER //
CREATE TRIGGER after_transfusion_insert
AFTER INSERT ON transfusions
FOR EACH ROW
BEGIN
    -- Update the blood_inventory table by decreasing the quantity for the corresponding blood group
    UPDATE blood_inventory
    SET quantity = quantity - 1
    WHERE blood_group = NEW.blood_group;
END//
DELIMITER ;

USE blood_bank_management;

