# 7. Medidas Técnicas, Procedimientos y Plan de Acción para la Implementación de la Política de Seguridad de la Información

## 7.1 Objetivo

El presente capítulo tiene por objetivo definir las medidas técnicas, organizativas y procedimentales necesarias para garantizar la efectiva implementación y cumplimiento de la Política de Seguridad de la Información de Inmemorian.

Las medidas aquí definidas buscan reducir los riesgos identificados durante el relevamiento de la situación actual, fortalecer la protección de los activos de información y establecer una hoja de ruta de implementación alineada con las buenas prácticas de seguridad y con el objetivo estratégico de avanzar hacia una futura certificación ISO/IEC 27001.

---

# 7.2 Medidas Técnicas Recomendadas

## 7.2.1 Gestión de Identidades y Control de Accesos

### Situación Actual

* Existen cuentas compartidas en las áreas de Producción y Ventas.
* Los usuarios poseen privilegios administrativos en sus estaciones de trabajo.
* No se utiliza autenticación multifactor.
* Las contraseñas no poseen vencimiento ni controles de complejidad formalizados.

### Medidas a Implementar

#### Software

* Implementar autenticación multifactor (MFA) para correo electrónico, ERP y sistemas críticos.
* Implementar un gestor corporativo de contraseñas.
* Crear cuentas individuales para todos los usuarios.
* Aplicar políticas de complejidad y vencimiento de contraseñas.

#### Procedimientos

* Procedimiento formal de alta, modificación y baja de usuarios.
* Revisión trimestral de permisos y privilegios.
* Eliminación progresiva de todas las cuentas compartidas.

#### Hardware

* Evaluar el uso de llaves de autenticación FIDO2 para usuarios privilegiados.

---

## 7.2.2 Protección de Infraestructura y Redes

### Situación Actual

* No existe firewall perimetral.
* Las redes funcionan mediante configuraciones ad-hoc.
* No existe segmentación de red.
* No se realiza monitoreo de tráfico.

### Medidas a Implementar

#### Hardware

Instalar un firewall de nueva generación (NGFW) en cada sede.

Alternativas recomendadas:

* Fortinet FortiGate 40F
* Sophos XGS
* Appliance dedicado con pfSense

#### Software

* Activación de IDS/IPS.
* Filtrado web y de aplicaciones.
* Implementación de VPN para futuras conexiones remotas seguras.

#### Procedimientos

* Gestión formal de cambios de red.
* Auditoría semestral de configuraciones.

### Segmentación Recomendada

#### VLAN Administración

Dueños y personal administrativo.

#### VLAN Ventas

Equipos de atención comercial.

#### VLAN Producción

Equipos utilizados en planta.

#### VLAN Invitados

Dispositivos externos y visitantes.

---

## 7.2.3 Gestión de Respaldos

### Situación Actual

No existen respaldos de la información.

### Medidas a Implementar

#### Hardware

* Servidor NAS dedicado.
* Discos externos para almacenamiento offline.

#### Software

* Veeam Backup.
* Synology Active Backup.
* Cobian Backup.

### Estrategia de Respaldo

Implementar la regla 3-2-1:

* Tres copias de la información.
* Dos medios diferentes.
* Una copia offline o fuera del sitio.

### Procedimientos

* Respaldos automáticos diarios.
* Verificación periódica de integridad.
* Pruebas trimestrales de restauración.

---

## 7.2.4 Protección contra Malware

### Situación Actual

No existe una solución corporativa homogénea de protección antimalware.

### Medidas a Implementar

#### Software

* Microsoft Defender for Business.
* Bitdefender GravityZone.
* ESET Protect.

#### Procedimientos

* Escaneos automáticos programados.
* Aislamiento inmediato de equipos comprometidos.
* Reporte obligatorio de incidentes relacionados con malware.

---

## 7.2.5 Gestión de Equipos y Dispositivos Personales

### Situación Actual

Existen computadoras personales utilizadas para tareas laborales sin controles de seguridad definidos.

### Medidas a Implementar

#### Software

* Cifrado de disco mediante BitLocker.
* Antivirus corporativo obligatorio.
* Gestión centralizada mediante Microsoft Intune o solución equivalente.

#### Procedimientos

Implementar una Política BYOD que establezca:

* Antivirus obligatorio.
* Sistema operativo actualizado.
* Cifrado del dispositivo.
* Bloqueo automático de pantalla.
* Restricciones de acceso a sistemas críticos.

### Objetivo a Mediano Plazo

Reemplazar progresivamente los dispositivos personales por equipos corporativos administrados.

---

## 7.2.6 Gestión de Actualizaciones

### Situación Actual

La mayoría de los equipos opera con sistemas obsoletos o sin actualizaciones periódicas.

### Medidas a Implementar

#### Software

* Windows Update for Business.
* WSUS para administración centralizada.

#### Procedimientos

* Actualizaciones críticas dentro de los 15 días de su liberación.
* Ciclo mensual de actualización de seguridad.
* Inventario de versiones instaladas.

