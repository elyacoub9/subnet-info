
generate the following:
- **Class Type**
- **address Type** 
- **Subnet Mask**
- **Network ID**
- **Broadcast ID** 
- **First Address** 
- **Last Address.
- **Number of Addresses** 



1. Clone this repository:

   ```bash
   git clone https://github.com/elyacoub9/subnet-info.git
   ```

2. Change to the project directory:

   ```bash
   cd subnet-info
   ```


The script will provide information about the specified IP address and subnet.

run your code

```bash
   python3 subnet-info.py 172.16.0.7 23
   ```
Output
```Output
------------------------------------------------------------
                       10.10.10.0/23
------------------------------------------------------------
 class                        |            class A
 type [10.10.10.0]            |            private
 subnet mask                  |         255.255.254.0
 network id                   |           10.10.10.0
 broadcast id                 |          10.10.11.255
 first address                |           10.10.10.1
 last address                 |          10.10.11.254
 no of addresses              |              510

```
