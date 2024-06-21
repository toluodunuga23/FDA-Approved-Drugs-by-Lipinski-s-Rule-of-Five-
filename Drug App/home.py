import mols2grid
import streamlit as st
import time
import pandas as pd
import streamlit.components.v1 as components
from rdkit import Chem
from rdkit.Chem import Draw
from rdkit.Chem.Descriptors import ExactMolWt
from rdkit.Chem.Descriptors import MolLogP
from rdkit.Chem.Descriptors import NumHDonors
from rdkit.Chem.Descriptors import NumHAcceptors

st.set_page_config(
    page_title="Drug App",
    page_icon="👋",
)

st.title("Hypothetical FDA Approved Drugs by Lipinski's Rule of Five (Ro5)")
st.write(
    "This is a web app to show a hypothetical set FDA approved drugs that pass Lipinski's Rule of Five (Ro5)."
)
st.markdown(
    "The Lipinski's Rule of Five (Ro5) is a rule of thumb to evaluate druglikeness or determine if a chemical compound with a certain pharmacological or biological activity has properties that would make it a likely orally active drug in humans."
)


st.sidebar.title("Lipinski's Rule of Five (Ro5)")
# add a slider to the sidebar
mol_weight = st.sidebar.slider("Molecular Weight", 0, 1000, 500)
logp = st.sidebar.slider("LogP", -10.0, 10.0, 5.0)
hdonors = st.sidebar.slider("HDonors", 0, 10, 5)
hacceptors = st.sidebar.slider("HAcceptors", 0, 20, 10)


st.cache(allow_output_mutation=True)


def download_dataset():
    df = pd.read_csv(
        "https://www.cureffi.org/wp-content/uploads/2013/10/drugs.txt", sep="\t"
    ).dropna()
    return df


# Calulate the molecular descriptors


def calc_mw(smiles_string):
    mol_weight = Chem.MolFromSmiles(smiles_string)
    return ExactMolWt(mol_weight)


# Calculate LogP
def calc_logp(smiles_string):
    mol_logp = Chem.MolFromSmiles(smiles_string)
    return MolLogP(mol_logp)


# Calculute HDonors
def calc_hdonors(smiles_string):
    mol_hdonors = Chem.MolFromSmiles(smiles_string)
    return NumHDonors(mol_hdonors)


# Calculuate HAcceptors
def calc_hacceptors(smiles_string):
    mol_hacceptors = Chem.MolFromSmiles(smiles_string)
    return NumHAcceptors(mol_hacceptors)


# Copy the data set
df = download_dataset().copy()

# Create a new column for molecular weight
df["MW"] = df["smiles"].apply(calc_mw)
# Create a new column for LogP
df["LogP"] = df["smiles"].apply(calc_logp)
# Create a new column for HDonors
df["HDonors"] = df["smiles"].apply(calc_hdonors)
# Create a new column for HAcceptors
df["HAcceptors"] = df["smiles"].apply(calc_hacceptors)

# Displaying table based on the molecular weight, logP, HDonors, and HAcceptors
results_df = df.loc[
    (df["MW"] <= mol_weight)
    & (df["LogP"] <= logp)
    & (df["HDonors"] <= hdonors)
    & (df["HAcceptors"] <= hacceptors)
    & df["smiles"].notnull()
]
results_df = results_df[
    ["generic_name", "MW", "LogP", "HDonors", "HAcceptors", "smiles"]
]
# Sort the table based on the molecular weight
results_df = results_df.sort_values(by="MW", ascending=False)

with st.spinner("Loading data..."):
    time.sleep(2)
    st.success("Data loaded successfully!")
    st.dataframe(results_df)
    # Create the MolGrid object, specifying the subset to include "img" and "generic_name"
    mols = mols2grid.MolGrid(
        results_df,
        smiles_col="smiles",
        subset=["img", "generic_name"],
        molSize=(200, 200),
    )

    # Generate the HTML for the grid
    grid_html = mols.display(iframe=False)

# Display the grid using Streamlit's HTML component
st.components.v1.html(grid_html.data, width=1100, height=900, scrolling=True)
