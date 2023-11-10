# IP Address Calculator

This Python script provides a simple yet powerful tool for calculating various network-related values from a given IP address in a CIDR notation. It is particularly useful for anyone dealing with IP address manipulation.

## Features

- **Class Type:** Determine the class type of the given IP address.
- **address Type:** Privat/Public
- **Subnet Mask:** Calculate the subnet mask corresponding to the CIDR notation.
- **Network ID:** Obtain the network ID of the given IP address and CIDR.
- **Broadcast ID:** Find the broadcast ID for the specified network.
- **First Address:** Determine the first usable address in the given subnet.
- **Last Address:** Calculate the last usable address in the given subnet.
- **Number of Addresses:** Calculate the total number of addresses in the subnet.

## Prerequisites

- Python 3.x installed on your system.

## Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/a8m5d/ip-address-calculator.git
   ```

2. Change to the project directory:

   ```bash
   cd ip-address-calculator
   ```

## Usage

1. Input the IP address and CIDR notation when prompted.
2. The script will provide information about the specified IP address and subnet.

run your code

```bash
   python3 ip_calculator.py 172.16.0.7 23
   ```
Output
```Output
------------------------------------------------------------
                       172.16.0.7/23                        
------------------------------------------------------------
 class                        |            class B            
 type                         |             privat            
 subnet mask                  |         255.255.254.0         
 network id                   |           172.16.0.0          
 broadcast id                 |          172.16.1.255         
 first address                |           172.16.0.1          
 last address                 |          172.16.1.254         
 nb of addresses              |              510              


```

Feel free to use and modify the script to suit your specific needs.


## Acknowledgments

- Inspired by the need for a quick and easy way to calculate IP-related values.

i am open for any feedback or suggestions for improvement.
