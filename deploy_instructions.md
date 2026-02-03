# 🚀 Guía de Deploy - StepMind

## 📋 Preparación para Producción

### 1. Archivos Creados:
- ✅ `settings_production.py` - Configuración de producción
- ✅ `requirements.txt` - Dependencias actualizadas
- ✅ `staticfiles/` - Archivos estáticos generados

---

## 🔧 Opciones de Deploy

### Opción 1: PythonAnywhere (Recomendado para principiantes)

#### Pasos:
1. **Crear cuenta en PythonAnywhere**
   - Ve a [pythonanywhere.com](https://www.pythonanywhere.com)
   - Crea cuenta gratuita o de pago

2. **Crear Web App**
   - Dashboard → Web → Add new web app
   - Selecciona: Django + Python 3.10+
   - Configura el path: `/home/username/mi_proyecto_universitario_django`

3. **Subir Archivos**
   ```bash
   # En tu máquina local
   zip -r stepmind.zip mi_proyecto_universitario_django/
   
   # Sube el ZIP a PythonAnywhere (Files section)
   # Descomprime en el servidor
   unzip stepmind.zip
   ```

4. **Configurar Entorno Virtual**
   ```bash
   # En PythonAnywhere console
   cd mi_proyecto_universitario_django
   python -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

5. **Configurar Settings**
   ```bash
   # Editar wsgi.py
   # Cambiar: os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'proyecto_unellez.settings_production')
   ```

6. **Migrar y Static Files**
   ```bash
   python manage.py migrate
   python manage.py collectstatic --noinput
   python manage.py createsuperuser
   ```

---

### Opción 2: Heroku

#### Pasos:
1. **Instalar Heroku CLI**
   ```bash
   # Descargar desde devcenter.heroku.com
   heroku login
   ```

2. **Crear archivos Heroku**
   ```bash
   # Crear Procfile
   echo "web: gunicorn proyecto_unellez.wsgi" > Procfile
   
   # Crear runtime.txt
   echo "python-3.10.0" > runtime.txt
   ```

3. **Subir a Heroku**
   ```bash
   git init
   git add .
   git commit -m "Deploy StepMind"
   heroku create your-app-name
   git push heroku main
   ```

4. **Configurar Variables**
   ```bash
   heroku config:set DJANGO_SETTINGS_MODULE=proyecto_unellez.settings_production
   heroku config:set SECRET_KEY=tu-secret-key-aqui
   heroku run python manage.py migrate
   ```

---

### Opción 3: VPS DigitalOcean/Vultr

#### Pasos:
1. **Configurar Servidor**
   ```bash
   # Ubuntu 20.04+ recomendado
   sudo apt update
   sudo apt install python3 python3-pip python3-venv nginx postgresql
   ```

2. **Subir Proyecto**
   ```bash
   # Usar scp o git clone
   scp -r mi_proyecto_universitario_django/ user@server:/var/www/
   ```

3. **Configurar Entorno**
   ```bash
   cd /var/www/mi_proyecto_universitario_django
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

4. **Configurar Nginx + Gunicorn**
   ```bash
   # Instalar gunicorn
   pip install gunicorn
   
   # Configurar nginx
   sudo nano /etc/nginx/sites-available/stepmind
   ```

---

## 🔐 Configuración de Seguridad

### 1. Variables de Entorno
```bash
# En producción
export SECRET_KEY="tu-secret-key-seguro"
export DEBUG=False
export ALLOWED_HOSTS="tudominio.com,www.tudominio.com"
```

### 2. Base de Datos (Opcional)
```python
# Para PostgreSQL en settings_production.py
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'stepmind_db',
        'USER': 'stepmind_user',
        'PASSWORD': 'tu-password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

---

## 📱 Post-Deploy Checklist

### 1. Verificar Funcionalidad:
- ✅ Página principal carga correctamente
- ✅ Django Admin funciona
- ✅ Subida de APKs funciona
- ✅ Galería de imágenes funciona
- ✅ Formularios de contacto funcionan

### 2. Configurar Dominio:
- 🌐 Apuntar DNS a IP del servidor
- 🔒 Configurar SSL/TLS (Let's Encrypt)

### 3. Monitoreo:
- 📊 Configurar logs
- 📧 Notificaciones de errores
- 🔍 Backup automático

---

## 🆘 Soporte y Troubleshooting

### Problemas Comunes:
1. **Error 500**: Revisar logs de Django
2. **Static files 404**: Ejecutar `collectstatic`
3. **Database error**: Verificar credenciales
4. **Permission denied**: Configurar permisos de archivos

### Comandos Útiles:
```bash
# Ver logs
python manage.py check --deploy

# Crear superusuario
python manage.py createsuperuser

# Migrar datos
python manage.py migrate

# Recolectar estáticos
python manage.py collectstatic --noinput
```

---

## 🎯 Recomendación Final

**Para empezar rápido**: PythonAnywhere
**Para control total**: VPS DigitalOcean
**Para escalabilidad**: Heroku

**¡Tu web StepMind está lista para producción!** 🚀
