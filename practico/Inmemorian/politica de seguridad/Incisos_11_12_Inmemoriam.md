# 11. Administración de la Continuidad de las Actividades de la Organización

La administración de la continuidad de las actividades es un proceso crítico que debe involucrar a todos los niveles de la Organización. El desarrollo e implementación de planes de contingencia es una herramienta básica para garantizar que las actividades de la Organización puedan restablecerse dentro de los plazos requeridos.

Inmemoriam enfrenta una situación crítica de ciberseguridad que requiere atención inmediata: depende del 75% de sistemas informáticos (dos ERP, portales web, correo electrónico) sin poseer ningún sistema de respaldo de información. La falta de respaldos representa un riesgo existencial para la continuidad de la operación. Adicionalmente, la infraestructura está distribuida en tres locaciones con conexiones independientes a Internet, creando múltiples puntos de fallo. El proveedor externo de sistemas es un punto crítico único de dependencia para toda la organización.

Es fundamental establecer medidas inmediatas para proteger los procesos críticos mediante una combinación de controles preventivos, planes de recuperación, e implementación urgente de sistemas de respaldo.

## Objetivo

Minimizar los efectos de las posibles interrupciones de las actividades normales de la Organización y garantizar la continuidad del negocio ante: pérdida de datos, fallas de sistemas ERP, cortes de conectividad a Internet, fallas de equipamiento, indisponibilidad del proveedor externo de sistemas, desastres naturales o ataques informáticos.

Establecer procedimientos de recuperación y operación manual para los 8 empleados de Inmemoriam, asignando claramente responsabilidades en cada una de las tres locaciones operativas (Parque Industrial, Local Inmemorian, Local La Roca).

Implementar urgentemente un plan de respaldos regulares dado que actualmente no existen copias de seguridad de ninguna información crítica.

## Alcance

Esta Política se aplica a todos los procesos críticos para Inmemoriam: Ventas (placas conmemorativas, placas profesionales, mezadas), Compras, Importaciones, Logística, Finanzas, Producción, y Sistemas. Se aplica a las tres locaciones:

- **Parque Industrial**: 1 módem/router WiFi, 1 PC de producción, 2 PC de dueños
- **Local Inmemorian**: 1 módem/router WiFi, 1 PC de venta, 1 móvil corporativo
- **Local La Roca**: 1 módem/router WiFi, 2 PC de venta, 1 móvil corporativo

Se aplica también a los 2 ERP utilizados, portales web, correo electrónico, datos de clientes (nombres, fechas, datos bancarios) y registros de producción/logística.

## Responsabilidad

Los Dueños son los responsables finales de garantizar la continuidad del negocio y aprobar el presupuesto para implementar respaldos y sistemas de redundancia.

Seguridad de la Información (role que debe ser formalmente asignado, actualmente ausente) participará en la definición, documentación y actualización de los planes de contingencia.

El Proveedor Externo de Sistemas deberá implementar y mantener:
- Respaldos automáticos diarios de ambos ERP
- Respaldos de correo electrónico
- Procedimientos documentados de recuperación ante desastre
- Contacto 24/7 en caso de emergencia

Los Propietarios de la Información (por proceso) cumplirán las siguientes funciones:

- **Gerencia de Ventas (Placas Conmemorativas y Profesionales)**: Responsable de procedimientos manuales de toma de pedidos y de lista de clientes en papel
- **Gerencia de Ventas (Mezadas)**: Responsable de procedimientos manuales de toma de pedidos para mezadas
- **Gerencia de Producción**: Responsable de procedimientos manuales de órdenes de producción y registros de inventario
- **Gerencia de Logística**: Responsable de procedimientos manuales de seguimiento de entregas
- **Finanzas (Proveedor Externo)**: Responsable de respaldos de información financiera y registros bancarios

Todos los integrantes de la Organización comprenderán los riesgos y participarán en simulacros periódicos de contingencia.

## 11.1. Continuidad de las Actividades y Análisis de los Impactos

Con el fin de establecer un Plan de Continuidad de las Actividades de la Organización se deben contemplar los siguientes puntos:

### Amenazas Identificadas Críticas para Inmemoriam

