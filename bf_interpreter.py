def strip_unused(command):
    temp = ''
    for char in command:
        if char in ['+', '-', '>', '<', '[', ']', ',', '.']:
            temp += char
    command = temp
    return command
            

class Brainfuck:
    def __init__(self, tape_length=30000): # tape defaults to 30000 bytes long
        if tape_length in [69, 420, 42069, 69420]:
            print('haha nice tape length mate lmao')
        self.tape = [0] * tape_length # make int array of the specified tape length filled with zeroes
        self.pointer = 0 # tape pointer, initialised to leftmost byte in tape
    def run(self, command, live_input=True): # live input doesn't do anything
        cmd_pointer = 0
        while True:
            if cmd_pointer >= len(command):
                break
            
            if command[cmd_pointer] == '+': # increment modulo 256 (because byte)
                self.tape[self.pointer] = (self.tape[self.pointer] + 1) % 256
            elif command[cmd_pointer] == '-': # decrement modulo 256 (because byte)
                self.tape[self.pointer] = (self.tape[self.pointer] - 1) % 256
            elif command[cmd_pointer] == '<': # modulo for circular tape
                self.pointer = (self.pointer - 1) % len(self.tape)
            elif command[cmd_pointer] == '>': # modulo for circular tape
                self.pointer = (self.pointer + 1) % len(self.tape)
            elif command[cmd_pointer] == '.': # output
                print(chr(self.tape[self.pointer]), end='')
            elif command[cmd_pointer] == ',': # input
                try:
                    self.tape[self.pointer] = ord(input("input (one character): ")[0]) % 256
                except:
                    self.tape[self.pointer] = 0 # if there is EOL (no input)
            elif command[cmd_pointer] == '[': # uhoh time for parsing
                if self.tape[self.pointer] == 0: # skip to corresponding right bracket if byte at pointer is 0, otherwise do nothing
                    lbcounter = 0 # counter for left brackets encountered
                    searching = True
                    while searching:
                        cmd_pointer += 1
                        if command[cmd_pointer] == '[':
                            lbcounter += 1
                        elif lbcounter == 0 and command[cmd_pointer] == ']':
                            searching = False
                        elif command[cmd_pointer] == ']':
                            lbcounter -= 1
            elif command[cmd_pointer] == ']':
                if self.tape[self.pointer] != 0: # skip back to corresponding left bracket if byte at pointer is not 0, otherwise do nothing
                    rbcounter = 0 # counter for right brackets encountered
                    searching = True
                    while searching:
                        cmd_pointer -= 1
                        if command[cmd_pointer] == ']':
                            rbcounter += 1
                        elif rbcounter == 0 and command[cmd_pointer] == '[':
                            searching = False
                        elif command[cmd_pointer] == '[':
                            rbcounter -= 1
            cmd_pointer += 1
    def reset(self):
        self.tape = [0] * len(self.tape)
        self.pointer = 0
