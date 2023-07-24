## GitHub API Usage Understanding & Retrieved Results Investigation


**API Request ["regtech" Topic Repositories Search](https://api.github.com/search/repositories?q=regtech&sort=&order=desc&per_page=100) Endpoint 
URL Parameters:**

- Topic: "regtech"
- Sort: "" (is `best match` by def)
- Order: `desc`
- `per_page`: 100

---
### Returned Result Investigation

**Repository Considered:** [finos/open-regtech-sig](https://github.com/finos/open-regtech-sig)

```
"id": 309452891,
"node_id": "MDEwOlJlcG9zaXRvcnkzMDk0NTI4OTE=",
"name": "open-regtech-sig",
"full_name": "finos/open-regtech-sig",
"private": false,
"owner": {...}
"html_url": "https://github.com/finos/open-regtech-sig",
"description": "The FINOS Regulation Innovation Special Interest Group (SIG) is a community of people interested in creating open source solutions for regulatory and compliance issues in financial services.",
"fork": false,
"url": "https://api.github.com/repos/finos/open-regtech-sig",
... 
"created_at": "2020-11-02T17:58:19Z",
"updated_at": "2023-04-10T19:02:06Z",
"pushed_at": "2021-07-07T14:23:52Z",
```

---
### GitHub Repository Search Activity Date & Time Stamps Info Breakdown 



- `"created_at": "2020-11-02T17:58:19Z"`
  - GitHub date & time stamp: Nov 2, 2020, 5:58 PM GMT+1
  - Timezone: CET
  - Offset: UTC +1h
  - User: Maurizio Pillitu - [maoo](https://github.com/maoo)
  - Location: Barcelona

- `"updated_at": "2023-04-10T19:02:06Z"` 
  - **TEMP. NEGLECTED**

- `"pushed_at": "2021-07-07T14:23:52Z"`
  - GitHub date & time stamp: Jul 7, 2021, 4:23 PM GMT+2
  - Timezone: BST
  - Offset: UTC +1h
  - User: Aitana Myohl - [agitana](https://github.com/agitana)
  - Location: London

---
### UTC, CET/CEST & GMT/BTS Relationship Consideration

- Central European Union (E.U.)
  - E.U. (non daylight savings time) period = CET, UTC/GMT +1H
    - During E.U. CET Period: UTC/GMT +1h
  - E.U. (daylight savings time) period = CEST, UTC/GMT +2H
      - During E.U. CEST Period: UTC/GMT +2h


- United Kingdom (U.K.)
  - U.K. (daylight savings time) period = BST, UTC/GMT +1h
    - During U.K. BST Period: UTC/GMT +1h
  - U.K. (NON daylight savings time) period = GMT, UTC/GMT
    - During U.K. GMT Period: UTC/GMT



---

### GitHub User Accounts Under Consideration

Alexander Xavier O'Rourke Goby - [xaviergoby](https://github.com/xaviergoby)      
Location: Rotterdam    
[Current Offset: UTC/GMT +2 hours](https://www.timeanddate.com/time/zone/netherlands/rotterdam) 

Maurizio Pillitu - [maoo](https://github.com/maoo)  
Location: Barcelona    
[Current Offset: UTC/GMT +2 hours](https://www.timeanddate.com/time/zone/spain/barcelona)   

Aitana Myohl - [agitana](https://github.com/agitana)      
Location: London    
[Current Offset: UTC/GMT +1 hour](https://www.timeanddate.com/time/zone/uk/london)  

---
### GitHub API Datetime Stamps Timezone & Offset Consideration

- maoo (Barcelona): (UTC) "created_at": "2020-11-02T17:58:19Z" ==> xaviergoby (MY LOCAL DT OFFSET - Rotterdam): "created_at": 
"2020-11-02T19:58:19Z" --> 2020-11-02 19:58:19 (NL Time)

- agitana (London): (UTC) "pushed_at": "2021-07-07T14:23:52Z" ==> xaviergoby (MY LOCAL DT OFFSET - Rotterdam): "pushed_at": "2021-07-07T14:23:52Z" 
--> 2020

---
### GitHub API Datetime Stamps Timezone & Offset Consolidation

- So back when maoo did his 1ST commit, on the 2nd of Nov 2020, MY @ THAT POINT IN TIME LOCAL DT OFFSET WAS = UTC/GMT +1h.    

- Now, when agitana did her LAST/LATEST commit, on the 7th of Jul 2021, MY @ THAT POINT IN TIME LOCAL DT OFFSET WAS = UTC/GMT +2h

-----------
### Central European Summer Time Consideration 

- 6:00 PM (18:00) UTC = 8:00 PM (20:00) Central European Summer   

- 4:30 PM (16:30) UTC = 6:30 PM (18:30) Central European Summer   

∴

- 5:58 PM (17:58) UTC = 7:58 PM (19:58) Central European Summer 

- 4:23 PM (16:23) UTC = 6:23 PM (18:23) Central European Summer 

-----------




