- **Pérdida total de datos de ambos ERP**: Sin respaldos, esto implica pérdida total de información de pedidos, clientes, proveedores, inventario y finanzas. Impacto: CRÍTICO TOTAL. Probabilidad: ALTA (sin respaldos).
- **Corte de Internet en Parque Industrial**: Afecta producción (1 PC), datos de dueños. Impacto: ALTO. Probabilidad: MEDIA.
- **Corte de Internet en Local Inmemorian**: Afecta ventas de placas profesionales (1 PC), datos de clientes. Impacto: ALTO. Probabilidad: MEDIA.
- **Corte de Internet en Local La Roca**: Afecta ventas de mezadas (2 PC), datos de clientes. Impacto: ALTO. Probabilidad: MEDIA.
- **Falla completa del proveedor externo de sistemas**: Sin acceso a ERP, correo electrónico, portales web. Impacto: CRÍTICO. Probabilidad: MEDIA (dependencia única).
- **Corrupción de datos en ERP**: Transacciones incorrectas, información de clientes dañada. Impacto: CRÍTICO. Probabilidad: MEDIA (sin validaciones conocidas).
- **Indisponibilidad de un ERP**: Pérdida de funcionalidad para compras/ventas. Impacto: ALTO. Probabilidad: BAJA.
- **Falla de energía eléctrica prolongada**: Afecta todas las locaciones. Impacto: CRÍTICO. Probabilidad: BAJA a MEDIA.
- **Daño físico a equipamiento** (incendio, inundación, robo): Pérdida de PC en cualquier locación. Impacto: ALTO. Probabilidad: BAJA.
- **Ataque informático o ransomware**: Sin firewall, sin filtros anti-spam/phishing, sin antivirus centralizado. Impacto: CRÍTICO. Probabilidad: MEDIA-ALTA.
- **Pérdida de acceso a datos bancarios de clientes**: Falta de procedimientos de protección, múltiples accesos. Impacto: CRÍTICO LEGAL. Probabilidad: MEDIA.

### Evaluación de Riesgos por Escenario

**Escenario 1: Pérdida de un ERP durante 24 horas**
- Impacto: Imposibilidad de registrar nuevas ventas, compras u órdenes de producción. Operación manual únicamente.
- Tiempo de recuperación aceptable: Máximo 4-6 horas
- Prioridad: CRÍTICA
- Acción: Respaldo diario automático + pruebas semanales de restauración

**Escenario 2: Corte de Internet en todas las locaciones simultáneamente**
- Impacto: Sin acceso a ERP, sin correo, sin portales. Operación completamente manual.
- Tiempo de recuperación aceptable: Máximo 2-4 horas
- Prioridad: CRÍTICA
- Acción: Procedimientos manuales documentados para cada locación, lista de contactos de proveedor de Internet

**Escenario 3: Indisponibilidad del proveedor externo de sistemas por más de 48 horas**
- Impacto: Sin soporte, sin respaldos, sin recuperación de sistemas. Riesgo de pérdida total de datos.
- Tiempo de recuperación aceptable: Máximo 24 horas
- Prioridad: CRÍTICA
- Acción: Contrato SLA con proveedor que incluya garantías de tiempo de respuesta y disponibilidad de respaldos

**Escenario 4: Ataque de ransomware**
- Impacto: Todos los ERP cifrados, datos inaccesibles, posible demanda de rescate.
- Tiempo de recuperación aceptable: Máximo 8 horas
- Prioridad: CRÍTICA MÁXIMA
- Acción: Implementación urgente de firewall, filtros anti-phishing, antivirus centralizado, respaldos offline

**Escenario 5: Corrupción de datos de clientes (nombres, fechas, datos bancarios)**
- Impacto: Violación de Ley 25.326, demanda de clientes, multas administrativas.
- Tiempo de recuperación aceptable: Máximo 1 hora
- Prioridad: CRÍTICA LEGAL
- Acción: Respaldos con punto de recuperación horario, auditoría de accesos a datos sensibles

### Controles Preventivos Recomendados Inmediatamente

1. **Respaldos de Información** (URGENTE - No existen actualmente)
   - Respaldos automáticos diarios de ambos ERP (completos)
   - Respaldos de correo electrónico (diarios)
   - Respaldos de portales web (semanales)
   - Respaldos offline inmutables en disco externo o almacenamiento en nube (semanales)
   - Pruebas de restauración una vez por semana, documentadas

2. **Protección Perimetral** (URGENTE - No existe actualmente)
   - Firewall perimetral para bloquear acceso no autorizado
   - Filtros anti-spam y anti-phishing en correo
   - Antivirus/anti-malware centralizado en todas las PC

