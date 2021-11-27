import uiautomator2 as u2
# 连接手机

device = u2.connect("f1986ad8")

print(device.device_info)