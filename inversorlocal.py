import asyncio
import huawei_solar
from huawei_solar import create_tcp_client, SUN2000Device
from huawei_solar.register_names import (
    INPUT_POWER,
    ACTIVE_POWER,
    POWER_METER_ACTIVE_POWER,
)
from datetime import datetime
import pytz

# IP local del inversor
HOST = "192.168.0.111"


async def main():
    client = create_tcp_client(host=HOST)
    device = SUN2000Device(client, "SUN2000")

    try:
        input_power = await device.get(INPUT_POWER)
        active_power = await device.get(ACTIVE_POWER)
        power_meter_active_power = await device.get(POWER_METER_ACTIVE_POWER)

        # Publicar la hora local de un timezone particular
        tz_ES = pytz.timezone("Europe/Madrid")
        datetime_ES = datetime.now(tz_ES)

        print("")
        print("Energía entrada:     " + str(input_power.value))
        print("Energía generada:    " + str(active_power.value))
        print("Energía exportada:   " + str(power_meter_active_power.value))
        print(
            "Energía consumida:   "
            + str(active_power.value - power_meter_active_power.value)
        )
        print(
            "Fecha y hora:       ",
            datetime_ES.strftime("%d/%m/%Y y son las %H:%M:%S"),
        )
    except Exception as e:
        print(f"Error al leer el inversor: {e}")
    finally:
        await client.disconnect()


if __name__ == "__main__":
    asyncio.run(main())