3. **Infraestructura Resiliente** (Mediano Plazo)
   - Estabilizadores de energía (UPS) en Parque Industrial (producción), Local Inmemorian, Local La Roca
   - Conexión redundante a Internet en al menos Parque Industrial y Local Inmemorian
   - Acuerdos SLA con proveedor de Internet para tiempo de reparación máximo de 4 horas

4. **Infraestructura de Redes** (Mediano Plazo)
   - Segmentación de redes por locación y por área funcional
   - VPN para conectividad remota segura entre locaciones
   - Separación de red de producción de red de administración

5. **Monitoreo y Alertas** (Mediano Plazo)
   - Monitoreo centralizado de disponibilidad de sistemas
   - Alertas automáticas en caso de falla de ERP, corte de Internet, o falla de respaldo
   - Registros centralizados de accesos y cambios en sistemas

Esta actividad será llevada a cabo con la activa participación de los Dueños, Propietarios de la Información, y el Proveedor Externo de Sistemas.

## 11.2. Elaboración e Implementación de los Planes de Continuidad

Los Dueños en conjunto con el Proveedor Externo de Sistemas y Propietarios de la Información elaborarán los planes de contingencia necesarios para garantizar la continuidad de las actividades de la Organización.

### 11.2.1 Plan de Contingencia por Escenario

**Escenario A: Indisponibilidad de Ambos ERP (Duración: Hasta 6 horas)**

*Responsables: Dueños, Proveedor de Sistemas*

Acciones inmediatas:
- Proveedor de Sistemas intenta restauración de respaldos (máximo 30 minutos)
- Si restauración no es posible, se activa Plan B

Plan B - Operación Manual:
- Gerencia de Ventas (Placas): Registra pedidos en formato papel pre-impreso (modelo adjunto)
- Gerencia de Ventas (Mezadas): Registra pedidos en formato papel pre-impreso (modelo adjunto)
- Gerencia de Producción: Registra órdenes de producción en papel
- Gerencia de Logística: Registra entregas en papel
- Finanzas: Registra transacciones en planilla Excel local (si está disponible)
- Una vez restaurado ERP, ingresa manualmente la información acumulada

Tiempo de activación: Inmediato (mientras se intenta restauración)
Tiempo de restablecimiento: Máximo 6 horas

**Escenario B: Corte de Internet en una Locación (Parque Industrial, Inmemorian o La Roca)**

*Responsable: Dueños / Gerente Local*

Acciones inmediatas:
- Verificar conexión, reiniciar módem/router
- Contactar a proveedor de Internet para reporte de falla
- Activar modo offline si es posible en ERP
- Si no hay modo offline, activar Plan B

Plan B - Operación Manual:
- **Parque Industrial**: Producción continúa sin ERP. Registra órdenes en papel hasta 6 horas
- **Local Inmemorian**: Ventas registra en papel, no puede acceder a ERP ni portales web
- **Local La Roca**: Ventas registra en papel, no puede acceder a ERP ni portales web
- Dueños en otra locación continúan operaciones normales

Tiempo de restablecimiento objetivo: 2-4 horas (según proveedor de Internet)
Máximo tiempo de operación manual: 8 horas

**Escenario C: Indisponibilidad del Proveedor Externo de Sistemas**

*Responsable: Dueños*

Acciones inmediatas:
- Intentar contactar al proveedor (teléfono, WhatsApp)
- Si no responde en 30 minutos, escalar a contacto secundario
- Activar Plan B

Plan B - Operación Parcial Manual:
- **Sistema de respaldo**: Si existen respaldos en almacenamiento externo, intentar acceder directamente (necesita documentación de cómo hacer)
- **Correo electrónico**: No disponible (depende del proveedor)
- **ERP**: No disponible
- **Pedidos**: Manual en papel
- **Comunicación interna**: WhatsApp (ya que no hay correo)
- **Comunicación con clientes**: Teléfono/WhatsApp

Contacto de emergencia del proveedor: DEBE ESTAR DOCUMENTADO Y DISPONIBLE EN TODOS LOS LOCALES

Tiempo de restablecimiento: Máximo 24 horas

**Escenario D: Ataque de Ransomware o Malware**

*Responsable: Dueños / Proveedor de Sistemas*

Acciones inmediatas (CRÍTICAS):
- Desconectar todos los PC de Internet inmediatamente
- NO pagar rescate
- Contactar a Proveedor de Sistemas
- Contactar a autoridades (Policía Cibernética)
- Restaurar desde respaldo offline (si existe)

