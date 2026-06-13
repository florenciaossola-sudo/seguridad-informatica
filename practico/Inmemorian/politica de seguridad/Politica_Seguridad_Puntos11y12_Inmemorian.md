# Plan de Seguridad de la Información
## Inmemorian
### Puntos 11 y 12 — Administración de la Continuidad de las Actividades / Cumplimiento

---

# 11. Administración de la Continuidad de las Actividades de la Organización

La administración de la continuidad de las actividades es un proceso crítico que debe involucrar a todos los niveles de la Organización. El desarrollo e implementación de planes de contingencia es una herramienta básica para garantizar que las actividades de Inmemorian puedan restablecerse dentro de los plazos requeridos.

Dichos planes deben mantenerse actualizados y transformarse en una parte integral del resto de los procesos de administración y gestión.

El relevamiento de la situación actual evidenció condiciones que elevan el riesgo de interrupción operativa: la organización depende aproximadamente en un **75 %** de sus sistemas informáticos (2 ERP, portales web, correo electrónico, WhatsApp) para coordinar ventas, producción, logística y finanzas; **no existen respaldos de información** de ningún tipo; la infraestructura está distribuida en **tres locaciones** con conexiones a Internet independientes y sin segmentación; y existe **dependencia crítica de un proveedor externo de sistemas** sin acuerdos formales de nivel de servicio ni definición de responsabilidades ante incidentes. Asimismo, la ausencia de firewall perimetral, filtros anti-phishing, antivirus centralizado y actualizaciones regulares incrementa la probabilidad de incidentes que comprometan la disponibilidad de los sistemas.

## Objetivo

- Minimizar los efectos de las posibles interrupciones de las actividades normales de Inmemorian —sean éstas resultado de desastres naturales, accidentes, fallas en el equipamiento, cortes de conectividad, indisponibilidad del proveedor externo, ataques informáticos u otros hechos— y proteger los procesos críticos mediante una combinación de controles preventivos y acciones de recuperación.
- Analizar las consecuencias de la interrupción del servicio y tomar las medidas correspondientes para la prevención de hechos similares en el futuro.
- Asegurar la coordinación con el personal de la organización —8 empleados en total, distribuidos entre las tres sedes— y los contactos externos que participarán en las estrategias de planificación de contingencias, asignando funciones para cada actividad definida.
- Implementar de forma urgente un esquema de respaldos y procedimientos de operación manual, dado que actualmente no existen copias de seguridad ni procedimientos formales de recuperación.

## Alcance

Esta política se aplica a todos los procesos críticos identificados de Inmemorian:

- **Ventas** de placas conmemorativas, placas para profesionales y mesadas para baños y cocinas.
- **Compras e importaciones** de materiales (mármol, granito y otras piedras naturales y sintéticas).
- **Producción** (grabados, pinturas, imágenes y símbolos religiosos).
- **Logística** y distribución.
- **Finanzas** y administración.
- **Sistemas** y tecnología.

Comprende las tres locaciones operativas:

| Locación | Equipamiento informático |
|---|---|
| **Parque Industrial** | 1 módem/router WiFi, 1 PC de producción, 2 PC de dueños |
| **Local Inmemorian** | 1 módem/router WiFi, 1 PC de venta, 1 móvil corporativo |
| **Local La Roca** | 1 módem/router WiFi, 2 PC de venta, 1 móvil corporativo |

Asimismo, se aplica a los 2 ERP, portales web, correo electrónico, cuentas comerciales de WhatsApp, Instagram y Facebook, y a la información crítica del negocio —incluyendo datos personales y bancarios de clientes— procesada en dichos sistemas.

## Responsabilidad

Dado que Inmemorian **no cuenta con un responsable formal del área de sistemas ni con un área de Seguridad de la Información dedicada**, las funciones se distribuyen de la siguiente manera:

### Dueños de la organización

En su carácter de autoridad que toma las decisiones más importantes —incluidas las tecnológicas— y que actualmente responde ante emergencias junto con los gerentes:

- Aprobar el presupuesto y los recursos necesarios para implementar respaldos, controles preventivos y planes de contingencia.
- Declarar formalmente una **"Situación de Contingencia"** cuando la interrupción supere los umbrales definidos en el plan.
- Asumir provisionalmente la función de **responsable de Seguridad de la Información** hasta que se formalice la designación, participando en la definición, documentación y actualización de los planes de contingencia.

