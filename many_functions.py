
import os
import logging
import sys
import json


def split_file(inp_file, op_dir, max_size=20*(2**20), 
               max_num_files=None, nLineGroup=1,
               report_amt = 10**5
               remove_orig=False):
    '''This function splits up a file into smaller parts while maintaining
        line integrity
    max_size (int): Max number of bytes in a file, 2**30 is a GB, 
                    2.5*(2**30) would be 2.5 GB
    remove_orig (bool): Should we remove the input file after splitting it
    max_num_files (int or None): If we want to limit the number of outputs
                                after a certain amount then set this to
                                a number
    nLineGroup (+ int): This is the amount of lines in a grouping that
                              need to stay together. For example, in FASTQ
                              files, this value would be 4, since in order
                              to keep the file correct, it needs to have
                              the 4 lines in a row.
    '''
    
    check_split_file_inputs(inp_file, op_dir, max_num_files, nLineGroup)

    # Checking file name:
    split_fn = os.path.basename(inp_file).split(".")
    file_base, file_ext = split_fn[0:-1], split_fn[-1]
     
    # file_size should be bytes (int)
    file_size = os.path.getsize(inp_file)
    if file_size < max_size:
        logging.info(f"Not splitting file {inp_file} since it's size is under" + \
                    f"the file size max limit ({file_size}<{max_size}). " + \
                    f"But the file will be copied to {op_dir}/{file_base}_1.fq")
        file_op_loc = os.path.join(op_dir, file_base + "_1." + file_ext) 
        shutil.copy(inp_file, file_op_loc)
        return None 
    else:
        logging.info(f"Splitting file {inp_file} since it's size is over the file size max limit.")

    FH = open(inp_file)
    
    # maintains the lines for the new file
    new_file_list = []
    crt_line_list = []
    crt_new_file_size = 0
    total_bytes_processed = 0
    start_line = FH.readline()
    file_num = 1
    line_num = 1
    while start_line != "":
        crt_line_list = [start_line]
        additional_lines_size = len(start_line)
        for i in range(1, nLineGroup):
            c_line = FH.readline()
            crt_line_list.append(c_line)
            additional_lines_size = len(c_line)

        if crt_new_file_size + additional_lines_size > max_size:
            new_file_name = file_base + "_" + str(file_num) + file_ext
            out_fp = os.path.join(op_dir, new_file_name)
            logging.info("Writing out split file at " + out_fp)
            # If file size passes 1 GB, we print out sub_file
            with open(out_fp, "w") as g:
                g.write("".join(new_file_list))
            files_to_process.append(out_fp)
            new_file_list = []
            file_num += 1
            if max_num_files is not None and file_num > max_num_files:
                return None

            crt_new_file_size = 0

        crt_new_file_size += additional_lines_size
        total_bytes_processed += additional_lines_size
        new_file_list += crt_line_list 
        line_num += nLineGroup
        start_line = FH.readline()
        if line_num % report_amt < nLineGroup:
            logging.info("Just processed line " + str(line_num) + "." + \
                f"\nCompleted {round(((total_bytes_processed/file_size) * 100),3)}% " + \
                "of file.")


    FH.close()

    if file_num > 1:
        if remove_orig:
            os.unlink(inp_file)
        new_file_name = file_base + "_" + str(file_num) + file_ext
        out_fp = os.path.join(op_dir, new_file_name)
        logging.info( "Completed 100% of file '" + file_base + \
                    "'. Writing out final split file at " + out_fp)
        with open(out_fp, "w") as g:
            g.write("".join(new_file_list))

    return None 

def check_split_file_inputs(inp_file, op_dir 
                            max_num_files, nLineGroup):
    if not os.path.exists(inp_file):
        raise Exception(f"Input file at {inp_file} does not exist.")
    if not os.path.isdir(op_dir):
        raise Exception(f"Output dir at {op_dir} does not exist.")
    if max_num_files is not None:
        if not isinstance(max_num_files, int):
            raise Exception("max_num_files must be an int")
        elif max_num_files < 1:
            raise Exception("max_num_files must be 1 or greater.")
    if not isinstance(nLineGroup, int):
        raise Exception("nLineGroup must be an int")
    else:
        if nLineGroup < 1:
            raise Exception("nLineGroup must be 1 or greater.")


    return None

def load_json(fp):
    with open(fp, 'r') as f:
        x = json.loads(f.read())
    return x


def force_create_dir(op_dir):
    if os.path.exists(op_dir):
        shutil.rmtree(op_dir, ignore_errors=True)
    os.mkdir(op_dir)


def get_help_str():
    return "incomplete."

def main():

    args = sys.argv
    help_str = get_help_str()
    opt = []
    if args[-1] not in opt:
        print(help_str)
        sys.exit(0)
    else:
        print("Incomplete")
        return None
    return None

if __name__ == "__main__":
    main()

