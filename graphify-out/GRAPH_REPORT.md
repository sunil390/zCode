# Graph Report - .  (2026-04-12)

## Corpus Check
- Corpus is ~26,779 words - fits in a single context window. You may not need a graph.

## Summary
- 27 nodes · 31 edges · 8 communities detected
- Extraction: 94% EXTRACTED · 6% INFERRED · 0% AMBIGUOUS · INFERRED: 2 edges (avg confidence: 0.7)
- Token cost: 0 input · 0 output

## Community Hubs (Navigation)
- [[_COMMUNITY_IBM Z Network Protocols|IBM Z Network Protocols]]
- [[_COMMUNITY_Mainframe Shift Automation|Mainframe Shift Automation]]
- [[_COMMUNITY_Workflow Data Platform|Workflow Data Platform]]
- [[_COMMUNITY_File Generation Utilities|File Generation Utilities]]
- [[_COMMUNITY_NVIDIA Script|NVIDIA Script]]
- [[_COMMUNITY_Task Tracking Script|Task Tracking Script]]
- [[_COMMUNITY_TN3270 Protocol|TN3270 Protocol]]
- [[_COMMUNITY_JMESPath Library|JMESPath Library]]

## God Nodes (most connected - your core abstractions)
1. `Network Express Physical Adapter` - 6 edges
2. `n8n Workflow Orchestration Platform` - 6 edges
3. `Mainframe Shift Operations Platform` - 6 edges
4. `FastMCP Integration Bridge` - 4 edges
5. `SQLite Task Tracking Database` - 4 edges
6. `Python TN3270 Scripts` - 4 edges
7. `z/OS Communications Server` - 3 edges
8. `VS Code GitHub Copilot` - 3 edges
9. `Open Systems Adapter (OSA)` - 2 edges
10. `RDMA over Converged Ethernet (RoCE)` - 2 edges

## Surprising Connections (you probably didn't know these)
- `Ansible Automation Framework` --semantically_similar_to--> `Python TN3270 Scripts`  [INFERRED] [semantically similar]
  README.md → You said  We have the schedule of health checks a....md
- `Python TN3270 Scripts` --references--> `z/OS Communications Server`  [INFERRED]
  You said  We have the schedule of health checks a....md → 2026-03-27-Network-Express-Feature.md

## Hyperedges (group relationships)
- **Network Express Protocol Implementation Stack** — network_express_feature, eqdio_protocol, neth_protocol, smc_r_protocol [EXTRACTED 1.00]
- **Mainframe Shift Operations Architecture** — shift_operations_platform, n8n_platform, fastmcp_bridge, copilot_agent, python_tn3270 [EXTRACTED 1.00]
- **Task State and Data Persistence Layer** — sqlite_database, markdown_checklist_template, github_enterprise_repo, webhook_receiver [EXTRACTED 1.00]

## Communities

### Community 0 - "IBM Z Network Protocols"
Cohesion: 0.36
Nodes (8): Enhanced QDIO (EQDIO) Protocol, NETH Protocol, Network Express Physical Adapter, Open Systems Adapter (OSA), RDMA over Converged Ethernet (RoCE), Shared Memory Communications over RDMA (SMC-R), IBM Z17 Processor, z/OS Communications Server

### Community 1 - "Mainframe Shift Automation"
Cohesion: 0.43
Nodes (7): Ansible Automation Framework, Automated Health Checks, VS Code GitHub Copilot, FastMCP Integration Bridge, Manual Task Workflow, Python TN3270 Scripts, Mainframe Shift Operations Platform

### Community 2 - "Workflow Data Platform"
Cohesion: 0.47
Nodes (6): Docker Container Environment, GitHub Enterprise Repository, Markdown Checklist Template, n8n Workflow Orchestration Platform, SQLite Task Tracking Database, n8n Webhook Receiver

### Community 3 - "File Generation Utilities"
Cohesion: 1.0
Nodes (0): 

### Community 4 - "NVIDIA Script"
Cohesion: 1.0
Nodes (0): 

### Community 5 - "Task Tracking Script"
Cohesion: 1.0
Nodes (0): 

### Community 6 - "TN3270 Protocol"
Cohesion: 1.0
Nodes (1): IBM TN3270 Terminal Emulation

### Community 7 - "JMESPath Library"
Cohesion: 1.0
Nodes (1): jmespath Python Library

## Knowledge Gaps
- **4 isolated node(s):** `IBM TN3270 Terminal Emulation`, `GitHub Enterprise Repository`, `Ansible Automation Framework`, `jmespath Python Library`
  These have ≤1 connection - possible missing edges or undocumented components.
- **Thin community `File Generation Utilities`** (2 nodes): `generate_shift_load_data()`, `FileGenerator.py`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `NVIDIA Script`** (1 nodes): `nvidia1.py`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Task Tracking Script`** (1 nodes): `tasktracker.py`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `TN3270 Protocol`** (1 nodes): `IBM TN3270 Terminal Emulation`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `JMESPath Library`** (1 nodes): `jmespath Python Library`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `Python TN3270 Scripts` connect `Mainframe Shift Automation` to `IBM Z Network Protocols`?**
  _High betweenness centrality (0.331) - this node is a cross-community bridge._
- **Why does `z/OS Communications Server` connect `IBM Z Network Protocols` to `Mainframe Shift Automation`?**
  _High betweenness centrality (0.280) - this node is a cross-community bridge._
- **What connects `IBM TN3270 Terminal Emulation`, `GitHub Enterprise Repository`, `Ansible Automation Framework` to the rest of the system?**
  _4 weakly-connected nodes found - possible documentation gaps or missing edges._