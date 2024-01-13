# Subnet Info

This Python script provides a simple yet powerful tool for calculating various network-related values from a given IP address in a CIDR notation (Subnet). It is useful for anyone dealing with IP address manipulation.

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
   git clone https://github.com/a8m5d/subnet-info.git
   ```

2. Change to the project directory:

   ```bash
   cd subnet-info
   ```

## Usage

1. Input the IP address and CIDR notation when prompted.
2. The script will provide information about the specified IP address and subnet.

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
## licence

This project is licensed under the [GPL-3.0](https://github.com/a8m5d/subnet-info/blob/main/LICENSE) license  License

Feel free to use and modify the script to suit your specific needs.


## Acknowledgments

- Inspired by the need for a quick and easy way to calculate IP-related values.

I am open to any feedback or suggestions for improvement.
