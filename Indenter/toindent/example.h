// TemperatureTMP.h - Arduino library for retrieving data from Analog Devices TMP Temperature sensors
// Copyright 2012 Jeroen Doggen (jeroendoggen@gmail.com)
//
// Version History:
//  Version 0.1: TMP36: getTemperatureRaw, getTemperatureCelcius, getTemperatureFahrenheit
// Roadmap:
//  Version 0.2: Support for TMP35 & TMP37
//
// This library is free software; you can redistribute it and/or
// modify it under the terms of the GNU Lesser General Public
// License as published by the Free Software Foundation; either
// version 2.1 of the License, or (at your option) any later version.
//
// This library is distributed in the hope that it will be useful,
// but WITHOUT ANY WARRANTY; without even the implied warranty of
// MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
// Lesser General Public License for more details.
//
// You should have received a copy of the GNU Lesser General Public
// License along with this library; if not, write to the Free Software
// Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA

#ifndef TemperatureTMP_h
#define TemperatureTMP_h
#include <Arduino.h>

class TemperatureTMP
{
  public:
    TemperatureTMP();
    void begin();                                 // begin using default values
    void begin(int temperaturePin);               // begin using a user selected analog pin

    void setARefVoltage(int refVoltage);          // set analog reference voltage

    int getTemperatureRaw();                      // get the temperature raw ADC value
    float getTemperatureCelcius();                // get the temperature in degrees Celcius
    float getTemperatureFahrenheit();             // get the temperature in degrees Fahrenheit

  private:
    int _temperaturePin;                          // analog pin where the sensor is connected
    int _refVoltage;                              // analog reference voltage (for the ADC and the sensor Vcc!)
};
#endif
