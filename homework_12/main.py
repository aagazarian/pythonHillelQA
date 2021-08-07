from homework_12.PhilipsCleaner import PhilipsCleaner
from homework_12.XiaomiCleaner import XiaomiCleaner

if __name__ == '__main__':
    philips = PhilipsCleaner("Philips XC900", 450, 50)
    xiaomi = XiaomiCleaner("Xiaomi RDS231", 400, 40)

    philips.vacuum(10)
    xiaomi.vacuum(10)
