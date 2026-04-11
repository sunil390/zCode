z/OS Communications Server
use of Network Express Feature

Linda Harrison
lharriso@us.ibm.com

IBM Washington Systems Center

Trademarks and Credits

• See URL for a list of Trademarks:

– http://www.ibm.com/legal/copytrade.shtml

• This presentation was created from materials created by

Randy Kunkel and Patty Driever

3/27/2026

https://www.ibm.com/support/pages/node/7231685 © IBM Corporation, 2026 --- Last Updated 3/27/2026

Page 2

Agenda

• Network Express Physical Adapter
• Protocols
• Interface Parameters
• Migration Option
• Display Output
• Limitations/Guidelines
• APARs
• Configurations
• Matches
• VLAN
• Examples
• Appendix – Backup Charts

3/27/2026

https://www.ibm.com/support/pages/node/7231685 © IBM Corporation, 2026 --- Last Updated 3/27/2026

Page 3

Network Express Physical
Adapter

3/27/2026

https://www.ibm.com/support/pages/node/7231685 © IBM Corporation, 2026 --- Last Updated 3/27/2026

Page 4

OSA CHPID Type History

• OSA > OSA-2 > OSA-Express > OSA-Express2 > … > OSA-Express7
• OSA CHPID type OSE - obsolete

– Non-QDIO mode connection to external Ethernet LAN supporting both TCP/IP

and SNA traffic concurrently.

– SNA should be migrated to APPN and Enterprise Extender.
– https://www.ibm.com/support/pages/node/7185089

• OSA CHPID type OSX - obsolete

– QDIO mode connection to Intraensemble Data Network (IEDN)

• OSA CHPID type OSM - obsolete

– QDIO mode connection to Intranode Management Network (INMN)

• OSA CHPID type OSN - obsolete

– OSA for NCP mode connects NCP running in LPARs with Communication

Controller for Linux on System z (CCL) to LPARs running TPF and VTAM in
z/OS, z/VM, and z/VSE.

• OSA CHPID type OSD

– QDIO mode connection to external Ethernet LAN

• OSA CHPID type OSC

– Console mode connection to external Ethernet LAN for console, TN3270, and

telnet access to LPARs.

3/27/2026

https://www.ibm.com/support/pages/node/7231685 © IBM Corporation, 2026 --- Last Updated 3/27/2026

Page 5

Evolution of RoCE
RDMA & InfiniBand

Host A
Application
Server

Application
Server

Host B

Application
Client

Application
Client

RDMA

TCP/IP

TCP/IP

RDMA

InfiniBand
Adapter

Ethernet
NIC

Ethernet
NIC

InfiniBand
Adapter

Ethernet
network

InfiniBand
network

• Programs were either written to

use RDMA or TCP/IP.
– Two separate networks were required.
• Ethernet network for TCP/IP traffic.
• InfiniBand network for RDMA traffic.

3/27/2026

https://www.ibm.com/support/pages/node/7231685 © IBM Corporation, 2026 --- Last Updated 3/27/2026

6

RDMA over Converged Ethernet
(RoCE)

• Native RoCE

Host A
Application
Server

Application
Server

Host B

Application
Client

Application
Client

– Programs are still written to use either

RDMA or TCP/IP.

RDMA

TCP/IP

TCP/IP

RDMA

• RoCE supports RDMA over Converged

RoCE

RoCE

Ethernet.

Ethernet
network

• RoCE supports TCP/IP over Converged

Ethernet.

– Native RoCE has been available for a
long time prior to IBM Z RoCE support.

– z/OS does not support native RoCE
(RoCE without Shared Memory
Communications over RDMA (SMC-R)).

3/27/2026

https://www.ibm.com/support/pages/node/7231685 © IBM Corporation, 2026 --- Last Updated 3/27/2026

7

SMC-R and RoCE

LPAR A

LPAR B

•

Shared Memory Communication over RDMA (SMC-R)
– Is a sockets over RDMA communication protocol

that allows existing TCP applications to
transparently benefit from RoCE.

Application Server

Application Client

– Requires no application change. Applications still

SMC-R

TCP/IP

TCP/IP SMC-R

RNIC

RNIC

Ethernet
network

programmed to use TCP/IP.

– Provides host-to-host direct memory access
without the traditional TCP/IP processing
overhead.

– Allows customers to benefit from InfiniBand

technology by leveraging their existing Ethernet
infrastructure.

– TCP protocol only! No UDP (ie. EE), SNA, etc.

• All TCP traffic except IPsec

•
•

z/OS includes SMC-R support.
SMC-R is only used over the RoCE Express feature to a partner SMC-R and RoCE.

– While other platforms (non-Z) RoCE RNICs might exist in your network, the Z RoCE Express

feature is only able to communicate with them if they use SMC-R as well (when z/OS is used on
the IBM side).

3/27/2026

https://www.ibm.com/support/pages/node/7231685 © IBM Corporation, 2026 --- Last Updated 3/27/2026

8

Network Express

Host A
Application
Server

RDMA
SMC-R

Application
Server

TCP/IP

Network
Express

Host B

Application
Client

Application
Client

RDMA
SMC-R

TCP/IP

Network
Express

Ethernet
network

• Network Express combines OSA and Z RoCE capabilities

• Network Express supports RDMA over Converged Ethernet (RoCE) without SMC-R

(native RoCE). Programs are written to use RDMA.

– Linux only. z/OS does not support RoCE without SMC-R.

• Network Express supports RoCE with SMC-R.
• Network Express supports TCP/IP using native PCIe.

– Linux only. z/OS does not support this.

• Network Express supports TCP/IP similar to how OSA supports TCP/IP connectivity.

– z/OS only. Linux does not support this.

• See table summary of this on later page of this presentation.

3/27/2026

https://www.ibm.com/support/pages/node/7231685 © IBM Corporation, 2026 --- Last Updated 3/27/2026

9

RoCE Feature History

• RoCE Express
• RoCE Express2
• RoCE Express3
• Remote Direct Memory Access (RDMA) over Converged

Ethernet (RoCE)
– Linux supports the RoCE feature sending data using TCP/IP and

Shared Memory Communications over RDMA (SMC-R).

– z/OS Communications Server only supports RoCE feature sending

data using SMC-R.

• QDIO (OSD) OSA is required for sending TCP/IP data.
• SMC-R and RoCE are required for sending data using RDMA.
• In either case, the application is still written to communicate using

TCP/IP.

– RoCEv2 support allows multiple subnets.

3/27/2026

https://www.ibm.com/support/pages/node/7231685 © IBM Corporation, 2026 --- Last Updated 3/27/2026

Page 10

IBM Z17 Processor

• When migrating to Z17 there are two options:

– OSA-Express7
– Network Express
– RoCE is not supported on Z17

• OSA-Express7

– OSD CHPID for QDIO TCP/IP
– OSC CHPID for Console/TN3270 connections

• Network Express

– OSH – see following pages (TCP/IP)
– NETH – see following pages (RDMA)(TCP/IP for Linux only)

3/27/2026

https://www.ibm.com/support/pages/node/7231685 © IBM Corporation, 2026 --- Last Updated 3/27/2026

Page 11

New Network Express Feature

OSA

CHPID OSD or OSC

Port

Port

Network
Express

CHPID OSH and/or FID NETH

CHPID OSH and/or FID NETH

Port

Port

OSA

CHPID OSD or OSC

Port

New

RoCE

FID ROC2

Port

FID ROC2

Port

• The Network Express feature combines the functionality
of both the OSA-Express in OSD (QDIO) mode and the
RoCEv2 Express feature.

• Console support still requires the OSA-Express in OSC

