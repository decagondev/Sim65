class Sim65:
    # 1 byte opcodes
    BRK = 0x0000
    NOP = 0x00EA
    CLC = 0x0018
    CLD = 0x00D8
    CLI = 0x0058
    CLV = 0x00B8
    DEX = 0x00CA
    DEY = 0x0088
    INX = 0x00E8
    INY = 0x00C8
    PHA = 0x0048
    PHP = 0x0008
    PLA = 0x0068
    PLP = 0x0028
    RTI = 0x0040
    RTS = 0x0060
    SEC = 0x0038
    SED = 0x00F8
    SEI = 0x0078
    TAX = 0x00A8
    TSX = 0x00BA
    TXA = 0x008A
    TXS = 0x009A
    TYA = 0x0098


    def __init__(self):
        self.x = 0
        self.y = 0
        self.a = 0
        self.y = 0
        self.PC = 0
        self.SP = 0
        self.SR = 0
        self.ram = [0] * 0xffff
        self.flags = [0] * 8
        self.running = False

    def start(self):
        self.running = True

    def stop(self):
        self.running = False


    def f_clc(self):
        self.flags[4] = 0


    def f_nop(self):
        pass

    def f_brk(self):
        self.stop()









# main
cpu = Sim65()

 
