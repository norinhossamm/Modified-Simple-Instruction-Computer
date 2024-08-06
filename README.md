# Modified Simple Instruction Computer

The MODI-SIC project, is a software tool that automates the assembly process of SIC machine code.

**Tools Used**: Python 

## Program Components and Usage:

- Input File: The program starts with an input file named In.txt, where each column of data is separated by a tab. This file contains the source code for the SIC machine, which needs to be assembled.

- Running the Program:

  - Merged Code: To process the entire assembly in one go, execute modi-SIC_merged_code.py. This script integrates all phases of the assembly process, from reading the input to generating the final machine code.

  - Individual Code Execution:
    
    - Intermediate Code: Run code_intermediate.py to generate an intermediate file that prepares the code for further assembly processes.
      
      <div align="center">
      <img width="260" alt="Screenshot 2024-08-06 at 3 32 05 PM" src="https://github.com/user-attachments/assets/0288ff17-9894-468d-90b4-6f6d5078d769">
      </div>

    - Pass 1: Execute code_pass1.py to analyze the source code and produce two outputs:
      
      - Address List (out_pass1.txt): Contains the addresses for each instruction or data element.
        
        <div align="center">
        <img width="238" alt="Screenshot 2024-08-06 at 3 33 44 PM" src="https://github.com/user-attachments/assets/bbe89ee0-84ad-43d7-816d-20b783b02607">
        </div>
      
      - Symbol Table (symbTable.txt): Maps symbols or labels found in the source code to their corresponding addresses.
 
        <div align="center">
          <img width="195" alt="Screenshot 2024-08-06 at 3 34 25 PM" src="https://github.com/user-attachments/assets/f5601243-7ab1-400c-a72f-d0282c76a80f">
        </div>
        
    - Pass 2: Run code_pass2.py for the second pass, which converts the assembled instructions into object code and forms:
      
      - Object Code Output (out_pass2.txt): This file contains the machine-readable object code that can be loaded into the SIC machine for execution.
        
        <div align="center">
          <img width="240" alt="Screenshot 2024-08-06 at 3 35 08 PM" src="https://github.com/user-attachments/assets/1d3b4de0-3053-45ce-aa2b-2e311e0421aa">
        </div>
      
      - HTE Record (HTE.txt): Stands for Header, Text, and End records, which summarize the object program's header, define the actual machine code, and mark the end of the object file.
        
         <div align="center">
         <img width="816" alt="Screenshot 2024-08-06 at 3 35 37 PM" src="https://github.com/user-attachments/assets/77d29153-a8c5-4a61-89be-13ab4a9e4020">
         </div>