mode.

3/27/2026

https://www.ibm.com/support/pages/node/7231685 © IBM Corporation, 2026 --- Last Updated 3/27/2026

Page 12

Protocols and Ports

Network
Express

CHPID OSH and/or FID NETH

CHPID OSH and/or FID NETH

Port

Port

• Network Express feature supports new protocols (H for Hybrid)

– OSH protocol - Enhanced QDIO (EQDIO)
– NETH protocol - RoCE, RDMA, SMC-R, TCP/IP (Linux only)

OSA QDIO like

RoCE like

• Network Express physical feature

– 2 CHPIDs per card - 2 Ports per card

• 1 Port per CHPID

– 10GbE or 25GbE
– Both PCHIDs must be the same type

• Can’t mix ports with different speed or optics
– “OSA” name will still be used as well in manuals

• Network Express port support

– CHPID OSH and FID NETH – one or both supported on the same port
– LPAR to LPAR traffic supported (as OSA always has)

3/27/2026

https://www.ibm.com/support/pages/node/7231685 © IBM Corporation, 2026 --- Last Updated 3/27/2026

Page 13

Protocols

3/27/2026

https://www.ibm.com/support/pages/node/7231685 © IBM Corporation, 2026 --- Last Updated 3/27/2026

Page 14

EQDIO Protocol

• For each Network Express feature port

– Define CHPID type OSH for EQDIO - OSA QDIO like support
– Define FID type NETH for SMC-R - RoCE like support

• EQDIO Protocol

– CHPID type OSH
– A single Device Number (QDIO requires 3 for Read/Write/Control)

• Control Queues replace OSD Read/Write devices

– VTAM TRLE is dynamically created
– New Interface EQENET / EQENET6
– Layer 2 (QDIO is Layer 3 only for z/OS)
– Default MTU is 9000 (Jumbo Frames)

• Linux Network Express support does not use EQDIO since
Linux RoCE support already includes SMC-R and TCP/IP.

3/27/2026

https://www.ibm.com/support/pages/node/7231685 © IBM Corporation, 2026 --- Last Updated 3/27/2026

Page 15

NETH Protocol

• NETH Protocol

z/OS

Linux

YES

NO

YES

YES

YES

NO

OSH Only

NETH Only

OSH and NETH

– PFID type NETH
– PF defined in OSA firmware
– No more Management of RoCE PFIDs

in Resource Groups
– No more port parameter

Note:  IDAA is a Linux system. TCP/IP is used by
OSH on the z/OS side and NETH on the IDAA side.
IDAA does not support RDMA or SMC.

• Port number is NOT configured anywhere (HCD or the Operating System)

– No z/OS Communications Server SMC-R configuration changes

• z/OS Communications Server Network Express Support

– CHPID type OSH
– PFID NETH

Interface EQENET (or OSA IPAQENET) SMCRIPADDR parameter required for NETH
•
• NETH (Interface EZARIUTxyyyy) dynamically created/started when Interface EQENET

(or OSA-Express7S IPAQENET) is started

– x is always 1 for port and yyyy is the PFID number

3/27/2026

https://www.ibm.com/support/pages/node/7231685 © IBM Corporation, 2026 --- Last Updated 3/27/2026

Page 16

z17 Support

IP Connectivity (TCP,
UDP, etc.)

RDMA over Converged
Ethernet (native RoCE
and SMC-R)

Layer 3
Support

Layer 2
Support

RoCEv1

RoCEv2

Console
Support

Yes

No

Yes

Yes

No

Yes

No

No

No

No

No

No

No

No

No

No

No

No

No

No

No

No

No

Yes, with
SMC-Rv1

Yes, with
SMC-Rv2

No

No

Yes

No

No

No

No

Operating System
Adapter
Mode (Protocol)

z/OS
OSA-Express7s
QDIO

Linux
OSA-Express7s
QDIO

z/OS
OSA-Express7s
Integrated Console Controller (ICC)

z/OS
Network Express
EQDIO

Linux
Network Express
EQDIO

z/OS
Network Express
NETH

Linux
Network Express
NETH

CHPID
or PFID

CHPID
OSD

CHPID
OSD

CHPID
OSC

CHPID
OSH

CHPID
OSH

PFID
NETH

PFID
NETH

3/27/2026

https://www.ibm.com/support/pages/node/7231685 © IBM Corporation, 2026 --- Last Updated 3/27/2026

Page 17

Yes

Yes

Yes

Interface Parameters

3/27/2026

https://www.ibm.com/support/pages/node/7231685 © IBM Corporation, 2026 --- Last Updated 3/27/2026

Page 18

EQENET and EQENET6 Parameters

•

Interface inf_name DEFINE EQENET DEVNUM xxxx VMAC
IPADDR ipaddr/mask…
– DEVNUM replaces PORTNAME – required
– IPADDR – required (subnet mask required for IPv4)
– VMAC – will be auto-generated if missing
– Other parameters that remain valid

• MTU
• VLANID
• SECCLASS
• MONSYSPLEX
•
•
• SOURCEVIPAINTERFACE
• TEMPIP
• SMCR
• SMCD

IPBCAST
ISOLATE

– Parameters not supported/needed

• CHPIDTYPE
• PORTNAME
• PRIROUTER/SECROUTER
•

INBPERF (eliminated, internal capability is DYNAMIC
with IWQ)

• READSTORAGE (eliminated, dynamically managed)
• DYNVLANREG
• OLM – IPAQENET only
• ADDADDR – IPAQENET6 only
• DELADDR – IPAQENET6 only
• ADDTEMPPREFIX – IPAQENET6 only
• DELTEMPPREFIX – IPAQENET6 only

3/27/2026

https://www.ibm.com/support/pages/node/7231685 © IBM Corporation, 2026 --- Last Updated 3/27/2026

Page 19

DEVNUM Parameter

• Device number (DEVNUM) allows a specific OSH CHPID to

be identified where any available (arbitrary) device (under the
specific OSH CHPID) can be selected and used.
– Configure the first device number in the defined range, such as
2F00, for all INTERFACE statements for a given CHPID, and the
first available device will be used.

• The configured device and the actual device selected for the

•

INTERFACE are not always the same (OSH NETSTAT
displays both the configured and actual device)
If multiple INTERFACEs are configured for the same OSH
CHPID on a TCP/IP stack, then each INTERFACE must
conform to the following rules:
– The configured DEVNUM value must be the same
– A unique VLAN ID for each INTERFACE is required
– VMAC with Route ALL setting is required
– Maximum number of interfaces supported per IP protocol is 32

3/27/2026

https://www.ibm.com/support/pages/node/7231685 © IBM Corporation, 2026 --- Last Updated 3/27/2026

Page 20

Migration Option

3/27/2026

https://www.ibm.com/support/pages/node/7231685 © IBM Corporation, 2026 --- Last Updated 3/27/2026

Page 21

Migration

• As a TEMPORARY migration option from IPAQENET to

EQENET, add the following to IPAQENET:
– DEVNUM parameter
– IPADDR with subnet mask (IPv4) if not already defined
– VMAC if not already defined (if missing it will by dynamically

created)

•

•

If IPAQENET is started on a pre-z17 the Interface will be
brought up as an IPAQENET, ignoring DEVNUM.
If IPAQENET is started on a z17 the Interface will be
brought up as an EQENET, ignoring PORTNAME and
other IPAQENET only parameters.

3/27/2026

https://www.ibm.com/support/pages/node/7231685 © IBM Corporation, 2026 --- Last Updated 3/27/2026

Page 22

Migration

•

Temporary IPAQENET example:

•

Final EQENET example:

