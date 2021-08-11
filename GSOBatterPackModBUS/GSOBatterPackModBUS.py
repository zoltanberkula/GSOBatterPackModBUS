import pymodbus
import time
from pymodbus.client.sync import ModbusSerialClient

device_address = 0x03
funcCode = 0x03 #reading input registers
start_address = 0x03EB
baudRate = 9600

###Basic Information
basic_reg_address = {
    "TotalSystemVoltage": 20000,
    "TotalSystemCurrent": 20001,
    "SystemSOC": 20002,
    "MaxVsysCell": 20003,
    "MinVsysCell": 20004,
    "AvgVsysCell": 20005,
    "HighestTempBatCell": 20006,
    "LowestTempBatCell": 20007,
    "AvgTempBatCell": 20008,
    "Not used0": 20009,
    "Not used1": 20010,
    "Not used2": 20011,
    "Not used3": 20012,
    "SysUnitPressDif": 20013,
    "SysUnitTempDif": 20014,
    "SysTotalCurrent": 20015,
    "HighestSingleClustNum": 20016,
    "SerNumSysHighSingleClust": 20017,
    "LowestCLusterNum": 20018,
    "SerNumSysLowClust": 20019,
    "SysHighTClustNum": 20020,
    "SerNumLowTClust": 20021,
    "SysHighTClustNum": 20022,
    "SerNumLowTClust": 20023,
    "TotalSysCapacity": 20024,
    "SysRemainingCapacity": 20025,
    "soh": 20026,
    "BatteryFullSign": 20027,
    "BatteryEmptyFlag": 20028,
    "NumOfClusters": 20029,
    "Not used4": 20030,
    "Terminating": None
    }

###Accident Information
accident_reg_address = {
    "Not used5": 20063,
    "TotalChargingVoltageHigh": 20064,
    "TotalChargingVoltageLow": 20065,
    "SysCharUnitOverV": 20066,
    "SysCharUnitUnderV": 20067,
    "SysCharPressDifLarge": 20068,
    "SysCharTempHigh": 20069,
    "SysCharTempLow": 20070,
    "SysCharTempDifLarge": 20071,
    "SysCharOverCurr": 20072,
    "SysTotDischVHigh": 20073,
    "SysTotDischVLow": 20074,
    "SysDischCellOverV": 20075,
    "SysDischCellUnderV": 20076,
    "SysDischVDifLarge": 20077,
    "SysDischTLow": 20078,
    "SysDischTHigh": 20079,
    "SysDischTDifLarge": 20080,
    "SysDischOverCurr": 20081,
    "SysSocLow": 20082,
    "SysInsResLow":20083,
    "Not used6": 20084,
    "Terminating": None
    }

###HMI Interface Basic Information
hmi_basic_reg_address = {
    "NClusterTotalVoltage": 21000,
    "NClusterTotalCurrent": 21001,
    "NClusterSOC": 21002,
    "NClusterSingleCellMaxVoltage": 21003,
    "NClusterSingleCellMinVoltage": 21004,
    "NClusterSingleCellAvgVoltage": 21005,
    "NClusterCellHighestTemp": 21006,
    "NClusterCellLowestTemp": 21007,
    "NClusterCellAvgTemp": 21008,
    "NClusterHighestMonNum": 21009,
    "NClusterLowestMonNum": 21010,
    "NClusterMaxTempSerNum": 21011,
    "NClusterLowestTempSerNum": 21012,
    "NClusterMonomerPressDiff": 21013,
    "NClusterMonomerTempDiff": 21014,
    "NClusterTotalCurrent": 21015,
    "Not used": 21016,
    "Not used": 21017,
    "Not used": 21018,
    "Not used": 21019,
    "Not used": 21020,
    "Not used": 21021,
    "Not used": 21022,
    "Not used": 21023,
    "NClusterTotalCapacity": 21024,
    "NClusterRemainingCapacity": 21025,
    "SOH": 21026,
    "BatteryFullSign": 21027,
    "BatteryEmptyFlag": 21028,
    "NumOfSingleCells": 21029,
    "NumOfMonomerTemp": 21030,
    }

###HMI Interface Accident Information
hmi_accident_reg_address = {
    "NClusterTotalChargVoltHigh": 21064,
    "NClusterTotalChargVoltLow": 21065,
    "NClusterChargingCellOvervoltage": 21066,
    "NClusterChargingCellUndervoltage": 21067,
    "NClusterChargingVoltageDiffLarge": 21068,
    "NClusterChargingTempHigh": 21069,
    "NClusterChargingTempLow": 21070,
    "NClusterTempDiffLarge": 21071,
    "NClusterChargingOvercurrent": 21072,
    "NClusterDischTotalVoltHigh": 21073,
    "NClusterDischTotalVoltLow": 21074,
    "NClusterDischCellOvervoltage": 21075,
    "NClusterDischCellUndervoltage": 21076,
    "NClusterDischVoltageDiffLarge": 21077,
    "NClusterDischTempHigh": 21078,
    "NClusterDischTempLow": 21079,
    "NClusterDischTempDiffLarge": 21080,
    "NClusterDischOvercurrent": 21081,
    "NClusterSOCLow": 21082,
    "NClustetInsulationResLow": 21083,
    }


while True:
    client = ModbusSerialClient(method = 'rtu', port ='COM4', stopbits = 1, bytesize = 8, parity = 'N', baudrate = baudRate)
    client.connect()
    if client.connect() == True:
        print("Reading input registers! Basic Information.")
        bi_d = client.read_input_registers(address = basic_reg_address["TotalSystemVoltage"], count = 30, unit = 1)
        time.sleep(3)
        print("Total System Voltage:", bi_d.registers)
        time.sleep(5)
        bvr_iter = iter(basic_reg_address)
        for w in bi_d.registers:
            print("{} Value: {}".format(next(bvr_iter),w))
            time.sleep(1.5)
        print("----")
        time.sleep(5)
        print("Reading input registers! Accident Information.")
        ai_d = client.read_input_registers(address = accident_reg_address["TotalChargingVoltageHigh"], count = 20, unit = 1)
        time.sleep(3)
        avr_iter = iter(accident_reg_address)
        for x in ai_d.registers:
            print("{} Value: {}".format(next(avr_iter),x))
            time.sleep(1.5)
        print("----")
        time.sleep(5)
        print("Reading input registers! HMI Interface Basic Information.")
        hmi_b_d = client.read_input_registers(address = hmi_basic_reg_address["NClusterTotalVoltage"], count = 31, unit = 1)
        time.sleep(3)
        hmibr_iter = iter(hmi_basic_reg_address)
        for y in hmi_b_d.registers:
            print("{} Value: {}".format(next(hmibr_iter),y))
            time.sleep(1.5)
        print("----")
        time.sleep(5)
        print("Reading input registers! HMI Interface Accident Information.")
        hmi_a_d = client.read_input_registers(address = hmi_accident_reg_address["NClusterTotalChargVoltHigh"], count = 20, unit = 1)
        time.sleep(3)
        hmiar_iter = iter(hmi_accident_reg_address)
        for z in hmi_a_d.registers:
            print("{} Value: {}".format(next(hmiar_iter),z))
            time.sleep(1.5)
        print("----")
        time.sleep(5)
        client.close()
        print("Connection closed!")
    else:
        print("Could not connect to provider!")