Plan B - Recuperación:
- Si hay respaldo offline anterior a ataque, restaurar (máximo 24 horas)
- Si no hay respaldo, pérdida total de datos (escenario worst-case)
- Operación manual hasta recuperación

Prevención (URGENTE):
- Implementar firewall perimetral
- Implementar filtros anti-phishing
- Actualizar sistemas operativos
- Antivirus en todas las PC

**Escenario E: Falla de Energía Eléctrica**

*Responsable: Gerentes Locales*

Acciones inmediatas:
- Verificar si es falla local o general
- Si hay UPS/estabilizador, sistema continúa funcionando por 30 minutos a 1 hora
- Guardar trabajo en ERP si aún hay energía
- Apagar equipamiento ordenadamente

Operación durante falla:
- Sin energía: Sin ERP, sin correo, sin Internet
- Activar Plan B - Operación Manual en papel
- Si falla es prolongada (>2 horas), cerrar operaciones hasta restauración de energía

Prevención:
- Instalar UPS en Parque Industrial (producción crítica)
- Instalar UPS en Local Inmemorian
- Instalar UPS en Local La Roca

### 11.2.2 Procedimientos Operativos Alternativos Documentados

Cada Gerencia debe tener documentados los siguientes procedimientos en papel y revisables:

**Gerencia de Ventas - Placas Conmemorativas y Profesionales**
- Formulario de pedido manual con campos: Nombre cliente, Fecha pedido, Descripción placa, Fecha entrega, Datos de contacto, Datos bancarios
- Libro de registro de pedidos (numeración secuencial)
- Procedimiento de ingreso posterior a ERP

**Gerencia de Ventas - Mezadas**
- Formulario de pedido manual con campos: Nombre cliente, Medidas, Material, Diseño, Fecha entrega, Datos de contacto, Datos bancarios
- Libro de registro de pedidos
- Procedimiento de ingreso posterior a ERP

**Gerencia de Producción**
- Formulario de orden de producción con campos: Número orden, Descripción producto, Cantidad, Material, Diseño, Fechas hito, Estado
- Registro de inventario manual
- Registro de máquinas/equipos utilizados

**Gerencia de Logística**
- Formulario de envío con campos: Número pedido, Cliente, Dirección, Fecha entrega, Transportista, Número seguimiento
- Registro de entregas
- Registro de devoluciones

**Finanzas**
- Registro manual de transacciones: Ingresos, egresos, cuentas por cobrar, cuentas por pagar
- Procedimiento de ingreso posterior a ERP

### 11.2.3 Ubicación de Documentación y Contactos de Emergencia

Cada locación debe tener de forma física (no digital):

1. **Plan de Continuidad impreso** - Accesible incluso sin electricidad
2. **Formularios de pedido/orden en blanco** - Stock de al menos 100 unidades
3. **Lista de contactos de emergencia**:
   - Proveedor de Sistemas (nombre, teléfono, WhatsApp, email)
   - Proveedor de Internet (nombre, teléfono, número de cliente)
   - Proveedor de Energía Eléctrica (número de cliente)
   - Dueños (teléfono, WhatsApp)
   - Gerentes de otras locaciones (teléfono, WhatsApp)
   - Autoridades (Policía, Bomberos, Policía Cibernética)

4. **Procedimientos de operación manual** - Paso a paso para cada área
5. **Guía de restauración de respaldos** - Pasos para restaurar desde almacenamiento externo

### 11.2.4 Pruebas y Simulacros

- **Frecuencia**: Mínimo semestralmente (cada 6 meses)
- **Tipo**: 
  - Simulacro de corte de Internet (sin desconectar realmente)
  - Simulacro de indisponibilidad de ERP (sin desconectar realmente)
  - Prueba real de restauración de respaldos (mínimo trimestral)
- **Documentación**: Cada simulacro debe ser documentado con fecha, hora, área participante, resultado, incidencias encontradas
- **Mejora continua**: Después de cada simulacro, revisar Plan y hacer ajustes
- **Participación**: Al menos un integrante de cada área debe participar en cada simulacro

### 11.2.5 Plan de Respaldos - Implementación Urgente

**CRITICIDAD**: Este es el punto más urgente e importante. Sin respaldos, cualquier falla de datos es catastrófica.

**Responsable**: Proveedor Externo de Sistemas

