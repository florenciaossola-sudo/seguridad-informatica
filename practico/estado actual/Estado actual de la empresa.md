# Estado actual de la empresa

## Objetivo del relevamiento

Este documento unifica las preguntas de relevamiento necesarias para conocer el estado actual de la PyME y contar con una base completa para elaborar el Plan de Seguridad de la Información.

El objetivo es identificar activos críticos, procesos de negocio, riesgos, controles existentes, brechas de seguridad y necesidades de mejora luego del incidente de ransomware sufrido por la organización.

## Contexto inicial

| Característica | Detalle conocido / a completar |
| --- | --- |
| Tipo de empresa | PyME industrial |
| Ubicación | Casa central en Salta |
| Operaciones | Ventas y distribución nacional; exportaciones a Brasil y Uruguay |
| Infraestructura | 100% on-premise |
| Modalidad de trabajo | Presencial y teletrabajo parcial |
| Incidente reciente | Ataque de ransomware con días de inactividad y pérdidas económicas importantes |

## Debilidades identificadas inicialmente

Del relevamiento preliminar surgen las siguientes debilidades:

- Inexistencia de un área formal de Seguridad de la Información.
- Ausencia de políticas y normativa interna.
- Infraestructura completamente on-premise.
- Falta de inventario de hardware y software.
- Sistemas operativos desactualizados.
- Elevado nivel de correo spam y phishing.
- Navegación web sin filtros ni controles.
- Inexistencia de un plan de contingencia y recuperación.
- Gran cantidad de empleados bajo modalidad de teletrabajo.
- Falta de controles de acceso y monitoreo centralizado.

Estas vulnerabilidades generaron un entorno propicio para el ataque de ransomware sufrido por la organización.

## Criterio de prioridad

| Prioridad | Descripción |
| --- | --- |
| Crítica | Preguntas directamente vinculadas con el ransomware, la continuidad del negocio o brechas graves de seguridad. |
| Incidente | Preguntas específicas para analizar el ataque sufrido y las lecciones aprendidas. |
| Normal | Preguntas necesarias para completar el diagnóstico general de seguridad. |

## 1. Información general de la empresa

| N° | Pregunta | Prioridad | Respuesta / notas |
| --- | --- | --- | --- |
| 1 | ¿Cuál es la actividad industrial específica de la empresa? | Crítica | |
| 2 | ¿Cuántos empleados posee la organización? | Normal | |
| 3 | ¿Cuántos empleados trabajan de manera remota o híbrida? | Crítica | |
| 4 | ¿Cuántas sedes, depósitos o plantas posee? | Normal | |
| 6 | ¿Cuál es el nivel de dependencia de los sistemas informáticos para operar? | Crítica | |
| 8 | ¿Cuánto tiempo estuvo detenida total o parcialmente la empresa por el incidente? | Incidente | |
| 9 | ¿Qué procesos del negocio fueron más afectados por el ataque? | Incidente | |

## 2. Organización, roles y responsabilidades

| N° | Pregunta | Prioridad | Respuesta / notas |
| --- | --- | --- | --- |
| 10 | ¿Existe un responsable de sistemas o IT designado formalmente? | Crítica | |
| 11 | ¿Cuántas personas componen el área de sistemas o soporte tecnológico? | Normal | |
| 13 | ¿Hay definidos roles y responsabilidades en materia de seguridad? | Normal | |
| 14 | ¿Quién administra servidores, red, usuarios, backups, correo y sistemas críticos? | Crítica | |
| 15 | ¿Los directivos participan en decisiones relacionadas con seguridad de la información? | Normal | |
| 16 | ¿Hay presupuesto asignado o estimado para implementar mejoras de seguridad? | Normal | se supone que contamos con presupuesto ilimitado |
| 18 | ¿Existe interés futuro en certificar o alinearse a normas como ISO 27001? | Normal | |

## 3. Activos, información y sistemas críticos