INTERFACE O4ETHA2 DEFINE IPAQENET
DEVNUM 2B70
PORTNAME PORTQDIO
IPADDR 16.12.37.160/20
VLANID 702
MTU 1500
READSTORAGE GLOBAL
INBPERF DYNAMIC WORKLOADQ
SMCR PFID 3140 SMCRIPADDR 16.12.37.165

INTERFACE O4ETHA2 DEFINE EQENET
DEVNUM 2B70
IPADDR 16.12.37.160/20
VLANID 702
MTU 1500
SMCR PFID 3140 SMCRIPADDR 16.12.37.165

•

Temporary IPAQENET6 example:

•

Final EQENET6 example:

INTERFACE V6O4ETHA2 DEFINE IPAQENET6
DEVNUM 2B70
PORTNAME PRT6QDIO
INTFID 0:16:207:3
IPADDR 2001:0DB8:172::16:207:13
VLANID 601
MTU 9000
READSTORAGE GLOBAL INBPERF DYNAMIC WORKLOADQ

INTERFACE V6O4ETHA2 DEFINE EQENET6
DEVNUM 2B70
INTFID 0:16:207:3
IPADDR 2001:0DB8:172::16:207:13
VLANID 601
MTU 9000

Change Interface type to EQENET/6 after move to z17.

3/27/2026

https://www.ibm.com/support/pages/node/7231685 © IBM Corporation, 2026 --- Last Updated 3/27/2026

Page 23

Display Output

3/27/2026

https://www.ibm.com/support/pages/node/7231685 © IBM Corporation, 2026 --- Last Updated 3/27/2026

Page 24

Display CHPID

08.57.47 D M=CHP(09)
08.57.47 IEE174I 08.57.47 DISPLAY M 867
CHPID 09: TYPE=35, DESC=OSA HYBRID, ONLINE
DEVICE STATUS FOR CHANNEL PATH 09

0 1 2 3 4 5 6 7 8 9 A B C D E F
2B7 + + + + . . . . . . . . . . . .
SWITCH DEVICE NUMBER = NONE
****************** SYMBOL EXPLANATIONS ******************
+ ONLINE @ PATH NOT VALIDATED - OFFLINE . DOES NOT EXIST
* PHYSICALLY ONLINE $ PATH NOT OPERATIONAL

CHPID Type 35 for OSH

The number of devices defined in VTAM is not required to match the number in HCD.
The VTAM definition can’t exceed the number defined in HCD.
3/27/2026

https://www.ibm.com/support/pages/node/7231685 © IBM Corporation, 2026 --- Last Updated 3/27/2026

Page 25

Display PCIE

09.38.57 D PCIE
09.38.57 IQP022I 09.38.57 DISPLAY PCIE 767
PCIE 0010 ACTIVE
PFID     DEVICE TYPE NAME STATUS ASID JOBNAME CHID VFN PN
00000501 Network Express  CNFG                02FC 0001 1
00000502 Network Express  CNFG                02FC 0002 1

Port Number is always 1.

09.58.32 D PCIE,PFID=501
09.58.32 IQP024I 09.58.32 DISPLAY PCIE 776
PCIE 0010 ACTIVE
PFID     DEVICE TYPE NAME STATUS ASID JOBNAME CHID VFN PN
00000501 Network Express  CNFG                02FC 0001 1
CLIENT ASIDS: NONE
PNetID 1: ZOSNET

3/27/2026

https://www.ibm.com/support/pages/node/7231685 © IBM Corporation, 2026 --- Last Updated 3/27/2026

Page 26

Migration Netstat DevLinks

INTFNAME: O4ETHA2 INTFTYPE: EQENET INTFSTATUS: READY
**AUTOMIGRATED**
DEVNUM: 8102 ACTDEVNUM: 8104 DEVSTATUS: READY
CHPIDTYPE: OSH CHPID: 71 PCHID: 0139
SMCD: YES SMCR: YES PNETID: NETWORK7CD
ADAPTER GEN: NETWORK EXPRESS V1.0
TRLE: IUTE8104 CODE LEVEL: 3031000000001440
PORTNAME: EZAP8104
SPEED: 0000010000 (10G)
IPBROADCASTCAPABILITY: NO
VMACADDR: 42000C69C925 VMACORIGIN: OSA VMACROUTER: ALL
CFGMTU: 9000 ACTMTU: 9000
IPADDR: 16.12.37.160/20
VLANID: 702 VLANPRIORITY: DISABLED
TOTAL READ STORAGE: 19.0M
CHECKSUMOFFLOAD: YES SEGMENTATIONOFFLOAD: YES
SECCLASS: 255 MONSYSPLEX: YES
ISOLATE: NO

**AUTOMIGRATED** indicates that IPAQENET was automatically migrated to EQENET.
EQENET missing VMAC parameter is auto-generated.
IP Address and Subnet Mask is required.

3/27/2026

https://www.ibm.com/support/pages/node/7231685 © IBM Corporation, 2026 --- Last Updated 3/27/2026

Page 27

Migration Netstat DevLinks (cont.)

DISPLAY OSAINFO RESULTS FOR INTFNAME: O7ETHB0
DATAPATH: 2FA0 REALADDR: 0045
PCHID: 0114 CHPID: D2 CHPID TYPE: OS?
OSA CODE LEVEL: 3031240022221484
ACTIVE SPEED: 10 GB/SEC GEN: NETWORK EXPRESS V1.0
MEDIA: MULTIMODE FIBER JUMBO FRAMES: YES ISOLATE: NO
PHYSICALMACADDR: 9C63C0530F12 LOCALLYCFGMACADDR: 9C63C0530F12
QUEUES DEFINED OUT: 5 IN: 8 ANCILLARY QUEUES IN USE: 7
SAPSUP: 00400001 SAPENA: 00000000
INTERFACE PACKET DROPS: 0
CONNECTION MODE: LAYER 2
IPV4 ATTRIBUTES:
VLAN ID: 663 VMAC ACTIVE: YES
VMAC ADDR: 42006A530F12 VMAC ORIGIN: OSA VMAC ROUTER: ALL
REGISTERED ADDRESSES:
IPV4 UNICAST ADDRESSES FOR ARP OFFLOAD:
ADDR: 16.11.16.105
ADDR: 16.11.17.105
ADDR: 16.11.19.105
TOTAL NUMBER OF IPV4 ADDRESSES: 3

3/27/2026

https://www.ibm.com/support/pages/node/7231685 © IBM Corporation, 2026 --- Last Updated 3/27/2026

Page 28

EQENET Netstat DevLinks

INTFNAME: O4ETHA1 INTFTYPE: EQENET INTFSTATUS: READY
DEVNUM: 8102 ACTDEVNUM: 8102 DEVSTATUS: READY
CHPIDTYPE: OSH CHPID: 71 PCHID: 0139
SMCD: YES SMCR: YES PNETID: NETWORK7CD
ADAPTER GEN: NETWORK EXPRESS V1.0
TRLE: IUTE8102 CODE LEVEL: 3031000000001440
PORTNAME: EZAP8102
SPEED: 0000010000 (10G)
IPBROADCASTCAPABILITY: NO
VMACADDR: 42000A69C925 VMACORIGIN: OSA VMACROUTER: ALL
CFGMTU: 9000 ACTMTU: 9000
IPADDR: 16.11.37.160/20
VLANID: 602 VLANPRIORITY: DISABLED
TOTAL READ STORAGE: 19.0M
CHECKSUMOFFLOAD: YES SEGMENTATIONOFFLOAD: YES
SECCLASS: 255 MONSYSPLEX: YES
ISOLATE: NO
MULTICAST SPECIFIC:
MULTICAST CAPABILITY: YES
GROUP REFCNT SRCFLTMD
----- ------ --------
224.0.0.5 0000000001 EXCLUDE
SRCADDR: NONE
224.0.0.1 0000000001 EXCLUDE
SRCADDR: NONE
3/27/2026

