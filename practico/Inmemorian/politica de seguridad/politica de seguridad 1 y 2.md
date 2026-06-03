Plan de Seguridad de la Información para Inmemorian

1 alcance
2 seguridad de la informacion
3 politica de seguridad de la informacion
4 seguridad frente al acceso por parte de terceros
5 clasificacion y control de activos
6 seguridad del personal
7 seguridad fisica y ambiental
8 gestion de comunicaciones y operaciones
9 control de accesos
10 desarrollo y mantenimiento de sistemas
11 administracion de la continuidad de las actividades de la organizacion
12 cumplimiento


Primer documento

Desarrollo del Punto 1 — Alcance
1. Alcance

El presente Plan de Seguridad de la Información tiene como finalidad establecer los lineamientos, políticas, procedimientos y controles necesarios para proteger los activos de información de la organización, garantizando adecuados niveles de confidencialidad, integridad y disponibilidad.

El plan se desarrolla para Inmemorian, empresa dedicada al tratamiento y distribución de materiales como mármol, granito y otras piedras naturales y sintéticas. La organización produce y comercializa placas conmemorativas para cementerios, placas para profesionales, placas para monumentos — con grabados, pinturas, imágenes y símbolos religiosos — y mesadas de piedra para baños y cocinas, incluyendo accesorios como bachas.

La necesidad de implementar este plan surge a partir del relevamiento de la situación actual de ciberseguridad, que evidenció importantes brechas de control — ausencia de respaldos, falta de segmentación de red, uso de equipos personales sin políticas, cuentas compartidas y sistemas desactualizados — en un contexto de alta dependencia tecnológica (aproximadamente 75 %) para la operación diaria. Asimismo, la dirección ha expresado el objetivo de avanzar hacia una futura certificación ISO/IEC 27001.

El alcance del presente documento comprende:

Infraestructura tecnológica distribuida en tres locaciones (Parque Industrial, Local Inmemorian y Local La Roca).
Estaciones de trabajo y equipos móviles corporativos.
Equipos personales utilizados para actividades laborales.
Redes internas ad-hoc y conexiones a internet en cada sede.
Sistemas de gestión, aplicaciones corporativas y portales web.
Correo electrónico y canales de comunicación digital (WhatsApp, redes sociales).
Información digital, documentación sensible y datos de clientes.
Usuarios internos y proveedores externos con acceso a los sistemas.
Procesos relacionados con modalidad híbrida del personal administrativo.
Servicios tercerizados vinculados a tecnología, finanzas e importaciones.

Asimismo, este plan será aplicable a:

Dueños y gerentes de la organización.
Empleados permanentes.
Personal administrativo en modalidad presencial o híbrida.
Personal tercerizado y proveedores externos de sistemas, finanzas e importaciones.
Consultores externos.
Toda persona que acceda a información o recursos tecnológicos de la organización.

Quedan comprendidos dentro del alcance todos los procesos críticos vinculados a:

Ventas de placas conmemorativas, placas profesionales y mesadas.
Compras e importaciones de materiales.
Producción y tratamiento de piedras.
Logística y distribución.
Finanzas y administración.
Gestión de sistemas y tecnología.

El presente documento servirá como base para la implementación de controles de seguridad alineados a buenas prácticas internacionales, tomando como referencia estándares como ISO/IEC 27001.

Desarrollo del Punto 2 — Seguridad de la Información
2. Seguridad de la Información

La seguridad de la información constituye un conjunto de políticas, procedimientos, controles y buenas prácticas orientadas a proteger los activos de información de la organización frente a amenazas internas y externas.

La empresa reconoce que la información es un activo estratégico fundamental para el desarrollo de sus actividades comerciales, productivas y administrativas — incluyendo datos de clientes, información financiera, diseños de placas conmemorativas y registros operativos de los ERP — por lo que resulta indispensable implementar mecanismos adecuados para su protección.

El objetivo principal de la seguridad de la información es preservar:

2.1 Confidencialidad

Garantizar que la información únicamente sea accesible por personas, sistemas o procesos autorizados.

Se implementarán medidas orientadas a:

