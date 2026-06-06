# Deploy en 5 minutos

## 1 — GitHub
```bash
cd invest_memoria
git init
git add .
git commit -m "Invest Memoria v1.0"
git remote add origin https://github.com/TU_USUARIO/invest-memoria.git
git push -u origin main
```

## 2 — Streamlit Cloud
1. https://share.streamlit.io
2. New app → tu repo → main file: `app.py`
3. Deploy 🚀

## 3 — Agregar cartas de un paper
1. Copia el prompt de `PAPER_EXTRACTION_PROMPT.py`
2. Pégalo en Claude con el texto del paper
3. El output es un bloque Python — pégalo en `content/invest_cards.py`
4. `git add . && git commit -m "nuevo paper" && git push`
5. Streamlit Cloud se actualiza en ~2 min
