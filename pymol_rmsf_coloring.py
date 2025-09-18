# Open the file and read the B-factors
inFile = open("RMSF_Bfactor_Apo.txt", "r")
stored.newB = [float(line.strip()) for line in inFile.readlines()]  # Read and store all B-factors
inFile.close()

# Iterate over all objects that match the pattern Apo_*
for obj in cmd.get_object_list("Apo_*"):
    stored.newB = []
    inFile = open('RMSF_Bfactor_Apo.txt', 'r')
    for line in inFile.readlines():
        stored.newB.append(float(line))
    inFile.close()
    print(len(stored.newB))
    # Reset all B-factors to 0.0 initially
    cmd.alter(f"{obj}", "b = 0.0")

    # Assign B-factors to specified CA atoms
    cmd.alter(f"{obj} and (name CA and resid 176-186)", "b = stored.newB.pop(0)", space=locals())

# Apply color spectrum based on B-factors
cmd.spectrum("b", "blue_white_red", "Apo_*", 0.0, 2.5)

