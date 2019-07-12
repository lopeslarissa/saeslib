Documentação S_AES
==================
.. toctree::
   functions/functions


Algoritmo
---------

Implementação em Python de um algoritmo AES simplificado que segue o modelo S-AES desenvolvido por Edward Schaefer

`Repositório do projeto <https://github.com/lopeslarissa/saeslib>`_

`Exemplo de uso <https://github.com/lopeslarissa/S-AES-Web>`_ 



Instalação
----------

* ``$ pip install -r requirements.txt``
* ``$ python setup.py sdist``
* ``$ pip install -e  s_aes/``



CLI
---

Criptografia 
++++++++++++

* ``$ encrypt -k (chave) -t (texto)``
* ``$ encrypt -k (chave) -t (texto) -p (opcional: caminho para salvar o relatório)``


Descriptografia 
+++++++++++++++

* ``$ decrypt -k (chave) -t (texto)``


Testes 
++++++

* ``$ tests``
