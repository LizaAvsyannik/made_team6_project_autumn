## Usage

1. Download Faiss Index and put in `index` folder:
https://drive.google.com/drive/folders/1SnW7H2TlliBOnybYA1MkLBDswXJ2Dch1

2. Download authors and papers embeddings and put in `embeddings` folder:
https://drive.google.com/drive/folders/1t-xgeS4ovlsMly16Bsw2l0s6Pu274Haj

3. Install faiss using pip:
```
pip3 install faiss-cpu
```
or
```
pip3 install faiss-gpu
```
3. Usage example is in `4_usage.ipynb`


### To reproduce training steps
- Install CogDL library from source
```
cd cogdl
pip3 install -e .
```
- Download OAG-Bert zip archive and put it in `saved`:
https://drive.google.com/drive/folders/1be9mJMX0L8SHAPWl7RO3xvSew2_afwKJ

- Run notebooks `1_preprocess_data_author_rec.ipynb`, `2_embedding_oag.ipynb`, `3_build_faiss_storage.ipynb`
