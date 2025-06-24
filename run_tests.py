import unittest

if __name__ == "__main__":
    # Descobre e executa todos os testes automaticamente
    loader = unittest.TestLoader()
    suite = loader.discover('.', pattern='*.py')  # Pega todos os arquivos .py

    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)