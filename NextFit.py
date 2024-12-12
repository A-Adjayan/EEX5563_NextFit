def next_fit(memory_blocks, processes):
    n = len(memory_blocks)
    allocation = [-1] * len(processes)  # Track which block each process is allocated to

    # Start searching from the beginning
    search_pointer = 0

    for i, process in enumerate(processes):
        allocated = False
        for _ in range(n):  # Loop over all blocks starting from the search pointer
            # Check if the current block can accommodate the process
            if memory_blocks[search_pointer] >= process:
                # Allocate process to this block
                allocation[i] = search_pointer
                memory_blocks[search_pointer] -= process

                # Update the search pointer to the next block
                allocated = True
                break

            # Move to the next block
            search_pointer = (search_pointer + 1) % n

        if not allocated:
            print(f"Process {i + 1} ({process} KB) could not be allocated.")

    return allocation, memory_blocks

# Get user inputs for memory blocks and processes
print("Enter sizes for 5 memory blocks (in KB):")
memory_blocks = [int(input(f"Block {i + 1} size: ")) for i in range(5)]

print("\nEnter sizes for 3 processes (in KB):")
processes = [int(input(f"Process {i + 1} size: ")) for i in range(3)]

allocation, updated_memory = next_fit(memory_blocks, processes)

# Display results
print("\nFinal Memory Allocation:")
for i, block in enumerate(allocation):
    if block != -1:
        print(f"Process {i + 1}: Allocated in Block {block + 1}")
    else:
        print(f"Process {i + 1}: Not Allocated")

print("\nUpdated Memory Blocks:")
for i, size in enumerate(updated_memory):
    print(f"Block {i + 1}: {size} KB free")