Interface type = EQENET
Configured Device Number = DEVNUM
Actual Device Number = ACTDEVNUM
CHPID Type = OSH
OSA Adapter Generation = NETWORK EXPRESS V1.0
TRLE and PORTNAME dynamically created
OSA Firmware displayed = CODE LEVEL
ReadStorage dynamically managed

https://www.ibm.com/support/pages/node/7231685 © IBM Corporation, 2026 --- Last Updated 3/27/2026

Page 29

EQENET Netstat DevLinks (cont.)

INTERFACE STATISTICS:
BYTESIN = 8042214
INBOUND PACKETS = 81593
INBOUND PACKETS IN ERROR = 0
INBOUND PACKETS DISCARDED = 0
INBOUND PACKETS WITH NO PROTOCOL = 0
BYTESOUT = 1025416
OUTBOUND PACKETS = 10502
OUTBOUND PACKETS IN ERROR = 0
OUTBOUND PACKETS DISCARDED = 0
ASSOCIATED IQD CONVERGED INTERFACE: EZAIQCF9 IQC STATUS: READY
BYTESIN = 19714
INBOUND PACKETS = 121
BYTESOUT = 53236
OUTBOUND PACKETS = 464
SMCR CAPABILITY: V2
ASSOCIATED MULTI-SUBNET RNIC INTERFACE: EZARIUT1314E
ROCE PFID: 314E SMCRMTU: 4096
SMCRIPADDR: 16.11.39.160
UNASSOCIATED ISM INTERFACES: EZAISMU1 EZAISMU2 EZAISMU3 EZAISMU4
IPV4 LAN GROUP SUMMARY
LANGROUP: 00002
NAME STATUS ARPOWNER VIPAOWNER
---- ------ -------- ---------
O4ETHA1 ACTIVE O4ETHA1 NO
O4ETHA0 ACTIVE O4ETHA0 YES xxx

HiperSockets Converged Interface

Shared Memory Communications

3/27/2026

https://www.ibm.com/support/pages/node/7231685 © IBM Corporation, 2026 --- Last Updated 3/27/2026

Page 30

D NET,TRL,TRLE=IUTE3B20

IST2480I CACHED READ STORAGE = 3.0M
IST2481I TOTAL READ STORAGE = 28.0M
IST924I -----------------------------------
IST2473I OUTBOUND TRANSMISSION INFORMATION:
IST924I -----------------------------------
IST2474I QUEUE/ QUEUE UNITS OF WORK QUEUE
IST2475I ID TYPE CUR AVG MAX STATUS
IST2205I ------- --------- ----------------
IST2476I CTRL/1 CONTROL 0 1 4 UNCONGESTED
IST2477I WRT/2 PRIORITY1 0 2 2 UNCONGESTED
IST2477I WRT/3 PRIORITY2 0 2 3 UNCONGESTED
IST2477I WRT/4 PRIORITY3 0 0 0 UNCONGESTED
IST2477I WRT/5 PRIORITY4 0 2 3 UNCONGESTED

IST075I NAME = IUTE3B20, TYPE = TRLE
IST1954I TRL MAJOR NODE = ISTTRL
IST486I STATUS= ACTIV, DESIRED STATE= ACTIV
IST087I TYPE = *NA* , CONTROL = MPC , HPDT = *NA*
IST1715I MPCLEVEL = EQDIO MPCUSAGE = EXCLUSIVE
IST2337I CHPID TYPE = OSH CHPID = D5 PNETID = PLEX1
IST1221I EQDIO DEV = 3B20 STATUS = ACTIVE STATE = ONLINE
IST1717I ULPID = TCPSVT ULP INTERFACE = O7ETHD0
IST2309I ACCELERATED ROUTING ENABLED
IST924I ------------------------------------------------
IST2468I INBOUND TRANSMISSION INFORMATION:
IST924I ------------------------------------------------
IST2469I QUEUE/ QUEUE STORAGE QUEUE
IST2470I ID TYPE CUR MIN MAX STATUS
IST2205I ------- -------- ------------------- ----------
IST2471I CTRL/0 CONTROL 1.0M 1.0M 1.0M ACTIVE
IST2472I READ/6 PRIMARY 8.0M 8.0M 8.0M ACTIVE
IST2472I READ/7 BULKDATA 8.0M 8.0M 8.0M ACTIVE
IST2472I READ/8 SYSDIST *NA* *NA* *NA* NOT IN USE
IST2472I READ/9 EE 4.0M 4.0M 4.0M ACTIVE
IST2472I READ/11 ZCX *NA* *NA* *NA* NOT IN USE
IST2472I READ/12 IPROUTER 4.0M 4.0M 4.0M ACTIVE
IST924I ------------------------------------------------

3/27/2026

https://www.ibm.com/support/pages/node/7231685 © IBM Corporation, 2026 --- Last Updated 3/27/2026

Page 31

Limitations/Guidelines

3/27/2026

https://www.ibm.com/support/pages/node/7231685 © IBM Corporation, 2026 --- Last Updated 3/27/2026

Page 32

Limitations/Guidelines

• No EQDIO support on z/OS 2.4 or a VSE client
• SNMP support for OSH will not be available at z17 GA (now targeted for First

Quarter 2026 – depending upon successful testing)

• OSAENTA (NetworkTraffic Analyzer) trace support will not be available

– Alternatively, a sniffer (wireshark) trace may be used

• QDIOSYNC support will not be available

– Automated mechanism to collect Software and Hardware traces concurrently

• NETH PFIDs (RoCE) Guideline

–

For clients using IBM Network Express 10G or 25G with z/OS Communications Server V2.5 or
V3.1, it is recommended to set up a maximum of 16 NETH FIDs.

•

z/OS guest deployed in zVM vSwitch environment must be Layer 3 QDIO
(IPAQENET OSD CHPID OSA-Express)

– A z/VM vSwitch attached to a Network Express card must operate in Layer-2 mode.
– A z/OS guest cannot be deployed on this vSwitch, as the z/OS guest must use a QDIO interface

(a current z/VM limitation) and z/OS does not support Layer-2 with QDIO.
Linux supports both modes today, so Linux guests using QDIO can use this configuration

https://www.ibm.com/support/pages/node/7231685 © IBM Corporation, 2026 --- Last Updated 3/27/2026

Page 33

–

3/27/2026

APARs

3/27/2026

https://www.ibm.com/support/pages/node/7231685 © IBM Corporation, 2026 --- Last Updated 3/27/2026

Page 34

APARs and Performance

• z/OS Communications Server V2.5 and V3.1) APARs:

– OA64896 for SNA
– PH54596 for TCP/IP
IOS APAR:
– OA63265

•

• Performance for new Network Express is here:

– https://www.ibm.com/support/pages/zos-communications-server-

performance-index

3/27/2026

https://www.ibm.com/support/pages/node/7231685 © IBM Corporation, 2026 --- Last Updated 3/27/2026

Page 35

Configurations

3/27/2026

https://www.ibm.com/support/pages/node/7231685 © IBM Corporation, 2026 --- Last Updated 3/27/2026

Page 36

QDIO OSA HCD and TRL

• HCD (Hardware Configuration Definition) or IOCP (Input

Output Configuration Program)
– CHPID type OSD

 Channel path type = OSD
 CNTLUNIT UNIT = OSA
 Device type = OSA

 1 Control (Data Path) device per TCP/IP Interface
 1 Read device per LPAR
 1 Write device per LPAR

 PNET must match RoCE for SMC-R or ISM for SMC-D

