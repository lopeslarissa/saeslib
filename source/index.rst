Documentação S_AES
==================
.. toctree::
   functions/functions


Algoritmo
---------

Implementação em Python de um algoritmo AES simplificado que segue o modelo S-AES desenvolvido por Edward Schaefer

`Repositório do projeto <http://https://bitbucket.org/lopeslarissa/s_aes/>`_
`Exemplo de uso <http://https://bitbucket.org/lopeslarissa/simple-aes/>`_


Instalação
----------

* ``$ pip install -r requirements.txt``
* ``$ python setup.py sdist``
* ``$ pip install -e  s_aes/``


CLI
---

* ``$ encrypt -k (chave) -t (texto)``
* ``$ encrypt -k (chave) -t (texto) -p (opcional: caminho para salvar o relatório)``