### Proveedor externo de sistemas

En su carácter de administrador de servidores, usuarios, accesos y sistemas críticos:

- Implementar y mantener respaldos automáticos de los ERP, correo electrónico y portales web.
- Documentar y ejecutar los procedimientos de recuperación ante desastre.
- Proveer contacto de emergencia y tiempos de respuesta acordados contractualmente (SLA).
- Participar activamente en las pruebas periódicas de restauración de respaldos.

### Propietarios de la información (gerentes de área)

Cumplirán las siguientes funciones, en coordinación con los dueños:

- Identificar las amenazas que puedan ocasionar interrupciones de los procesos y actividades de su área.
- Evaluar los riesgos para determinar el impacto de dichas interrupciones.
- Elaborar y mantener los procedimientos manuales de contingencia de su área.
- Identificar y priorizar los procesos críticos bajo su responsabilidad.
- Asegurar que el personal a su cargo comprenda los riesgos y conozca los procedimientos de operación alternativa.
- Coordinar actualizaciones periódicas de los planes y procesos implementados.

Asignación por área:

| Área | Responsabilidad principal en contingencia |
|---|---|
| Gerencia de Ventas (Placas Conmemorativas y Profesionales) | Procedimientos manuales de toma de pedidos; registro en papel de clientes y pedidos |
| Gerencia de Ventas (Mesadas) | Procedimientos manuales de toma de pedidos para mesadas |
| Gerencia de Producción | Órdenes de producción e inventario en formato manual |
| Gerencia de Logística | Seguimiento de entregas y envíos en formato manual |
| Finanzas (proveedor externo) | Respaldo y recuperación de información financiera y registros bancarios |

### Todo el personal

- Comprender los riesgos que enfrenta la organización y los efectos que una interrupción puede tener en la actividad diaria.
- Conocer y aplicar los procedimientos de operación manual definidos para su área.
- Participar en simulacros periódicos de contingencia.

---

## 11.1. Continuidad de las Actividades y Análisis de los Impactos

Con el fin de establecer un Plan de Continuidad de las Actividades de la Organización, se deben contemplar los siguientes puntos:

### 11.1.1. Identificación de amenazas

Se identificarán los eventos (amenazas) que puedan ocasionar interrupciones en los procesos de las actividades de Inmemorian. Las principales amenazas relevadas son:

| Amenaza | Impacto estimado | Probabilidad |
|---|---|---|
| **Pérdida total de datos de los ERP** (sin respaldos existentes) | Crítico — pérdida de pedidos, clientes, proveedores, inventario y finanzas | Alta |
| **Indisponibilidad del proveedor externo de sistemas** | Crítico — sin acceso a ERP, correo ni portales web | Media |
| **Corte de Internet** en Parque Industrial, Local Inmemorian o Local La Roca | Alto — imposibilidad de operar con ERP y portales en la sede afectada | Media |
| **Ataque de ransomware o malware** (sin firewall, sin filtros anti-phishing, sin antivirus centralizado) | Crítico — cifrado o pérdida de datos | Media-Alta |
| **Falla de equipamiento** (mayoría de equipos sin soporte u obsoletos) | Alto — pérdida de PC en cualquier locación | Media |
| **Falla de energía eléctrica prolongada** | Crítico — afecta las tres locaciones | Baja-Media |
| **Corrupción o pérdida de datos de clientes** (nombres, fechas, datos bancarios) | Crítico legal — incumplimiento Ley N.º 25.326 | Media |
| **Pérdida o robo de móviles corporativos** (2 dispositivos con acceso a WhatsApp comercial) | Medio — interrupción de comunicación con clientes | Media |
| **Daño físico a instalaciones** (incendio, inundación, robo) | Alto — pérdida de equipos e información local | Baja |

### 11.1.2. Evaluación de riesgos e impacto

La evaluación de riesgos determinará el impacto de las interrupciones identificadas, tanto en términos de magnitud de daño como del período de recuperación. Dicha evaluación debe identificar:

- **Recursos críticos**: los 2 ERP, portales web, correo electrónico, conectividad a Internet en cada sede, equipos de producción y venta, datos de clientes y registros financieros.
- **Impactos por interrupción**: imposibilidad de registrar pedidos, retrasos en producción y entregas, pérdida de comunicación con clientes, incumplimiento de obligaciones legales de protección de datos.
- **Tiempos de interrupción aceptables**:

