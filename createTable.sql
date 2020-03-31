CREATE TABLE grafana.SpeedTestLog (
id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY,
ping INT NOT NULL,
download INT  NOT NULL,
upload INT  NOT NULL,
connectionTimeOut BOOLEAN NOT NULL,
reg_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);