• VTAM TRL major node member

TRL VBUILD TYPE=TRL

trl_name TRLE LNCTL=MPC,
READ=(xxx),
MPCLEVEL=QDIO,
WRITE=(yyy),
DATAPATH=(zzz),
PORTNAME=device_name,  (must match Interface)
PORTNUM=n
 Port number is always 0 for 1 port per CHPID cards.

https://www.ibm.com/support/pages/node/7231685 © IBM Corporation, 2026 --- Last Updated 3/27/2026

3/27/2026

Page 37

Network Express OSH HCD & TRLE

• OSH

– HCD or IOCP

 PCHID (Physical Channel ID) – 3 digit hex value of physical slot location

 If defining OSH and NETH, the PCHID must match

 CHPID type OSH to work with EQDIO protocol
 A single Device Number per TCP/IP Interface
 Make sure there is no UNIT=OSAD

 OSA Support Facility (OSA/SF) has not been required for a long time.

– VTAM TRLE is dynamically created

•

If you migrated with manually created TRLE you may remove it after you are
successful with the migration.

3/27/2026

https://www.ibm.com/support/pages/node/7231685 © IBM Corporation, 2026 --- Last Updated 3/27/2026

Page 38

RoCE HCD

• HCD (Hardware Configuration Definition) or IOCP (Input Output

Configuration Program)
‒ PCIe type ROCE or ROCE-2
‒ PCHID (Physical Channel ID) – 3 digit hex value of physical slot location

 PFID (PCIe Function ID) – unique 3 digit hex value per PCHID

 Must match GlobalConfig PFID

 VF (Virtual Function) – unique 2 digit decimal value per PCHID

 Different PFID and VF per TCP/IP stack/port

 PNET (Physical Network) ID - PNET on RoCE and OSA must match
 Adapter Port Number

 SMCv1 port is defined in PROFILE.TCPIP).
 SMCv2 port is defined in HCD.

3/27/2026

https://www.ibm.com/support/pages/node/7231685 © IBM Corporation, 2026 --- Last Updated 3/27/2026

Page 39

Network Express NETH HCD

• NETH

– HCD

 PCHID (Physical Channel ID) – 3 digit hex value of physical slot location

 If defining OSH and NETH, the PCHID must match

 PFID type NETH to work with SMC-R protocol – unique 3 digit hex value per PCHID
 VF (Virtual Function) – unique 2 digit decimal value per PCHID

 Different PFID and VF per TCP/IP stack/port

 PF defined in OSA firmware

– Interface EZARIUTxyyyy dynamically created/started when

Interface EQENET (or OSA-Express7S IPAQENET) is started

 x is always 1 for port and yyyy is the PFID number

3/27/2026

https://www.ibm.com/support/pages/node/7231685 © IBM Corporation, 2026 --- Last Updated 3/27/2026

Page 40

QDIO OSA Interface

• PROFILE.TCPIP INTERFACE IPAQENET or IPAQENET6

‒ PORTNAME device_name (must match OSA TRL)
‒ IPADDR with mask – Required for SMC-R
‒ VLANID optional – see VLAN Considerations on later page
‒ VMAC optional
‒ SMCR – Required for SMC-R (default)

 PFID – Required for SMCv2
 SMCRIPADDR – Required for SMCv2

 Must be in the same subnet as this OSA.
 SMC-Rv2 only supports IPv4. SMC-Dv2 supports IPv4 and IPv6.

 SMCRMTU (defaults to 1024) – Set to 1024, 2048, and 4096
 Used by SMCv2 – Defined on GLOBALCONFIG for SMCv1

‒ SMCD – Required for SMC-D (default)

3/27/2026

https://www.ibm.com/support/pages/node/7231685 © IBM Corporation, 2026 --- Last Updated 3/27/2026

Page 41

Network Express OSH Interface

– PROFILE.TCPIP

 Interface EQENET or EQENET6

 DEVNUM required (define the first device number in the HCD defined range)
 IPADDR required (subnet mask is required for IPv4)
 IPBCAST – optional (enables broadcast packet support)
 ISOLATE – optional (forces packets out onto the LAN rather than allowing packets to route
from LPAR to another LPAR only through the OSA when shared between the two LPARs)

 SECCLASS – optional (used when Multi-level Security is defined)
 MONSYSPLEX – optional (defines sysplex monitoring)
 SMCR – Required for NETH (enabled by default)

o PFID – Required for NETH
o SMCRIPADDR – Required for NETH – Must be in the same subnet as defined above on the

IPADDR parameter or must match the PNET paired OSA IP address.

 SMC-Rv2 only supports IPv4. SMC-Dv2 supports IPv4 and IPv6.

o SMCRMTU – optional (defaults to 1024)

 SMCD – Required for SMC-D (enabled by default)
 SCOURCEVIPAINTERFACE – optional
 MTU – optional (default MTU is 9000 Jumbo Frames)
 VLANID – optional
 VMAC – optional (will be auto-generated if not defined)

3/27/2026

https://www.ibm.com/support/pages/node/7231685 © IBM Corporation, 2026 --- Last Updated 3/27/2026

Page 42

PROFILE.TCPIP for SMC-R

‒ PORT 4791 UDP

 Required for SMCv2 traffic to be routed
 Open port on Routers

‒ GLOBALCONFIG

 SMCR – Required for SMC-R - Default is NOSMCR
 PFID (PCIe Function ID) – Must match HCD PFID

o Required for SMCv1 – (Defined on Interface for SMCv2)
o PORTNUM (Port Number) - defaults to 1

 SMCv1 port is defined here in PROFILE.TCPIP.
 SMCv2 port is defined in HCD.

o MTU (Maximum Transmission Unit)(defaults to 1024)

 Used by SMCv1 – (Defined on Interface for SMCv2)

 SMCGLOBALCONFIG

 SMCEID/ENDSMCEID – creates User Enterprise ID (UEID)

o Required for SMC-Rv2

3/27/2026

https://www.ibm.com/support/pages/node/7231685 © IBM Corporation, 2026 --- Last Updated 3/27/2026

Page 43

SMC-D with ISM

• HCD (Hardware Configuration Definition) or IOCP (Input Output

Configuration Program)
‒ VCHID (Virtual Channel ID)
‒ PNET – Required for SMCv1 but not recommended for SMCv2

• PROFILE.TCPIP
‒ GLOBALCONFIG

 SMCD – Required for SMC-D – Default is NOSMCD

 SYSTEMEID – causes System Enterprise ID (SEID) to be generated

 SMCGLOBALCONFIG

 SMCEID/ENDSMCEID – causes User Enterprise ID (UEID) to be generated

o Required for SMC-Rv2

‒ SMC-Dv2 requires SEID or UEID

3/27/2026

https://www.ibm.com/support/pages/node/7231685 © IBM Corporation, 2026 --- Last Updated 3/27/2026

Page 44

Matches

3/27/2026

https://www.ibm.com/support/pages/node/7231685 © IBM Corporation, 2026 --- Last Updated 3/27/2026

Page 45

OSA and RoCE for SMC-R Matches

• OSA HCD

– CHPID type OSD

 PNET must match RoCE

• RoCE HCD

– PFID must match GlobalConfig
– PNET must match OSA
– Port Number required for SMCv2

 Defined in Profile for SMCv1
• OSA TRL PORTNAME must match

Interface

• PROFILE.TCPIP OSA Interface
IPAQENET or IPAQENET6
– PORTNAME must match TRL
IPADDR with mask required for SMC
–
– SMCR required for SMC-R (default)
 PFID required for SMC-Rv2
 SMCRIPADDR required for SMC-Rv2