| Escenario | Tiempo máximo de interrupción aceptable | Prioridad de recuperación |
|---|---|---|
| Indisponibilidad de uno o ambos ERP | 6 horas | Crítica |
| Corte de Internet en una sede | 4 horas | Alta |
| Indisponibilidad del proveedor externo de sistemas | 24 horas | Crítica |
| Ataque de ransomware | 8 horas (con respaldo offline disponible) | Crítica máxima |
| Corrupción de datos de clientes | 1 hora | Crítica legal |

- **Prioridades de recuperación**: (1) datos de clientes y registros financieros; (2) ERP de ventas y producción; (3) conectividad e Internet; (4) correo electrónico y portales web; (5) redes sociales comerciales.

### 11.1.3. Controles preventivos

Se identificarán e implementarán controles preventivos, priorizando las brechas más críticas detectadas en el relevamiento:

**Acciones urgentes (situación actual crítica):**

1. **Respaldos de información** — actualmente inexistentes:
   - Respaldos automáticos diarios de ambos ERP.
   - Respaldos diarios de correo electrónico.
   - Respaldos semanales de portales web.
   - Copias offline o en nube almacenadas fuera del Parque Industrial, con cifrado para proteger datos de clientes.
   - Pruebas de restauración documentadas, como mínimo trimestrales.

2. **Protección perimetral y endpoint** — actualmente inexistente:
   - Firewall perimetral en cada locación.
   - Filtros anti-spam y anti-phishing en correo electrónico.
   - Antivirus o anti-malware en las 6 estaciones de trabajo, 2 laptops personales autorizadas y equipos de dueños.

**Acciones de mediano plazo:**

3. **Infraestructura resiliente**:
   - UPS o estabilizadores en Parque Industrial (producción), Local Inmemorian y Local La Roca.
   - Evaluación de conexión redundante a Internet en al menos Parque Industrial y Local Inmemorian.

4. **Formalización de dependencias externas**:
   - Acuerdos SLA con el proveedor externo de sistemas (tiempo de respuesta, disponibilidad de respaldos, contacto de emergencia).
   - Documentación de accesos, credenciales y configuraciones críticas para no depender exclusivamente del proveedor.

5. **Segmentación y conectividad segura**:
   - Segmentación de redes por locación y área funcional.
   - VPN para conectividad remota segura del personal administrativo en modalidad híbrida.

Esta actividad será llevada a cabo con la activa participación de los **dueños**, los **propietarios de la información** (gerentes de área) y el **proveedor externo de sistemas**.

---

## 11.2. Elaboración e Implementación de los Planes de Continuidad

Los **dueños**, los **propietarios de la información** y el **proveedor externo de sistemas** elaborarán los planes de contingencia necesarios para garantizar la continuidad de las actividades de la Organización.

El proceso de planificación de la continuidad de las actividades considerará los siguientes puntos:

### 11.2.1. Escenarios de contingencia y acciones correctivas

**Escenario A — Indisponibilidad de uno o ambos ERP**

*Responsables: dueños, proveedor externo de sistemas.*

Acciones inmediatas:
- El proveedor externo de sistemas intentará restauración desde respaldo (objetivo: 30 minutos).
- Si la restauración no es posible, se activa el plan de operación manual.

Plan B — Operación manual:
- Gerencias de Ventas registran pedidos en formularios en papel (modelos estandarizados por área).
- Gerencia de Producción registra órdenes de producción e inventario en papel.
- Gerencia de Logística registra entregas en papel.
- Finanzas registra transacciones en planilla local autorizada.
- Una vez restaurado el ERP, se ingresa manualmente la información acumulada, verificando integridad.

Tiempo máximo de restablecimiento: **6 horas**.

**Escenario B — Corte de Internet en una locación**

*Responsable: gerente local / dueño presente en la sede.*

Acciones inmediatas:
- Verificar conexión y reiniciar módem/router.
- Contactar al proveedor de Internet con el número de cliente documentado.
- Activar modo offline del ERP si está disponible; de lo contrario, activar plan manual.

Plan B — Operación manual por sede:
- **Parque Industrial**: producción continúa registrando órdenes en papel.
- **Local Inmemorian**: ventas de placas registra pedidos en papel; comunicación con clientes vía teléfono/WhatsApp desde móvil corporativo.
- **Local La Roca**: ventas de mesadas registra pedidos en papel; comunicación vía teléfono/WhatsApp.
- Las demás sedes continúan operaciones normales.