---

## 7.2.7 Seguridad del Correo Electrónico

### Situación Actual

No existen filtros antispam ni antiphishing.

### Medidas a Implementar

#### Software

* Microsoft 365 Business Premium o equivalente.
* Google Workspace Business.

#### Controles

* SPF.
* DKIM.
* DMARC.
* Antispam.
* Antiphishing.

#### Procedimientos

* Capacitación periódica sobre phishing.
* Simulaciones de ataques de ingeniería social.

---

## 7.2.8 Monitoreo y Registro de Eventos

### Situación Actual

No existen mecanismos de monitoreo centralizado ni registros de auditoría.

### Medidas a Implementar

#### Software

* Wazuh.
* Graylog.
* Microsoft Sentinel.

#### Eventos a Registrar

* Inicios de sesión.
* Cambios de privilegios.
* Accesos de terceros.
* Eventos de firewall.
* Incidentes de seguridad.
* Errores críticos de sistemas.

---

# 7.3 Procedimientos Organizacionales Necesarios

Para asegurar el cumplimiento efectivo de las políticas definidas, deberán desarrollarse e implementarse los siguientes procedimientos formales:

1. Procedimiento de alta, modificación y baja de usuarios.
2. Procedimiento de gestión de contraseñas.
3. Procedimiento de gestión de incidentes de seguridad.
4. Procedimiento de gestión de respaldos y recuperación.
5. Procedimiento de gestión de activos.
6. Procedimiento de gestión de cambios.
7. Procedimiento de gestión de terceros.
8. Procedimiento de uso aceptable de recursos tecnológicos.
9. Procedimiento de gestión de dispositivos personales (BYOD).
10. Procedimiento de clasificación y tratamiento de la información.

---

# 7.4 Recursos Humanos y Gobierno de Seguridad

## Responsable de Seguridad de la Información

La organización deberá designar formalmente un Responsable de Seguridad de la Información.

Sus funciones incluirán:

* Seguimiento del presente plan.
* Gestión de incidentes.
* Coordinación con proveedores.
* Seguimiento de auditorías.
* Control de cumplimiento de políticas.

## Comité de Seguridad

Se recomienda conformar un comité integrado por:

* Dueños.
* Gerentes.
* Responsable de Seguridad.
* Proveedor de Sistemas.

El comité deberá reunirse al menos trimestralmente para revisar riesgos, incidentes y avances del plan.

---

# 7.5 Plan de Acción Priorizado

## Fase 1 – Implementación Crítica (0 a 30 días)

### Prioridad Muy Alta

1. Formalización de SLA y acuerdos de confidencialidad con el proveedor de sistemas.
2. Elaboración del inventario de activos.
3. Implementación de respaldos automáticos.
4. Adquisición de almacenamiento para respaldos.
5. Eliminación de cuentas compartidas.
6. Eliminación de privilegios administrativos innecesarios.
7. Implementación de antivirus corporativo.

### Objetivo

Reducir el riesgo de pérdida total de información y accesos indebidos.

---

## Fase 2 – Fortalecimiento de Controles (30 a 90 días)

### Prioridad Alta

1. Implementación de MFA.
2. Implementación de firewall en las tres sedes.
3. Segmentación de red.
4. Implementación de filtros antispam y antiphishing.
5. Actualización de sistemas operativos obsoletos.
6. Capacitación inicial de todo el personal.

### Objetivo

Fortalecer la protección de infraestructura y credenciales.

---

## Fase 3 – Monitoreo y Gestión (3 a 6 meses)

### Prioridad Media

1. Implementación de monitoreo centralizado.
2. Formalización de la gestión de incidentes.
3. Formalización de la gestión de cambios.
4. Implementación de controles BYOD.
5. Ejecución de pruebas de recuperación de respaldos.

### Objetivo

Mejorar las capacidades de detección, respuesta y recuperación.

---

## Fase 4 – Madurez y Mejora Continua (6 a 12 meses)

### Prioridad Estratégica

1. Auditoría interna de cumplimiento.
2. Revisión de clasificación de información.
3. Revisión integral de riesgos.
4. Renovación de equipos obsoletos restantes.
5. Preparación para auditorías alineadas con ISO/IEC 27001.

### Objetivo

Consolidar el Sistema de Gestión de Seguridad de la Información y preparar a la organización para futuros procesos de certificación.

---

# 7.6 Conclusión

La implementación de las medidas descritas permitirá reducir significativamente los riesgos identificados durante el relevamiento, mejorar la protección de la información crítica de clientes y garantizar la continuidad operativa de la organización.

Se consideran prioritarias la implementación de respaldos, la eliminación de cuentas compartidas, la incorporación de protección perimetral mediante firewalls, la adopción de autenticación multifactor y la formalización de los procedimientos de gestión de usuarios e incidentes, por constituir los controles de mayor impacto para la reducción del riesgo actual de Inmemorian.
