from huawei_solar import AsyncHuaweiSolar, register_names as rn

slave_id = 0
client = AsyncHuaweiSolar.create("192.168.1.132",6607, slave_id)

# Reading a single register

result = bridge.client.get(rn.NB_PV_STRINGS, slave_id)
print("Number of PV strings: ", result.value)

# Batched reading of multiple registers
# Only possible when they are located closely to each other in the Modbus register space

results = self.client.get_multiple([rn.LINE_VOLTAGE_A_B, rn.LINE_VOLTAGE_B_C, rn.LINE_VOLTAGE_C_A], self.slave_id)
print("A-B voltage: ", results[0].value)
print("B-C voltage: ", results[1].value)
print("C-A voltage: ", results[2].value)