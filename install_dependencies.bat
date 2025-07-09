@echo off
echo 🏗️ CONSORCIO DEJ - Instalador de Dependencias para Windows
echo ========================================================
echo.

echo 📦 Actualizando pip...
python -m pip install --upgrade pip
echo.

echo 📦 Instalando dependencias principales...
pip install streamlit>=1.28.0
pip install pandas>=2.0.0
pip install numpy>=1.24.0
pip install matplotlib>=3.7.0
pip install plotly>=5.15.0
pip install reportlab>=4.0.0
echo.

echo 📦 Instalando dependencias adicionales...
pip install openpyxl>=3.1.0
pip install stripe>=7.0.0
pip install streamlit-authenticator>=0.2.0
pip install streamlit-option-menu>=0.3.0
pip install Pillow>=10.0.0
pip install scipy>=1.10.0
pip install seaborn>=0.12.0
echo.

echo 🔍 Verificando instalación...
python verify_dependencies.py
echo.

echo 🎉 Instalación completada!
echo 🚀 Para ejecutar la aplicación: streamlit run APP.py
echo.

pause 