| N° | Pregunta | Prioridad | Respuesta / notas |
| --- | --- | --- | --- |
| 19 | ¿Qué información maneja la empresa? Clientes, proveedores, empleados, producción, finanzas, exportaciones u otra. | Crítica | |
| 21 | ¿Existe clasificación de la información según confidencialidad, integridad y disponibilidad? | Normal | |
| 22 | ¿Cómo se maneja la documentación sensible, tanto física como digital? | Normal | |
| 23 | ¿Existe inventario actualizado de hardware? | Crítica | NO |
| 24 | ¿Existe inventario actualizado de software? | Crítica | NO |
| 25 | ¿Qué sistemas de negocio utilizan? ERP, CRM, sistemas de producción, facturación, logística u otros. | Crítica | |
| 26 | ¿Los sistemas son propios, desarrollados a medida o provistos por terceros? | Normal | |
| 27 | ¿Utilizan licencias de software legítimas? | Normal | |
| 28 | ¿Hay control sobre el software instalado en los equipos de usuarios? | Normal | |

## 4. Infraestructura tecnológica

| N° | Pregunta | Prioridad | Respuesta / notas |
| --- | --- | --- | --- |
| 29 | ¿Cuántos servidores físicos poseen? | Crítica | |
| 30 | ¿Utilizan virtualización? ¿Qué plataforma? | Normal | |
| 31 | ¿Qué sistemas operativos utilizan en servidores y estaciones de trabajo? | Crítica | |
| 32 | ¿Existen sistemas operativos o aplicaciones desactualizadas o sin soporte? | Crítica | |
| 33 | ¿Existe Active Directory u otro servicio centralizado de identidad? | Crítica | |
| 34 | ¿Qué servicios críticos dependen de infraestructura on-premise? | Crítica | |
| 35 | ¿Cuentan con equipamiento de reemplazo o redundancia para servidores críticos? | Normal | |
| 36 | ¿Contemplan incorporar componentes cloud para almacenamiento, backup, correo u otros servicios? | Normal | |
| 37 | ¿Existe separación entre ambientes de desarrollo, prueba y producción? | Normal | |

## 5. Comunicaciones, red e Internet

| N° | Pregunta | Prioridad | Respuesta / notas |
| --- | --- | --- | --- |
| 38 | ¿Cómo está diseñada la red interna de la empresa? | Crítica | |
| 39 | ¿Existe segmentación entre red administrativa, producción, servidores, WiFi e invitados? | Crítica | |
| 40 | ¿Utilizan firewall perimetral? ¿Cuál? | Crítica | |
| 41 | ¿Quién administra el firewall y con qué frecuencia se revisan sus reglas? | Normal | |
| 42 | ¿Hay filtros o controles para la navegación web? | Crítica | |
| 43 | ¿Existe control o bloqueo de sitios maliciosos o categorías riesgosas? | Normal | |
| 44 | ¿Existe política de uso del correo electrónico? | Incidente | |
| 45 | ¿Se usa algún filtro antispam o antiphishing? | Incidente | |
| 46 | ¿Cuál es el nivel actual de spam, phishing o correos sospechosos recibidos? | Incidente | |
| 47 | ¿Las comunicaciones con Brasil y Uruguay se realizan por canales cifrados como VPN o HTTPS? | Normal | |
| 48 | ¿Existe monitoreo centralizado de red, servidores y eventos de seguridad? | Crítica | |

## 6. Gestión de usuarios y control de accesos

| N° | Pregunta | Prioridad | Respuesta / notas |
| --- | --- | --- | --- |
| 49 | ¿Cómo se crean, modifican y eliminan usuarios? | Crítica | |
| 50 | ¿Existe un proceso formal de baja de accesos cuando un empleado se desvincula? | Crítica | |
| 51 | ¿Cada empleado tiene credenciales únicas o existen cuentas compartidas? | Crítica | |
| 52 | ¿Existen políticas de complejidad, vencimiento y reutilización de contraseñas? | Crítica | |
| 53 | ¿Utilizan autenticación multifactor para correo, VPN, sistemas críticos o administración? | Crítica | |
| 54 | ¿Quiénes poseen privilegios de administrador? | Crítica | |
| 55 | ¿Se aplica el principio de mínimo privilegio? | Crítica | |
| 56 | ¿Se revisan periódicamente los permisos y accesos otorgados? | Normal | |
| 57 | ¿Se generan y revisan logs de acceso a sistemas críticos? | Normal | |
| 58 | ¿Hay control sobre dispositivos removibles como pendrives o discos externos? | Normal | |

