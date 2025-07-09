#!/bin/bash

echo "🏗️ CONSORCIO DEJ - Instalador de Dependencias para Linux/Mac"
echo "=========================================================="
echo

# Verificar si Python está instalado
if ! command -v python3 &> /dev/null; then
    echo "❌ ERROR: Python3 no está instalado"
    echo "Por favor instala Python 3.8 o superior"
    exit 1
fi

echo "✅ Python detectado"
python3 --version
echo

echo "📦 Actualizando pip..."
python3 -m pip install --upgrade pip
echo

echo "📦 Instalando dependencias principales..."
pip3 install streamlit>=1.28.0
pip3 install pandas>=2.0.0
pip3 install numpy>=1.24.0
pip3 install matplotlib>=3.7.0
pip3 install plotly>=5.15.0
pip3 install reportlab>=4.0.0
echo

echo "📦 Instalando dependencias adicionales..."
pip3 install openpyxl>=3.1.0
pip3 install stripe>=7.0.0
pip3 install streamlit-authenticator>=0.2.0
pip3 install streamlit-option-menu>=0.3.0
pip3 install Pillow>=10.0.0
pip3 install scipy>=1.10.0
pip3 install seaborn>=0.12.0
echo

# En Linux, instalar dependencias del sistema para matplotlib
if [[ "$OSTYPE" == "linux-gnu"* ]]; then
    echo "🔧 Instalando dependencias del sistema para Linux..."
    if command -v apt-get &> /dev/null; then
        sudo apt-get update
        sudo apt-get install -y python3-tk
    elif command -v yum &> /dev/null; then
        sudo yum install -y python3-tkinter
    elif command -v dnf &> /dev/null; then
        sudo dnf install -y python3-tkinter
    fi
    echo
fi

echo "🔍 Verificando instalación..."
python3 verify_dependencies.py
echo

echo "🎉 Instalación completada!"
echo "🚀 Para ejecutar la aplicación: streamlit run APP.py"
echo

read -p "Presiona Enter para continuar..." 