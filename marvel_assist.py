from ctypes import *
import time
#For Python 3.4
gcapi = windll.LoadLibrary("gcdapi.dll")
XB360_XBOX = 0
XB360_BACK = 1
XB360_START = 2
XB360_RB = 3
XB360_RT = 4
XB360_RS = 5
XB360_LB = 6
XB360_LT = 7
XB360_LS = 8
XB360_RX = 9
XB360_RY = 10
XB360_LX = 11
XB360_LY = 12
XB360_UP = 13
XB360_DOWN = 14
XB360_LEFT = 15
XB360_RIGHT = 16
XB360_Y = 17
XB360_B = 18
XB360_A = 19
XB360_X = 20
GCAPI_OUTPUT_TOTAL = 36

button_mapping = {'L': XB360_X, 'M': XB360_Y, 'H': XB360_B, 'S': XB360_A, 'A1': XB360_LB, 'A2': XB360_RB,
           'up': XB360_UP, 'down': XB360_DOWN, 'left': XB360_LEFT, 'right': XB360_RIGHT,
            'start': XB360_START, 'back': XB360_BACK, 'RS': XB360_RS, 'LS': XB360_LS, 'LT': XB360_LT}

one_frame = 1/60 #in seconds

def start(filename):
    gcapi.gcapi_Write.argtypes = [POINTER(c_int8)]
    button_id_rows = get_inputs_from_file(filename)

    outputs_array = []
    
    for button_ids in button_id_rows:
        outputs = (c_int8*GCAPI_OUTPUT_TOTAL)()
        for button_id in button_ids:
            outputs[button_id] = 100
        outputs_array.append(outputs)

    playback(outputs_array)

    print('Done')

def playback(outputs_array):
    previous = time.clock()
    for outputs in outputs_array:
        res = gcapi.gcapi_Write(outputs)
        while (time.clock() < previous + one_frame):
            continue
        previous = time.clock()
        
def write_output(line):
    inputs = line.split(' ')
    
def get_inputs_from_file(filename):
    with open(filename) as file:
        lines = file.readlines()
    file.close()
    return convert_to_full_inputs(lines)
        
def convert_to_full_inputs(lines):
    inputs = []
    loop_inputs = []
    in_loop_section = 0;
    for line in lines:
        line = line.rstrip('\r\n')
        repeat = 0
        commands = ''
        if '#' in line:
            continue
        elif ']' in line:
            for i in range(0, in_loop_section):
                inputs = inputs + loop_inputs
            in_loop_section = 0
            loop_inputs = []
            continue
        elif ' ' in line:
            part = line[0:line.find(' ')]
            commands = line[line.find(' '):]
            if part.isdigit():
                repeat = int(part)
            if '[' in commands:
                in_loop_section = int(part)
                continue
        elif line.isdigit():
            repeat = int(line)
        else:
            print('missing repeat value on line: ' + line)
        for r in range(repeat):
            button_ids = []
            for button_id in commands.strip().split():
                if button_id in button_mapping:
                    button_ids.append(button_mapping[button_id])
            if in_loop_section > 0:
                loop_inputs.append(button_ids)
            else:
                inputs.append(button_ids)
    return inputs

def end():
    gcapi.gcdapi_Unload()
    print('Unloaded')

def marvel_assist(filename):
    if(gcapi.gcdapi_Load()):
        print('Loaded API')
        if(gcapi.gcapi_IsConnected()):
            print('Connected to device')
            start(filename)
        else:
            print('Could not connect to device')
    else:
        print('Could not load API')
    end()

marvel_assist('scripts/dashtest.txt')
