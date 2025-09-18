import MDAnalysis as mda
import os
import argparse

convert_dict = {'ARG': 'ARN', 'LYS': 'LYN', 'ASP': 'ASH', 'GLU': 'GLH'}

def get_reference_residues(input_file: str) -> list:
    """Get residue numbers of neutralized residues from reference file"""
    u = mda.Universe(input_file)

    resids = [f for f in u.residues if f.resname in convert_dict.values()]
    return resids

def neutralize_residues(input_file: str, residues: list, output_file: str) -> None:
    """Neutralize given residue list and save new PDB file"""
    u = mda.Universe(input_file)

    for residue in residues:
        res = u.residues[residue.resid-1] #0-index
        res.resname = convert_dict[res.resname]

    with mda.coordinates.PDB.PDBWriter(output_file) as w:
        w.write(u.atoms)

def parse_args() -> argparse.Namespace:
    """Parse command line arguments"""
    parser = argparse.ArgumentParser(description='Alter charged residues to be neutral. Most often used when setting up topologies for EVB simulations\nUsage: python update_protonation.py --input INPUT_FILE/DIRECTORY --residues 23,421,29 --output OUTPUT_FILE')
    parser.add_argument('--input', type=str, help='Input file or directory containing input files', required=True)
    parser.add_argument('--residues', type=str, help='Comma-separated list of residues to modfiy ids', required=False)
    parser.add_argument('--reference', type=str, help='Reference PDB to use to match protonation states', required=False)
    parser.add_argument('--output', type=str, help='Output filename', required=False)
    return parser.parse_args()


if __name__ == '__main__':
    args = parse_args()
    
    if args.reference is None and args.residues is None:
        raise SystemExit("User must provide either a reference structure or list of residues to neutralize")

    if not args.reference:
        residues = args.residues.split(',')
    else:
        residues = get_reference_residues(args.reference)

    if os.path.isdir(args.input):
        # use all files in given directory
        for input_file in os.listdir(args.input):
            print(f'Processing {input_file}')
            output = f"{input_file.split('.')[0]}-out.pdb"
            neutralize_residues(os.path.join(args.input, input_file), residues, os.path.join('neutralized',output))
    else:
        if not args.output:
            output = f"{args.input.split('.')[0]}-out.pdb"
        else:
            output = args.output

        neutralize_residues(args.input, residues, output)
