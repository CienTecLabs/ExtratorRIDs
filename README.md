# ExtratorRIDs

Script simples para extração dos arquivos PDF dos RIDs, presentes na página do Corpo Docente ICT da Unifla-MG.

```
git clone https://github.com/CienTecLabs/ExtratorRIDs.git

cd ExtratorRIDs
```

```
pip -m venv .venv

#Linux
source .venv/bin/activate

#Windows
./.venv/Scripts/Activate.ps1

pip install -r requirements.txt

python main.py
```

Os arquivos serão baixados na pasta `RawRIDs`

Este script é totalmente dependente da estrutura atual da página Corpo Docente ICT. Qualquer alteração na estrutura ou seus elementos, tornará o script incompatível, sendo necessário uma adaptação.