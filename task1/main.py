# System Health Monitoring Bot
print('Welcome to System Health Monitoring Bot.\n')

# Function to check CPU usage
def checkCpuUsage(cpuUsage):
    if cpuUsage <40:
        return 'underutilised'
    elif cpuUsage <76:
        return 'optimal'
    else:
        return 'overloaded'

# Function to check memory usage
def checkMemoryUsage(memoryUsage):
    if memoryUsage <4:
        return 'underutilised'
    elif memoryUsage <9:
        return 'optimal'
    else:
        return 'overloaded'

# User input for CPU and memory usage
cpuUserInput = float(input("Please enter your system's CPU usage in %: \n"))
memoryUserInput = float(input("Please enter your system's memory usage in GB: \n"))

# Variables for usage message equal to functions
cpuStatus = checkCpuUsage(cpuUserInput)
memoryStatus = checkMemoryUsage(memoryUserInput)

# Status message
status = f'Your system is running at {cpuStatus} CPU usage and {memoryStatus} memory usage.\n'
print(status)

print("Thank you for using TechComp's monitoring bot.")