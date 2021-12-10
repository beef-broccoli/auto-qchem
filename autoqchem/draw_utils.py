from ipywidgets import interact, fixed
from rdkit import Chem
import py3Dmol


def graph_conf(m, confId=0, energies=[]):
    mb = Chem.MolToMolBlock(m, confId=confId)
    p = py3Dmol.view(width=400, height=400)
    p.removeAllModels()
    p.addModel(mb, 'sdf')
    p.setStyle({'stick': {}})
    p.setBackgroundColor('0xeeeeee')
    p.zoomTo()
    if len(energies) > 0:
        print(f"G: {min(energies):.2f} + {energies[confId] - min(energies):.2f} kcal/mol")
    return p.show()


def draw(mol: Chem.Mol, energies: list = []) -> interact:
    """Make a drawing of all conformers in 3d"""

    p = py3Dmol.view(width=400, height=400)
    return interact(graph_conf, m=fixed(mol), p=fixed(p),
                    confId=[c.GetId() for c in mol.GetConformers()],
                    energies=fixed(energies))
