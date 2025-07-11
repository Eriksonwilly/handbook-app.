#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ANÁLISIS COMPARATIVO COMPLETO: RANKINE vs COULOMB
Diseño de Muro de Contención - Ejemplo Práctico
CONSORCIO DEJ - Ingeniería y Construcción
"""

import math
import pandas as pd

def calcular_rankine(datos):
    """
    Calcula el empuje activo según teoría de Rankine
    """
    # Extraer datos
    h1 = datos['h1']
    phi_relleno = datos['phi_relleno']
    gamma_relleno = datos['gamma_relleno']
    qsc = datos['qsc']
    Df = datos['Df']
    phi_cimentacion = datos['phi_cimentacion']
    gamma_cimentacion = datos['gamma_cimentacion']
    gamma_concreto = datos['gamma_concreto']
    hm = datos['hm']
    
    # 1. Coeficiente de empuje activo (Rankine)
    ka = math.tan(math.radians(45 - phi_relleno/2))**2
    
    # 2. Altura equivalente por sobrecarga
    hs = qsc / gamma_relleno
    
    # 3. Factor kc para concreto
    kc = 14.28  # Para fc = 210 kg/cm²
    
    # 4. Dimensiones calculadas
    Bz = (h1 + Df) * (1 + hs/(h1 + Df)) * math.sqrt(ka)
    Bz = round(Bz, 2)
    
    hz = math.sqrt(((h1 + Df)**2 * (1 + hs/(h1 + Df))) / (9 * kc))
    hz = round(hz * 100) / 100
    hz = max(0.4, hz)
    
    b = math.sqrt(((h1 + hm)**2 * (1 + hs/(h1 + hm))) / (10 * kc))
    b = round(b * 100) / 100
    b = max(0.35, b)
    
    r = (2 * Bz - 3 * b) / 6
    r = round(r * 100) / 100
    r = max(0.7, r)
    
    t = Bz - r - b
    t = round(t * 100) / 100
    
    # 5. Empujes activos
    Ea_relleno = 0.5 * ka * (gamma_relleno/1000) * h1**2
    Ea_sobrecarga = ka * (qsc/1000) * h1
    Ea_total = Ea_relleno + Ea_sobrecarga
    
    # 6. Empuje pasivo
    kp = math.tan(math.radians(45 + phi_cimentacion/2))**2
    Ep = 0.5 * kp * (gamma_cimentacion/1000) * Df**2
    
    # 7. Pesos
    W_muro = b * h1 * (gamma_concreto/1000)
    W_zapata = Bz * hz * (gamma_concreto/1000)
    W_relleno = t * h1 * (gamma_relleno/1000)
    W_total = W_muro + W_zapata + W_relleno
    
    # 8. Momentos
    x_muro = r + b/2
    x_zapata = Bz/2
    x_relleno = r + b + t/2
    
    Mr_muro = W_muro * x_muro
    Mr_zapata = W_zapata * x_zapata
    Mr_relleno = W_relleno * x_relleno
    Mr_pasivo = Ep * Df/3
    M_estabilizador = Mr_muro + Mr_zapata + Mr_relleno + Mr_pasivo
    
    Mv_relleno = Ea_relleno * h1/3
    Mv_sobrecarga = Ea_sobrecarga * h1/2
    M_volcador = Mv_relleno + Mv_sobrecarga
    
    # 9. Factores de seguridad
    FS_volcamiento = M_estabilizador / M_volcador
    
    mu = math.tan(math.radians(phi_cimentacion))
    Fr_friccion = mu * W_total
    Fr_pasivo = Ep
    Fr_total = Fr_friccion + Fr_pasivo
    FS_deslizamiento = Fr_total / Ea_total
    
    # 10. Presiones sobre el suelo
    sum_momentos_verticales = Mr_muro + Mr_zapata + Mr_relleno
    x_barra = sum_momentos_verticales / W_total
    e = abs(x_barra - Bz/2)
    
    q_max = (W_total / Bz) * (1 + 6*e/Bz)
    q_min = (W_total / Bz) * (1 - 6*e/Bz)
    
    return {
        'metodo': 'Rankine',
        'ka': ka,
        'Bz': Bz,
        'hz': hz,
        'b': b,
        'r': r,
        't': t,
        'Ea_total': Ea_total,
        'Ep': Ep,
        'W_total': W_total,
        'FS_volcamiento': FS_volcamiento,
        'FS_deslizamiento': FS_deslizamiento,
        'q_max': q_max,
        'q_min': q_min,
        'e': e
    }

def calcular_coulomb(datos):
    """
    Calcula el empuje activo según teoría de Coulomb
    """
    # Extraer datos
    H = datos['H']
    h1 = datos['h1']
    t2 = datos['t2']
    b2 = datos['b2']
    phi1 = datos['phi1']
    delta = datos['delta']
    alpha = datos['alpha']
    gamma1 = datos['gamma1']
    S_c = datos['S_c']
    Df = datos['Df']
    phi_cimentacion = datos['phi_cimentacion']
    gamma_cimentacion = datos['gamma_cimentacion']
    gamma_concreto = datos['gamma_concreto']
    
    # 1. Ángulo de inclinación del muro (β)
    beta = math.atan((H - h1) / t2)
    beta_deg = math.degrees(beta)
    
    # 2. Coeficiente de empuje activo (Coulomb)
    phi1_rad = math.radians(phi1)
    delta_rad = math.radians(delta)
    alpha_rad = math.radians(alpha)
    
    # Validar dominio de la raíz cuadrada
    num_sqrt = (math.sin(phi1_rad + delta_rad) * math.sin(phi1_rad - alpha_rad))
    den_sqrt = (math.sin(beta - delta_rad) * math.sin(beta + alpha_rad))
    if den_sqrt == 0:
        print("[ADVERTENCIA] División por cero en la fórmula de Coulomb. Parámetros no válidos.")
        return None
    arg_sqrt = num_sqrt / den_sqrt
    if arg_sqrt < 0:
        print(f"[ADVERTENCIA] Argumento negativo en raíz cuadrada de Coulomb: {arg_sqrt:.4f}. Parámetros no válidos.")
        return None
    
    numerador = math.sin(beta + phi1_rad)**2
    denominador = math.sin(beta)**2 * math.sin(beta - delta_rad) * (
        1 + math.sqrt(arg_sqrt)
    )**2
    
    Ka = numerador / denominador
    
    # 3. Altura efectiva
    H_efectiva = H + (t2/2 + b2/2) * math.tan(alpha_rad)
    
    # 4. Empuje activo total
    Pa = 0.5 * Ka * gamma1 * (H_efectiva)**2
    
    # 5. Componentes del empuje
    Ph = Pa * math.cos(math.radians(90) - beta + delta_rad)
    Pv = Pa * math.sin(math.radians(90) - beta + delta_rad)
    
    # 6. Empuje por sobrecarga
    PSC = Ka * H * (S_c / 1000) * (math.sin(beta) / math.sin(beta + alpha_rad))
    
    # 7. Empuje total horizontal
    P_total_horizontal = Ph + PSC
    
    # 8. Dimensiones estimadas para comparación
    Bz_estimado = (h1 + Df) * (1 + (S_c/1000)/(h1 + Df)) * math.sqrt(Ka)
    Bz_estimado = round(Bz_estimado, 2)
    
    # 9. Empuje pasivo (similar a Rankine)
    kp = math.tan(math.radians(45 + phi_cimentacion/2))**2
    Ep = 0.5 * kp * (gamma_cimentacion/1000) * Df**2
    
    # 10. Pesos estimados
    b_estimado = 0.4  # Espesor típico para Coulomb
    W_muro = b_estimado * h1 * (gamma_concreto/1000)
    W_zapata = Bz_estimado * 0.4 * (gamma_concreto/1000)
    W_relleno = (Bz_estimado - b_estimado) * h1 * (gamma1/1000)
    W_total = W_muro + W_zapata + W_relleno
    
    # 11. Factores de seguridad estimados
    FS_volcamiento_estimado = (W_total * Bz_estimado/2) / (P_total_horizontal * h1/3)
    
    mu = math.tan(math.radians(phi_cimentacion))
    Fr_friccion = mu * W_total
    Fr_pasivo = Ep
    Fr_total = Fr_friccion + Fr_pasivo
    FS_deslizamiento_estimado = Fr_total / P_total_horizontal
    
    return {
        'metodo': 'Coulomb',
        'ka': Ka,
        'beta': beta_deg,
        'alpha': alpha,
        'delta': delta,
        'H_efectiva': H_efectiva,
        'Pa': Pa,
        'Ph': Ph,
        'Pv': Pv,
        'PSC': PSC,
        'P_total_horizontal': P_total_horizontal,
        'Bz_estimado': Bz_estimado,
        'Ep': Ep,
        'W_total': W_total,
        'FS_volcamiento': FS_volcamiento_estimado,
        'FS_deslizamiento': FS_deslizamiento_estimado
    }

# Ajustar los ángulos del ejemplo para que sean compatibles
# Por ejemplo, reducir alpha y delta para evitar dominio negativo

def main():
    print("=" * 80)
    print("ANÁLISIS COMPARATIVO: RANKINE vs COULOMB")
    print("CONSORCIO DEJ - Ingeniería y Construcción")
    print("=" * 80)
    
    # Datos del ejemplo práctico (ajustados)
    datos_ejemplo = {
        # Datos comunes
        'h1': 3.0,  # Altura del talud (m)
        'Df': 1.2,  # Profundidad de desplante (m)
        'hm': 0.2,  # Altura de coronación (m)
        'qsc': 1000,  # Sobrecarga (kg/m²)
        
        # Datos del suelo de relleno
        'gamma_relleno': 1800,  # Peso específico (kg/m³)
        'phi_relleno': 32,  # Ángulo de fricción (°)
        
        # Datos del suelo de cimentación
        'gamma_cimentacion': 1900,  # Peso específico (kg/m³)
        'phi_cimentacion': 28,  # Ángulo de fricción (°)
        
        # Datos del concreto
        'gamma_concreto': 2400,  # Peso específico (kg/m³)
        
        # Datos específicos de Coulomb (ajustados)
        'H': 3.2,  # Altura total del muro (m)
        't2': 0.8,  # Base del triángulo (m)
        'b2': 1.2,  # Longitud del talón (m)
        'phi1': 32,  # Ángulo de fricción del relleno (°)
        'delta': 10,  # Ángulo de fricción muro-suelo (°) (ajustado)
        'alpha': 2,   # Ángulo de inclinación del terreno (°) (ajustado)
        'gamma1': 1800,  # Peso específico del relleno (kg/m³)
        'S_c': 1000  # Sobrecarga (kg/m²)
    }
    
    print("\n📊 DATOS DEL EJEMPLO PRÁCTICO:")
    print(f"• Altura del talud: {datos_ejemplo['h1']} m")
    print(f"• Profundidad de desplante: {datos_ejemplo['Df']} m")
    print(f"• Ángulo de fricción del relleno: {datos_ejemplo['phi_relleno']}°")
    print(f"• Peso específico del relleno: {datos_ejemplo['gamma_relleno']} kg/m³")
    print(f"• Sobrecarga: {datos_ejemplo['qsc']} kg/m²")
    print(f"• Ángulo de inclinación del terreno (Coulomb): {datos_ejemplo['alpha']}°")
    print(f"• Ángulo de fricción muro-suelo (Coulomb): {datos_ejemplo['delta']}°")
    
    # Calcular con ambos métodos
    print("\n" + "=" * 80)
    print("🔬 CÁLCULOS CON MÉTODO RANKINE")
    print("=" * 80)
    
    resultados_rankine = calcular_rankine(datos_ejemplo)
    
    print(f"📐 Coeficiente Ka: {resultados_rankine['ka']:.6f}")
    print(f"📏 Base de zapata (Bz): {resultados_rankine['Bz']:.2f} m")
    print(f"📏 Peralte de zapata (hz): {resultados_rankine['hz']:.2f} m")
    print(f"📏 Espesor del muro (b): {resultados_rankine['b']:.2f} m")
    print(f"📏 Longitud de puntera (r): {resultados_rankine['r']:.2f} m")
    print(f"📏 Longitud de talón (t): {resultados_rankine['t']:.2f} m")
    print(f"⚖️ Empuje activo total: {resultados_rankine['Ea_total']:.3f} tn/m")
    print(f"⚖️ Empuje pasivo: {resultados_rankine['Ep']:.3f} tn/m")
    print(f"⚖️ Peso total: {resultados_rankine['W_total']:.3f} tn/m")
    print(f"🛡️ FS Volcamiento: {resultados_rankine['FS_volcamiento']:.2f}")
    print(f"🛡️ FS Deslizamiento: {resultados_rankine['FS_deslizamiento']:.2f}")
    print(f"📊 Presión máxima: {resultados_rankine['q_max']:.2f} tn/m²")
    print(f"📊 Presión mínima: {resultados_rankine['q_min']:.2f} tn/m²")
    
    print("\n" + "=" * 80)
    print("🔬 CÁLCULOS CON MÉTODO COULOMB")
    print("=" * 80)
    
    resultados_coulomb = calcular_coulomb(datos_ejemplo)
    if resultados_coulomb is None:
        print("❌ No se pudo calcular Coulomb con los parámetros dados. Ajusta los ángulos para evitar dominio negativo en la raíz cuadrada.")
        return
    
    print(f"📐 Coeficiente Ka: {resultados_coulomb['ka']:.6f}")
    print(f"📐 Ángulo β (inclinación muro): {resultados_coulomb['beta']:.2f}°")
    print(f"📐 Ángulo α (inclinación terreno): {resultados_coulomb['alpha']:.1f}°")
    print(f"📐 Ángulo δ (fricción muro-suelo): {resultados_coulomb['delta']:.1f}°")
    print(f"📏 Altura efectiva: {resultados_coulomb['H_efectiva']:.2f} m")
    print(f"⚖️ Empuje activo total (Pa): {resultados_coulomb['Pa']:.3f} tn/m")
    print(f"⚖️ Componente horizontal (Ph): {resultados_coulomb['Ph']:.3f} tn/m")
    print(f"⚖️ Componente vertical (Pv): {resultados_coulomb['Pv']:.3f} tn/m")
    print(f"⚖️ Empuje por sobrecarga (PSC): {resultados_coulomb['PSC']:.3f} tn/m")
    print(f"⚖️ Empuje total horizontal: {resultados_coulomb['P_total_horizontal']:.3f} tn/m")
    print(f"📏 Base estimada: {resultados_coulomb['Bz_estimado']:.2f} m")
    print(f"⚖️ Peso total estimado: {resultados_coulomb['W_total']:.3f} tn/m")
    print(f"🛡️ FS Volcamiento estimado: {resultados_coulomb['FS_volcamiento']:.2f}")
    print(f"🛡️ FS Deslizamiento estimado: {resultados_coulomb['FS_deslizamiento']:.2f}")
    
    # Comparación
    print("\n" + "=" * 80)
    print("📊 COMPARACIÓN DE RESULTADOS")
    print("=" * 80)
    
    diferencia_ka = ((resultados_coulomb['ka'] - resultados_rankine['ka']) / resultados_rankine['ka']) * 100
    diferencia_empuje = ((resultados_coulomb['P_total_horizontal'] - resultados_rankine['Ea_total']) / resultados_rankine['Ea_total']) * 100
    
    print(f"📈 Diferencia en Ka: {diferencia_ka:+.1f}%")
    print(f"📈 Diferencia en empuje horizontal: {diferencia_empuje:+.1f}%")
    
    if diferencia_ka > 0:
        print("✅ Coulomb proporciona un Ka mayor (menos conservador)")
    else:
        print("⚠️ Rankine proporciona un Ka mayor (más conservador)")
    
    if diferencia_empuje > 0:
        print("✅ Coulomb proporciona un empuje mayor")
    else:
        print("⚠️ Rankine proporciona un empuje mayor")
    
    # Análisis de factores de seguridad
    print("\n" + "=" * 80)
    print("🛡️ ANÁLISIS DE FACTORES DE SEGURIDAD")
    print("=" * 80)
    
    print("RANKINE:")
    print(f"• FS Volcamiento: {resultados_rankine['FS_volcamiento']:.2f} (Límite: 2.0)")
    print(f"• FS Deslizamiento: {resultados_rankine['FS_deslizamiento']:.2f} (Límite: 1.5)")
    
    print("\nCOULOMB:")
    print(f"• FS Volcamiento: {resultados_coulomb['FS_volcamiento']:.2f} (Límite: 2.0)")
    print(f"• FS Deslizamiento: {resultados_coulomb['FS_deslizamiento']:.2f} (Límite: 1.5)")
    
    # Recomendación
    print("\n" + "=" * 80)
    print("🎯 RECOMENDACIÓN FINAL")
    print("=" * 80)
    
    print("📋 ANÁLISIS DE AMBOS MÉTODOS:")
    print()
    print("🔵 MÉTODO RANKINE:")
    print("✅ Ventajas:")
    print("   • Fórmulas más simples y directas")
    print("   • Aproximación conservadora (segura)")
    print("   • Apropiado para muros verticales")
    print("   • Cálculos más rápidos")
    print("   • Menor costo computacional")
    print()
    print("❌ Limitaciones:")
    print("   • No considera fricción muro-suelo")
    print("   • Asume muro vertical liso")
    print("   • Puede ser excesivamente conservador")
    print("   • No considera inclinación del terreno")
    print()
    
    print("🔴 MÉTODO COULOMB:")
    print("✅ Ventajas:")
    print("   • Considera fricción muro-suelo")
    print("   • Apropiado para muros inclinados")
    print("   • Más realista para muros rugosos")
    print("   • Considera inclinación del terreno")
    print("   • Proporciona componentes horizontal y vertical")
    print()
    print("❌ Limitaciones:")
    print("   • Fórmulas más complejas")
    print("   • Requiere más parámetros de entrada")
    print("   • Cálculos más laboriosos")
    print("   • Mayor costo computacional")
    print()
    
    print("🏆 RECOMENDACIÓN:")
    print()
    print("Para este ejemplo específico:")
    
    if resultados_rankine['FS_volcamiento'] >= 2.0 and resultados_rankine['FS_deslizamiento'] >= 1.5:
        print("✅ RANKINE es RECOMENDABLE porque:")
        print("   • Los factores de seguridad son adecuados")
        print("   • Proporciona un diseño conservador y seguro")
        print("   • Es más simple de implementar")
        print("   • Menor costo de diseño")
    else:
        print("✅ COULOMB es RECOMENDABLE porque:")
        print("   • Considera efectos de fricción muro-suelo")
        print("   • Proporciona un diseño más realista")
        print("   • Mejor aprovechamiento de la resistencia del suelo")
    
    print()
    print("📊 RECOMENDACIÓN GENERAL:")
    print("• Usar RANKINE para:")
    print("  - Diseños preliminares")
    print("  - Muros verticales simples")
    print("  - Cuando se requiere máxima seguridad")
    print("  - Proyectos con limitaciones de tiempo/costo")
    print()
    print("• Usar COULOMB para:")
    print("  - Diseños finales detallados")
    print("  - Muros inclinados o rugosos")
    print("  - Optimización de costos")
    print("  - Proyectos de alta importancia")
    print()
    
    print("🎯 CONCLUSIÓN:")
    print("Ambos métodos son válidos y complementarios.")
    print("Rankine para diseño conservador y rápido.")
    print("Coulomb para diseño optimizado y realista.")
    print("La elección depende del contexto del proyecto.")

if __name__ == "__main__":
    main() 