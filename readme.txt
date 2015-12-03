Project repository for Systems Software [CMPE220] - Fall 2015

PROJECT TITLE: SDN based threat vector and security solutions.

Folder Contents: Classification

1. Tutorial
    This directory contains the step by step tutorial or the commands that are necessary to 
    perform DDoS attack and prevent it.

2. Presentation
    This directory contains the presentation file which provides an overview of the project.
    Proposal.pptx - intial presentation used for project proposal
    CMPE220_Team_SPRINT_Presentation.pptx - Final presentation for the project.

3. Progress report
    Provides the informations on the progress of the report on a weekly basis. It contains 
    only one file "Progress Report.docx".

4. Python Code
    Lists all the python code that are necessary to simulate. Please refer the manual directory
    for how to run the code and place the code in the requried location.

    launchTraffic.py -- to simulate traffic using scapy package
    launchAttack.py -- to launch DDOS attack on any host
    l3_editing.py -- updated existing l3_learning.py of pox controller to detect, collect flow
    statistics and prevent DDoS attack.
    detection.py -- contains algorithm to measure entropy.
    BasicFlowchart.png -- diagram illustrate the flow chart used to prevent DDoS attack

5. References
    Lists some of the references papers and an excel file (Summary.xlsx) documents important 
    takeway points from the reference papers. 

6. Report
    Contains final report in IEEE format.

7. Videos
    List some of the videos that were gathered during the project implementation. 
    
    It includes 4 files
    
    Introduction.mov --Introduction to team members
    DDOS_Detection.mov --Demo of DDoS attack and detection
    DDOS_Prevention.mov --Demo of DDoS attack and prevention
    CMPE220_demo.mp4 -- Final demo, aggregate of the above 3 videos

8. Logs
    This directory lists the logs that were collected during the demo. 
    Before.txt -- logs collected without the prevention of DDoS attack.
    After.txt -- logs collected with DDoS prevention.

9. Screenshots ( self explanatory unless other specified )
    Attack_Host.png 
    DDoS_pervention.png
    EntropyDecreased.png 
    EntropyLog.png
    Flow_Table_1.png
    LaunchAttackCommand.png
    LaunchTrafficCommand.png
    Mininet_Command.png
    MonitorProcess.png
    Packets.png
    Simple_Mininet_Topology.png
    StartController.png
    StartControllerWithDDoSPrevention.png
    XtermCommand.png

10. Misc
    This directory contains other related data used in the project.
    MininetBasics.pdf -- decsribes usage of Mininet
    


