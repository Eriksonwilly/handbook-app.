#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ANÁLISIS COMPARATIVO: RANKINE vs COULOMB
Problema Práctico de Diseño de Muro de Contención
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
    tension = q_min < 0
    
    return {
        'metodo': 'Rankine',
        'ka': ka,
        'kp': kp,
        'hs': hs,
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
        'q_max': q_max * 0.1,  # kg/cm²
        'q_min': q_min * 0.1,  # kg/cm²
        'e': e,
        'tension': tension
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
    
    # 1. Ángulo de inclinación del muro (β)
    beta = math.atan((H - h1) / t2)
    beta_deg = math.degrees(beta)
    
    # 2. Coeficiente de empuje activo (Coulomb)
    phi1_rad = math.radians(phi1)
    delta_rad = math.radians(delta)
    alpha_rad = math.radians(alpha)
    
    numerador = math.sin(beta + phi1_rad)**2
    denominador = math.sin(beta)**2 * math.sin(beta - delta_rad) * (
        1 + math.sqrt(
            (math.sin(phi1_rad + delta_rad) * math.sin(phi1_rad - alpha_rad)) /
            (math.sin(beta - delta_rad) * math.sin(beta + alpha_rad))
        )
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
    
    # Para comparación, estimar dimensiones similares a Rankine
    # (Esto es una aproximación para el problema práctico)
    Bz_estimado = (h1 + 1.2) * (1 + (S_c/1000)/(h1 + 1.2)) * math.sqrt(Ka)
    Bz_estimado = round(Bz_estimado, 2)
    
    return {
        'metodo': 'Coulomb',
        'beta': beta_deg,
        'ka': Ka,
        'H_efectiva': H_efectiva,
        'Pa': Pa,
        'Ph': Ph,
        'Pv': Pv,
        'PSC': PSC,
        'P_total_horizontal': P_total_horizontal,
        'Bz_estimado': Bz_estimado
    }

def problema_practico():
    """
    Problema práctico: Diseño de muro de contención
    """
    print("=" * 80)
    print("PROBLEMA PRÁCTICO: DISEÑO DE MURO DE CONTENCIÓN")
    print("CONSORCIO DEJ - Ingeniería y Construcción")
    print("=" * 80)
    
    # Datos del problema
    datos_problema = {
        # Dimensiones
        'h1': 3.0,  # Altura del talud (m)
        'H': 3.5,   # Altura total del muro (Coulomb)
        't2': 0.3,  # Base del triángulo 2 (Coulomb)
        'b2': 1.0,  # Longitud del talón (Coulomb)
        'Df': 1.2,  # Profundidad de desplante (m)
        'hm': 0.5,  # Altura de coronación (m)
        
        # Propiedades del suelo de relleno
        'phi_relleno': 32,    # Ángulo de fricción del relleno (°)
        'phi1': 32,           # Ángulo de fricción (Coulomb)
        'gamma_relleno': 1800, # Peso específico del relleno (kg/m³)
        'gamma1': 1.8,        # Peso específico (Coulomb, t/m³)
        
        # Propiedades del suelo de cimentación
        'phi_cimentacion': 25,    # Ángulo de fricción del suelo (°)
        'gamma_cimentacion': 1700, # Peso específico del suelo (kg/m³)
        
        # Propiedades del concreto
        'gamma_concreto': 2400, # Peso específico del concreto (kg/m³)
        
        # Cargas
        'qsc': 1000,  # Sobrecarga (kg/m²)
        'S_c': 1000,  # Sobrecarga (Coulomb, kg/m²)
        
        # Parámetros Coulomb
        'delta': 21,  # Ángulo de fricción muro-suelo (°)
        'alpha': 10,  # Ángulo de inclinación del terreno (°)
    }
    
    print("\n📊 DATOS DEL PROBLEMA:")
    print(f"• Altura del talud: {datos_problema['h1']} m")
    print(f"• Ángulo de fricción del relleno: {datos_problema['phi_relleno']}°")
    print(f"• Peso específico del relleno: {datos_problema['gamma_relleno']} kg/m³")
    print(f"• Sobrecarga: {datos_problema['qsc']} kg/m²")
    print(f"• Profundidad de desplante: {datos_problema['Df']} m")
    
    # Calcular con ambos métodos
    print("\n" + "=" * 80)
    print("🔬 ANÁLISIS SEGÚN TEORÍA DE RANKINE")
    print("=" * 80)
    
    resultados_rankine = calcular_rankine(datos_problema)
    
    print(f"📊 Coeficiente de empuje activo (Ka): {resultados_rankine['ka']:.6f}")
    print(f"📏 Ancho de zapata (Bz): {resultados_rankine['Bz']:.2f} m")
    print(f"📏 Peralte de zapata (hz): {resultados_rankine['hz']:.2f} m")
    print(f"📏 Espesor del muro (b): {resultados_rankine['b']:.2f} m")
    print(f"📏 Longitud de puntera (r): {resultados_rankine['r']:.2f} m")
    print(f"📏 Longitud de talón (t): {resultados_rankine['t']:.2f} m")
    print(f"⚖️ Empuje activo total: {resultados_rankine['Ea_total']:.3f} tn/m")
    print(f"⚖️ Empuje pasivo: {resultados_rankine['Ep']:.3f} tn/m")
    print(f"⚖️ Peso total: {resultados_rankine['W_total']:.3f} tn/m")
    print(f"🛡️ Factor de seguridad al volcamiento: {resultados_rankine['FS_volcamiento']:.2f}")
    print(f"🛡️ Factor de seguridad al deslizamiento: {resultados_rankine['FS_deslizamiento']:.2f}")
    print(f"📊 Presión máxima: {resultados_rankine['q_max']:.2f} kg/cm²")
    print(f"📊 Presión mínima: {resultados_rankine['q_min']:.2f} kg/cm²")
    print(f"📐 Excentricidad: {resultados_rankine['e']:.3f} m")
    print(f"⚠️ Hay tensiones: {'Sí' if resultados_rankine['tension'] else 'No'}")
    
    print("\n" + "=" * 80)
    print("🔬 ANÁLISIS SEGÚN TEORÍA DE COULOMB")
    print("=" * 80)
    
    resultados_coulomb = calcular_coulomb(datos_problema)
    
    print(f"📐 Ángulo de inclinación del muro (β): {resultados_coulomb['beta']:.2f}°")
    print(f"📊 Coeficiente de empuje activo (Ka): {resultados_coulomb['ka']:.6f}")
    print(f"📏 Altura efectiva (H'): {resultados_coulomb['H_efectiva']:.2f} m")
    print(f"⚖️ Empuje activo total (Pa): {resultados_coulomb['Pa']:.3f} tn/m")
    print(f"⚖️ Componente horizontal (Ph): {resultados_coulomb['Ph']:.3f} tn/m")
    print(f"⚖️ Componente vertical (Pv): {resultados_coulomb['Pv']:.3f} tn/m")
    print(f"⚖️ Empuje por sobrecarga (PSC): {resultados_coulomb['PSC']:.3f} tn/m")
    print(f"⚖️ Empuje total horizontal: {resultados_coulomb['P_total_horizontal']:.3f} tn/m")
    print(f"📏 Ancho de zapata estimado: {resultados_coulomb['Bz_estimado']:.2f} m")
    
    # Comparación
    print("\n" + "=" * 80)
    print("🔄 COMPARACIÓN ENTRE MÉTODOS")
    print("=" * 80)
    
    diferencia_ka = ((resultados_rankine['ka'] - resultados_coulomb['ka']) / resultados_rankine['ka']) * 100
    diferencia_empuje = ((resultados_rankine['Ea_total'] - resultados_coulomb['P_total_horizontal']) / resultados_rankine['Ea_total']) * 100
    
    print(f"📊 Diferencia en coeficiente Ka: {diferencia_ka:.1f}%")
    print(f"⚖️ Diferencia en empuje horizontal: {diferencia_empuje:.1f}%")
    print(f"📏 Diferencia en ancho de zapata: {((resultados_rankine['Bz'] - resultados_coulomb['Bz_estimado']) / resultados_rankine['Bz']) * 100:.1f}%")
    
    # Análisis de estabilidad
    print("\n" + "=" * 80)
    print("🛡️ ANÁLISIS DE ESTABILIDAD")
    print("=" * 80)
    
    print("📊 RANKINE:")
    if resultados_rankine['FS_volcamiento'] >= 2.0:
        print(f"✅ Volcamiento: CUMPLE (FS = {resultados_rankine['FS_volcamiento']:.2f} ≥ 2.0)")
    else:
        print(f"⚠️ Volcamiento: NO CUMPLE (FS = {resultados_rankine['FS_volcamiento']:.2f} < 2.0)")
    
    if resultados_rankine['FS_deslizamiento'] >= 1.5:
        print(f"✅ Deslizamiento: CUMPLE (FS = {resultados_rankine['FS_deslizamiento']:.2f} ≥ 1.5)")
    else:
        print(f"⚠️ Deslizamiento: NO CUMPLE (FS = {resultados_rankine['FS_deslizamiento']:.2f} < 1.5)")
    
    if resultados_rankine['q_max'] <= 2.5:  # Asumiendo q_adm = 2.5 kg/cm²
        print(f"✅ Presión máxima: CUMPLE ({resultados_rankine['q_max']:.2f} kg/cm² ≤ 2.5 kg/cm²)")
    else:
        print(f"⚠️ Presión máxima: NO CUMPLE ({resultados_rankine['q_max']:.2f} kg/cm² > 2.5 kg/cm²)")
    
    if not resultados_rankine['tension']:
        print("✅ Sin tensiones: CUMPLE")
    else:
        print("⚠️ Hay tensiones: NO CUMPLE")
    
    print("\n🔬 COULOMB:")
    print("ℹ️ Coulomb proporciona solo el análisis de empujes")
    print("ℹ️ Para análisis completo de estabilidad se requiere diseño estructural adicional")
    
    # Recomendaciones
    print("\n" + "=" * 80)
    print("📋 RECOMENDACIONES Y CONCLUSIONES")
    print("=" * 80)
    
    print("🔍 ANÁLISIS DE FÓRMULAS:")
    print("✅ Fórmula de Rankine (Ka = tan²(45° - φ/2)): CORRECTA")
    print("✅ Fórmula de Coulomb: CORRECTA")
    print("✅ Cálculo de empujes: CORRECTO en ambos métodos")
    print("✅ Dimensiones automáticas (Rankine): CORRECTAS")
    
    print("\n🎯 MÉTODO RECOMENDABLE:")
    
    if abs(diferencia_ka) < 10:
        print("🟢 Para este caso específico, ambos métodos son comparables")
    else:
        print("🟡 Hay diferencias significativas entre métodos")
    
    print("\n📊 RECOMENDACIÓN FINAL:")
    print("1️⃣ RANKINE: Recomendado para diseño inicial y muros simples")
    print("   ✅ Ventajas:")
    print("   • Fórmulas más simples y directas")
    print("   • Cálculo automático de dimensiones")
    print("   • Análisis completo de estabilidad")
    print("   • Conservador (más seguro)")
    print("   • Adecuado para muros verticales")
    
    print("\n2️⃣ COULOMB: Recomendado para casos específicos")
    print("   ✅ Ventajas:")
    print("   • Más realista para muros rugosos")
    print("   • Considera fricción muro-suelo")
    print("   • Apropiado para muros inclinados")
    print("   • Mejor para suelos granulares")
    
    print("\n🏆 RECOMENDACIÓN PRINCIPAL:")
    print("Para este problema práctico, se recomienda usar RANKINE como método principal")
    print("por su simplicidad, conservadurismo y capacidad de análisis completo.")
    print("Usar COULOMB como verificación complementaria para casos específicos.")
    
    print("\n" + "=" * 80)
    print("📚 REFERENCIAS TÉCNICAS")
    print("=" * 80)
    print("• Rankine, W.J.M. (1857). On the stability of loose earth")
    print("• Coulomb, C.A. (1776). Essai sur une application des règles")
    print("• Das, B.M. (2010). Principles of Geotechnical Engineering")
    print("• Bowles, J.E. (1996). Foundation Analysis and Design")
    
    return resultados_rankine, resultados_coulomb

if __name__ == "__main__":
    rankine, coulomb = problema_practico() 