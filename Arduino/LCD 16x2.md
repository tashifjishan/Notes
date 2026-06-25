

| LCD Pin | Connect To |
| ------- | ---------- |
| GND     | GND        |
| VCC     | 5V         |
| VO      | GND        |
| RS      | D12        |
| RW      | GND        |
| E       | D11        |
| DB4     | D5         |
| DB5     | D4         |
| DB6     | D3         |
| DB7     | D2         |
| LED+    | 5V(220 ohm ke saath)         |
| LED−    | GND        |



```cpp
#include <LiquidCrystal.h>

LiquidCrystal lcd(12, 11, 5, 4, 3, 2);

void setup() {
  lcd.begin(16, 2);
  lcd.print("Hello!");
}

void loop() {
}
```
