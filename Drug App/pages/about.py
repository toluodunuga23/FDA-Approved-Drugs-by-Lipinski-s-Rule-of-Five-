import streamlit as st

st.markdown(
    """
    # About Lipinski's Rule of Five (Ro5)
    **Definition**: Lipinski's Rule of Five is a set of guidelines used in drug discovery to predict whether a chemical compound is likely to be an orally active drug in humans. These rules help scientists determine if a compound has properties that would make it a good candidate for oral medication. The rules were formulated by Christopher A. Lipinski and his colleagues in 1997.

    ## Lipinski's Rule of Five (Ro5)
    1. **Molecular weight < 500 daltons**
        - *Why?* To ensure the compound is small enough to be absorbed by the digestive system.
        
    2. **LogP (Partition Coefficient) < 5**
        - *Why?* LogP measures the compound's lipophilicity (ability to dissolve in fats, oils, lipids, and non-polar solvents). A LogP value less than 5 indicates that the compound can balance between being hydrophilic (water-loving) and lipophilic (fat-loving), making it easier for the body to absorb.
        
    3. **Hydrogen bond donors < 5**
        - *Why?* Hydrogen bond donors are atoms like nitrogen or oxygen with attached hydrogen atoms that can form hydrogen bonds. Having too many hydrogen bond donors can make the compound too polar, reducing its ability to pass through cell membranes.
        
    4. **Hydrogen bond acceptors < 10**
        - *Why?* Hydrogen bond acceptors are typically nitrogen or oxygen atoms that can accept hydrogen bonds. Similar to donors, having too many acceptors can make the compound too polar.
        
    5. **Polar Surface Area (PSA) < 140 Å²**
        - *Why?* Polar surface area is a measure of the size of the compound's polar region. A smaller PSA value indicates that the compound is less likely to be too polar.

    ## Exceptions to Lipinski's Rule of Five
    While Lipinski's Rule of Five is a useful guideline, there are exceptions. Some compounds that do not meet all the criteria can still be successful drugs. For example, some antibiotics and antifungal agents have molecular weights greater than 500 daltons.

    - **Exceptions**: Some drugs that are successfully used as medications do not adhere to these rules. For example, certain antibiotics, antifungals, vitamins, and cardiac glycosides may not follow the Ro5 but are still effective.
    - **Not Absolute**: The rules are not absolute predictors of a compound's oral bioavailability. They are more of a starting point for further investigation.
    - **Other Factors**: Oral bioavailability is also influenced by factors such as solubility, permeability, and metabolic stability, which are not covered by the Ro5.
    """
)
