"""
NOSLEEP FAST RANGER IPS - Copyright (c) 2023
Author: @Tux-MacG1v (Tux Macgiver)
--
Licensed under the GNU General Public License v3.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at
    https://www.gnu.org/licenses/gpl-3.0.en.html
Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

import numpy as np
from numba import jit
import time

banner = """
    [!]   NOSLEEP FAST RANGER IPS (FREE)
          - FILE FORMAT: STARTIP-ENDIP
          -  CW: CODED BY TUX-MACG1V
          -  DM: @I_am_a_silent_killer
          -  CH: @tuxbotandtoolshop

"""

ip_buffer = []


def save(ip_addresses):
    global ip_buffer
    ip_buffer.extend(ip_addresses)
    if len(ip_buffer) >= 1000:
        with open("ip_addresses.txt", "a") as file:
            file.write("\n".join(ip_buffer) + "\n")
        ip_buffer.clear()


@jit(forceobj=True, parallel=True)
def process_ip_range(ip_range, start_ip, end_ip):
    start = time.time()
    ip_addresses = []
    while np.all(start_ip <= end_ip):
        ip_addresses.append('.'.join(map(str, start_ip)))
        start_ip = np.add(start_ip, np.array([0, 0, 0, 0]))
        start_ip[3] += 1
        for i in range(3, 0, -1):
            if start_ip[i] == 256:
                start_ip[i] = 0
                start_ip[i - 1] += 1
            else:
                break
    rangeipformat = ip_range.replace("\n", "")
    print(f'\n┏─╼RANGE INPUT: [{rangeipformat}]\n┠─╼Total IPs: [{len(ip_addresses)}]\n┗┉┉WORKTIME: [{(time.time() - start)}] SECOND!')
    save(ip_addresses)


@jit(forceobj=True, parallel=True)
def starting(ip_ranges):
    for ip_range in ip_ranges:
        start_ip, end_ip = ip_range.strip().split("-")
        start_ip = np.array([int(x) for x in start_ip.split('.')])
        end_ip = np.array([int(x) for x in end_ip.split('.')])
        process_ip_range(ip_range, start_ip, end_ip)


def main():
    print(banner)
    file_path = input("GIVE ME RANGER FILE: ")
    startr = time.time()
    with open(file_path, 'r') as file:
        ip_ranges = file.readlines()
        starting(ip_ranges)
    print(f'\n\n╓───►[WORKED DONE SIR]\n╠───►MY MACHINE TOOK [{(time.time() - startr):.2f}] SEC FOR HELP YOU:)')
    print(f'╙►------------- [ - TuxMacG1v]')
    time.sleep(50)


if __name__ == '__main__':
    main()
