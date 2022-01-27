'''

This file is supposed to run a 
loop which checks, every certain amount of time,
whether the node.js server is running within the
current server.
If it stops running, it should send an email report.
'''

import psutil
import json
from report_mod import send_emails
import time
import datetime

def sleep_and_check(cfg_fp, email):
    '''
    Description:
        This process sleeps 'sleep_time' seconds and
        then checks if a process exists with the commands
        and a given expected process id (pid). If the expected
        pid is not given, then it finds the pid once, and expects
        it to remain at that pid. If it is discovered that the
        process is not found at that pid, it sends an email
        to the email given in the parameter 'email'.
        Note that it does not prepare for multiple processes
        to run with the command, since that would mean
        the found pid could switch from the original process
        we are checking for while it is still running.
        This is geared towards a single process with 'node js'
        running.
    '''
    with open(cfg_fp, 'r') as f:
        cfg_d = json.loads(f.read())
    commands = cfg_d["command_list"]
    sleep_time = cfg_d["sleep_time"]
    expected_pid = cfg_d["expected_pid"]
    if expected_pid is None:
        # this function returns -1 if no process found that matches
        expected_pid = get_process_pid(commands)
        if expected_pid == -1:
            raise Exception("No process running with existing commands.")


    pid = get_process_pid(commands)
    while pid == expected_pid:
        time.sleep(sleep_time)
        pid = get_process_pid(commands)

    report_str = f"Process with commands '" + "', '".join(commands) + \
                f"' no longer running at pid {expected_pid}." + \
                f" Datetime: {str(datetime.now())}"
    #  Send report to yourself
    send_emails(report_str) 

    sys.exit(0)




def get_process_pid(command_list=None):
    '''
    Args:
        command_list is a list of strings, all of which
                should match the first several commands associated
                with the process. e.g. [1,2] matches [1,2,3,4],
                but [1,2] does not match [1].
                [1,2] is command list; [1,2,3,4] and [1] are cmdline
                from process.
    Returns:
        pid is an int, -1 if not found

    '''

    for proc in psutil.process_iter():
        cmds = proc.cmdline()
        if len(cmds) >= len(command_list):
            match = True
            for i in range(len(command_list)):
                if command_list[i] != cmds[i]:
                    match = False
                    break
            if match:
                return proc.pid

    return -1

def get_p_info_d(pid):
    proc = psutil.Process(pid=pid)
    p_d = proc.as_dict()
    return p_d


   
def print_all_processes(cbreak=False):

    print_list = []
    for proc in psutil.process_iter():
        p_d = proc.as_dict()
        '''
        for k in p_d.keys():
            print(f"{k}: {p_d[k]}")
        '''

        if len(p_d["cmdline"]) > 0:
            print_list.append('|'.join(p_d["cmdline"]))
            #print("SPECIAL COMMAND: " + ''.join(p_d["cmdline"]))
        if cbreak:
            break


    print("\n\n".join(print_list))
    return True




