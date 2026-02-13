from rich import print
import platform
import cpuinfo 
import psutil
from uptime import uptime
import tkinter as tk
import wmi

root = tk.Tk()
root.withdraw()
Largura = root.winfo_screenwidth()
Altura = root.winfo_screenheight()
my_cpuinfo = cpuinfo.get_cpu_info()
pc = wmi.WMI()

LOGO = r"""                                                                               
                              ::++::mmmm++++mm++                                                    
                          ++++++++++++++++++++++++++++                              ++              
                        ++::++++++++++++++++++++++++::  ++++::++..            ++mm++::              
                        ::++++++++++++++++++++++++++::  ++++++++++++++++++++++++++++                
                        ::++++++++++++++++++++++++++    ++++++++++++++++++++++++++++                
                        ++++++++++++++++++++++++++++    ::++++++++++++++++++++++++++             
                        ++++++++++++++++++++++++++++  --::++++++++++++++++++++++++++                
                      --::++++++++++++++++++++++++++  --::++++++++++++++++++++++++++                
                      ++++++++++++++++++++++++++++++  ++++++++++++++++++++++++++++++                
                      ++++++++++++++++++++++++++++++  ++++++++++++++++++++++++++++++                
                      ++++++++++++++++++++++++++++--  ++++++++++++++++++++++++++++--                
                      ++++++++++++++++++++++++++++--  ++++++++++++++++++++++++++++--                
                      ++++++++++++++::++++++++++++    ++++++++++++++++++++++++++++                  
                      ++::                ..++++::    ++++++++++++++++++++++++++::                  
                            ::++++++mm++            ::::++++++++++++++++++++++++++                  
                      ++++++++++++++++++++++++++..        --++++++++++++++++--                      
                    ++++++++++++++++++++++++++++++  mm++                      ..mm                  
                    ++++++++++++++++++++++++++++++  ++++++++++++::--..::++++++++::                  
                    ++++++++++++++++++++++++++++    ++++++++++++++++++++++++++++++                  
                    ++++++++++++++++++++++++++++    +++++++++++++++++++++++++++++:                  
                  ..++++++++++++++++++++++++++++    ++++++++++++++++++++++++++++                    
                  ++++++++++++++++++++++++++++++  --++++++++++++++++++++++++++++                    
                  ++++++++++++++++++++++++++++++  ++++++++++++++++++++++++++++++                    
                  ++++++++++++++++++++++++++++++  ++++++++++++++++++++++++++++++                    
                  ++++++++++++++++++++++++++++::  ++++++++++++++++++++++++++++++                    
                  ::++++++++++++++++++++++++++--  ++++++++++++++++++++++++++++++                    
                ..++++::++++++++++::++++++++++    ++++++++++++++++++++++++++++--                    
                ++++++::..      ..--++++++++++    ++++++++++++++++++++++++++++--                    
                ++                          ++  ..++++++++++++++++++++++++++++                      
                                                  --++++++++++++++++++++++++::                      
                                                          ..++++++++++::                            
                                                                                                    
"""

INFO = [
    f"[blue]root[/blue]@[blue]{platform.node()}PC[/blue]",
    f"--------------------------------------------------",
    f"[blue]OS: [/blue]{platform.platform()}",
    f"[blue]Architecture: [/blue]{platform.architecture()}",
    f"[blue]Uptime: [/blue]{uptime()} secs",
    f"[blue]Resolution: [/blue]{Largura}x{Altura}",
    f"[blue]Processor: [/blue]{platform.processor()}",
    f"[blue]CPU info: [/blue]{my_cpuinfo['brand_raw']}",
    f"[blue]Total RAM: [/blue]{psutil.virtual_memory().total / (1024 ** 3):.2F} GB",
    f"[blue]GPU: [/blue]{pc.Win32_VideoController()[0].name}"
]

#Divide o texto em varias linhas
logo_lines =LOGO.splitlines()

#Define quantos espaços vão existir entre a logo e as informações
padding = 5

distancia = max(len(line) for line in logo_lines)

for i in range(max(len(logo_lines), len(INFO))):
    left = logo_lines[i] if i < len(logo_lines) else ""
    right = INFO[i] if i < len(INFO) else ""
    print(f"[blue]{left:<{distancia}}[/blue]" + " " * padding + right)

input("Press Enter to continue...")
