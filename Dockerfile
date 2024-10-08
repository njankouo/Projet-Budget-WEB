# Utilisez une image de base contenant Python  
FROM python:3.9  

# Définir le répertoire de travail  
WORKDIR /app  

# Copier le fichier de dépendances  
COPY requirements.txt .  

# Installer les dépendances  
RUN pip install --no-cache-dir -r requirements.txt  

# Copier le code de l'application  
COPY . .  

# Exposer le port sur lequel l'application sera accessible  
EXPOSE 8000  

# Commande à exécuter pour lancer l'application  
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "tutorial.wsgi:application"]