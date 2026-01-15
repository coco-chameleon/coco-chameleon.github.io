.. SPDX-FileCopyrightText: 2026 Sam Hanes <sam@maltera.com>
.. SPDX-License-Identifier: CC-BY-SA-4.0

************************
CoCo Cartridge Interface
************************

===  =============  ===========
Pin  Signal         Description
===  =============  ===========
  1  :net:`-12V`    RS-323 power supply, only on CoCo 1
  2  :net:`+12V`    RS-323 power supply, only on CoCo 1
  3  :net:`HALT*`   puts the CPU in a wait state
  4  :net:`NMI*`    triggers a CPU non-maskable interrupt
  5  :net:`RESET*`  system reset / power good
  6  :net:`E`       main CPU clock
  7  :net:`Q`       quadrature clock
  8  :net:`CART*`   interrupt input for Program Pak detection
  9  :net:`+5V`     main logic power supply
 10  :net:`D0`      CPU data bus
 11  :net:`D1`      CPU data bus
 12  :net:`D2`      CPU data bus
 13  :net:`D3`      CPU data bus
 14  :net:`D4`      CPU data bus
 15  :net:`D5`      CPU data bus
 16  :net:`D6`      CPU data bus
 17  :net:`D7`      CPU data bus
 18  :net:`R/W*`    CPU read/write signal
 19  :net:`A0`      CPU address bus
 20  :net:`A1`      CPU address bus
 21  :net:`A2`      CPU address bus
 22  :net:`A3`      CPU address bus
 23  :net:`A4`      CPU address bus
 24  :net:`A5`      CPU address bus
 25  :net:`A6`      CPU address bus
 26  :net:`A7`      CPU address bus
 27  :net:`A8`      CPU address bus
 28  :net:`A9`      CPU address bus
 29  :net:`A10`     CPU address bus
 30  :net:`A11`     CPU address bus
 31  :net:`A12`     CPU address bus
 32  :net:`CTS*`    cartridge ROM select
 33  :net:`GND`
 34  :net:`GND`
 35  :net:`SND`     sound input to CoCo audio mux
 36  :net:`SCS*`    cartridge IO select
 37  :net:`A13`     CPU address bus
 38  :net:`A14`     CPU address bus
 39  :net:`A15`     CPU address bus
 40  :net:`SLENB*`  disables CoCo internal peripherals
===  =============  ===========

:net:`CTS*` Select
==================

:net:`CTS*` is the primary select line for the cartridge.
It's asserted when:

1. the MPU reads from the range 0xC000 - 0xFEFF (16k words)
2. the SAM is in address map type 0 (ROMs)
3. :net:`SLENB*` is not asserted
4. the :net:`E` clock is high


:net:`SCS*` Select
==================

:net:`SCS*` is a secondary / spare select line for the cartridge.
It's typically used for IO devices like floppy controllers.
It's asserted when:

1. the MPU reads or writes in the range 0xFF40 - 0xFF5F
2. :net:`SLENB*` is not asserted


:net:`CART*` Interrupt
======================

:net:`CART*` is used to indicate that a cartridge with a ROM in the
:net:`CTS*` region is connected and the system should boot from it.
It's connected to :net:`CB1` on PIA2, which is an edge-triggered
interrupt input that asserts the MPU's :net:`FIRQ*` interrupt.
Program Paks usually wire this directly to the :net:`Q` clock.

:net:`SLENB*` and Address Decoding
==================================

All three CoCos use a 74-138 decoder to generate the select lines for
most of their peripherals. Unlike other microprocessor systems, the
decoder's inputs are driven by the S0..S2 device select outputs from
the SAM (MC8803) rather than the processor address lines. 