Tiempo máximo de restablecimiento: **4 horas** (según proveedor de Internet).

**Escenario C — Indisponibilidad del proveedor externo de sistemas**

*Responsable: dueños.*

Acciones inmediatas:
- Contactar al proveedor por teléfono y WhatsApp.
- Si no responde en 30 minutos, escalar a contacto secundario documentado.
- Activar plan de operación parcial manual.

Plan B:
- ERP y correo electrónico: no disponibles.
- Pedidos y operaciones: registro manual en papel.
- Comunicación interna: WhatsApp.
- Comunicación con clientes: teléfono/WhatsApp.
- Si existen respaldos en almacenamiento externo, intentar acceso según guía documentada.

Tiempo máximo de restablecimiento: **24 horas**.

**Escenario D — Ataque de ransomware o malware**

*Responsables: dueños, proveedor externo de sistemas.*

Acciones inmediatas:
- Desconectar todos los equipos de Internet de inmediato.
- No pagar rescate.
- Contactar al proveedor externo de sistemas y a las autoridades competentes (Policía Cibernética).
- Restaurar desde respaldo offline anterior al ataque, si existe.

Plan B:
- Operación manual hasta completar la recuperación.
- Si no hay respaldo disponible, evaluar alcance de la pérdida de datos y activar procedimientos legales de notificación a clientes afectados (Ley N.º 25.326).

**Escenario E — Falla de energía eléctrica**

*Responsables: gerentes locales.*

Acciones inmediatas:
- Verificar si la falla es local o generalizada.
- Si hay UPS, el sistema continúa funcionando el tiempo de autonomía disponible; guardar trabajo en curso.
- Apagar equipamiento ordenadamente si la falla se prolonga.

Plan B:
- Operación manual en papel mientras dure la interrupción.
- Si la falla supera 2 horas, evaluar cierre temporal de la sede afectada.

### 11.2.2. Procedimientos de emergencia y dependencias externas

Se implementarán procedimientos de emergencia para permitir la recuperación y restablecimiento en los plazos requeridos. Se dedicará especial atención a:

- **Dependencias del proveedor externo de sistemas**: formalizar SLA con tiempos de respuesta, obligación de mantener respaldos y procedimientos de recuperación documentados.
- **Dependencias del proveedor externo de finanzas e importaciones**: definir procedimientos alternativos ante indisponibilidad de sus servicios.
- **Proveedores de Internet** en cada locación: mantener número de cliente y contacto de soporte en la documentación física de cada sede.
- **Contratos vigentes**: revisar cláusulas de continuidad y confidencialidad con todos los terceros que accedan a información de la organización.

### 11.2.3. Procedimientos operativos alternativos documentados

Cada gerencia mantendrá en **formato físico** (accesible sin electricidad ni Internet) los siguientes documentos:

- Formularios de pedido manual con campos mínimos: nombre del cliente, fecha, descripción del producto, fecha de entrega, datos de contacto y, cuando corresponda, datos bancarios.
- Libro de registro de pedidos con numeración secuencial.
- Formularios de orden de producción, envío y registro financiero manual.
- Procedimiento de ingreso posterior al ERP una vez restaurado el sistema.

Stock mínimo recomendado: **100 formularios en blanco por tipo** en cada locación.

### 11.2.4. Documentación física de emergencia en cada sede

Cada locación dispondrá de forma impresa y accesible:

1. Plan de Continuidad resumido.
2. Formularios de operación manual en blanco.
3. Lista de contactos de emergencia: proveedor de sistemas, proveedor de Internet, proveedor de energía, dueños, gerentes de otras sedes, autoridades (Policía, Bomberos, Policía Cibernética).
4. Guía de restauración de respaldos (una vez implementado el esquema de respaldos).

### 11.2.5. Escalamiento y comunicación ante incidentes

| Fase | Plazo | Acción |
|---|---|---|
| **Fase 1** | 0–15 min | Gerente local o dueño presente intenta resolver el incidente |
| **Fase 2** | 15–30 min | Contacto al proveedor de sistemas o servicio externo correspondiente |
| **Fase 3** | 30 min–2 h | Dueños declaran Situación de Contingencia y activan plan manual |
| **Fase 4** | >2 h | Evaluación de cierre temporal de operaciones si el impacto es crítico |