Restringir accesos no autorizados.
Eliminar progresivamente el uso de cuentas compartidas, especialmente en áreas de producción y ventas.
Aplicar controles de autenticación y, en sistemas críticos, autenticación multifactor (MFA).
Definir perfiles y privilegios de usuario acordes a cada rol organizacional.
Proteger información sensible de clientes — incluyendo datos personales y bancarios —, proveedores y empleados.
Implementar políticas de contraseñas seguras con vencimiento periódico.
Regular el uso de equipos personales y canales de comunicación no corporativos (WhatsApp, redes sociales).
2.2 Integridad

Asegurar que la información permanezca completa, exacta y libre de modificaciones no autorizadas.

Para ello se establecerán controles destinados a:

Evitar alteraciones indebidas de datos en los ERP y portales web.
Mantener registros de auditoría y trazabilidad de cambios.
Gestionar adecuadamente cambios en sistemas y configuraciones de red.
Aplicar controles sobre bases de datos y sistemas críticos.
Implementar respaldos periódicos y verificables de la información empresarial.
Restringir la instalación libre de software por parte de los usuarios.
2.3 Disponibilidad

Garantizar que la información y los servicios tecnológicos estén disponibles cuando sean requeridos por la operación.

Se adoptarán medidas como:

Implementación de sistemas de respaldo y recuperación — actualmente inexistentes — con copias offline o inmutables.
Protección contra malware mediante soluciones antivirus homogéneas en todos los equipos.
Monitoreo de infraestructura distribuida en las tres locaciones.
Planes de contingencia y continuidad operativa para procesos críticos (ventas, producción, logística, finanzas).
Mantenimiento preventivo de hardware y software, incluyendo la actualización regular de sistemas operativos obsoletos.
Protección perimetral mediante firewall en cada sede.
2.4 Gestión de Riesgos

La organización implementará un enfoque preventivo basado en la identificación, evaluación y tratamiento de riesgos asociados a la seguridad de la información.

Entre las principales amenazas identificadas se encuentran:

Pérdida total de información por ausencia de respaldos.
Phishing y correo spam — sin filtros anti-spam ni anti-phishing implementados.
Accesos indebidos facilitados por cuentas compartidas y privilegios administrativos en estaciones de trabajo.
Fallas de hardware en equipos sin soporte o con sistemas operativos obsoletos.
Errores humanos y falta de capacitación en ciberseguridad.
Software desactualizado por ausencia de gestión de parches.
Uso de dispositivos personales sin controles (BYOD).
Exposición de datos de clientes a través de canales informales de comunicación.
Interrupciones eléctricas o de conectividad en alguna de las tres locaciones.
Dependencia crítica de proveedores externos de sistemas sin acuerdos formales de nivel de servicio.
2.5 Cultura de Seguridad

La seguridad de la información no será responsabilidad exclusiva del proveedor externo de sistemas, sino de toda la organización — desde los dueños y gerentes hasta el personal operativo.

Por ello se promoverán:

Capacitaciones periódicas en ciberseguridad para todo el personal.
Concientización sobre riesgos del uso de WhatsApp y redes sociales para intercambio de información de clientes.
Buenas prácticas de uso de sistemas y equipos corporativos.
Procedimientos formales de reporte y escalamiento de incidentes — actualmente inexistentes.
Políticas internas de cumplimiento obligatorio.
Designación de un responsable formal de seguridad de la información dentro de la organización.
2.6 Objetivos Generales del Plan

Los objetivos generales del presente plan son:

Reducir la probabilidad de incidentes de seguridad derivados de las brechas actuales identificadas.
Implementar respaldos y capacidad de recuperación ante pérdida de información.
Minimizar el impacto operativo ante fallas tecnológicas o ciberataques.
Proteger la información crítica de clientes, incluyendo datos personales y bancarios, en cumplimiento de obligaciones legales y contractuales.
Fortalecer los controles de acceso y eliminar prácticas inseguras (cuentas compartidas, privilegios administrativos innecesarios).
Mejorar la postura de seguridad de la infraestructura distribuida en las tres locaciones.
Establecer una base formal de gobernanza de seguridad orientada a la futura certificación ISO/IEC 27001.