**Requerimientos mínimos**:
- Respaldos automáticos diarios de ambos ERP (completos)
- Respaldos automáticos diarios de correo electrónico
- Respaldos semanales de portales web
- Respaldos offline (disco externo o almacenamiento en nube) semanales, guardados en locación diferente a Parque Industrial
- Cifrado de respaldos para proteger datos de clientes
- Punto de recuperación de máximo 24 horas (RPO = 24h)
- Tiempo máximo de recuperación de 6 horas (RTO = 6h)

**Pruebas de restauración**:
- Una vez por semana, mínimo
- Documentadas (fecha, hora, qué se restauró, resultado)
- Involucrar a Finanzas para validar datos restaurados

**Costos estimados**:
- Almacenamiento en nube (respaldos incrementales): $30-50 USD/mes
- Disco externo de 2-4TB (respaldos offline): $100-200 USD (inversión única)
- Horas de implementación y testing: 10-15 horas proveedor

### 11.2.6 Escalamiento y Comunicación

En caso de incidente:

1. **Fase 1 (0-15 min)**: Gerente local/dueño local intenta resolver
2. **Fase 2 (15-30 min)**: Contacta a proveedor de sistemas / proveedor de servicio
3. **Fase 3 (30 min - 2 horas)**: Dueños declaran "Situación de Contingencia" y activan Plan B manual
4. **Fase 4 (>2 horas)**: Evalúan cierre temporal de operaciones si el impacto es crítico

Comunicación:
- Comunicado a todos los empleados vía WhatsApp
- Comunicado a clientes (si es necesario) vía teléfono
- Registro del incidente: fecha, hora, descripción, causa identificada, acciones tomadas, duración, datos perdidos (si aplica)

### 11.2.7 Expectativas de Disponibilidad por Servicio

| Servicio | Disponibilidad Objetivo | Impacto si No Disponible | Tiempo Recuperación |
|----------|------------------------|--------------------------|---------------------|
| ERP Ventas | 99.5% | Alto (pedidos no registrados) | 6 horas máximo |
| ERP Producción | 99.5% | Alto (órdenes no procesadas) | 6 horas máximo |
| Correo electrónico | 99% | Bajo-Medio (usar WhatsApp) | 2-4 horas |
| Internet Parque Industrial | 99% | Alto (producción parada) | 4 horas máximo |
| Internet Local Inmemorian | 99% | Alto (ventas parada) | 4 horas máximo |
| Internet Local La Roca | 99% | Alto (ventas parada) | 4 horas máximo |
| Respaldos | 100% (diarios) | Crítico (pérdida de datos) | N/A (preventivo) |

---

# 12. Cumplimiento

El diseño, operación, uso y administración de los sistemas de información están regulados por disposiciones legales y contractuales. Inmemoriam debe cumplir con obligaciones específicas relacionadas con la protección de datos de clientes y datos bancarios compartidos, conforme a la Ley 25.326 de Protección de Datos Personales de la República Argentina.

## Objetivo

Cumplir con las disposiciones normativas y contractuales a fin de evitar sanciones administrativas y legales a la Organización, así como proteger los derechos de los clientes cuya información es procesada.

Garantizar que los sistemas cumplan con la política, normas y procedimientos de seguridad de la Organización.

## Alcance

Esta Política se aplica a todo el personal de la Organización, a sus clientes y proveedores cuya información es procesada.

Asimismo, se aplica a los sistemas de información (ERP, portales web, correo electrónico), normas, procedimientos, documentación y plataformas técnicas de la Organización y a las auditorías efectuadas sobre los mismos.

## Responsabilidad

Seguridad de la Información verificará periódicamente que los sistemas de información cumplan la política, normas y procedimientos de seguridad establecidos.

Sistemas verificará que sólo se instalen productos con licencia y software autorizado, y cumplirá con los requisitos de protección de datos establecidos en los contratos con terceros y en la legislación vigente.

Legales será responsable de verificar el cumplimiento de la presente Política en la gestión de todos los contratos, acuerdos u otra documentación de la Organización con sus clientes, proveedores, empleados y terceros. Asimismo, asesorará en materia legal a la Organización en lo que se refiere a la seguridad de la información y protección de datos.

Todos los empleados comprenderán, darán a conocer y cumplirán la presente Política. Cada responsable de área asegurará que su equipo de trabajo cumpla con los requisitos legales y contractuales aplicables a la información que manejan.

## 12.1. Cumplimiento de Requisitos Legales

### 12.1.1. Protección de Datos Personales