Comunicación interna: WhatsApp a todo el personal.
Comunicación con clientes (si corresponde): teléfono o WhatsApp.
Registro del incidente: fecha, hora, descripción, causa, acciones tomadas, duración y datos afectados.

### 11.2.6. Prueba y actualización del plan

- **Frecuencia mínima**: revisión semestral del plan; prueba real de restauración de respaldos trimestral.
- **Tipo de ejercicios**: simulacro de corte de Internet, simulacro de indisponibilidad de ERP, prueba de restauración de respaldos.
- **Participación**: al menos un integrante de cada área crítica en cada ejercicio.
- **Documentación**: cada ejercicio quedará registrado con fecha, participantes, resultado e incidencias detectadas.
- **Actualización**: el plan se revisará ante cambios significativos en infraestructura, personal, proveedores o sistemas, y como mínimo una vez al año.

### 11.2.7. Objetivos de disponibilidad por servicio

| Servicio | Disponibilidad objetivo | Impacto si no disponible | Tiempo máximo de recuperación |
|---|---|---|---|
| ERP (ventas y producción) | 99,5 % | Alto — pedidos y órdenes no registrados | 6 horas |
| Correo electrónico | 99 % | Medio — alternativa WhatsApp | 4 horas |
| Internet — Parque Industrial | 99 % | Alto — producción detenida | 4 horas |
| Internet — Local Inmemorian | 99 % | Alto — ventas detenidas | 4 horas |
| Internet — Local La Roca | 99 % | Alto — ventas detenidas | 4 horas |
| Respaldos | 100 % (diarios) | Crítico — riesgo de pérdida total de datos | N/A (preventivo) |

---

# 12. Cumplimiento

El diseño, operación, uso y administración de los sistemas de información están regulados por disposiciones legales y contractuales. Inmemorian procesa información personal y bancaria de clientes —incluyendo nombres, fechas, textos conmemorativos, imágenes y datos de pago— lo que genera obligaciones específicas bajo la legislación argentina vigente.

## Objetivo

- Cumplir con las disposiciones normativas y contractuales a fin de evitar sanciones administrativas y legales a la Organización.
- Garantizar que los sistemas cumplan con la política, normas y procedimientos de seguridad de la Organización.
- Proteger los derechos de los clientes cuya información es procesada, en línea con el objetivo de la dirección de avanzar hacia una futura certificación **ISO/IEC 27001**.

## Alcance

Esta política se aplica a:

- **Todo el personal** de la organización (8 empleados), incluido el personal administrativo en modalidad híbrida.
- Los **proveedores externos** de Sistemas, Finanzas e Importaciones, en la medida en que accedan a información o sistemas de la organización.
- Los **sistemas de información**: 2 ERP, portales web, correo electrónico, cuentas de WhatsApp, Instagram y Facebook, estaciones de trabajo, laptops personales autorizadas y móviles corporativos.
- Las **normas, procedimientos, documentación y plataformas técnicas** de la Organización.
- Las **auditorías** efectuadas sobre los sistemas y procesos de seguridad.

## Responsabilidad

Dado que Inmemorian no cuenta con áreas formales de Seguridad de la Información, Sistemas, Legales ni Auditoría Interna, las funciones se asignan provisionalmente de la siguiente manera:

### Dueños de la organización

- Verificar periódicamente que los sistemas de información cumplan la política, normas y procedimientos de seguridad establecidos.
- Garantizar el cumplimiento normativo general de la organización.
- Aprobar las medidas correctivas ante incumplimientos detectados.

### Proveedor externo de sistemas

En su carácter de responsable técnico de Sistemas:

- Verificar que solo se instalen productos con licencia y software autorizado.
- Implementar los controles técnicos requeridos para el cumplimiento de la Ley N.º 25.326 en los sistemas bajo su administración.
- Informar a los dueños sobre vulnerabilidades, incumplimientos técnicos o incidentes de seguridad detectados.

### Gerentes de área

- Velar por la correcta implementación y cumplimiento de las normas y procedimientos de seguridad dentro de su área de responsabilidad.
- Reportar a los dueños toda anomalía o incumplimiento detectado.
- Asegurar que su equipo conozca y respete las obligaciones legales aplicables a la información que manejan —en particular, la prohibición de compartir datos de clientes por canales informales no autorizados (WhatsApp personal, redes sociales).

### Todo el personal

