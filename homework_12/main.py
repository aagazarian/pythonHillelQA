from ArpineAgazaryan.pythonHillelQA.homework_12.philips_cleaner import PhilipsCleaner
from ArpineAgazaryan.pythonHillelQA.homework_12.xiaomi_cleaner import XiaomiCleaner

if __name__ == "__main__":
    philips = PhilipsCleaner("Philips XC900", 450, 50)
    xiaomi = XiaomiCleaner("Xiaomi RDS231", 400, 40)

    philips.vacuum(10)
    xiaomi.vacuum(10)
