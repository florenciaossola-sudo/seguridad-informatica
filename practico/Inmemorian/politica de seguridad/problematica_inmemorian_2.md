# Análisis de Riesgos y Situación Actual de Seguridad de la Información

## Introducción

Como resultado del relevamiento realizado sobre la infraestructura tecnológica, los procesos operativos y las prácticas de gestión de la información de **Inmemorian**, desde nuestra consultora especializada en seguridad informática y ciberseguridad hemos identificado una serie de debilidades que representan riesgos significativos para la continuidad operativa del negocio, la protección de los datos y el cumplimiento de las obligaciones legales vigentes.

El relevamiento abarcó las tres locaciones operativas de la empresa (**Parque Industrial, Local Inmemorian y Local La Roca**), su infraestructura tecnológica, sistemas ERP, redes de comunicación y procedimientos de gestión de información. Asimismo, se entrevistó a los responsables de las distintas áreas y se analizó la relación con proveedores externos de tecnología.

Se constató que la organización posee una dependencia tecnológica aproximada del **75 %** para la ejecución de sus procesos críticos, incluyendo ventas, producción, logística, finanzas e importaciones. Este nivel de dependencia incrementa significativamente el impacto potencial de cualquier incidente de seguridad informática.

---

# Problemáticas Críticas – Acción Inmediata Requerida

## Ausencia Total de Respaldos (Backups)

La principal problemática detectada es la ausencia total de un sistema de respaldos de la información en las tres locaciones de la empresa.

Actualmente, la organización no dispone de mecanismos que permitan recuperar datos ante una falla de hardware, errores humanos, ataques de ransomware o cualquier otro incidente que afecte la disponibilidad de la información. Esta situación representa el riesgo más crítico identificado, ya que una pérdida de información podría provocar la interrupción total de las operaciones sin posibilidad de recuperación.

---

## Compartición de Datos Bancarios por Canales Informales

Se observó que información sensible de clientes, incluyendo datos bancarios, es compartida mediante aplicaciones y redes sociales como WhatsApp, Instagram y Facebook.

Esta práctica expone a la organización a riesgos de filtración de información, accesos no autorizados y posibles incumplimientos de la Ley N.° 25.326 de Protección de Datos Personales. Además, representa un riesgo reputacional significativo ante posibles incidentes de seguridad.

---

## Inexistencia de Firewall Perimetral

Ninguna de las sedes de Inmemorian dispone de dispositivos de protección perimetral que permitan controlar el tráfico entre la red interna e Internet.

La ausencia de un firewall incrementa considerablemente la exposición frente a ataques externos, accesos no autorizados y propagación de amenazas informáticas dentro de la organización.

---

## Dependencia del Proveedor Externo sin Acuerdos Formales

Se detectó una fuerte dependencia del proveedor externo responsable de la administración de la infraestructura tecnológica y los sistemas ERP.

Este proveedor posee acceso administrativo total sobre activos críticos de la organización sin que existan acuerdos formales de nivel de servicio (SLA), cláusulas de confidencialidad ni procedimientos documentados de gestión de incidentes. Esta situación genera riesgos operativos, contractuales y de seguridad de la información.

---

# Problemáticas de Alta Severidad – Resolución a Corto Plazo

## Utilización de Cuentas Compartidas

Se identificó el uso de cuentas compartidas principalmente en las áreas de producción y ventas.

Esta práctica impide determinar responsabilidades individuales, dificulta la trazabilidad de acciones dentro de los sistemas y compromete los procesos de auditoría e investigación de incidentes. Además, incrementa el impacto potencial ante el compromiso de credenciales.

---

## Privilegios de Administrador en Todos los Equipos

Se constató que los usuarios operan con privilegios administrativos locales sobre sus estaciones de trabajo.

Esta configuración permite instalar software sin control, modificar configuraciones críticas y ejecutar aplicaciones potencialmente maliciosas, amplificando considerablemente el impacto de ataques de malware o phishing.

---

## Sistemas Operativos Obsoletos

Una parte importante del parque tecnológico utiliza sistemas operativos que ya no reciben soporte ni actualizaciones de seguridad por parte de sus fabricantes.

