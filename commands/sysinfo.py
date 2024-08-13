import psutil
import platform
import socket
import datetime
import click
from commands import logger

@click.group(help="a group of commands to display system info.")
def sysinfo():
    """
    main entry point for the system monitoring commands.
    this function allows us to group multiple commands together.
    """
    # placeholder for grouping commands
    pass

# ===== SYSTEM ================

@click.command(help="generate system info.")
def system():
    """
    function collects and displays various system info.
    """
    # calculate uptime in seconds
    uptime_seconds = int(datetime.datetime.now().timestamp() - psutil.boot_time())
    system_info = {
        "System": platform.system(),
        "Node name": platform.node(),
        "Release": platform.release(),
        "Version": platform.version(),
        "Machine": platform.machine(),
        "Processor": platform.processor(),
        "Uptime (seconds)": uptime_seconds,
        "Uptime (human-readable)": str(datetime.timedelta(seconds=uptime_seconds))
    }
    
    # log and print system info
    click.echo(logger.info("\nsystem info:"))
    for k, v in system_info.items():
        click.echo(f"{k}: {v}")
    print()

# ===== CPU ===================

@click.command(help="generate cpu info.")
def cpu():
    """
    function collects and displays system cpu info.
    """
    cpu_info = {
        "Physical Cores": psutil.cpu_count(logical=False),
        "Total Cores": psutil.cpu_count(logical=True),
        "Max Frequency (MHz)": psutil.cpu_freq().max if psutil.cpu_freq() else "N/A",
        "Current Frequency (MHz)": psutil.cpu_freq().current if psutil.cpu_freq() else "N/A",
        "CPU Usage (%)": psutil.cpu_percent(interval=1),
        "CPU Times": psutil.cpu_times()._asdict()
    }

    # log and print cpu info
    click.echo(logger.info("\ncpu info:"))
    for k, v in cpu_info.items():
        print(f"{k}: ", end="")
        if isinstance(v, dict):
            # new line for nested dict
            print()
            for inner_k, inner_v in v.items():
                # print nested values
                print(f"  - {inner_k}: {inner_v}")
        else:
            # print the value
            print(v)
    # for better spacing
    print()

# ===== RAM ===================

@click.command(help="generate ram info.")
def ram():
    """
    function collects and displays system ram info.
    """
    ram_info = {
        "Total RAM (GB)": round(psutil.virtual_memory().total / (1024 ** 3), 2),
        "Available RAM (GB)": round(psutil.virtual_memory().available / (1024 ** 3), 2),
        "Used RAM (GB)": round(psutil.virtual_memory().used / (1024 ** 3), 2),
        "RAM Usage (%)": psutil.virtual_memory().percent,
    }

    # log and print ram info
    click.echo(logger.info("\nram info:"))
    for k, v in ram_info.items():
        click.echo(f"{k}: {v}")
    # consistent spacing
    print()

# ===== DISK ==================

@click.command(help="generate disk info.")
def disk():
    """
    function collects and displays system disk info.
    """
    disk_usage = psutil.disk_usage('/')
    disk_info = {
        "Total Disk Space (GB)": round(disk_usage.total / (1024 ** 3), 2),
        "Used Disk Space (GB)": round(disk_usage.used / (1024 ** 3), 2),
        "Free Disk Space (GB)": round(disk_usage.free / (1024 ** 3), 2),
        "Disk Usage (%)": disk_usage.percent,
        "Disk Partitions": [part._asdict() for part in psutil.disk_partitions()]
    }

    # log and print disk info
    click.echo(logger.info("\ndisk information:"))
    for k, v in disk_info.items():
        print(f"{k}: ", end="")
        if isinstance(v, list):
            # new line for list
            print()
            for inner in v:
                # label for partition info
                print("  - Partition Info:")
                for inner_k, inner_v in inner.items():
                    # print partition details
                    print(f"    {inner_k}: {inner_v}")
                # blank line for spacing
                print()
        else:
            # print the value
            print(v)
    # for better spacing
    print()

# ===== NETWORK ===============

@click.command(help="generate network info.")
def network():
    """
    collects and displays network information.
    """
    # gather network information
    network_info = {
        "Hostname": socket.gethostname(),
        "IP Address": socket.gethostbyname(socket.gethostname()),
        "Network Interfaces": {}
    }

    # retrieve network interface addresses
    for interface, addrs in psutil.net_if_addrs().items():
        network_info["Network Interfaces"][interface] = []
        for addr in addrs:
            network_info["Network Interfaces"][interface].append({
                "Address": addr.address,
                "Family": addr.family,
                "Netmask": addr.netmask,
                # handle possible None
                "Broadcast": addr.broadcast if addr.broadcast else "N/A"
            })

    # log and print network info
    click.echo(logger.info("\nnetwork information:"))
    
    # prepare output as a list of strings
    output = []
    output.append(f"Hostname: {network_info['Hostname']}")
    output.append(f"IP Address: {network_info['IP Address']}")
    output.append("Network Interfaces:")
    
    for interface, addresses in network_info["Network Interfaces"].items():
        output.append(f"  - {interface}:")
        for addr in addresses:
            output.append(f"    - Address: {addr['Address']}")
            output.append(f"      Family: {addr['Family']}")
            output.append(f"      Netmask: {addr['Netmask']}")
            if addr['Broadcast'] != "N/A":
                output.append(f"      Broadcast: {addr['Broadcast']}")
        # blank line for spacing
        output.append("")

    # print all at once
    # join and print the entire output
    print("\n".join(output))

# ===== PROCESS ===============

@click.command(help="generate process info.")
def process():
    """
    collects and displays process information.
    """
    process_info = {
        "Total Processes": len(psutil.pids()),
        "Running Processes": len([p.info for p in psutil.process_iter(attrs=['pid', 'name', 'status']) if p.info['status'] == psutil.STATUS_RUNNING]),
        "Sleeping Processes": len([p.info for p in psutil.process_iter(attrs=['pid', 'name', 'status']) if p.info['status'] == psutil.STATUS_SLEEPING]),
        "Stopped Processes": len([p.info for p in psutil.process_iter(attrs=['pid', 'name', 'status']) if p.info['status'] == psutil.STATUS_STOPPED]),
    }

    # log and print process info
    click.echo(logger.info("\nprocess information:"))
    for k, v in process_info.items():
        click.echo(f"{k}: {v}")
    # for better spacing
    print()

# ===== GROUP =================

# add commands to the sysinfo group
sysinfo.add_command(system)
sysinfo.add_command(cpu)
sysinfo.add_command(ram)
sysinfo.add_command(disk)
sysinfo.add_command(network)
sysinfo.add_command(process)

# check if this is the main module
if __name__ == "__main__":
    sysinfo()
