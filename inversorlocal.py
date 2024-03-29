# coding=utf-8
import huawei_solar, pytz
#IP local del inversor
h = huawei_solar.HuaweiSolar(host="192.168.1.132")

input_power = h.get("input_power")
active_power = h.get("active_power")
power_meter_active_power = h.get("power_meter_active_power")

#Publicar la hora local de un timezone particular
from datetime import datetime
tz_ES = pytz.timezone('Europe/Madrid') 
datetime_ES = datetime.now(tz_ES)

print("Model:          " + str(h.get("model_name")))
#print("Model_ID:       " + str(h.get("model_id")))
#print("Serial N:       " + str(h.get("serial_number")))
#print("Pv_strings:     " + str(h.get("nb_pv_strings")))
#print("rated_power:    " + str(h.get("rated_power")))
#print("Time Zone:      " + str(h.get("time_zone")))
#print("System time:    " + str(h.get("system_time")))
#print("")
#print("PV01_voltage:   " + str(h.get("pv_01_voltage")))
#print("PV01_current:   " + str(h.get("pv_01_current")))
#print("Input power :   " + str(input_power))
#print("Active Power:   " + str(active_power))
#print("Reactive Power: " + str(h.get("reactive_power")))
#print("Eficiency:      " + str(h.get("efficiency")))
#print("Power factor:   " + str(h.get("power_factor")))
#print("Line V A_B:     " + str(h.get("line_voltage_A_B")))
#print("phase_A_current:" + str(h.get("phase_A_current")))
#print("PM_active_power:" + str(power_meter_active_power))
#print("")
#print("Input power :   " + str(input_power))
#print("Active Power:   " + str(active_power))
#print("PM_active_power:" + str(power_meter_active_power))
print("")
print("Energía entrada:     "  + str(input_power.value))
print("Energía generada:    "  + str(active_power.value))
print("Energía exportada:   "  + str(power_meter_active_power.value))
print("Energía consumida:   "  + str(active_power[0] - power_meter_active_power[0]))
print("Fecha y hora:       ",datetime_ES.strftime("%d/%m/%Y y son las %H:%M:%S"))
