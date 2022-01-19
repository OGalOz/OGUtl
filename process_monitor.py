'''
This file monitors processes
'''

import sys
import time
import ps_util
import json
import logging



def monitor_process(process_num, delay=30):
    '''
    Args:
        process_num int process number to check.
        delay int: Number of seconds between each check
    Description:
        Every {delay (int)} we check if the process is running
        or not. If it is no longer running, we
        send a report to emails on the email_list
    '''



    return None


def send_report(broken_process, email_list):
    '''
    Description:
    '''



    return None

def run_file(inp_json, delay_str):
    prc_num, delay = check_inputs(inp_json, delay_str)
    monitor_processes(prc_num, delay=delay)

def check_inputs(process_num, delay_str):


    try:
        prc_num = int(process_num)
    except Exception as inst:
        print("Input process number string failed. Should be integer.")
        raise Exception(inst)

    try:
        delay = int(delay_str)
    except Exception as inst:
        print("Input delay string failed. Should be integer.")
        raise Exception(inst)
    

    return prc_num, delay


def get_help_str():
    help_str = "python3 process_monitor.py inp_json delay 1"
    help_str += ""
    return help_str

def main():
    args = sys.argv
    help_str = get_help_str()
    opt = ["1"]
    if args[-1] not in opt:
        print(help_str)
        sys.exit(0)
    else:
        fn, process_num, delay_str, indic = args
        prepare_args(process_num, delay_str)
        return None
    return None



if __name__ == "__main__":
    main()
