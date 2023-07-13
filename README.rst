kuplift package
===============

.. raw:: html

   <p align="center">

.. raw:: html

   </p>

kuplift is a *Python* package that provides a series of uplift modeling
methods based on recent research work. kuplift allows users to easily
use the following algorithms:

1. Encoding data using a discretization method for treatment effect
   (uplift) modeling called *UMODL*\  [1]_

2. Variable selection for uplift modeling with *UMODL-FS*. [2]_

3. Learning a Bayesian decision tree model for uplift modeling with
   *UB-DT*. [3]_

4. Learning a random forest model for uplift modeling with *UB-RF*. [4]_

**How to install**:

.. code:: python

   pip install kuplift

**User Guide**:

.. code:: python

   import kuplift as kp
   import pandas as pd

   df = pd.read_csv("dataname.csv")

   # Univariate variable transformation:
   ue = kp.UnivariateEncoding()
   encoded_data = ue.fit_transform(df, "treatment", "outcome")

   # Feature selection
   fs = kp.FeatureSelection()
   important_vars = fs.filter(df, "treatment", "outcome")

   # Uplift Bayesian Decision Tree
   tree = kp.BayesianDecisionTree(df, "treatment", "outcome")
   tree.fit()
   preds = tree.predict(df[column_names])

   # Uplift Bayesian Random Forest
   forest = kp.BayesianRandomForest(df, "treatment", "outcome", nb_trees)
   forest.fit()
   preds = forest.predict(df[features])

.. [1]
   Rafla, M., Voisine, N., Crémilleux, B., & Boullé, M. (2023, March). A
   non-parametric bayesian approach for uplift discretization and
   feature selection. **ECML PKDD 2022**

.. [2]
   Rafla, M., Voisine, N., Crémilleux, B., & Boullé, M. (2023, March). A
   non-parametric bayesian approach for uplift discretization and
   feature selection. **ECML PKDD 2022**

.. [3]
   Rafla, M., Voisine, N., & Crémilleux, B. (2023, May). Parameter-free
   Bayesian decision trees for uplift modeling. **PAKDD 2023**

.. [4]
   Rafla, M., Voisine, N., & Crémilleux, B. (2023, May). Parameter-free
   Bayesian decision trees for uplift modeling. **PAKDD 2023**
