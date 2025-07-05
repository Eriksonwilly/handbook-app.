#!/usr/bin/env python3
"""
Script para optimizar la aplicación Streamlit para móviles y PWA
CONSORCIO DEJ - Optimización Móvil
"""

import os
import shutil
import requests
from PIL import Image, ImageDraw, ImageFont

def create_mobile_icons():
    """Crear iconos para PWA"""
    print("🎨 Creando iconos para PWA...")
    
    # Crear directorio static si no existe
    if not os.path.exists('static'):
        os.makedirs('static')
    
    # Crear icono 192x192
    icon_192 = Image.new('RGBA', (192, 192), (255, 215, 0, 255))  # Amarillo CONSORCIO DEJ
    draw = ImageDraw.Draw(icon_192)
    
    # Dibujar símbolo de muro de contención
    draw.rectangle([40, 60, 152, 140], fill=(255, 69, 0, 255), outline=(139, 69, 19, 255), width=3)
    draw.rectangle([60, 80, 132, 120], fill=(255, 215, 0, 255), outline=(255, 69, 0, 255), width=2)
    
    # Agregar texto
    try:
        font = ImageFont.truetype("arial.ttf", 16)
    except:
        font = ImageFont.load_default()
    
    draw.text((96, 150), "CONSORCIO", fill=(0, 0, 0, 255), anchor="mm", font=font)
    draw.text((96, 170), "DEJ", fill=(0, 0, 0, 255), anchor="mm", font=font)
    
    icon_192.save('static/icon-192x192.png')
    
    # Crear icono 512x512
    icon_512 = Image.new('RGBA', (512, 512), (255, 215, 0, 255))
    draw = ImageDraw.Draw(icon_512)
    
    # Dibujar símbolo más grande
    draw.rectangle([100, 150, 412, 370], fill=(255, 69, 0, 255), outline=(139, 69, 19, 255), width=8)
    draw.rectangle([150, 200, 362, 320], fill=(255, 215, 0, 255), outline=(255, 69, 0, 255), width=5)
    
    try:
        font_large = ImageFont.truetype("arial.ttf", 40)
    except:
        font_large = ImageFont.load_default()
    
    draw.text((256, 400), "CONSORCIO", fill=(0, 0, 0, 255), anchor="mm", font=font_large)
    draw.text((256, 450), "DEJ", fill=(0, 0, 0, 255), anchor="mm", font=font_large)
    
    icon_512.save('static/icon-512x512.png')
    
    print("✅ Iconos creados exitosamente")

def optimize_streamlit_config():
    """Optimizar configuración de Streamlit para móviles"""
    print("⚙️ Optimizando configuración de Streamlit...")
    
    config_content = """[theme]
primaryColor = "#FFD700"
backgroundColor = "#FFFFE0"
secondaryBackgroundColor = "#FFFACD"
textColor = "#000000"

[server]
headless = true
port = 8501
enableCORS = false
enableXsrfProtection = false
maxUploadSize = 200

[browser]
gatherUsageStats = false

[client]
showErrorDetails = false

[runner]
magicEnabled = false
"""
    
    # Crear directorio .streamlit si no existe
    if not os.path.exists('.streamlit'):
        os.makedirs('.streamlit')
    
    with open('.streamlit/config.toml', 'w') as f:
        f.write(config_content)
    
    print("✅ Configuración optimizada")

def create_pwa_manifest():
    """Crear manifest.json optimizado para PWA"""
    print("📱 Creando manifest.json para PWA...")
    
    manifest_content = """{
  "name": "CONSORCIO DEJ - Muros de Contención",
  "short_name": "CONSORCIO DEJ",
  "description": "Aplicación profesional para diseño y análisis de muros de contención",
  "start_url": "/",
  "display": "standalone",
  "background_color": "#FFD700",
  "theme_color": "#FFD700",
  "orientation": "portrait-primary",
  "scope": "/",
  "lang": "es",
  "dir": "ltr",
  "categories": ["engineering", "education", "business", "productivity"],
  "icons": [
    {
      "src": "/static/icon-192x192.png",
      "sizes": "192x192",
      "type": "image/png",
      "purpose": "any maskable"
    },
    {
      "src": "/static/icon-512x512.png",
      "sizes": "512x512",
      "type": "image/png",
      "purpose": "any maskable"
    }
  ],
  "screenshots": [
    {
      "src": "/static/screenshot-1.png",
      "sizes": "1280x720",
      "type": "image/png",
      "form_factor": "wide"
    },
    {
      "src": "/static/screenshot-2.png",
      "sizes": "750x1334",
      "type": "image/png",
      "form_factor": "narrow"
    }
  ],
  "shortcuts": [
    {
      "name": "Cálculo Básico",
      "short_name": "Básico",
      "description": "Análisis rápido de estabilidad",
      "url": "/?page=basico",
      "icons": [
        {
          "src": "/static/icon-192x192.png",
          "sizes": "192x192"
        }
      ]
    },
    {
      "name": "Análisis Completo",
      "short_name": "Completo",
      "description": "Diseño profesional completo",
      "url": "/?page=completo",
      "icons": [
        {
          "src": "/static/icon-192x192.png",
          "sizes": "192x192"
        }
      ]
    }
  ]
}"""
    
    with open('manifest.json', 'w') as f:
        f.write(manifest_content)
    
    print("✅ Manifest.json creado")

