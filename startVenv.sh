!/bin/bash

# This script activates a Python virtual environment
if [ -d "venv" ]; then
    source venv/bin/activate
    echo "✅ Virtual environment 'venv' activado. Usa 'deactivate' para salir."
else
    echo "❌ No se encontró la carpeta 'venv'."
    echo "   Crealo con: python3 -m venv venv"
fi