Esta situación incrementa la exposición frente a vulnerabilidades conocidas y facilita la explotación por parte de atacantes externos.

---

## Ausencia de Filtros Anti-Spam y Anti-Phishing

Los servicios de correo electrónico corporativo carecen de mecanismos específicos para detectar y bloquear correos maliciosos.

El phishing constituye actualmente uno de los principales vectores de ataque utilizados para comprometer credenciales, distribuir malware y ejecutar campañas de ransomware. La ausencia de estas protecciones incrementa considerablemente la exposición al riesgo.

---

# Problemáticas de Severidad Media y Estructural

## Ausencia de Protección Antivirus Homogénea

No existe una solución corporativa de protección endpoint desplegada y administrada de manera uniforme en todos los equipos de la organización.

Esta situación dificulta la detección temprana de amenazas y aumenta la probabilidad de infecciones por malware.

---

## Uso de Dispositivos Personales (BYOD) sin Controles

Se identificó el uso de dispositivos personales para actividades laborales sin políticas de seguridad ni mecanismos de administración centralizada.

La ausencia de controles sobre estos equipos genera riesgos adicionales de fuga de información y acceso no autorizado a recursos corporativos.

---

## Falta de Inventario Formal de Activos

La organización no dispone de un inventario actualizado de hardware, software y activos de información.

Sin este registro resulta imposible administrar adecuadamente los recursos tecnológicos, controlar accesos o planificar renovaciones y actualizaciones.

---

## Ausencia de Gestión de Licencias y Parches

No existen procedimientos formales para controlar licencias de software ni gestionar actualizaciones de seguridad.

Esta situación genera riesgos tanto legales como técnicos asociados al uso de software no autorizado o vulnerable.

---

## Inexistencia de un Procedimiento de Gestión de Incidentes

La organización carece de protocolos documentados para detectar, reportar, contener y resolver incidentes de seguridad.

Las decisiones se toman de manera reactiva, lo que puede generar demoras, errores operativos y pérdida de evidencia durante situaciones críticas.

---

## Ausencia de un Responsable Formal de Seguridad

Actualmente no existe una persona o área designada para coordinar las actividades relacionadas con la seguridad de la información.

La falta de liderazgo y seguimiento dificulta la implementación efectiva de controles y la continuidad de las mejoras propuestas.

---

## Falta de Capacitación en Ciberseguridad

No se desarrollan actividades periódicas de capacitación y concientización para los empleados.

Considerando que el factor humano constituye uno de los principales vectores de riesgo, esta debilidad incrementa significativamente la probabilidad de incidentes relacionados con phishing, ingeniería social y manejo inadecuado de la información.

---

## Redes sin Segmentación

Las distintas sedes y áreas operan sobre redes planas sin segmentación lógica.

Esta configuración facilita la propagación de amenazas y permite que un incidente originado en un área afecte a toda la infraestructura tecnológica de la organización.

---

# Conclusiones

El análisis realizado evidencia que Inmemorian presenta un conjunto de vulnerabilidades técnicas, organizacionales y procedimentales que requieren atención prioritaria.

Se recomienda iniciar de forma inmediata acciones orientadas a:

* Implementar un esquema formal de respaldos y recuperación de información.
* Proteger adecuadamente los datos sensibles de clientes.
* Incorporar firewalls perimetrales en las tres sedes.
* Formalizar la relación contractual con proveedores tecnológicos críticos.
* Eliminar el uso de cuentas compartidas.
* Actualizar sistemas operativos obsoletos.
* Implementar protección antivirus y filtros anti-phishing.
* Desarrollar políticas de seguridad para dispositivos personales.
* Formalizar la gestión de activos tecnológicos.
* Designar un responsable de seguridad de la información.
* Implementar programas permanentes de capacitación y concientización.

La aplicación progresiva de estas medidas permitirá reducir significativamente la exposición actual al riesgo y establecer una base sólida para la futura adopción de buenas prácticas alineadas con la norma **ISO/IEC 27001**, objetivo estratégico manifestado por la dirección de Inmemorian.
