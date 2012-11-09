// TemperatureTMP.cpp - Arduino library for retrieving data from Analog Devices TMP Temperature sensors
// Copyright 2012 Jeroen Doggen (jeroendoggen@gmail.com)
// For more information: variable declaration, changelog,... see TemperatureTMP.h
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

#include <Arduino.h>
#include <TemperatureTMP.h>

#define AREF 5

/// Constructor
TemperatureTMP::TemperatureTMP()
{
}

/// Begin function to set pins: temperaturePin = A0.
void
TemperatureTMP::begin()
{                                                 // default value: 20° Celcius
  begin (A0);
}

/// Begin variables
/// - int _temperaturePin: number indicating the temperature sensor pin: ANALOG IN
/// When you use begin() without variables standard values are loaded: A0
void TemperatureTMP::begin(int temperaturePin)
{
  pinMode(temperaturePin, INPUT);
  _temperaturePin=temperaturePin;
  setARefVoltage(5);
}

/// setARefVoltage(int _refV): Sets the AREF voltage to external, (now only takes 3.3 or 5 as parameter)
/// default is 5 when no AREF is used. When you want to use 3.3 AREF, put a wire between the AREF pin and the
/// 3.3 V VCC pin and change the  This increases accuracy
void TemperatureTMP::setARefVoltage(int refV)
{
  _refVoltage = refV;
  if (refV == 3)
  {
    analogReference(EXTERNAL);
  }
}

/// getTemperatureRaw(): Returns the temperature as a raw value: ADC output: 0 -> 1023
int TemperatureTMP::getTemperatureRaw()
{
  return (analogRead(_temperaturePin));
}

/// getTemperaturePercentage(): Returns the temperature percentage
float TemperatureTMP::getTemperatureCelcius()
{
  if (_refVoltage == 5)
  {
    return ( float(getTemperatureRaw()) * 0.5124 - 54.61);
// Calculation based on estimated tranfer function temp = 0.5124173 * ADCvalue - 54.61202  (for Aref = 5 Volt)
// Truncated to 4 significant digits because of the 10 bit ADC
  }
  if (_refVoltage == 3)
  {
    return ( float(getTemperatureRaw()) * 0.3382 - 54.61);
// Calculation based on estimated tranfer function temp = 0.3381954 * ADCvalue - 54.61202  (for Aref = 5 Volt)
// Truncated to 4 significant digits because of the 10 bit ADC
  }
}

/// getTemperaturePercentage(): Returns the temperature percentage
float TemperatureTMP::getTemperatureFahrenheit()
{
  return (( getTemperatureCelcius() * 9 / 5 )+ 32);
}
