import os 
import argparse

def pdb_to_fasta(pdb_file, fasta_out, name='STATE'):
    """
    Convert pdb to fasta, includes nonstandard residue names

    Parameters:
    - pdb_file: input
    - fasta_out: output directory
    - name: name (.fa extension added automatically)

    Returns:
    None
    """

    amino_acid_dict = {'ALA': 'A', 'ARG': 'R', 'ASN': 'N', 'ASP': 'D',
    'CYS': 'C', 'GLN': 'Q', 'GLU': 'E', 'GLY': 'G',
    'HIS': 'H', 'ILE': 'I', 'LEU': 'L', 'LYS': 'K',
    'MET': 'M', 'PHE': 'F', 'PRO': 'P', 'SER': 'S',
    'THR': 'T', 'TRP': 'W', 'TYR': 'Y', 'VAL': 'V',
    'HIP': 'H', 'HID': 'H', 'HIE': 'H', 'HISD': 'H',
    'HISE': 'H', 'HISP': 'H', 'AS4': 'D','ASH': 'D',
    'GL4': 'E', 'GLH': 'E', 'ARH': 'R', 'LYN': 'K',
    'CYX': 'C', 'CYM': 'C', 'CSP': 'C', 'SEP': 'S', 'ASX': 'D'
}
    sequence = []
    with open(pdb_file, 'r') as PDB:
        pdb_lines = PDB.readlines()

    for line in pdb_lines:
        if ('ATOM' in line) and ('CA' in line):
            aa = line.split()[3]
            sequence.append(amino_acid_dict[aa])


    with open(os.path.join(fasta_out,f"{name}.fa"), 'w') as FASTA:
        FASTA.write(f'>{name}\n')
        FASTA.write(''.join(sequence))

def main():
    parser = argparse.ArgumentParser(description='Convert a pdb file to a fasta file, includes nonstandard residue names')
    parser.add_argument("--fasta_path", required=True, help='Path to fasta directory')
    parser.add_argument("--pdb_file", required=True, help='Path to pdb file')
    parser.add_argument("--name", required=False, help='Name of sequence')

    args = parser.parse_args()
    pdb_to_fasta(args.pdb_file, args.fasta_path, args.name)

if __name__ == '__main__':
    main()