def create_service_worker():
    """Crear service worker para funcionalidad offline"""
    print("🔧 Creando service worker...")
    
    sw_content = """const CACHE_NAME = 'consorcio-dej-v2';
const urlsToCache = [
  '/',
  '/manifest.json',
  '/static/icon-192x192.png',
  '/static/icon-512x512.png'
];

// Instalar service worker
self.addEventListener('install', (event) => {
  event.waitUntil(
    caches.open(CACHE_NAME)
      .then((cache) => {
        console.log('CONSORCIO DEJ: Cache abierto');
        return cache.addAll(urlsToCache);
      })
  );
});

// Interceptar requests
self.addEventListener('fetch', (event) => {
  event.respondWith(
    caches.match(event.request)
      .then((response) => {
        // Retornar desde cache si está disponible
        if (response) {
          return response;
        }
        
        // Si no está en cache, hacer fetch desde red
        return fetch(event.request).then(
          (response) => {
            // Verificar si la respuesta es válida
            if(!response || response.status !== 200 || response.type !== 'basic') {
              return response;
            }

            // Clonar la respuesta
            const responseToCache = response.clone();

            caches.open(CACHE_NAME)
              .then((cache) => {
                cache.put(event.request, responseToCache);
              });

            return response;
          }
        );
      })
  );
});

// Actualizar cache cuando hay nueva versión
self.addEventListener('activate', (event) => {
  event.waitUntil(
    caches.keys().then((cacheNames) => {
      return Promise.all(
        cacheNames.map((cacheName) => {
          if (cacheName !== CACHE_NAME) {
            console.log('CONSORCIO DEJ: Eliminando cache antiguo:', cacheName);
            return caches.delete(cacheName);
          }
        })
      );
    })
  );
});

// Manejar notificaciones push
self.addEventListener('push', (event) => {
  const options = {
    body: '¡Tu análisis de muro de contención está listo!',
    icon: '/static/icon-192x192.png',
    badge: '/static/icon-192x192.png',
    vibrate: [100, 50, 100],
    data: {
      dateOfArrival: Date.now(),
      primaryKey: 1
    },
    actions: [
      {
        action: 'explore',
        title: 'Ver resultados',
        icon: '/static/icon-192x192.png'
      },
      {
        action: 'close',
        title: 'Cerrar',
        icon: '/static/icon-192x192.png'
      }
    ]
  };

  event.waitUntil(
    self.registration.showNotification('CONSORCIO DEJ', options)
  );
});"""
    
    with open('static/sw.js', 'w') as f:
        f.write(sw_content)
    
    print("✅ Service worker creado")

def create_deployment_guide():
    """Crear guía de despliegue"""
    print("📋 Creando guía de despliegue...")
    
    guide_content = """# 🚀 GUÍA DE DESPLIEGUE RÁPIDO - CONSORCIO DEJ

## ⚡ PASOS PARA GENERAR APK (15 minutos)

### 1. Desplegar en Streamlit Cloud (5 min)
```bash
# 1. Ve a https://share.streamlit.io
# 2. Conecta tu GitHub
# 3. Selecciona repositorio HANDBOOK
# 4. Archivo principal: APP.py
# 5. Deploy
```

### 2. Generar APK con PWA Builder (10 min)
```bash
# 1. Ve a https://www.pwabuilder.com
# 2. Pega URL de tu app Streamlit
# 3. Build My PWA
# 4. Descarga APK
```

## 💰 MONETIZACIÓN

### Plan Gratuito
- Cálculos básicos
- Sin reportes PDF

### Plan Premium ($9.99/mes)
- Análisis completo
- Reportes PDF
- Diseño del fuste

### Plan Empresarial ($29.99/mes)
- Múltiples usuarios
- API access
- Soporte técnico

## 📱 PUBLICACIÓN

### Google Play Store
1. Cuenta desarrollador: $25
2. Subir APK
3. Configurar pagos
4. Publicar

### Huawei AppGallery
1. Registro gratuito
2. Subir APK
3. Publicar

## 🎯 INGRESOS ESPERADOS

### Conservador: $2,498/mes
### Optimista: $10,993/mes

---
**Inversión: $25**
**ROI: 10,000%+**
"""
    
    with open('GUIA_DESPLIEGUE.md', 'w') as f:
        f.write(guide_content)
    
    print("✅ Guía de despliegue creada")

def main():
    """Función principal"""
    print("🏗️ CONSORCIO DEJ - Optimización Móvil")
    print("=" * 50)
    
    try:
        # Crear iconos
        create_mobile_icons()
        
        # Optimizar configuración
        optimize_streamlit_config()
        
        # Crear manifest
        create_pwa_manifest()
        
        # Crear service worker
        create_service_worker()
        
        # Crear guía
        create_deployment_guide()
        
        print("\n🎉 ¡Optimización completada!")
        print("\n📱 Tu app está lista para:")
        print("   ✅ Desplegar en Streamlit Cloud")
        print("   ✅ Generar APK con PWA Builder")
        print("   ✅ Publicar en Google Play")
        print("   ✅ Monetizar con suscripciones")
        
        print("\n🚀 Próximos pasos:")
        print("   1. Subir a GitHub")
        print("   2. Desplegar en Streamlit Cloud")
        print("   3. Generar APK en PWA Builder")
        print("   4. Publicar en tiendas")
        print("   5. ¡Monetizar!")
        
    except Exception as e:
        print(f"❌ Error: {e}")
        print("Verifica que tienes PIL instalado: pip install Pillow")

if __name__ == "__main__":
    main() 