- Comprender, dar a conocer y cumplir la presente Política.
- Conocer el alcance preciso del uso adecuado de los recursos informáticos provistos por la organización.

---

## 12.1. Cumplimiento de Requisitos Legales

### 12.1.1. Protección de Datos Personales

Inmemorian procesa datos personales de clientes —nombres, fechas, direcciones, datos de contacto, textos e imágenes conmemorativas— y, en algunos casos, datos sensibles vinculados a difuntos. Asimismo, maneja **datos bancarios compartidos con clientes** para procesar pagos.

La organización debe cumplir con la **Ley N.º 25.326 de Protección de Datos Personales**, que establece normas para la recolección, almacenamiento, uso y transmisión de datos personales. Entre las obligaciones aplicables:

- Obtener **consentimiento informado** de los clientes para el tratamiento de sus datos personales.
- Informar a los clientes sobre qué datos se recopilan, para qué se utilizan, con quién se comparten y cómo pueden acceder, corregir o solicitar eliminación de sus datos.
- Implementar **medidas de seguridad técnicas y organizativas** para proteger los datos contra acceso no autorizado, modificación, pérdida o destrucción —brecha crítica dado que actualmente no existen respaldos, controles de acceso formales ni cifrado documentado.
- Limitar el acceso a los datos personales únicamente al personal que lo necesite para sus funciones; evitar el uso de cuentas compartidas para acceder a información de clientes.
- **No exponer datos de clientes** —en particular datos bancarios— a través de canales informales como WhatsApp personal, Instagram o Facebook, salvo que exista una política expresa que autorice y controle dicho uso.
- Reportar violaciones de datos a la **Dirección Nacional de Protección de Datos Personales** en caso de acceso no autorizado o incidentes graves.
- Establecer **cláusulas de confidencialidad** en contratos con proveedores externos (Sistemas, Finanzas, Importaciones) que accedan a datos personales de clientes.

### 12.1.2. Datos Bancarios y Transacciones Financieras

Cuando Inmemorian procesa datos bancarios de clientes, debe aplicar controles adicionales:

- Los datos bancarios se consideran información **altamente sensible**. Deben protegerse mediante cifrado en tránsito y en reposo, una vez implementados los controles técnicos correspondientes.
- No almacenar números de tarjeta de crédito completos en bases de datos propias; utilizar servicios de terceros certificados para el procesamiento de pagos.
- Mantener registro de quién accede a información bancaria y cuándo, una vez implementado el esquema de auditoría de accesos (punto 9).
- Verificar que los proveedores externos que manejen datos bancarios cumplan estándares de seguridad reconocidos.

### 12.1.3. Derecho de Propiedad Intelectual del Software

El software es considerado una obra intelectual que goza de la protección de la **Ley N.º 11.723 de Propiedad Intelectual**.

Los productos de software se suministran normalmente bajo acuerdos de licencia que suelen limitar el uso al equipamiento específico y restringir la copia a la creación de copias de resguardo solamente.

Los **dueños**, con la asistencia del **proveedor externo de sistemas**, verificarán que solo se instalen productos con licencia y software autorizado. El relevamiento evidenció que **no existe control de licenciamiento** y que los usuarios pueden instalar software libremente —situación que deberá regularizarse mediante un inventario de software y licencias a cargo del proveedor externo de sistemas, con revisión semestral.

### 12.1.4. Prevención del Uso Inadecuado de los Recursos de Procesamiento de Información

Los recursos de procesamiento de información de Inmemorian —6 estaciones de trabajo, 2 laptops personales autorizadas, 2 móviles corporativos, conectividad a Internet y acceso a ERP, portales web y correo— se suministran con un propósito determinado vinculado a las actividades comerciales, productivas y administrativas de la organización.

Toda utilización de estos recursos con propósitos no autorizados o ajenos al destino por el cual fueron provistos debe considerarse **uso indebido**, incluyendo:

- Instalación de software no autorizado (situación actual permitida sin restricción).
- Uso de equipos corporativos o móviles corporativos para actividades personales que expongan la organización a riesgos de seguridad.
- Compartir credenciales de acceso, especialmente en Producción y Ventas donde existen cuentas compartidas.
- Utilizar recursos informáticos para acceder a contenido que pueda comprometer la seguridad de los sistemas (sitios maliciosos, descargas no autorizadas).
- Cargar datos personales de clientes en herramientas de inteligencia artificial u otros servicios en la nube no autorizados por la dirección.

