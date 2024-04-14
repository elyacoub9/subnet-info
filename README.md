

- **Class Type:** Determine the class type of the given IP address.
- **address Type:** Privat/Public
- **Subnet Mask:** Calculate the subnet mask corresponding to the CIDR notation.
- **Network ID:** Obtain the network ID of the given IP address and CIDR.
- **Broadcast ID:** Find the broadcast ID for the specified network.
- **First Address:** Determine the first usable address in the given subnet.
- **Last Address:** Calculate the last usable address in the given subnet.
- **Number of Addresses:** Calculate the total addresses in the subnet.



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


I am open to any feedback or suggestions you might have.