o must be in same subnet as this OSA

 SMCRMTU – used by SMC-Rv2

– SMCD required for SMC-D (default)

• PROFILE.TCPIP PORT 4791 UDP

– Required for SMCv2 traffic to be routed
– Open port on Routers

• PROFILE.TCPIP GLOBALCONFIG

– SMCR required for SMC-R
 PFID must match HCD PFID

o Required for SMCv1
o Defined on Interface for SMCv2

 PORTNUM (Port Number) - defaults to 1
o SMCv1 port is defined here.
o SMCv2 port is defined in HCD.

 MTU defaults to 1024

o Used by SMCv1
o Defined on Interface for SMCv2

– SMCGLOBALCONFIG

 SMCEID/ENDSMCEID – creates User

Enterprise ID (UEID)

o Required for SMC-Rv2

3/27/2026

https://www.ibm.com/support/pages/node/7231685 © IBM Corporation, 2026 --- Last Updated 3/27/2026

Page 46

OSA and NETH for SMC-R Matches

• OSA HCD

– CHPID type OSD

 PNET must match RoCE

• NETH HCD

– PFID must match GlobalConfig
– PNET must match OSA
• OSA TRL PORTNAME must

match Interface

• PROFILE.TCPIP OSA Interface
IPAQENET or IPAQENET6
– PORTNAME must match TRL
– IPADDR with mask required for SMC
– SMCR required for SMC-R (default)
 PFID required for SMC-Rv2
 SMCRIPADDR required for SMC-Rv2
o must be in same subnet as this OSA

 SMCRMTU – used by SMC-Rv2

– SMCD required for SMC-D (default)

• PROFILE.TCPIP PORT 4791 UDP

– Required for SMCv2 traffic to be routed
– Open port on Routers

• PROFILE.TCPIP GLOBALCONFIG

– SMCR required for SMC-R
 PFID must match HCD PFID

o Required for SMCv1
o Defined on Interface for SMCv2

 MTU defaults to 1024

o Used by SMCv1
o Defined on Interface for SMCv2

– SMCGLOBALCONFIG

 SMCEID/ENDSMCEID – creates User

Enterprise ID (UEID)

o Required for SMC-Rv2

3/27/2026

https://www.ibm.com/support/pages/node/7231685 © IBM Corporation, 2026 --- Last Updated 3/27/2026

Page 47

OSH and NETH for SMC-R Matches

• OSH HCD

– PCHID must match NETH
– CHPID type OSH

• PROFILE.TCPIP PORT 4791 UDP

– Required for SMCv2 traffic to be routed
– Open port on Routers

 PNET must match NETH

• PROFILE.TCPIP GLOBALCONFIG

• NETH HCD

– PCHID must match OSH

 PFID must match GlobalConfig
 PNET must match OSH
• PROFILE.TCPIP OSH Interface

EQENET

– DEVNUM
– IPADDR with mask required for SMC
– SMCR required for SMC-R (default)
 PFID required for SMC-Rv2
 SMCRIPADDR required for SMC-Rv2

o must be in same subnet as OSH

 SMCRMTU – used by SMC-Rv2

– SMCD required for SMC-D (default)

– SMCR required for SMC-R
 PFID must match HCD PFID

o Required for SMCv1
o Defined on Interface for SMCv2

 MTU defaults to 1024

o Used by SMCv1
o Defined on Interface for SMCv2

– SMCGLOBALCONFIG

 SMCEID/ENDSMCEID – creates User

Enterprise ID (UEID)

o Required for SMC-Rv2

3/27/2026

https://www.ibm.com/support/pages/node/7231685 © IBM Corporation, 2026 --- Last Updated 3/27/2026

Page 48

OSA and ISM for SMC-D Matches

• PROFILE.TCPIP GLOBALCONFIG

– SMCD required for SMC-D

 SYSTEMEID – creates Enterprise ID (EID)

o SMC-Dv2 requires EID or UEID.

– SMCGLOBALCONFIG

 SMCEID/ENDSMCEID – creates User

Enterprise ID (UEID)

o SMC-Dv2 requires UEID or EID

• OSA HCD

– CHPID type OSD

 PNET must match RoCE

•

ISM HCD
– VCHID
– PNET must match OSA

– Required for SMCv1 but not
recommended for SMCv2.

• OSA TRL PORTNAME must

match Interface

• PROFILE.TCPIP OSA Interface
IPAQENET or IPAQENET6
– PORTNAME must match TRL
– IPADDR with mask required for SMC
– SMCR required for SMC-R (default)
– SMCD required for SMC-D (default)

3/27/2026

https://www.ibm.com/support/pages/node/7231685 © IBM Corporation, 2026 --- Last Updated 3/27/2026

Page 49

HS and ISM for SMC-D Matches

• PROFILE.TCPIP GLOBALCONFIG

– SMCD required for SMC-D

 SYSTEMEID – creates Enterprise ID (EID)

o SMC-Dv2 requires EID or UEID.

– SMCGLOBALCONFIG

 SMCEID/ENDSMCEID – creates User

Enterprise ID (UEID)

o SMC-Dv2 requires UEID or EID

• HiperSockets HCD
– CHPID type IQD

 PNET must match ISM

•

ISM HCD
– VCHID
– PNET must match HS

– Required for SMCv1 but not
recommended for SMCv2.

• PROFILE.TCPIP HS Interface

IPAQDIO or IPAQDIO6

– IPADDR with mask required for SMC
– SMCR required for SMC-R (default)
– SMCD required for SMC-D (default)

3/27/2026

https://www.ibm.com/support/pages/node/7231685 © IBM Corporation, 2026 --- Last Updated 3/27/2026

Page 50

OSH and ISM for SMC-D Matches

• PROFILE.TCPIP GLOBALCONFIG

– SMCD required for SMC-D

 SYSTEMEID – creates Enterprise ID (EID)

o SMC-Dv2 requires EID or UEID.

– SMCGLOBALCONFIG

 SMCEID/ENDSMCEID – creates User

Enterprise ID (UEID)

o SMC-Dv2 requires UEID or EID

• OSH HCD

– CHPID type OSH

 PNET must match RoCE

•

ISM HCD
– VCHID
– PNET must match OSA

– Required for SMCv1 but not
recommended for SMCv2.

• PROFILE.TCPIP OSH Interface

EQENET or EQENET6

– IPADDR with mask required for SMC
– SMCR required for SMC-R (default)
– SMCD required for SMC-D (default)

3/27/2026

https://www.ibm.com/support/pages/node/7231685 © IBM Corporation, 2026 --- Last Updated 3/27/2026

Page 51

VLAN

https://www.ibm.com/support/pages/system/files/inline-files/SMC-
Rv2%20RoCE%20VLAN%20Requirements_0.pdf

3/27/2026

https://www.ibm.com/support/pages/node/7231685 © IBM Corporation, 2026 --- Last Updated 3/27/2026

Page 52

VLAN Considerations – VLAN Mode

1. Switch Configuration - VLAN mode

Ethernet switch port “VLAN mode” consistency (trunk or access).
The Ethernet switch port “VLAN mode” must be consistent among
all of the OSA Express (or Network Express OSH) Ethernet ports
and their associated RoCE Express (or Network Express NETH)
ports.
– Trunk Mode:

• When your OSA (or Network Express OSH) switch ports are configured in

trunk mode, then your RoCE (or NETH) switch ports must also be
configured in trunk mode and enabled for all associated OSA (or OSH)
VLANs

– Access Mode:

• When your OSA (or OSH) switch ports are configured in access mode, then
your RoCE (or NETH) switch ports must also be configured in access mode
within a single VLAN. The single VLAN ID used for RoCE (or NETH) is not
required to match your OSA (or OSH) VLAN IDs.

3/27/2026

https://www.ibm.com/support/pages/node/7231685 © IBM Corporation, 2026 --- Last Updated 3/27/2026

Page 53

VLAN Considerations – RoCE VLAN IDs

2. Switch Configuration:  RoCE features (switch ports)

VLAN IDs
The RoCE Express (or Network Express NETH) require consistent
(equal) VLAN access.
The RoCE Express (or Network Express NETH) must all have
access to the same VLAN ID(s).
– Trunk mode:

•

If you are using trunk mode, the switch ports that are serving the RoCE
Express (or Network Express NETH) features (ports) on a PNET must all be
configured with the same set of VLAN IDs as all of the associated OSA
Express (or Network Express OSH) features (switch ports).

– Access mode:

•

If you are using access mode, the switch ports that are serving the RoCE
Express (or Network Express NETH) features (ports) on a PNET must all be
configured with the same (single) VLAN ID. The RoCE (or NETH) VLAN ID
is not required to match any of the VLAN IDs of the associated OSA Express
or (Network Express OSH) features.

3/27/2026

https://www.ibm.com/support/pages/node/7231685 © IBM Corporation, 2026 --- Last Updated 3/27/2026

Page 54

VLAN Considerations – VLAN Mode

3. z/OS Host: z/OS (hosts) VLAN mode consistency

The VLAN mode (as defined within the OS) must be consistent
among all of the hosts that will communicate over a LAN fabric
(PNET) using SMC-R.
You can't mix access and trunk modes among the z/OS hosts
(TCP/IP OSA or OSH INTERFACE statement) on the same PNET.
– The INTERFACE statement in the TCP/IP profile does not have a VLAN

Mode parameter. Instead, the INTERFACE statement supports the
concept of VLAN mode as follows:

• The host definition is considered to be in access mode when VLANs are not

defined (i.e. the host is “unaware” of VLAN).

• The host definition is considered to be in trunk mode when a VLAN ID is

configured (i.e. the host is “aware” of VLANs).

– VLAN IDs are not configured in z/OS for RoCE (or NETH).  Instead the
RoCE (or NETH) VLAN IDs are “inherited” from the OSA (or OSH)
definitions (INTERFACE statements).

3/27/2026

https://www.ibm.com/support/pages/node/7231685 © IBM Corporation, 2026 --- Last Updated 3/27/2026

Page 55

Examples

3/27/2026

https://www.ibm.com/support/pages/node/7231685 © IBM Corporation, 2026 --- Last Updated 3/27/2026

Page 56

ROCE HCD PFID Details

•

Define PFID (PCIe Function ID) with PNet ID
Must match what is defined in PROFILE.TCPIP.

FUNCTION FID=fid_value,PCHID=pchid_value,VF=virt_func,PART=((init_access),

(candidate_list)),PNETID=pnetid_name

Must match what is defined on OSA.

– FID fid_value is 3 hex characters (000-0FF on zEC12)(000-FFF on z13)

• Unique per FUNCTION statement