## 7. Teletrabajo y acceso remoto

| N° | Pregunta | Prioridad | Respuesta / notas |
| --- | --- | --- | --- |
| 59 | ¿Qué áreas o perfiles trabajan de forma remota? | Crítica | |
| 60 | ¿Cómo acceden los empleados remotos a los sistemas de la empresa? | Crítica | |
| 61 | ¿Existe acceso VPN para teletrabajo? | Crítica | |
| 62 | ¿La VPN tiene MFA, logs y restricciones por usuario o grupo? | Crítica | |
| 63 | ¿Los empleados remotos utilizan equipos corporativos o personales? | Crítica | |
| 64 | ¿Existe una política formal de teletrabajo o BYOD? | Normal | |
| 65 | ¿Se controla que los dispositivos remotos tengan antivirus y sistema operativo actualizado antes de conectarse? | Crítica | |
| 66 | ¿Los empleados pueden descargar, copiar o transferir información sensible a equipos personales? | Crítica | |

## 8. Protección contra malware y seguridad de endpoints

| N° | Pregunta | Prioridad | Respuesta / notas |
| --- | --- | --- | --- |
| 67 | ¿Tienen antivirus corporativo o solución EDR en servidores y estaciones de trabajo? | Crítica | |
| 68 | ¿La solución está actualizada y administrada centralmente? | Crítica | |
| 69 | ¿Se generan alertas ante detecciones de malware? ¿Quién las revisa? | Crítica | |
| 70 | ¿Existe una política de actualización y parchado de sistemas operativos y aplicaciones? | Crítica | |
| 71 | ¿Cómo se controla la instalación de software no autorizado? | Normal | |
| 72 | ¿Qué controles se implementaron luego del ransomware para evitar reinfecciones? | Incidente | |

## 9. Backups, recuperación y continuidad operativa

| N° | Pregunta | Prioridad | Respuesta / notas |
| --- | --- | --- | --- |
| 73 | ¿Poseen backups automáticos? | Crítica | |
| 74 | ¿Existe una política formal de backups? | Crítica | |
| 75 | ¿Con qué frecuencia se realizan los backups? | Crítica | |
| 76 | ¿Dónde se almacenan los backups? | Crítica | |
| 77 | ¿Los backups están aislados de la red principal o protegidos contra ransomware? | Crítica | |
| 78 | ¿Los backups fueron afectados durante el ataque? | Incidente | |
| 79 | ¿Se realizan pruebas periódicas de restauración? | Crítica | |
| 80 | ¿Cuánto tardaron en recuperarse del ataque? | Incidente | |
| 81 | ¿Cuál fue el proceso de recuperación utilizado? | Incidente | |
| 82 | ¿Existe un plan de contingencia, continuidad del negocio o recuperación ante desastres? | Crítica | |
| 83 | ¿Cuánto tiempo máximo puede detenerse la empresa sin operar antes de sufrir pérdidas críticas? | Crítica | |
| 84 | ¿Existe un sitio alternativo o mecanismo de operación manual temporal? | Normal | |
| 85 | ¿Qué procesos críticos no pueden interrumpirse bajo ninguna circunstancia? | Crítica | |

## 10. Gestión de incidentes y lecciones aprendidas

| N° | Pregunta | Prioridad | Respuesta / notas |
| --- | --- | --- | --- |
| 86 | ¿Existe un procedimiento para reportar y gestionar incidentes de seguridad? | Crítica | |
| 87 | ¿Se registran formalmente los incidentes de seguridad? | Normal | |
| 88 | ¿Tras el ransomware se realizó análisis forense para identificar el vector de entrada? | Incidente | |
| 89 | ¿Cuál fue la causa probable del ataque? Correo, credenciales, VPN, vulnerabilidad, acceso de terceros u otra. | Incidente | |
| 90 | ¿Se notificó el incidente a algún organismo, aseguradora, proveedor o autoridad regulatoria? | Incidente | |
| 91 | ¿Tienen contratado soporte externo para incidentes, ciberseguridad o monitoreo? | Normal | |
| 92 | ¿Qué aprendió la organización del ataque ransomware? | Incidente | |
| 93 | ¿Qué controles se implementaron o modificaron después del incidente? | Incidente | |

