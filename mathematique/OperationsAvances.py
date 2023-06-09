class OperationsAvances:
    "Classe contenant des opérations arithmétiques avancées."

    def puissance(self, a, b):
        """
        Fonction arithmétique de la puissance.

        Parameters
        ----------
        a : int
            nombre quelconque.
        b : int
            nombre en exposant.

        Returns
        -------
        int
            Résultat de a puissance b.
        """
        return a**b

    def racine_x(self, a, b):
        """
        Fonction arithmétique de la racine.

        Parameters
        ----------
        a : int
            nombre quelconque.
        b : int
            nombre en exposant.

        Returns
        -------
        int
            Résultat de a racine de b.
        """
        return a ** (1.0 / b)