Inmemoriam procesa información personal de clientes (nombres, fechas, direcciones, datos de contacto) y en algunos casos datos sensibles como información relacionada a difuntos e imágenes conmemorativas. Asimismo, maneja datos bancarios compartidos con clientes para procesar pagos.

La Organización debe cumplir con la Ley 25.326 de Protección de Datos Personales, que establece normas para la recolección, almacenamiento, uso y transmisión de datos personales. Entre otras obligaciones:

- Obtener consentimiento informado de los clientes para el tratamiento de sus datos personales.

- Informar a los clientes sobre qué datos se recopilan, para qué se utilizan, con quién se comparten, y cómo pueden acceder, corregir o solicitar eliminación de sus datos.

- Implementar medidas de seguridad técnicas y organizativas para proteger los datos contra acceso no autorizado, modificación, pérdida o destrucción.

- Limitar el acceso a los datos personales únicamente al personal que necesita conocerlos para sus funciones.

- Reportar violaciones de datos a la Autoridad de Control de Datos Personales (Dirección Nacional de Protección de Datos Personales) en caso de acceso no autorizado o incidentes graves.

- Establecer cláusulas de confidencialidad en contratos con proveedores y terceros que accedan a datos personales de clientes.

### 12.1.2. Datos Bancarios y Transacciones Financieras

Cuando Inmemoriam procesa datos bancarios de clientes (números de cuenta, datos de tarjeta de crédito, información de transacciones), debe cumplir con regulaciones adicionales:

- Los datos bancarios se consideran información altamente sensible y crítica. Deben estar cifrados en tránsito y en reposo.

- Nunca almacenar números de tarjeta de crédito completos en bases de datos propias. Utilizar servicios de terceros certificados (procesadores de pago) para el manejo de datos bancarios.

- Realizar auditorías regulares y mantener registros de quién accede a información bancaria y cuándo.

- Asegurar que cualquier proveedor externo que maneje datos bancarios cumpla con estándares de seguridad reconocidos internacionalmente.

### 12.1.3. Derecho de Propiedad Intelectual del Software

El software es considerado una obra intelectual que goza de la protección de la Ley 11.723 de Propiedad Intelectual.

Los productos de software se suministran normalmente bajo acuerdos de licencia que suelen limitar el uso de los productos al equipamiento específico y su copia a la creación de copias de resguardo solamente.

Seguridad de la Información, con la asistencia de Sistemas, verificará que sólo se instalen productos con licencia y software autorizado. Se realizarán auditorías periódicas de licenciamiento de software para garantizar cumplimiento legal.

### 12.1.4. Cumplimiento de Obligaciones Contractuales

Inmemoriam mantiene contratos con terceros (proveedor de sistemas, proveedores de servicios) que incluyen cláusulas de seguridad y confidencialidad.

Legales verificará que todos los contratos incluyan cláusulas que obliguen a los terceros a cumplir con la Política de Seguridad de la Información y con la legislación vigente en materia de protección de datos. Se realizarán revisiones periódicas de estos contratos para garantizar su cumplimiento.

## 12.2. Cumplimiento de la Política de Seguridad

Cada Sector velará por la correcta implementación y cumplimiento de las normas y procedimientos de seguridad establecidos, dentro de su área de responsabilidad, dando a conocer y reportando a Seguridad de la Información toda anomalía o incumplimiento que detecte.

La Dirección de la Organización debe demostrar un compromiso activo con la seguridad de la información, asignando recursos presupuestarios y humanos suficientes para implementar los controles necesarios.

### 12.2.1. Auditorías Internas de Cumplimiento

Auditoría Interna (o un auditor externo en caso de no existir) es responsable de practicar auditorías periódicas (al menos anualmente) sobre los sistemas y actividades vinculadas con la tecnología de información y la protección de datos.

Deberá informar sobre el cumplimiento de las especificaciones y medidas de seguridad de la información establecidas por esta Política y por las normas y procedimientos que de ella surjan, incluyendo compliance con leyes de protección de datos personales.

### 12.2.2. Sanciones por Incumplimiento

Los empleados que incumplan la presente Política de Seguridad de la Información podrán estar sujetos a medidas disciplinarias proporcionales al incumplimiento, que pueden incluir desde capacitación adicional hasta la terminación de la relación laboral, según lo establezcan las políticas de personal y la legislación laboral vigente. Asimismo, Inmemoriam podrá estar sujeta a sanciones legales y administrativas en caso de violación de leyes de protección de datos.