– PCHID pchid_value is physical slot location (3 hex characters)
– VF virt_func is unique per FUNCTION statement (2 digit decimal number)
– PNET pnetid_name_port1 defines network name for port 1
• Must be the same on all FUNTION statements for the same PCHID
– PNET pnetid_name_port2 defines network name for port 2
• Must be the same on all FUNTION statements for the same PCHID
Example:
FUNCTION FID=100,PCHID=400,VF=1,PART=((LPA,(LPA,LPB)),PNETID=(ZOSNET1,ZOSNET2)
FUNCTION FID=101,PCHID=400,VF=2,PART=((LPA,(LPA,LPB)),PNETID=(ZOSNET1,ZOSNET2)
FUNCTION FID=102,PCHID=400,VF=3,PART=((LPA,(LPA,LPB)),PNETID=(ZOSNET1,ZOSNET2)
RoCE not defined with CHPID number.
RoCE Physical Channel ID (PCHID) represents the physical location of the PCIe device in the
PCIe drawer.
Separate FUNCTION statement / FID/ VF per LPAR per TCP/IP stack per port

3/27/2026

https://www.ibm.com/support/pages/node/7231685 © IBM Corporation, 2026 --- Last Updated 3/27/2026

57

•

•
•

•

PNet ID in HCD Details

Hardware Configuration Definition (HCD)

Defined on OSA and RoCE and
must match for required association.

•
•
•

•

The PNet ID (Physical Network Identifier) is how the OSA and RoCE are bound together.
Used to identify the physical network and may contain multiple logical networks (VLANs).
Add PNet ID to RoCE and OSA in HCD

–
–
–

Enter Physical network ID on the “Add/Modify Physical Network IDs” panel.
Physical network ID 1 maps to OSA port 0 or RoCE port 1
Physical network ID 2 maps to OSA port 1 or RoCE port 2

Dynamic I/O Reconfiguration may be used to define PNET on an OSA that is in use. In order to pick
up the change the OSA will require a CHPID OFF and then CHPID ON (from every LPAR sharing it).

3/27/2026

https://www.ibm.com/support/pages/node/7231685 © IBM Corporation, 2026 --- Last Updated 3/27/2026

58

GLOBALCONFIG Details

• Define GLOBALCONFIG in PROFILE.TCPIP

GLOBALCONFIG

Must match
what is defined
in HCD.

Required to enable SMC-R in TCP/IP

SMCR
PFID fid_value PORTNUM port_number
MTU mtusize FIXEDMEMORY mem_amount
TCPKEEPMININTERVAL interval_amount

PORTNUM defaults to 1 (for
physical port labeled D1)

When this memory is exceeded
all new sessions will use the
TCP/IP OSA OSD connection.

•

Example
GLOBALCONFIG

SMCR
PFID 001C
PFID 0015 PORTNUM 2
FIXEDMEMORY 200
TCPKEEPMININTERVAL 300

PORTNUM 2 (for physical port labeled D2)

HCD FID = 000 to 0FF on zEC12 or 000-FFF on z13
SMCR PFID = 0000 to 00FF on zEC12 or 0000-0FFF on z13
Values must match!

3/27/2026

https://www.ibm.com/support/pages/node/7231685 © IBM Corporation, 2026 --- Last Updated 3/27/2026

59

Other Optional PROFILE.TCPIP
GLOBALCONFIG Definitions

• SMCGLOBAL

‒ AUTOCACHE - Specifies whether this stack caches unsuccessful attempts

to use SMC communication. AUTOCACHE is the default.

‒ AUTOSMC - Specifies whether this stack monitors inbound TCP

connections to dynamically determine whether SMC is beneficial for a local
TCP server application. AUTOSMC is the default.

‒ SMCPERMIT/ENDSMCPERMIT - Specifies the SMC filter that allows SMC

negotiation with peers within the listed TCP/IP address(es)/subnet(s).

‒ SMCEXCLUDE/ENDSMCEXCLUDE - Specifies the SMC filter that prevents
SMC negotiation with peers within the listed TCP/IP address(es)/subnet(s).

• SMCD and SMCR

‒ FIXEDMEMORY - Specifies the maximum amount of 64-bit storage that the
stack can use for the send and receive buffers that are required for SMC-D
and SMC-R communications. 256 megabytes default.

‒ TCPKEEPMININTERVAL - This interval specifies the minimum interval that
TCP keepalive packets are sent on the TCP path of an SMC-D or SMC-R
link. 300 seconds default.

3/27/2026

https://www.ibm.com/support/pages/node/7231685 © IBM Corporation, 2026 --- Last Updated 3/27/2026

Page 60

Network Express Example

• OSH and NETH IOCDS Example

FUNCTION PCHID=100,FID=(2000,3),PART=((LP1),(LP3)),TYPE=NETH,VF=1
FUNCTION PCHID=100,FID=(2100,2),PART=LP2,TYPE=NETH,VF=8
FUNCTION PCHID=100,FID=2200,PART=LP2,TYPE=NETH,VF=40,FIDPARM=01
CHPID PCHID=100,TYPE=OSH,PART=(LP1,LP2,LP3),PATH=80,SHARED
CHPID PCHID=101,TYPE=OSH,PART=(LP5,LP6),PATH=85,SHARED
–

–

–

FIDs 2000-2002 with VFs 1-3 are defined on a new VCHID1 as type NETH. They are assigned to partition LP1 and
can be reconfigured to LP3. FID 2000 also defines PCHID 100 as a Hybrid PCHID. So FID 2000 defines PCHID 100
and a VCHID. The VCHID points back to PCHID 100. All FIDs point to the VCHID.
FIDs 2100-2101 with VFs 8-9 are also defined for PCHID 100 and the same VCHID as above with type NETH. They
are assigned to partition LP2 and can be reconfigured to any partition in the system. The FIDs point to the VCHID
created with FID 2000.
FID 2200 with VF 40 is also defined for PCHID 100 and the same VCHID as above with type NETH. It is assigned to
LP2 and can be reconfigured to any partition in the system. The VF permits the exploitation of Promiscuous Mode by
the operating system. FIDPARM=01 allows the FID(s) on that statement to use promiscuous mode but the operating
system has to turn it on. If the FIDPARM value is 00 or not specified, then promiscuous mode is not allowed, and the
OS can not turn it on. The 01 value is a permission setting.

– CHPID 80 (ignoring CSS for this discussion) defines a VCHID as type OSH. The CHPID is shared by partitions LP1,
LP2, and LP3 and can be configured to any partition in the same CSS. The VCHID points to Hybrid PCHID 100.
– CHPID 85 (ignoring CSS for this discussion) defines a VCHID as type OSH. The CHPID is shared by partitions LP5
and LP6 and can be configured to any partition in the CSS. The CHPID also defines PCHID 101 as a Hybrid PCHID.
The VCHID points back to Hybrid PCHID 101.

– Note 1. OSH / NETH VCHIDs are an internal construct used internally to represent one of two “personalities” OSA or

RoCE.

– Note 2. The z/OS requirement for PNETID for OSA or RoCE (SMC-R or HSCI) has not changed.

3/27/2026

https://www.ibm.com/support/pages/node/7231685 © IBM Corporation, 2026 --- Last Updated 3/27/2026

Page 61

Some Useful Commands for OSA
Information

•

IP Commands

– See the IP System Administrator’s Commands manual for syntax and details.
– Vary TCPIP,procname,OSAENTA

• Control the OSA-Express Network Traffic Analyzer (OSAENTA) tracing facility.

– Vary TCPIP,procname,START/STOP,device_name/interface_name

• Start or stop device or interface.
– NETSTAT ARp/-R ip_addr/ALL…

• Output includes the ip_addr to MAC address mapping.

– NETSTAT DEvlinks/-d…

• Output includes information about devices, links, and interfaces.

– NETSTAT HOme/-h…

• Output includes the IP Addresses to links/interfaces mapping.

– NETSTAT SRCIP/-J…

• Output includes Source IP Address information.

•

VTAM Commands

– See the SNA Operations manual for syntax and details.
– DISPLAY NET,ID=xcaname…
• Output includes LINE and PU.

– DISPLAY NET,TNSTAT

• Output indicates which TRLEs are collecting statistics if start option TNSTAT is specified.

– DISPLAY NET,TRL… and DISPLAY NET,TRL,TRLE=…

• Output includes TRL/TRLE information.

– MODIFY procname,TRACE/NOTRACE,TYPE=QDIOSYNC…

• Control QDIO Synchronization Trace

3/27/2026

https://www.ibm.com/support/pages/node/7231685 © IBM Corporation, 2026 --- Last Updated 3/27/2026

Page 62

Appendix
Backup Charts

3/27/2026

https://www.ibm.com/support/pages/node/7231685 © IBM Corporation, 2026 --- Last Updated 3/27/2026

63

Memory

• SMC-R RDMA Memory

– Is managed and owned by the TCP/IP stack.
– Is allocated within TCP (ASID) 64-bit private.
– Is not CSM-managed.
– Application memory management is not affected.
– Most is a variable amount defined and managed by the TCP/IP

stack.

• Small static portion is managed by the device driver.

– Is fixed memory.
– Defined and limited by the FIXEDMEMORY parameter on the

GLOBALCONFIG SMCR statement.

3/27/2026

https://www.ibm.com/support/pages/node/7231685 © IBM Corporation, 2026 --- Last Updated 3/27/2026

64

Exclude Some Traffic

LPAR A

Application

SMC-R

TCP/IP

RNIC

OSA

CEC 1

HiperSockets
network

LPAR A
Application

Application

CEC 1

LPAR A

Application

TCP/IP SMC-R

SMC-R

TCP/IP

OSA

RNIC

RNIC

OSA

10Gb
Ethernet
network

• NOSMCR parameter may be used on the PORT or PORTRANGE

statement in the PROFILE.TCPIP to prevent traffic being eligible for SMC-R
RoCE.

– PORT

3301 TCP ABC01 NOSMCR

3/27/2026

https://www.ibm.com/support/pages/node/7231685 © IBM Corporation, 2026 --- Last Updated 3/27/2026

65

SMC-R and RoCE

• Both SMC-Rv1 and RoCEv1 Client and Server:
- Must have profile GLOBALCONFIG SMCR with PFID
- Must have OSA interface configured with the same IP Subnet (for IPv4 or IP mask
for IPv6), the same VLAN ID (if VLAN is applicable), and configured with SMCR.
- Must have RoCE RNIC access to the same physical Layer-2 network (same physical

LAN)

- TCP/IP connection must not require IPsec encryption

• Both SMC-Rv2 and RoCEv2 Client and Server:

- Must have profile GLOBALCONFIG SMCR SMCGLOBAL SMCEID/ENDSMCEID
- Must have OSA interface configured with SMCR PFID and SMCIPADDR
- Must have RoCE RNIC
- TCP/IP connection must not require IPsec encryption

663/27/2026

https://www.ibm.com/support/pages/node/7231685 © IBM Corporation, 2026 --- Last Updated 3/27/2026

SMC-D and ISM

• Both SMCv1 and ISMv1 Client and Server:

- Must have access to a common ISM VCHID and PNET
- Must be enabled for SMCD in the Profile
- Must not be associated with a TCP/IP connection that requires IPsec

encryption

• Both SMCv2 and ISMv2 Client and Server:

- Must be updated to support SMC-Dv2 (z/OS 2.4 with PTFs)
- Must execute on the same IBM Z System CPC that supports ISMv2 (z15+)
- Must have access to a common ISM VCHID
- Must be SMCv2 enabled, defined with the same EID (user defined (UEID) or

system defined(SEID))

- Must not be associated with a TCP/IP connection that requires IPsec

encryption

673/27/2026

https://www.ibm.com/support/pages/node/7231685 © IBM Corporation, 2026 --- Last Updated 3/27/2026

END

3/27/2026

https://www.ibm.com/support/pages/node/7231685 © IBM Corporation, 2026 --- Last Updated 3/27/2026

Page 68

