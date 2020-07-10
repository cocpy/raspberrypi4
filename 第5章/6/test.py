import smbus

# I2C端口号，即0或1
I2C_port_no = 1

# 创建SMBus类的对象以访问基于I2C的Python函数
smb_name = smbus.SMBus(I2C_port_no)

# 使用Bus对象访问SMBus类
Bus = smbus.SMBus(1)

# 将数据写入所需的寄存器
# Bus.write_byte_data(Device Address, Register Address, Value)
# Device Address ：7位或10位器件地址
# Register Address ：需要编写的寄存器地址
# Value ：传递需要写入寄存器的值
Bus.write_byte_data(0x68, 0x01, 0x07)

# 写入32字节的块
# Bus.write_i2c_block_data(Device Address, Register Address, [value1, value2,….])
# 从0地址写入6个字节的数据
Bus.write_i2c_block_data(0x68, 0x00, [0, 1, 2, 3, 4, 5])

# 从所需寄存器读取数据字节
# Bus.read_byte_data(Device Address, Register Address)
Bus.read_byte_data (0x68, 0x01)

# 读取32个字节的块
# Bus.read_i2c_block_data(Device Address, Register Address, block of bytes)
Bus.read_i2c_block_data(0x68, 0x00, 8)