Todos los empleados deben conocer el alcance preciso del uso adecuado de los recursos informáticos y respetarlo. Los gerentes de área son responsables de comunicar estas pautas a su personal.

### 12.1.5. Cumplimiento de Obligaciones Contractuales

Inmemorian mantiene relaciones contractuales con terceros —proveedor externo de sistemas, proveedores de finanzas e importaciones— que acceden a información de la organización.

Los dueños verificarán que todos los contratos incluyan cláusulas que obliguen a los terceros a:

- Cumplir con la Política de Seguridad de la Información y la legislación vigente en materia de protección de datos.
- Mantener la confidencialidad de la información de clientes y del negocio.
- Notificar incidentes de seguridad dentro de plazos definidos.
- Permitir auditorías de cumplimiento por parte de la organización.

Se realizarán revisiones periódicas de estos contratos, como mínimo una vez al año.

---

## 12.2. Cumplimiento de la Política de Seguridad

Cada sector —Ventas, Compras, Importaciones, Logística, Finanzas, Producción y Sistemas— velará por la correcta implementación y cumplimiento de las normas y procedimientos de seguridad establecidos, dentro de su área de responsabilidad, dando a conocer y reportando a los **dueños** (en calidad de responsables provisionales de Seguridad de la Información) toda anomalía o incumplimiento que detecte.

La dirección de la organización debe demostrar un compromiso activo con la seguridad de la información, asignando recursos presupuestarios y humanos suficientes para implementar los controles necesarios —priorizando la implementación de respaldos, controles de acceso y protección perimetral identificados como urgentes en el relevamiento.

### 12.2.1. Revisiones periódicas de cumplimiento

Los dueños —o un auditor externo en caso de no existir capacidad interna— realizarán revisiones periódicas, como mínimo **anuales**, sobre el cumplimiento de la presente política. Las revisiones incluirán:

- Estado de respaldos y pruebas de restauración.
- Uso de contraseñas y persistencia de cuentas compartidas.
- Manejo de datos de clientes en canales digitales (ERP, correo, WhatsApp, redes sociales).
- Inventario de software y cumplimiento de licencias.
- Estado de actualizaciones de sistemas operativos y antivirus.
- Cumplimiento de procedimientos de continuidad y simulacros realizados.
- Cláusulas de seguridad en contratos con terceros.

Los resultados de cada revisión serán documentados, comunicados a los gerentes de área y servirán de base para el plan de acción correctivo.

### 12.2.2. Sanciones por incumplimiento

Los empleados que incumplan la presente Política de Seguridad de la Información podrán estar sujetos a medidas disciplinarias proporcionales al incumplimiento, que pueden incluir desde capacitación adicional hasta la terminación de la relación laboral, según lo establezcan las políticas de personal y la legislación laboral vigente.

Asimismo, Inmemorian podrá estar sujeta a **sanciones legales y administrativas** en caso de violación de leyes de protección de datos personales, uso de software sin licencia o incumplimiento de obligaciones contractuales con clientes y proveedores.

### 12.2.3. Orientación hacia ISO/IEC 27001

La dirección ha expresado el objetivo de avanzar hacia una futura certificación **ISO/IEC 27001**. El presente plan constituye el punto de partida para ese proceso. Como pasos concretos vinculados al cumplimiento:

- Designar formalmente un **Responsable de Seguridad de la Información** dentro de la organización.
- Implementar un **registro de incidentes de seguridad** (actualmente inexistente).
- Establecer **revisiones anuales** del plan y sus controles.
- Documentar formalmente todos los procesos y procedimientos de seguridad implementados.
- Completar la implementación de los controles críticos identificados en el relevamiento: respaldos, control de accesos, protección perimetral, gestión de licencias y planes de continuidad.

---

*Documento elaborado en el marco del Plan de Seguridad de la Información de Inmemorian. Complementa y debe ser leído en conjunto con los puntos 1 (Alcance), 2 (Seguridad de la Información), 3 (Política de Seguridad de la Información), 4 (Seguridad Frente al Acceso por Parte de Terceros), 5 (Clasificación y Control de Activos), 6 (Seguridad del Personal), 7 (Seguridad Física y Ambiental), 8 (Gestión de Comunicaciones y Operaciones), 9 (Control de Accesos) y 10 (Desarrollo y Mantenimiento de Sistemas) del mismo plan.*