## 11. Seguridad física y ambiental

| N° | Pregunta | Prioridad | Respuesta / notas |
| --- | --- | --- | --- |
| 94 | ¿Dónde están ubicados los servidores y equipos críticos? | Normal | |
| 95 | ¿Quién puede ingresar al área de servidores? | Crítica | |
| 96 | ¿Existe control de acceso físico mediante llaves, tarjetas, registros o autorizaciones? | Normal | |
| 97 | ¿Hay cámaras, alarmas o registro de visitantes? | Normal | |
| 98 | ¿Poseen UPS, grupo electrógeno o protección contra cortes de energía? | Normal | |
| 99 | ¿Existe política de escritorios y pantallas limpias? | Normal | |
| 100 | ¿Cómo se protege la documentación física sensible? | Normal | |
| 101 | ¿Cómo se da de baja el equipamiento obsoleto? ¿Se destruyen de forma segura los datos almacenados? | Normal | |

## 12. Terceros, proveedores y operaciones externas

| N° | Pregunta | Prioridad | Respuesta / notas |
| --- | --- | --- | --- |
| 102 | ¿Proveedores, técnicos externos o clientes tienen acceso a sistemas o red interna? | Crítica | |
| 103 | ¿Cómo se autorizan, registran y revocan los accesos de terceros? | Crítica | |
| 104 | ¿Los contratos con terceros incluyen cláusulas de confidencialidad y requisitos de seguridad? | Normal | |
| 105 | ¿Las operaciones de exportación a Brasil y Uruguay implican intercambio de información con sistemas externos? | Normal | |
| 106 | ¿Qué datos se comparten con clientes, proveedores, despachantes, bancos u organismos externos? | Normal | |
| 107 | ¿Se evalúa la seguridad de proveedores críticos? | Normal | |

## 13. Capacitación y concientización

| N° | Pregunta | Prioridad | Respuesta / notas |
| --- | --- | --- | --- |
| 108 | ¿El personal recibe capacitación en ciberseguridad? | Crítica | |
| 109 | ¿Existe inducción en seguridad para nuevos empleados? | Normal | |
| 110 | ¿Se capacita específicamente sobre phishing, ransomware, contraseñas y manejo de información sensible? | Crítica | |
| 111 | ¿Se realizan campañas, simulaciones de phishing o comunicaciones internas sobre seguridad? | Normal | |
| 112 | ¿Los empleados conocen cómo reportar correos sospechosos o incidentes? | Crítica | |

## 14. Aspectos legales, normativos y auditoría

| N° | Pregunta | Prioridad | Respuesta / notas |
| --- | --- | --- | --- |
| 113 | ¿La empresa trabaja con datos personales de clientes, empleados o proveedores? | Crítica | |
| 114 | ¿Conocen sus obligaciones bajo la Ley 25.326 de Protección de Datos Personales? | Normal | |
| 115 | ¿Las operaciones con Brasil implican cumplimiento de LGPD u otra normativa aplicable? | Normal | |
| 116 | ¿Exportan o transfieren información al exterior? | Normal | |
| 117 | ¿Poseen contratos de confidencialidad con empleados, proveedores y terceros? | Normal | |
| 118 | ¿Se realizan auditorías internas o externas sobre sistemas, procesos o seguridad? | Normal | |
| 119 | ¿Deben cumplir alguna normativa específica por su industria, clientes o mercados internacionales? | Normal | |

## 15. Resultado esperado del relevamiento

Al completar estas preguntas se debería contar con información suficiente para:

- Identificar los activos críticos de información.
- Determinar amenazas, vulnerabilidades e impactos principales.
- Definir controles prioritarios para reducir el riesgo de nuevos incidentes.
- Establecer políticas y procedimientos básicos de seguridad.
- Diseñar un plan de continuidad y recuperación.
- Priorizar acciones según criticidad, costo, urgencia y capacidad operativa de la empresa.

