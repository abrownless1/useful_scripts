from pymol import cmd

objects = cmd.get_object_list('all')
for obj in objects:
    filename = f"{obj}_how.pdb"
    cmd.save(filename, obj)
