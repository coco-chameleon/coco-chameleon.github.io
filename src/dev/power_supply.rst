.. SPDX-FileCopyrightText: 2026 Sam Hanes <sam@maltera.com>
.. SPDX-License-Identifier: CC-BY-SA-4.0

************
Power Supply
************


Power Available From the Host
=============================


CoCo 1
******

The service manual for the CoCo 1 is quite explicit about its power
limits (on page 36 for the system and page 39 for the cartridge):

====  ======  =============
Rail  Rating  Cartridge Max
====  ======  =============
 +5V  1.35 A  300 mA
 -5V  100 uA
+12V  400 mA  300 mA
-12V  100 mA  100 mA
====  ======  =============



CoCo 2
******

The CoCo 2 power transformer provides a 17.2 VAC center-tapped
secondary winding rated for a maximum of 1.8 amps RMS.

CoCo 2 Service Manual page 40
SALT regulation

shunt resistor measures 0.097 ohms
shunt voltage ~ 70 mV at idle

drawing 1.31 A through the cartridge port
puts shunt voltage at 200.2 mV (~ 2 A)
seems stable, 4.73 V at cartridge port

at 1.1 A through the cartridge port (179 mV shunt)
the system draws its nameplate 0.2 A from the mains

SALT appears to trip at 213 mV shunt
that's 1.5 A through the cartridge port


CoCo 3
******


MultiPak
********



.. [sm1p38] Radio Shack,
   *Service Manual: TRS-80 Color Computer, Catalog Number 26-3001/3002*
   (Tandy Corporation, 1980), 38-39,
   https://colorcomputerarchive.com/repo/Documents/Manuals/Hardware/Color%20Computer%201%20Service%20Manual%20(26-3001%20&%2026-3002)%20(Tandy).pdf
