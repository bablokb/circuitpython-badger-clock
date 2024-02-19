# ----------------------------------------------------------------------------
# template/configuration-pyportal.py: runtime configuration settings template
# for Adafruit's Py-Portal.
#
# Adapt to your needs (credentials, active-time, hardware, ui) and rename to
# configuration.py
#
# Author: Bernhard Bablok
# License: GPL3
#
# Website: https://github.com/bablokb/circuitpython-clock
#
# ----------------------------------------------------------------------------

import board
from adafruit_pcf8523.pcf8523 import PCF8523
#import adafruit_ds3231        # DS3231 support
import adafruit_ahtx0          # AHT20
import adafruit_bus_device

class Settings:
  pass

# --- some containers ---

settings = Settings()
secrets  = Settings()
pins     = Settings()
ui       = Settings()

# --- WLAN credentials ---

secrets.ssid      = 'your_ssid'
secrets.password  = 'your_password'
secrets.retry     = 1
secrets.debugflag = False
secrets.channel   = 6        # optional
secrets.timeout   = 10       # optional

# optional for static IP configuration (for faster connects)
#secrets.hostname  = 'cpclock'
#secrets.address   = '192.168.100.42'
#secrets.netmask   = '255.255.255.255'
#secrets.gateway   = '192.168.100.1'
#secrets.dns       = '192.168.100.1'

# --- update via time-api ---

settings.TIMEAPI_URL      = "http://worldtimeapi.org/api/ip"
settings.TIMEAPI_UPD_HOUR = 8
settings.TIMEAPI_UPD_MIN  = 30

# --- sensor settings ---

settings.TEMP_OFFSET = 0
settings.HUM_OFFSET  = 0

# --- active time ---

#settings.ACTIVE_END_TIME   = "-1:00"           # always active
settings.ACTIVE_END_TIME    = "22:00"
#settings.ACTIVE_START_TIME = "07:00"           # start at time-point
settings.ACTIVE_START_TIME  = None              # start using a button

# --- hardware-setup ---

i2c = board.I2C()
settings.display = lambda: board.DISPLAY        # use builtin display
settings.deep_sleep = False

settings.rtc_ext = lambda: None                # no external RTC
#settings.rtc_ext = lambda: PCF8523(i2c)
#settings.rtc_ext = lambda: adafruit_ds3231.DS3231(i2c)

settings.sensor = lambda: None                 # no temp/humidity sensor
#settings.sensor = lambda: adafruit_ahtx0.AHTx0(i2c)

settings.wifi_module = "wifi_impl_esp32spi"     # implementing module

# --- pins ---

pins.PIN_ESP_BUSY  = board.ESP_BUSY
pins.PIN_ESP_GPIO0 = board.ESP_GPIO0
pins.PIN_ESP_RESET = board.ESP_RESET
pins.PIN_ESP_CS    = board.ESP_CS   
pins.PIN_SCK       = board.SCK
pins.PIN_MOSI      = board.MOSI
pins.PIN_MISO      = board.MISO
pins.PIN_ALARM = None                           # no wakeup pin

# --- UI ---

ui.fg_color  = 0x00FF00                         # green
ui.bg_color  = 0x000000                         # black
ui.font_s    = "DejaVuSans-Bold-24-min.bdf"     # small font
ui.font_l    = "DejaVuSans-Bold-52-min.bdf"     # large font
ui.day_names = {
  0: 'Montag',      1: 'Dienstag',  2: 'Mittwoch',
  3: 'Donnerstag',  4: 'Freitag',   5: 'Samstag',  6: 'Sonntag'
  }
ui.date_fmt  = "{0:02d}.{1:02d}.{2:02d}"        # dd.mm.yy

#ui.day_names = {
#  0: 'Monday',      1: 'Tuesday',   2: 'Wednesday',
#  3: 'Thursday',    4: 'Friday',    5: 'Saturday',  6: 'Sunday'
#  }
#ui.date_fmt  = "{1:02d}/{0:02d}/{2:02d}"       # mm/dd/yy
