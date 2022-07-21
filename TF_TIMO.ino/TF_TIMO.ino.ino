#include <SPI.h>    // Interfaz SPI
#include <SD.h>     // Tarjetas SD

#include <DHT.h>    // Adafruit DHT
#include <DHT_U.h>  // Adafruit Unified Sensor

#include <RTClib.h> // Adafruit RTC (timer)

// -----------------------------------------------------------------------------------------------------------------
// Configuración previa: DHT11 ------------------------------------|
#define DHTpin 4         // pin digital 4 (señal de DHT11)

DHT dht(DHTpin, DHT11);  // objeto DHT: dht, pin 4 y modelo DHT11

float temp;    // Nota: en C se crean la variable sin necesidad de asigna el valor
int hr;

// Configuración previa: microSD card adapter ---------------------|
#define SSpin 10        // pin digital 10 (Slave Select)

File datos;             // objeto File: datos

// Configuración previa: RTC --------------------------------------|
RTC_DS3231 rtc;       // objeto RTC_DS3231: rtc

// Horas ----------------------------------------------------------|
int h0 = 0; int h1 = 1; int h2 = 2; int h3 = 3; int h4 = 4; int h5 = 5; int h6 = 6;
int h7 = 7; int h8 = 8; int h9 = 9; int h10 = 10; int h11 = 11; int h12 = 12;
int h13 = 13; int h14 = 14; int h15 = 15; int h16 = 16; int h17 = 17; int h18 = 18;
int h19 = 19; int h20 = 20; int h21 = 21; int h22 = 22; int h23 = 23;

// Programación de ejecución única ---------------------------------------------------------------------------------
void setup() {
  
  // ---------------------------------------------------------------|
  Serial.begin(9600);   // Inicio: monitor serie a 9600 bps
  dht.begin();          // Inicio: sensor DHT11

  // test: Inicializar microSD card adapter
  if (! SD.begin(SSpin)) {                                       // si no se inicializa el controlador...
    Serial.println("Error: lectura de microSD card adapter.");   // imprimir mensaje y...
    return;                                                      // retornar vacío (finalizar configuración setup)
    }

  // test: Inicializar RTC
  if (! rtc.begin()) {
    Serial.println("Error: lectura de RTC.");
    while (1); 
    }

  // establecer horario actual
  rtc.adjust(DateTime(__DATE__, __TIME__));
  Serial.print("abcdefg");
  //datos.println("date,hour,temp_DHT,hr_DHT"); // encabezado

}

// Programación de ejecución recurrente
void loop() {
  
  DateTime date = rtc.now();

  // en cada hora
  if ( (date.hour()==h0 || date.hour()==h1 || date.hour()==h2 || date.hour()==h3 || date.hour()==h4 || date.hour()==h5 || date.hour()==h6 || date.hour()==h7 || date.hour()==h8 || date.hour()==h9 || date.hour()==h10 || date.hour()==h11 || date.hour()==h12 || date.hour()==h13 || date.hour()==h14 || date.hour()==h15 || date.hour()==h16 || date.hour()==h17 || date.hour()==h18 || date.hour()==h19 || date.hour()==h20 || date.hour()==h21 || date.hour()==h22 || date.hour()==h23) && (date.minute()==0 && date.second()==0) ) {
    
    // abrir (o crear y abrir) archivo: data.txt
    datos = SD.open("data.txt", FILE_WRITE);

    if (datos) {  // Si se abrió el archivo correctamente...

      // Lectura en el instante i
      temp = dht.readTemperature();    // leer temperatura
      hr = dht.readHumidity();         // leer humedad
      
      // Guardado en data.txt
      datos.print(date.year());    // escribir: año
      datos.print("-");
      datos.print(date.month());   // escribir: mes
      datos.print("-");
      datos.print(date.day());     // escribir: día
      
      datos.print(",");
      datos.print(date.hour());    // escribir: hora
      datos.print(":");
      datos.print(date.minute());  // escribir: minuto
      datos.print(":");
      datos.print(date.second());  // escribir: segundo
      
      datos.print(",");     // separador: ,
      datos.print(temp);    // escribir: temperatura
      datos.print(",");     // separador: ,
      datos.println(hr);    // escribir: humedad + salto de linea

      // Mostrar línea registrado en monitor serial
      Serial.print(date.year());    // escribir: año
      Serial.print("-");
      Serial.print(date.month());   // escribir: mes
      Serial.print("-");
      Serial.print(date.day());     // escribir: día
      
      Serial.print(",");
      Serial.print(date.hour());    // escribir: hora
      Serial.print(":");
      Serial.print(date.minute());  // escribir: minuto
      Serial.print(":");
      Serial.print(date.second());  // escribir: segundo
      
      Serial.print(",");     // separador: ,
      Serial.print(temp);    // escribir: temperatura
      Serial.print(",");     // separador: ,
      Serial.println(hr);    // escribir: humedad + salto de linea
    
      Serial.println("Guardado correcto");  // Aviso de almacenamiento adecuado
      }
    
    else {
      Serial.println("Error: no se pudo guardar");
      }
    
    datos.close();        // cerrar archivo
    
    }
  
  delay(1000);  // cada segundo comprobar la condición
  
}
