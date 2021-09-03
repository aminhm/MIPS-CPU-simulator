
class ControlUnit:
    def __init__(self,opcode):
        self.opcode=opcode
    def instruction(self):
        add_operation_opcode="000001"
        sub_operation_opcode="000010"
        and_operation_opcode="000011"
        or_operation_opcode="000100"
        set_less_than_operation_opcode="000101"
        nor_operation_opcode="000110"
        xor_operation_opcode="000111"
        load_word_operation_opcode="001000"
        store_word_operation_opcode="001001"
        branch_equal_operation_opcode="001010"
        branch_not_equal_operation_opcode="001011"
        jump_operation_opcode="001100"
        none_operating="000000"
        if (self.opcode==add_operation_opcode):
            return "Add"
        if (self.opcode==sub_operation_opcode):
            return "Sub"
        if (self.opcode==and_operation_opcode):
            return "And"
        if (self.opcode==or_operation_opcode):
            return "Or"
        if (self.opcode==set_less_than_operation_opcode):
            return "Slt"
        if (self.opcode==nor_operation_opcode):
            return "Nor"
        if (self.opcode==xor_operation_opcode):
            return "Xor"
        if (self.opcode==load_word_operation_opcode):
            return "Lw"
        if (self.opcode==store_word_operation_opcode):
            return "Sw"
        if (self.opcode==branch_equal_operation_opcode):
            return "Beq"
        if (self.opcode==branch_not_equal_operation_opcode):
            return "Bne"
        if (self.opcode==jump_operation_opcode):
            return "J"
        if(self.opcode==none_operating):
            return "None"
        else:
            return "Undefined opcode"
