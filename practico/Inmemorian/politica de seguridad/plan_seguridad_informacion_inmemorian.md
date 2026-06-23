# Plan de Seguridad de la Información — Inmemorian

---

## Índice

1. [Alcance](#1-alcance)
2. [Seguridad de la Información](#2-seguridad-de-la-información)
3. [Política de Seguridad de la Información](#3-política-de-seguridad-de-la-información)
4. [Seguridad Frente al Acceso por Parte de Terceros](#4-seguridad-frente-al-acceso-por-parte-de-terceros)
5. [Clasificación y Control de Activos](#5-clasificación-y-control-de-activos)
6. [Seguridad del Personal](#6-seguridad-del-personal)
7. [Seguridad Física y Ambiental](#7-seguridad-física-y-ambiental)
8. [Gestión de Comunicaciones y Operaciones](#8-gestión-de-comunicaciones-y-operaciones)
9. [Control de Accesos](#9-control-de-accesos)
10. [Desarrollo y Mantenimiento de Sistemas](#10-desarrollo-y-mantenimiento-de-sistemas)
11. [Administración de la Continuidad de las Actividades de la Organización](#11-administración-de-la-continuidad-de-las-actividades-de-la-organización)
12. [Cumplimiento](#12-cumplimiento)

---

# 1. Alcance

El presente Plan de Seguridad de la Información tiene como finalidad establecer los lineamientos, políticas, procedimientos y controles necesarios para proteger los activos de información de la organización, garantizando adecuados niveles de confidencialidad, integridad y disponibilidad.

El plan se desarrolla para **Inmemorian**, empresa dedicada al tratamiento y distribución de materiales como mármol, granito y otras piedras naturales y sintéticas. La organización produce y comercializa placas conmemorativas para cementerios, placas para profesionales, placas para monumentos —con grabados, pinturas, imágenes y símbolos religiosos— y mesadas de piedra para baños y cocinas, incluyendo accesorios como bachas.

La necesidad de implementar este plan surge a partir del relevamiento de la situación actual de ciberseguridad, que evidenció importantes brechas de control —ausencia de respaldos, falta de segmentación de red, uso de equipos personales sin políticas, cuentas compartidas y sistemas desactualizados— en un contexto de alta dependencia tecnológica (aproximadamente **75 %**) para la operación diaria. Asimismo, la dirección ha expresado el objetivo de avanzar hacia una futura certificación **ISO/IEC 27001**.

## Ámbito de aplicación

El alcance del presente documento comprende:

- Infraestructura tecnológica distribuida en tres locaciones (Parque Industrial, Local Inmemorian y Local La Roca).
- Estaciones de trabajo y equipos móviles corporativos.
- Equipos personales utilizados para actividades laborales.
- Redes internas ad-hoc y conexiones a internet en cada sede.
- Sistemas de gestión, aplicaciones corporativas y portales web.
- Correo electrónico y canales de comunicación digital (WhatsApp, redes sociales).
- Información digital, documentación sensible y datos de clientes.
- Usuarios internos y proveedores externos con acceso a los sistemas.
- Procesos relacionados con modalidad híbrida del personal administrativo.
- Servicios tercerizados vinculados a tecnología, finanzas e importaciones.

## Personas alcanzadas

Este plan será aplicable a:

- Dueños y gerentes de la organización.
- Empleados permanentes.
- Personal administrativo en modalidad presencial o híbrida.
- Personal tercerizado y proveedores externos de sistemas, finanzas e importaciones.
- Consultores externos.
- Toda persona que acceda a información o recursos tecnológicos de la organización.

## Procesos críticos comprendidos

Quedan comprendidos dentro del alcance todos los procesos críticos vinculados a:

- Ventas de placas conmemorativas, placas profesionales y mesadas.
- Compras e importaciones de materiales.
- Producción y tratamiento de piedras.
- Logística y distribución.
- Finanzas y administración.
- Gestión de sistemas y tecnología.

El presente documento servirá como base para la implementación de controles de seguridad alineados a buenas prácticas internacionales, tomando como referencia estándares como **ISO/IEC 27001**.

---

# 2. Seguridad de la Información

La seguridad de la información constituye un conjunto de políticas, procedimientos, controles y buenas prácticas orientadas a proteger los activos de información de la organización frente a amenazas internas y externas.

La empresa reconoce que la información es un activo estratégico fundamental para el desarrollo de sus actividades comerciales, productivas y administrativas —incluyendo datos de clientes, información financiera, diseños de placas conmemorativas y registros operativos de los ERP— por lo que resulta indispensable implementar mecanismos adecuados para su protección.

El objetivo principal de la seguridad de la información es preservar los siguientes principios:

## 2.1. Confidencialidad

Garantizar que la información únicamente sea accesible por personas, sistemas o procesos autorizados.

Se implementarán medidas orientadas a:

- Restringir accesos no autorizados.
- Eliminar progresivamente el uso de cuentas compartidas, especialmente en áreas de producción y ventas.
- Aplicar controles de autenticación y, en sistemas críticos, autenticación multifactor (MFA).
- Definir perfiles y privilegios de usuario acordes a cada rol organizacional.
- Proteger información sensible de clientes —incluyendo datos personales y bancarios—, proveedores y empleados.
- Implementar políticas de contraseñas seguras con vencimiento periódico.
- Regular el uso de equipos personales y canales de comunicación no corporativos (WhatsApp, redes sociales).

## 2.2. Integridad

Asegurar que la información permanezca completa, exacta y libre de modificaciones no autorizadas.

Para ello se establecerán controles destinados a:

- Evitar alteraciones indebidas de datos en los ERP y portales web.
- Mantener registros de auditoría y trazabilidad de cambios.
- Gestionar adecuadamente cambios en sistemas y configuraciones de red.
- Aplicar controles sobre bases de datos y sistemas críticos.
- Implementar respaldos periódicos y verificables de la información empresarial.
- Restringir la instalación libre de software por parte de los usuarios.

## 2.3. Disponibilidad

Garantizar que la información y los servicios tecnológicos estén disponibles cuando sean requeridos por la operación.

Se adoptarán medidas como:

- Implementación de sistemas de respaldo y recuperación —actualmente inexistentes— con copias offline o inmutables.
- Protección contra malware mediante soluciones antivirus homogéneas en todos los equipos.
- Monitoreo de infraestructura distribuida en las tres locaciones.
- Planes de contingencia y continuidad operativa para procesos críticos (ventas, producción, logística, finanzas).
- Mantenimiento preventivo de hardware y software, incluyendo la actualización regular de sistemas operativos obsoletos.
- Protección perimetral mediante firewall en cada sede.

## 2.4. Gestión de Riesgos

La organización implementará un enfoque preventivo basado en la identificación, evaluación y tratamiento de riesgos asociados a la seguridad de la información.

Entre las principales amenazas identificadas se encuentran:

- Pérdida total de información por ausencia de respaldos.
- Phishing y correo spam —sin filtros anti-spam ni anti-phishing implementados.
- Accesos indebidos facilitados por cuentas compartidas y privilegios administrativos en estaciones de trabajo.
- Fallas de hardware en equipos sin soporte o con sistemas operativos obsoletos.
- Errores humanos y falta de capacitación en ciberseguridad.
- Software desactualizado por ausencia de gestión de parches.
- Uso de dispositivos personales sin controles (BYOD).
- Exposición de datos de clientes a través de canales informales de comunicación.
- Interrupciones eléctricas o de conectividad en alguna de las tres locaciones.
- Dependencia crítica de proveedores externos de sistemas sin acuerdos formales de nivel de servicio.

## 2.5. Cultura de Seguridad

La seguridad de la información no será responsabilidad exclusiva del proveedor externo de sistemas, sino de toda la organización —desde los dueños y gerentes hasta el personal operativo.

Por ello se promoverán:

- Capacitaciones periódicas en ciberseguridad para todo el personal.
- Concientización sobre riesgos del uso de WhatsApp y redes sociales para intercambio de información de clientes.
- Buenas prácticas de uso de sistemas y equipos corporativos.
- Procedimientos formales de reporte y escalamiento de incidentes —actualmente inexistentes.
- Políticas internas de cumplimiento obligatorio.
- Designación de un responsable formal de seguridad de la información dentro de la organización.

## 2.6. Objetivos Generales del Plan

Los objetivos generales del presente plan son:

- Reducir la probabilidad de incidentes de seguridad derivados de las brechas actuales identificadas.
- Implementar respaldos y capacidad de recuperación ante pérdida de información.
- Minimizar el impacto operativo ante fallas tecnológicas o ciberataques.
- Proteger la información crítica de clientes, incluyendo datos personales y bancarios, en cumplimiento de obligaciones legales y contractuales.
- Fortalecer los controles de acceso y eliminar prácticas inseguras (cuentas compartidas, privilegios administrativos innecesarios).
- Mejorar la postura de seguridad de la infraestructura distribuida en las tres locaciones.
- Establecer una base formal de gobernanza de seguridad orientada a la futura certificación ISO/IEC 27001.

---

# 3. Política de Seguridad de la Información

La información es un recurso estratégico que, al igual que el resto de los activos de Inmemorian, posee valor para la organización y, por consiguiente, debe ser debidamente protegida. La presente Política de Seguridad de la Información establece los lineamientos que orientan la protección de la información frente a amenazas internas y externas, deliberadas o accidentales.

Inmemorian es una empresa dedicada al tratamiento y distribución de mármol, granito y otras piedras naturales y sintéticas, que produce y comercializa placas conmemorativas para cementerios, placas para profesionales, placas para monumentos y mesadas de piedra para baños y cocinas. Su operación diaria —ventas, producción, logística, finanzas e importaciones— depende en aproximadamente un **75 %** de los sistemas informáticos, lo que convierte a la seguridad de la información en un factor crítico para la continuidad del negocio.

El relevamiento de la situación actual evidenció brechas de control de alta severidad: **ausencia total de respaldos**, equipos mayoritariamente obsoletos sin soporte, cuentas compartidas en producción y ventas, inexistencia de firewall perimetral, ausencia de mecanismos de monitoreo, y dependencia crítica de un proveedor externo de sistemas sin acuerdos formales de nivel de servicio ni cláusulas de confidencialidad documentadas. Esta situación motivó la elaboración del presente plan.

## Objetivo

Proteger los recursos de información de Inmemorian y la tecnología utilizada para su procesamiento, frente a amenazas internas o externas, deliberadas o accidentales, con el fin de asegurar el cumplimiento de la confidencialidad, integridad, disponibilidad, auditabilidad y legalidad de la información.

## Alcance

Esta Política se aplica en todo el ámbito de la organización, incluyendo sus tres locaciones operativas:

- **Parque Industrial:** 1 módem/router WiFi, 1 PC de producción, 2 PC de dueños.
- **Local Inmemorian:** 1 módem/router WiFi, 1 PC de ventas, 1 móvil corporativo.
- **Local La Roca:** 1 módem/router WiFi, 2 PC de ventas, 1 móvil corporativo.

Están comprendidos dentro del alcance todos los recursos tecnológicos —estaciones de trabajo corporativas y personales, equipos móviles, sistemas ERP, portales web, correo electrónico y canales de comunicación digital como WhatsApp y redes sociales— y la totalidad de los procesos, ya sean internos o externos, vinculados a la organización.

Están sujetos a esta Política:

- Dueños y gerentes de la organización.
- Empleados permanentes y personal administrativo en modalidad presencial o híbrida.
- Personal tercerizado y proveedores externos de sistemas, finanzas e importaciones.
- Toda persona que acceda a información o recursos tecnológicos de la organización.

## Responsabilidades

### Dueños

Los dueños de Inmemorian son los responsables máximos de aprobar y avalar la presente Política, dado que en la organización **no existe un responsable formal del área de sistemas**. Les corresponde:

- Comunicar y difundir esta Política en todas las áreas.
- Autorizar los permisos y accesos especiales a los sistemas, incluyendo los otorgados a los proveedores externos.
- Aprobar cambios e inversiones tecnológicas sobre la base de las propuestas de las distintas áreas.
- Reportar inmediatamente cualquier desvío o incidente de seguridad del que tomen conocimiento.
- Gestionar el correo electrónico corporativo, que actualmente se encuentra bajo su administración directa.

### Gerentes

Los gerentes de cada área (Ventas de Placas Conmemorativas y Profesionales, Ventas de Mesadas, Producción y Logística) son responsables de:

- Cumplir y hacer cumplir la presente Política dentro de sus equipos.
- Actuar como propietarios de la información bajo su gestión en ausencia de un responsable formal de sistemas.
- Clasificar la información de su área según su grado de sensibilidad y criticidad.
- Informar al proveedor externo de sistemas sobre altas, bajas y modificaciones de accesos de su personal.
- Reportar de inmediato cualquier incidente, anomalía o sospecha de vulneración de la seguridad.

### Proveedor Externo de Sistemas

El proveedor externo de sistemas, en su carácter de administrador de servidores, red, usuarios, accesos y los dos sistemas ERP utilizados por la organización, deberá:

- Supervisar el cumplimiento de los controles técnicos de seguridad.
- Gestionar y documentar los incidentes relativos a la seguridad de los sistemas.
- Evaluar e implementar controles específicos para nuevos sistemas o servicios.
- Garantizar la integridad, disponibilidad y confidencialidad de los sistemas bajo su administración.
- Actuar en el marco de un acuerdo de nivel de servicio y confidencialidad formalizado con la organización, **el cual deberá suscribirse como acción prioritaria**, dado que actualmente no existe.

### Todos los Usuarios

Todos los usuarios de los sistemas —empleados permanentes, administrativos en modalidad híbrida y personal tercerizado— son responsables de:

- Conocer, cumplir y hacer cumplir la presente Política.
- Reportar inmediatamente cualquier incidente, anomalía o sospecha de vulneración de la seguridad.
- Utilizar los recursos informáticos exclusivamente para los fines laborales autorizados.
- Mantener la confidencialidad de sus credenciales de acceso y **no compartirlas bajo ninguna circunstancia**, eliminando la práctica actual de cuentas compartidas en producción y ventas.
- Abstenerse de instalar software libremente en sus equipos, práctica actualmente habitual que deberá ser regulada.
- No utilizar canales informales —WhatsApp, Instagram, Facebook u otras redes sociales— para el intercambio de información sensible de clientes.

---

## 3.1. Principios Rectores

La presente política se basa en los siguientes principios:

**Confidencialidad:** La información solo será accesible por personas, sistemas o procesos autorizados. Se eliminarán progresivamente las **cuentas compartidas actualmente existentes en las áreas de producción y ventas**, y se definirán perfiles de acceso acordes a cada rol organizacional. Se implementarán controles de autenticación y, en sistemas críticos, autenticación multifactor (MFA). Se regularán el uso de WhatsApp y redes sociales —actualmente utilizados por las gerencias de ventas y logística— para el intercambio de información de clientes.

**Integridad:** La información permanecerá completa, exacta y libre de modificaciones no autorizadas. Se implementarán controles de auditoría y trazabilidad en los dos ERP y portales web. La instalación libre de software por parte de los usuarios —actualmente sin restricción— deberá ser regulada formalmente.

**Disponibilidad:** La información y los servicios tecnológicos estarán disponibles cuando sean requeridos por la operación. Se implementarán **sistemas de respaldo y recuperación, actualmente inexistentes**, con copias offline o inmutables, así como planes de contingencia para los procesos críticos. Se incorporará protección perimetral mediante firewall en cada una de las tres locaciones, actualmente ausente.

**Legalidad:** La organización cumplirá con las obligaciones legales vigentes en materia de protección de datos, especialmente en lo que respecta a **información de clientes, datos bancarios y datos personales**, en cumplimiento de la Ley N.º 25.326 de Protección de Datos Personales.

**Auditabilidad:** Los eventos relevantes de los sistemas serán registrados para su control posterior. Actualmente **no existen mecanismos de monitoreo ni registros centralizados**, situación que deberá revertirse mediante la implementación de los controles previstos en este plan.

---

## 3.2. Gestión de Riesgos

La organización adoptará un enfoque preventivo basado en la identificación, evaluación y tratamiento de riesgos. A continuación se detallan las principales amenazas identificadas en el relevamiento de la situación actual, con referencia directa al contexto operativo de Inmemorian:

| Amenaza identificada | Situación actual relevada |
|---|---|
| Pérdida total de información | No existen respaldos de ningún tipo. |
| Accesos indebidos | Cuentas compartidas en producción y ventas; los usuarios poseen privilegios administrativos en sus equipos. |
| Sistemas obsoletos | La mayoría de los equipos opera con sistemas sin soporte ni actualizaciones de seguridad. |
| Phishing y correo malicioso | No existen filtros anti-spam ni anti-phishing. |
| BYOD sin controles | Se utilizan 2 computadoras portátiles personales para trabajar, sin ningún control de seguridad. |
| Exposición de datos de clientes | Los datos de clientes —incluyendo datos bancarios— se comparten por WhatsApp y redes sociales. |
| Ausencia de protección perimetral | No se utiliza firewall en ninguna de las tres locaciones. |
| Dependencia de proveedor sin formalización | El proveedor externo de sistemas opera sin SLA, sin cláusulas de confidencialidad y sin procedimientos formales de gestión de incidentes. |
| Falta de control de licencias | No existe ningún control sobre el licenciamiento de software. |
| Ausencia de gestión de incidentes | No existe un procedimiento formal definido para la comunicación y escalamiento de incidentes. |

---

## 3.3. Cultura de Seguridad

La seguridad de la información no es responsabilidad exclusiva del proveedor externo de sistemas, sino de toda la organización. Se promoverán las siguientes acciones:

- **Capacitaciones periódicas** en ciberseguridad para todo el personal, con énfasis en los riesgos del uso de WhatsApp, Instagram y Facebook para el intercambio de información de clientes, dado el uso intensivo de estos canales relevado en las gerencias de ventas.
- **Procedimientos formales de reporte y escalamiento de incidentes**, actualmente inexistentes, que definan la cadena de comunicación desde el usuario hasta los dueños y el proveedor externo de sistemas.
- **Designación de un responsable formal de seguridad de la información** dentro de la organización, actualmente ausente.
- **Política de uso aceptable de sistemas y equipos**, de conocimiento y cumplimiento obligatorio para todos los usuarios, que regule expresamente la instalación de software, el uso de dispositivos personales y el manejo de credenciales.
- **Concientización específica sobre credenciales**: eliminar la práctica de cuentas compartidas en producción y ventas, y establecer contraseñas individuales con vencimiento periódico.

---

## 3.4. Objetivos Específicos del Plan

- Implementar un sistema de **respaldos periódicos y verificables**, con copias offline o inmutables, como medida de máxima prioridad dada la ausencia total de respaldos relevada.
- Eliminar el uso de **cuentas compartidas** en producción y ventas, y asignar credenciales individuales a cada usuario.
- Reducir los **privilegios administrativos** en estaciones de trabajo, actualmente otorgados a todos los usuarios sin distinción.
- Incorporar **firewall perimetral** en las tres locaciones operativas.
- Implementar **filtros anti-spam y anti-phishing** en el sistema de correo electrónico administrado por los dueños.
- Formalizar la relación con el **proveedor externo de sistemas** mediante un acuerdo de nivel de servicio y cláusulas de confidencialidad.
- Proteger la información crítica de clientes —incluyendo datos personales y bancarios— en cumplimiento de la **Ley 25.326**.
- Establecer controles mínimos sobre los **dispositivos personales** utilizados para trabajar (2 laptops personales), mientras se avanza hacia su reemplazo o regularización.
- Regular el **uso de canales informales** (WhatsApp, redes sociales) para la transmisión de información organizacional.
- Establecer una base formal de gobernanza orientada a la futura **certificación ISO/IEC 27001**.

---

# 4. Seguridad Frente al Acceso por Parte de Terceros

Inmemorian mantiene relaciones con tres proveedores externos que acceden a sus sistemas e información interna en el ejercicio de sus funciones:

- **Proveedor externo de sistemas:** administra servidores, usuarios, accesos, red y los dos sistemas ERP de la organización, con acceso administrativo amplio a toda la infraestructura tecnológica.
- **Proveedor externo de finanzas:** accede a información financiera y contable.
- **Proveedor externo de importaciones:** gestiona información vinculada a compras y logística internacional.

> ⚠️ **Situación crítica identificada:** el proveedor externo de sistemas opera actualmente **sin acuerdo formal de nivel de servicio, sin cláusulas de confidencialidad documentadas y sin procedimientos formales de gestión de incidentes**, a pesar de poseer acceso administrativo total sobre la infraestructura tecnológica de la organización. Esta situación representa el riesgo de terceros más crítico a subsanar con carácter de urgencia.

Dado que estos accesos pueden comprometer la seguridad de la información si no se gestionan adecuadamente, se establecen a continuación las medidas de protección aplicables.

## Objetivo

Garantizar la aplicación de medidas de seguridad adecuadas en los accesos de terceros a la información de Inmemorian, minimizando el riesgo de exposición, pérdida o uso indebido de la información organizacional, con especial énfasis en la formalización de la relación con el proveedor externo de sistemas.

## Alcance

Esta política se aplica a todos los recursos de la organización y a todas sus relaciones con terceros que impliquen acceso a datos, sistemas, infraestructura o información de Inmemorian. Comprende específicamente a:

- Proveedor externo de sistemas (administración de servidores, usuarios, accesos y ERP).
- Proveedor externo de finanzas (acceso a información contable y financiera).
- Proveedor externo de importaciones (gestión de compras y logística internacional).
- Consultores externos o cualquier otro tercero que, de manera eventual, acceda a información de la organización.

## Responsabilidades

Los **dueños de la organización**, en tanto máximas autoridades decisoras y responsables de autorizar accesos especiales, son los responsables de aprobar todo acceso de terceros a los sistemas e información de Inmemorian. Esta función de supervisión será delegada al responsable formal de seguridad que se designe oportunamente.

Cada proveedor externo deberá:

- Cumplir con la presente Política de Seguridad de la Información.
- Restringir su acceso exclusivamente a los recursos necesarios para el cumplimiento de sus funciones.
- Reportar de inmediato cualquier incidente de seguridad que detecte o del que tome conocimiento.
- Garantizar la confidencialidad de la información a la que acceda en el marco de su relación con Inmemorian.

---

## 4.1. Identificación de Riesgos de Acceso de Terceros

Ante la necesidad de otorgar o mantener acceso de terceros a información o sistemas de la organización, se llevará a cabo una evaluación de riesgos que contemple, como mínimo:

- El tipo de acceso requerido: físico o lógico, y a qué recurso o sistema específico.
- Los motivos y la necesidad operativa que justifican el acceso.
- La criticidad y sensibilidad de la información a la que se tendrá acceso.
- Los riesgos potenciales sobre la confidencialidad, integridad y disponibilidad de la información.
- Los controles compensatorios disponibles para mitigar dichos riesgos.

Esta evaluación se documentará y será aprobada por los dueños de la organización. Los permisos a otorgar se restringirán al **mínimo necesario** para el cumplimiento de la función del tercero.

A continuación se detalla la situación de riesgo actual de cada proveedor externo relevado:

| Proveedor | Acceso actual | Riesgo identificado |
|---|---|---|
| Proveedor de sistemas | Administrativo total sobre servidores, usuarios, red y ERP | Sin SLA, sin acuerdo de confidencialidad, sin procedimiento de incidentes formalizado. Riesgo **CRÍTICO**. |
| Proveedor de finanzas | Información contable y financiera | Acceso a datos sensibles sin cláusulas de confidencialidad documentadas. |
| Proveedor de importaciones | Gestión de compras y logística internacional | Acceso a información de proveedores y operaciones de comercio exterior sin formalización contractual de seguridad. |

---

## 4.2. Requerimientos de Seguridad en Contratos con Terceros

Todos los contratos, acuerdos de servicio o cualquier otro instrumento que formalice la relación con terceros que accedan a información o sistemas de la organización deberán contemplar, como mínimo, los siguientes requerimientos:

- Cumplimiento de la presente Política de Seguridad de la Información de Inmemorian.
- Restricción de accesos al **mínimo necesario** para el cumplimiento de las funciones contratadas.
- **Acuerdo de confidencialidad** sobre toda información a la que el tercero acceda, incluyendo datos de clientes, datos bancarios e información financiera.
- **Acuerdo de nivel de servicio (SLA)** con tiempos de respuesta ante incidentes claramente definidos, priorizando la suscripción de este instrumento con el proveedor de sistemas como acción inmediata.
- Proceso formal de **administración de cambios** en sistemas y configuraciones.
- Controles que garanticen **protección contra software malicioso** en los sistemas que administren.
- Derecho de Inmemorian a realizar **auditorías** sobre los servicios prestados y los accesos efectuados.
- Acceso de Inmemorian a los **registros de eventos** de seguridad y transaccionales generados en el marco del servicio, una vez que los mecanismos de registro estén implementados.
- **Propiedad de la información** a favor de Inmemorian: toda información generada, procesada o almacenada en el marco del servicio es propiedad exclusiva de la organización.
- Cumplimiento de la **Ley N.º 25.326 de Protección de Datos Personales**, especialmente en lo que respecta a datos de clientes.
- En caso de desarrollo o personalización de software: entrega de los **programas fuente** al finalizar el proyecto y acuerdos de custodia de código fuente ante eventualidades.
- **Procedimiento de revocación de accesos** ante la finalización del contrato, con plazos definidos.

---

## 4.3. Acceso Remoto y Monitoreo

En la actualidad, **Inmemorian no utiliza VPN ni cuenta con conexiones remotas** a sus sistemas. El personal no se conecta de forma remota a la infraestructura organizacional. Sin embargo, a medida que la organización avance en la implementación de controles de seguridad, deberán establecerse las siguientes pautas para cualquier acceso remoto que se habilite a terceros:

- El acceso remoto de terceros deberá realizarse exclusivamente a través de **canales seguros y autenticados** (VPN corporativa con autenticación multifactor).
- Se registrarán las sesiones de acceso remoto de terceros, incluyendo usuario, fecha, hora y acciones realizadas.
- Los accesos remotos serán habilitados únicamente durante el tiempo estrictamente necesario para la tarea a realizar.
- Cualquier acceso remoto deberá ser **previamente autorizado por los dueños** de la organización.

> **Nota:** la habilitación de acceso remoto no deberá realizarse hasta tanto se encuentren implementados los controles de seguridad mínimos previstos en este plan, en especial el firewall perimetral y los mecanismos de registro de eventos.

---

## 4.4. Revisión y Auditoría de Accesos de Terceros

Los accesos otorgados a terceros serán revisados **periódicamente** para verificar que:

- Los privilegios asignados continúan siendo necesarios y proporcionales a las funciones actuales del tercero.
- No existen accesos activos de terceros cuya relación contractual con la organización haya concluido.
- El tercero está cumpliendo con las condiciones de seguridad establecidas en el contrato o acuerdo vigente.

Dado que actualmente el proveedor de sistemas posee acceso administrativo total sin que existan registros de auditoría ni mecanismos formales de control, la implementación de los controles de revisión periódica descritos en este punto queda supeditada al avance del plan de mejora de seguridad de la organización, con carácter prioritario.

Ante la **finalización de la relación contractual** con cualquier proveedor externo, se procederá de manera inmediata a la revocación de todos sus accesos a sistemas, redes e información de la organización. Esta acción será responsabilidad de los dueños en coordinación con el proveedor de sistemas vigente.

---

# 5. Clasificación y Control de Activos

Inmemorian debe conocer y documentar los activos de información y tecnología que utiliza en su operación diaria como parte fundamental de la administración de riesgos. Los activos de información deben ser clasificados de acuerdo con la sensibilidad y criticidad de la información que contienen, o bien de acuerdo a la funcionalidad que cumplen, con el objeto de señalar cómo ha de ser tratada y protegida dicha información.

El relevamiento de la situación actual evidenció que **no existe un inventario formal de activos informáticos**, **no hay proceso definido para altas y bajas de equipos** y **no se controla el licenciamiento de software**. Asimismo, la información crítica —incluyendo datos personales y bancarios de clientes— circula por canales informales como WhatsApp, Instagram y Facebook, sin criterios de clasificación ni controles acordes a su sensibilidad. Esta situación incrementa el riesgo de exposición, pérdida o uso indebido de la información organizacional.

## Objetivo

Identificar, clasificar y proteger adecuadamente los activos de información de Inmemorian, asignando a cada uno un responsable y un nivel de protección acorde a su criticidad e impacto potencial sobre la operación.

## Alcance

Esta política se aplica a toda la información administrada en Inmemorian, cualquiera sea el soporte en que se encuentre —digital o físico—, y a todos los activos tecnológicos distribuidos en sus tres locaciones operativas:

- **Parque Industrial:** 1 módem/router WiFi, 1 PC de producción, 2 PC de dueños.
- **Local Inmemorian:** 1 módem/router WiFi, 1 PC de ventas, 1 móvil corporativo.
- **Local La Roca:** 1 módem/router WiFi, 2 PC de ventas, 1 móvil corporativo.

Comprende además los 2 ERP, portales web, correo electrónico, redes sociales, equipos personales utilizados para trabajo (2 laptops) y la información gestionada por proveedores externos de sistemas, finanzas e importaciones.

## Responsabilidades

Dado que Inmemorian **no cuenta con un responsable formal del área de sistemas ni con un área de Recursos Humanos dedicada**, las funciones de propiedad y custodia de activos e información se distribuyen de la siguiente manera:

### Gerentes de área

Actúan como **propietarios de la información** bajo su gestión. Les corresponde:

- Identificar y registrar los activos de información y tecnología de su área.
- Clasificar la información según su grado de sensibilidad y criticidad, aplicando los criterios definidos en el punto 5.2.
- Informar al proveedor externo de sistemas y a los dueños sobre altas, bajas o modificaciones de equipos y accesos.

### Dueños de la organización

Son responsables de:

- Aprobar el inventario consolidado de activos y su actualización periódica.
- Autorizar el tratamiento y los accesos a información clasificada como criticidad alta.
- Supervisar el cumplimiento de esta política en coordinación con los gerentes.

### Proveedor externo de sistemas

En su carácter de administrador de servidores, red, usuarios, accesos y los dos ERP, deberá:

- Mantener actualizado el registro técnico de activos bajo su administración (servidores, sistemas, cuentas de usuario).
- Asegurar que los controles técnicos de seguridad contemplen los requerimientos establecidos según la criticidad de la información que procesan los sistemas bajo su gestión.
- Colaborar con los gerentes y dueños en la elaboración y mantenimiento del inventario de activos.

---

## 5.1. Inventario de Activos

Se deberá confeccionar y mantener actualizado un **inventario de activos de información** que incluya, como mínimo, los siguientes tipos de activos identificados en el relevamiento:

> **Acción prioritaria:** el inventario de activos deberá confeccionarse como una de las primeras acciones del plan, dado que actualmente no existe ningún registro formal. Sin inventario, no es posible gestionar adecuadamente las protecciones descritas en los puntos siguientes.

### Activos de Hardware

| Activo | Cantidad | Locación | Observaciones |
|---|---|---|---|
| Estaciones de trabajo (PC corporativas) | 6 | Parque Industrial (3), Local Inmemorian (1), Local La Roca (2) | La mayoría con sistemas operativos obsoletos sin soporte. |
| Computadoras portátiles personales | 2 | Variable (modalidad híbrida) | Equipos personales usados para trabajo. Sin controles de seguridad. |
| Teléfonos móviles corporativos | 2 | Local Inmemorian (1), Local La Roca (1) | Usados para comunicación con clientes vía WhatsApp e Instagram. |
| Módems/routers WiFi | 3 | Parque Industrial (1), Local Inmemorian (1), Local La Roca (1) | Redes ad-hoc sin segmentación. Sin firewall perimetral. |
| Servidores | A relevar | A relevar | Administrados por el proveedor externo de sistemas. |

### Activos de Software

| Activo | Tipo | Observaciones |
|---|---|---|
| ERP (sistema 1) | Crítico | Administrado por el proveedor externo de sistemas. |
| ERP (sistema 2) | Crítico | Administrado por el proveedor externo de sistemas. |
| Portales web | Crítico | Utilizados por las gerencias de ventas. |
| Correo electrónico | Crítico | Administrado por los dueños. |
| Sistemas operativos Windows | Crítico | La mayoría sin soporte ni actualizaciones de seguridad. |
| WhatsApp / Instagram / Facebook | Complementario | Utilizados operacionalmente por ventas, producción y logística. Sin controles corporativos. |
| Software adicional de estaciones de trabajo | A relevar | Los usuarios pueden instalar software libremente; no existe control de licenciamiento. |

### Activos de Información

| Activo | Área responsable | Observaciones |
|---|---|---|
| Datos de clientes (nombre, contacto, pedidos) | Gerencias de Ventas | Circulan por WhatsApp, redes sociales y ERP. Alcanzados por Ley 25.326. |
| Datos bancarios de clientes | Gerencias de Ventas / Dueños | Alta sensibilidad. Se comparten por canales informales. |
| Información financiera y contable | Finanzas (proveedor externo) | Accedida por el proveedor externo de finanzas. |
| Diseños de placas conmemorativas e imágenes | Gerencias de Ventas | Generados y compartidos digitalmente con clientes. |
| Registros operativos de producción | Gerencia de Producción | Gestionados a través del ERP. |
| Información de importaciones y compras | Proveedor externo de importaciones | Gestionada por el proveedor externo. |
| Credenciales de acceso a sistemas | Todos los usuarios | Actualmente sin vencimiento. Varias cuentas compartidas en producción y ventas. |

---

## 5.2. Clasificación de la Información

Para clasificar un activo de información, se evaluarán las tres características en las cuales se basa la seguridad: **Confidencialidad, Integridad y Disponibilidad**.

### Confidencialidad

| Nivel | Descripción |
|---|---|
| **0** | Información que puede ser conocida y utilizada sin autorización por cualquier persona, sea empleado de la organización o no. |
| **1** | Información que puede ser conocida por todos los empleados y algunas entidades externas debidamente autorizadas; su divulgación no autorizada podría ocasionar riesgos o pérdidas leves. |
| **2** | Información que solo puede ser conocida por un grupo de empleados que la necesiten para su trabajo; su divulgación no autorizada podría ocasionar pérdidas significativas. |
| **3** | Información que solo puede ser conocida por un grupo muy reducido de empleados, generalmente de la alta dirección; su divulgación no autorizada podría ocasionar pérdidas graves. |

### Integridad

| Nivel | Descripción |
|---|---|
| **0** | Información cuya modificación no autorizada puede repararse fácilmente, o no afecta la operatoria de la organización. |
| **1** | Información cuya modificación no autorizada puede repararse aunque podría ocasionar pérdidas leves. |
| **2** | Información cuya modificación no autorizada es de difícil reparación y podría ocasionar pérdidas significativas. |
| **3** | Información cuya modificación no autorizada no podría repararse, ocasionando pérdidas graves. |

### Disponibilidad

| Nivel | Descripción |
|---|---|
| **0** | Información cuya inaccesibilidad no afecta la operatoria de la organización. |
| **1** | Información cuya inaccesibilidad permanente durante una hora podría ocasionar pérdidas leves. |
| **2** | Información cuya inaccesibilidad permanente durante un día podría ocasionar pérdidas significativas. |
| **3** | Información cuya inaccesibilidad permanente durante una semana podría ocasionar pérdidas graves. |

Al referirse a pérdidas, se contemplan aquellas mesurables (materiales) y no mesurables (imagen, valor estratégico de la información, obligaciones contractuales, disposiciones legales, etc.).

Se asignará a cada activo de información un valor por cada uno de estos criterios. Luego, se clasificará en una de las siguientes categorías:

| Categoría | Criterio |
|---|---|
| **Criticidad baja** | Ninguno de los valores asignados supera el 1. |
| **Criticidad media** | Alguno de los valores asignados es 2. |
| **Criticidad alta** | Alguno de los valores asignados es 3. |

En adelante se mencionará como **Información Clasificada** a aquella que se encuadre en los niveles 1, 2 o 3 de Confidencialidad.

### Ejemplos de clasificación aplicados a Inmemorian

Los propietarios de información de cada área deberán clasificar sus activos conforme a los criterios anteriores. A título orientativo, se presentan ejemplos basados en el relevamiento de la organización:

| Tipo de información | Área | Conf. | Integ. | Disp. | Criticidad | Controles requeridos |
|---|---|:---:|:---:|:---:|---|---|
| Datos personales y bancarios de clientes | Ventas / Finanzas | 3 | 2 | 2 | **Alta** | Acceso restringido en ERP; prohibido compartir por WhatsApp o redes sociales; cumplimiento Ley 25.326 |
| Registros contables y financieros | Finanzas (proveedor externo) | 3 | 3 | 2 | **Alta** | Acceso mínimo necesario; respaldos verificables; acuerdo de confidencialidad con proveedor |
| Pedidos, diseños y grabados de placas conmemorativas | Ventas / Producción | 2 | 2 | 2 | **Media** | Credenciales individuales; trazabilidad en ERP; respaldo periódico |
| Datos de importaciones y proveedores internacionales | Importaciones (proveedor externo) | 2 | 2 | 2 | **Media** | Formalización contractual; acceso restringido |
| Información operativa de producción y logística | Producción / Logística | 2 | 2 | 3 | **Alta** | Disponibilidad crítica (~75 % dependencia de sistemas); respaldos; eliminación de cuentas compartidas |
| Material de marketing en redes sociales | Ventas | 1 | 1 | 0 | **Baja** | Publicación autorizada; sin datos personales de clientes |
| Comunicaciones generales internas | Todas | 1 | 1 | 0 | **Baja** | Uso laboral autorizado |

> **Situación crítica identificada:** los datos personales y bancarios de clientes —información de **criticidad alta**— se comparten actualmente por WhatsApp, Instagram y Facebook, canales no autorizados para Información Clasificada. Esta práctica deberá cesar y ser reemplazada por los sistemas corporativos (ERP, correo electrónico) con los controles de acceso definidos en este plan.

Los propietarios de información revisarán la clasificación de sus activos **al menos una vez al año**, o ante cambios significativos en los procesos, sistemas o obligaciones legales aplicables.

---

## 5.3. Etiquetado y Manejo de la Información

Una vez clasificada la información, se establecerán procedimientos de etiquetado y manejo acordes a cada nivel. Dada la situación actual de la organización —sin procesos formales de clasificación—, la implementación será gradual:

- En una primera etapa, se priorizará el etiquetado y control de la información **Confidencial**, con énfasis en los datos de clientes y bancarios.
- Los documentos digitales que contengan información Confidencial deberán identificarse claramente y transmitirse únicamente por canales seguros, evitando el uso de WhatsApp o redes sociales para este fin.
- Se establecerán procedimientos para la **eliminación segura** de información Confidencial cuando ya no sea necesaria, tanto en soportes digitales como físicos.

---

## 5.4. Control de Activos de Hardware y Software

### Hardware

- Todos los equipos —corporativos y personales utilizados para trabajo— deberán estar registrados en el inventario de activos.
- El **proceso de alta y baja de equipos**, actualmente inexistente, deberá formalizarse: ningún equipo deberá incorporarse o retirarse de la operación sin la aprobación de los dueños y el registro correspondiente.
- Los equipos con **sistemas operativos obsoletos sin soporte** —situación que afecta a la mayoría del parque tecnológico actual— deberán ser reemplazados o actualizados como parte del plan de mejora, priorizando aquellos que procesan información Confidencial.
- Los **dispositivos personales** utilizados para trabajo (2 laptops personales del personal administrativo) deberán sujetarse a controles mínimos de seguridad mientras permanezcan en uso, incluyendo protección antivirus y restricción de acceso a sistemas críticos.

### Software

- Se deberá elaborar un **inventario de software** instalado en todos los equipos, incluyendo versión, estado de licenciamiento y estado de actualización.
- La **instalación libre de software** por parte de los usuarios, práctica actualmente habitual, deberá ser prohibida. Solo el proveedor externo de sistemas o los dueños podrán autorizar nuevas instalaciones.
- Se implementará una política de **gestión de parches y actualizaciones** para los sistemas operativos y aplicaciones críticas, dado que actualmente no se gestionan regularmente.
- El **control de licencias**, actualmente inexistente, deberá implementarse para evitar el uso de software sin licencia que genere riesgos legales y de seguridad.

---

# 6. Seguridad del Personal

Es fundamental educar e informar al personal de Inmemorian desde su ingreso y de forma continua, acerca de las medidas de seguridad que afectan al desarrollo de sus funciones y de las expectativas depositadas en ellos en materia de seguridad y confidencialidad.

Con aproximadamente **8 empleados** —de los cuales solo **2 corresponden a personal administrativo con modalidad híbrida**— y una operación altamente dependiente de sistemas informáticos, el factor humano constituye uno de los riesgos más relevantes identificados en el relevamiento: **errores humanos, falta de capacitación en ciberseguridad, cuentas compartidas, privilegios administrativos innecesarios, uso de dispositivos personales sin controles y transmisión de datos sensibles por canales informales**.

## Objetivo

- Reducir los riesgos de error humano, uso inadecuado de instalaciones y recursos, y manejo no autorizado de la información.
- Garantizar que los usuarios se encuentren capacitados para respaldar la Política de Seguridad de la Información en el transcurso de sus tareas habituales.

## Alcance

Esta política se aplica a:

- Dueños y gerentes de la organización.
- Empleados permanentes y personal administrativo en modalidad presencial o híbrida.
- Personal tercerizado y proveedores externos de sistemas, finanzas e importaciones que desempeñen tareas dentro del ámbito de Inmemorian.
- Toda persona que acceda a información o recursos tecnológicos de la organización.

## Responsabilidades

Dada la estructura organizacional de Inmemorian, las responsabilidades en materia de seguridad del personal se asignan de la siguiente manera:

### Dueños de la organización

- Comunicar y difundir las obligaciones de seguridad a todo el personal.
- Designar o asumir provisionalmente la función de **responsable formal de seguridad de la información**, actualmente ausente, hasta que se formalice la designación.
- Aprobar el programa de capacitación y el procedimiento de gestión de incidentes.
- Recibir y escalar los reportes de incidentes de seguridad de gravedad alta.

### Gerentes de área

- Informar a todo el personal que ingresa a su área sobre sus obligaciones respecto del cumplimiento de la Política de Seguridad de la Información, en ausencia de un área formal de Recursos Humanos.
- Verificar que ningún usuario reciba accesos a sistemas antes de recibir la inducción en materia de seguridad.
- Canalizar los reportes de incidentes y anomalías detectados por su equipo hacia los dueños y el proveedor externo de sistemas.

### Proveedor externo de sistemas

- Brindar soporte técnico en la investigación y resolución de incidentes relacionados con sistemas, red, servidores y ERP.
- Documentar los incidentes de seguridad informáticos gestionados en el marco de sus funciones.
- Colaborar en las capacitaciones técnicas cuando corresponda.

### Todo el personal

Es responsable de:

- Conocer, cumplir y hacer cumplir la Política de Seguridad de la Información.
- Reportar de inmediato cualquier debilidad, incidente o sospecha de vulneración de la seguridad.
- No compartir credenciales de acceso ni utilizar cuentas compartidas.
- Abstenerse de transmitir Información Clasificada por WhatsApp, Instagram, Facebook u otros canales no autorizados.

---

## 6.1. Capacitación del Usuario

Todos los empleados de Inmemorian y, cuando sea pertinente, los proveedores externos que desempeñen funciones en la organización recibirán capacitación y actualización periódica en materia de la Política de Seguridad de la Información, normas y procedimientos de la organización.

El personal que ingrese a Inmemorian recibirá material de inducción en seguridad de la información, indicándosele el comportamiento esperado, **antes de serle otorgados los privilegios de acceso** a los sistemas que correspondan. Dado que actualmente no existe un proceso formal de incorporación en materia de seguridad, su implementación constituye una acción prioritaria.

### Contenidos mínimos de la capacitación

La capacitación deberá abordar, como mínimo, los siguientes temas adaptados al contexto operativo relevado:

| Tema | Motivo vinculado al relevamiento |
|---|---|
| Manejo de credenciales y contraseñas | Cuentas compartidas en producción y ventas; contraseñas sin vencimiento; privilegios administrativos en todos los equipos |
| Riesgos de phishing y correo malicioso | No existen filtros anti-spam ni anti-phishing en el correo administrado por los dueños |
| Uso seguro de WhatsApp y redes sociales | Datos de clientes —incluyendo datos bancarios— compartidos por WhatsApp, Instagram y Facebook en gerencias de ventas y logística |
| Clasificación y tratamiento de la información | Ausencia de criterios formales de clasificación; obligaciones de la Ley N.º 25.326 sobre datos personales de clientes |
| Uso aceptable de equipos y software | Instalación libre de software; 2 laptops personales sin controles; equipos obsoletos sin soporte |
| Procedimiento de reporte de incidentes | No existe procedimiento formal definido para comunicación y escalamiento |
| Importancia de respaldos | No existen respaldos de ningún tipo; riesgo de pérdida total de información |

### Periodicidad y registro

- Se realizará una **capacitación inicial** al ingreso de cada empleado o proveedor con acceso a sistemas.
- Se realizarán **actualizaciones periódicas** al menos **una vez al año**, o ante cambios significativos en la infraestructura, los sistemas o las amenazas identificadas.
- Los gerentes de área registrarán la asistencia y el contenido impartido, reportando a los dueños el cumplimiento del programa de capacitación.

---

## 6.2. Respuesta a Incidentes y Anomalías en Materia de Seguridad

Se establecerá un **procedimiento formal de comunicación y respuesta a incidentes**, actualmente inexistente, indicando la acción que ha de emprenderse al recibir un informe sobre incidentes o anomalías de seguridad.

> **Situación actual:** las decisiones ante emergencias o incidentes son tomadas por el dueño junto con los gerentes, pero **no existe una definición formal de responsabilidades ni un procedimiento documentado** para la comunicación interna de incidentes importantes.

### Procedimiento de reporte y escalamiento

Ante la detección de un supuesto incidente o violación de la seguridad, todo el personal deberá seguir la siguiente cadena de comunicación:

```
Usuario que detecta el incidente
        ↓ (reporte inmediato)
Gerente del área
        ↓
Dueños de la organización
        ↓ (si involucra sistemas, red o ERP)
Proveedor externo de sistemas
```

El procedimiento formal deberá contemplar, como mínimo:

1. **Detección y reporte inmediato:** cualquier empleado que detecte o sospeche un incidente de seguridad deberá informarlo de inmediato a su gerente de área, sin intentar ocultarlo ni resolverlo por cuenta propia si excede su competencia técnica.
2. **Evaluación inicial:** el gerente evaluará la gravedad del incidente y lo escalará a los dueños. Si el incidente involucra sistemas, accesos, malware, pérdida de datos o filtración de información de clientes, se contactará simultáneamente al proveedor externo de sistemas.
3. **Clasificación del incidente:** se categorizará según su impacto en confidencialidad, integridad o disponibilidad, con especial atención a incidentes que involucren **datos personales o bancarios de clientes** (obligaciones Ley N.º 25.326).
4. **Contención y resolución:** el proveedor externo de sistemas indicará las acciones técnicas necesarias para la contención y resolución. Los dueños coordinarán las decisiones de negocio y la comunicación interna.
5. **Registro y seguimiento:** todo incidente deberá quedar documentado con fecha, descripción, personas involucradas, acciones tomadas y resolución. El responsable formal de seguridad de la información —una vez designado— tendrá a cargo el seguimiento, documentación y análisis de los incidentes reportados.
6. **Lecciones aprendidas:** tras la resolución, se evaluará si se requieren cambios en controles, capacitación o procedimientos para prevenir recurrencias.

### Tipos de incidentes prioritarios para Inmemorian

En función de las amenazas identificadas en el relevamiento, se consideran de **prioridad alta** los siguientes tipos de incidentes:

| Tipo de incidente | Ejemplo en el contexto de Inmemorian |
|---|---|
| Pérdida o filtración de datos de clientes | Envío de datos bancarios o personales por WhatsApp/redes sociales a destinatarios no autorizados |
| Pérdida total de información | Falla de hardware en equipos obsoletos sin respaldos existentes |
| Acceso no autorizado | Uso de cuentas compartidas que impide identificar al responsable de una acción |
| Malware o phishing | Correo malicioso sin filtros anti-phishing; instalación libre de software |
| Incidente con proveedor externo | Acceso administrativo del proveedor de sistemas sin trazabilidad ni acuerdos formales |

Los dueños, en coordinación con el responsable formal de seguridad que se designe y el proveedor externo de sistemas, revisarán periódicamente los incidentes registrados para identificar tendencias y definir acciones correctivas.

---

# 7. Seguridad Física y Ambiental

La seguridad física y ambiental brinda el marco para minimizar los riesgos de daños e interferencias a la información y a las operaciones de Inmemorian. Asimismo, pretende evitar el riesgo de accesos físicos no autorizados mediante el establecimiento de perímetros de seguridad en cada una de sus locaciones.

El relevamiento de la situación actual evidenció que la organización opera con **infraestructura informática distribuida en tres sedes** —Parque Industrial, Local Inmemorian y Local La Roca—, cada una con red ad-hoc y equipos accesibles al personal sin controles formales de acceso físico. En el Parque Industrial, el entorno productivo de tratamiento de piedras (polvo, humedad, vibraciones) representa un riesgo ambiental adicional para el equipamiento informático. En los locales comerciales, los **móviles corporativos** utilizados para atención a clientes vía WhatsApp e Instagram permanecen expuestos en mostradores y escritorios. Asimismo, **no existe un proceso definido para altas y bajas de equipos**, y se utilizan **2 computadoras portátiles personales** en modalidad híbrida sin controles sobre su resguardo físico.

Adicionalmente, parte de la información operativa —pedidos, diseños de placas conmemorativas, datos de clientes— puede encontrarse en soporte físico o visible en pantallas de las estaciones de trabajo, lo que hace necesario establecer pautas de escritorios y pantallas limpias acordes al contexto de la organización.

## Objetivo

- Prevenir e impedir accesos no autorizados, daños e interferencias a las sedes, instalaciones e información de Inmemorian.
- Proteger el equipamiento de procesamiento de información ubicándolo en áreas adecuadas y resguardadas, con medidas de seguridad y controles de acceso apropiados a cada locación.
- Controlar los factores ambientales que podrían perjudicar el correcto funcionamiento del equipamiento informático que alberga la información de la organización.
- Implementar medidas para proteger la información manejada por el personal en el marco de sus labores habituales, incluyendo el uso de dispositivos móviles y equipos personales.

## Alcance

Esta política se aplica a todos los recursos físicos relativos a los sistemas de información de Inmemorian en sus tres locaciones operativas:

| Locación | Equipamiento informático | Características del entorno |
|---|---|---|
| **Parque Industrial** | 1 módem/router WiFi, 1 PC de producción, 2 PC de dueños | Entorno industrial: polvo de piedra, humedad, maquinaria. Área de producción y administración de dueños. |
| **Local Inmemorian** | 1 módem/router WiFi, 1 PC de ventas, 1 móvil corporativo | Local comercial con atención al público. Acceso de clientes y visitantes. |
| **Local La Roca** | 1 módem/router WiFi, 2 PC de ventas, 1 móvil corporativo | Local comercial con atención al público. Acceso de clientes y visitantes. |

Comprende además: cableado de red y energía, routers WiFi, equipos personales utilizados para trabajo (2 laptops), medios de almacenamiento removibles, documentación en papel, y cualquier servidor o infraestructura administrada por el proveedor externo de sistemas cuya ubicación física deba ser relevada e incorporada al inventario de activos.

## Responsabilidades

Dado que Inmemorian **no cuenta con un responsable formal del área de sistemas ni con un área de Seguridad de la Información dedicada**, las funciones se distribuyen de la siguiente manera:

### Dueños de la organización

- Definir, junto con el proveedor externo de sistemas y los gerentes, las medidas de seguridad física y ambiental para el resguardo de los activos críticos, en función del análisis de riesgos.
- Aprobar los niveles de acceso físico a las áreas donde se ubican los equipos de los dueños (Parque Industrial) y supervisar su cumplimiento.
- Autorizar el retiro de equipamiento de las sedes para mantenimiento o desafectación.
- Asumir provisionalmente la función de **responsable formal de seguridad de la información** hasta que se formalice la designación.

### Proveedor externo de sistemas

- Coordinar la implementación de las medidas de seguridad física y ambiental definidas para el equipamiento bajo su administración (servidores, infraestructura de red, sistemas ERP).
- Controlar el mantenimiento del equipamiento informático y documentar las intervenciones realizadas.
- Asesorar a los dueños y gerentes en la ubicación segura de equipos, protección eléctrica y resguardo de copias de seguridad una vez implementadas.

### Gerentes de área

Cada gerente (Ventas de Placas Conmemorativas y Profesionales, Ventas de Mesadas, Producción y Logística) definirá los niveles de acceso físico del personal de su área a las estaciones de trabajo, móviles corporativos y documentación bajo su responsabilidad.

| Gerencia | Locación principal | Activos bajo su custodia física |
|---|---|---|
| Gerencia de Producción | Parque Industrial | PC de producción |
| Gerencia de Ventas (Placas) | Local Inmemorian / Parque Industrial | PC de ventas, móvil corporativo |
| Gerencia de Ventas (Mesadas) | Local La Roca | PC de ventas, móvil corporativo |
| Gerencia de Logística | Parque Industrial | Equipos vinculados a logística |

### Todo el personal

Es responsable del cumplimiento de la política de **escritorios y pantallas limpias**, para la protección de la información relativa al trabajo diario en oficinas, locales comerciales y planta de producción.

---

## 7.1. Perímetro de Seguridad Física

La protección física se llevará a cabo mediante barreras y medidas de control adecuadas al tamaño y operación de Inmemorian, en cada una de sus tres sedes.

### Parque Industrial

- El área donde se ubican las **2 PC de los dueños** y la **PC de producción** deberá delimitarse como zona de acceso restringido, separada del piso de producción cuando sea posible, para reducir la exposición a polvo, humedad y circulación no autorizada.
- El **módem/router WiFi** deberá ubicarse en un lugar elevado y protegido, fuera del alcance directo de maquinaria y procesos de corte o pulido de piedras.
- Se evaluará la instalación de cerradura o control de acceso en el espacio que alberga el equipamiento informático crítico.

### Locales comerciales (Inmemorian y La Roca)

- Las estaciones de trabajo de ventas deberán ubicarse en áreas del local no accesibles directamente al público, o con orientación de pantalla que impida la visualización de información de clientes por terceros.
- Los **móviles corporativos** no deberán permanecer desatendidos en mostradores accesibles al público; se dispondrán en cajones con llave o bajo custodia del personal de turno al finalizar la jornada.

### Infraestructura del proveedor externo

- El proveedor externo de sistemas deberá documentar la ubicación física de servidores e infraestructura crítica (ERP, portales web) bajo su administración, y garantizar que dichas instalaciones cuenten con controles de acceso físico y ambientales acordes a la criticidad de la información que procesan.

> **Situación actual:** no existe delimitación formal de perímetros de seguridad ni registro de la ubicación física de la infraestructura administrada por el proveedor externo. Su relevamiento e incorporación al inventario de activos constituye una acción prioritaria.

---

## 7.2. Controles de Acceso Físico

Las áreas donde se ubica equipamiento de procesamiento de información deberán resguardarse mediante controles de acceso físico. Dada la escala de la organización (~8 empleados), los controles serán proporcionales pero documentados.

Los controles de acceso físico tendrán, como mínimo, las siguientes características:

- **Supervisión de visitantes:** en Parque Industrial y locales comerciales, todo visitante que requiera acceder a áreas donde haya equipamiento informático deberá ser acompañado por personal autorizado. Se registrará fecha, horario, nombre y motivo de la visita en un libro o registro digital.
- **Acceso restringido a información clasificada:** el acceso a equipos que procesen Información Clasificada —especialmente datos personales y bancarios de clientes— quedará limitado exclusivamente a personas autorizadas por los dueños o el gerente del área. Se mantendrá un registro que permita auditar los accesos concedidos.
- **Revisión periódica:** los gerentes de área, en coordinación con los dueños, revisarán **al menos una vez al año** los derechos de acceso físico a las estaciones de trabajo, móviles corporativos y documentación bajo su responsabilidad.

### Controles específicos por locación

| Locación | Control mínimo a implementar |
|---|---|
| Parque Industrial | Acceso a PC de producción y PC de dueños limitado al personal autorizado; bloqueo de sesión al ausentarse del puesto. |
| Local Inmemorian | PC de ventas y móvil corporativo bajo custodia del personal de turno; pantalla orientada para evitar visualización por clientes. |
| Local La Roca | Idem Local Inmemorian para las 2 PC de ventas y el móvil corporativo. |
| Equipos personales (híbrido) | Las 2 laptops personales utilizadas para trabajo deberán contar con bloqueo por contraseña y no almacenarse en vehículos o espacios públicos sin protección. |

---

## 7.3. Ubicación y Protección del Equipamiento y Copias de Seguridad

El equipamiento y las copias de seguridad serán ubicados y protegidos de manera que se reduzcan los riesgos ocasionados por amenazas ambientales, robos y accesos no autorizados.

### Ubicación del equipamiento

- Las estaciones de trabajo en el **Parque Industrial** deberán ubicarse alejadas de fuentes de polvo, líquidos y vibraciones intensas propias del procesamiento de mármol, granito y otras piedras. Se recomienda el uso de gabinetes cerrados o cubiertas protectoras para teclados y equipos.
- Los **routers WiFi** de las tres locaciones deberán instalarse en posición elevada y fija, con acceso restringido al personal autorizado y al proveedor externo de sistemas.
- Los **móviles corporativos** deberán contar con funda protectora, bloqueo por PIN o biometría, y política de no dejarlos conectados a cargadores públicos sin supervisión.

### Protección de copias de seguridad

> **Situación crítica identificada:** actualmente **no existen respaldos de ningún tipo** en la organización. Una vez implementado el sistema de respaldos previsto en el punto 8.3.1, las copias deberán almacenarse en:

- Un medio **offline o fuera del sitio** (disco externo en caja fuerte o ubicación alternativa), separado de los equipos de producción.
- Instalaciones con control de acceso físico, distintas de las áreas de mayor circulación de clientes o personal no autorizado.
- Condiciones ambientales adecuadas: seco, temperatura controlada, protegido de polvo en el Parque Industrial.

El proveedor externo de sistemas, en coordinación con los dueños y los propietarios de información de cada área, determinará la ubicación definitiva de las copias de resguardo conforme a la criticidad de los datos respaldados.

---

## 7.4. Suministros de Energía

El equipamiento informático estará protegido frente a posibles fallas en el suministro de energía u otras anomalías eléctricas, dado que la organización considera que **todos los servicios son importantes para la continuidad operativa** y la dependencia de los sistemas informáticos es del **75 %**.

### Medidas a implementar

| Medida | Aplicación |
|---|---|
| **Estabilizadores o UPS** | PC de producción y PC de dueños en Parque Industrial; PC de ventas en cada local comercial. Prioridad en equipos que ejecutan los ERP. |
| **Protección de routers** | Los 3 módem/router WiFi deberán contar al menos con estabilizador de tensión. |
| **Procedimiento ante corte de energía** | El personal de cada locación deberá conocer el procedimiento: guardar trabajo en curso, apagar equipos de forma ordenada si el corte es prolongado, y reportar al proveedor externo de sistemas ante daños o reinicios inesperados. |
| **Móviles corporativos** | Mantener batería suficiente durante la jornada laboral; no depender exclusivamente de cargadores en áreas públicas del local. |

> **Situación actual:** no se relevó la existencia de UPS ni estabilizadores en ninguna locación. Su incorporación es una acción prioritaria, especialmente en el Parque Industrial donde las interrupciones podrían afectar la PC de producción vinculada al ERP.

---

## 7.5. Seguridad del Cableado

El cableado de energía eléctrica y de comunicaciones que transporta datos o brinda apoyo a los servicios de información estará protegido contra intercepción, daño o desconexión accidental.

Dado que cada locación opera con una **red ad-hoc independiente** (sin segmentación ni cableado estructurado formal), se establecen los siguientes lineamientos:

- Los cables de red y alimentación de las estaciones de trabajo no deberán transitar por zonas de alto tránsito de clientes, maquinaria o manipulación de materiales en el Parque Industrial, donde puedan sufrir daño mecánico.
- Las conexiones entre routers y equipos deberán ser fijas siempre que sea posible; se evitará el uso de extensiones eléctricas en mal estado o sobrecargadas.
- Cualquier modificación del cableado deberá ser realizada o autorizada por el proveedor externo de sistemas, registrándose como cambio operativo conforme al punto 8.1.1.
- En los locales comerciales, los cables no deberán quedar expuestos en mostradores donde clientes o visitantes puedan desconectarlos o acceder a los puertos del router.

---

## 7.6. Mantenimiento de Equipos

Se realizará el mantenimiento del equipamiento para asegurar su disponibilidad e integridad permanentes, en un contexto donde **la mayoría de los equipos opera con sistemas operativos obsoletos sin soporte**.

### Mantenimiento preventivo y correctivo

- El **proveedor externo de sistemas** será responsable del mantenimiento de servidores, infraestructura de red, sistemas ERP y portales web bajo su administración.
- Los gerentes de área serán responsables de reportar fallas en las estaciones de trabajo y móviles corporativos de su locación, canalizando la solicitud al proveedor externo de sistemas o a los dueños según corresponda.
- Se establecerá un **calendario de mantenimiento preventivo** para los 6 equipos corporativos y los 2 móviles, con prioridad en aquellos que procesan información de criticidad alta.

### Retiro de equipamiento para mantenimiento externo

Cuando sea necesario retirar equipamiento de una sede de Inmemorian para su reparación o mantenimiento:

1. Se registrará la salida del equipo (fecha, responsable, motivo, destino) en el inventario de activos.
2. Se realizará previamente una **copia de resguardo** de la información contenida, una vez implementado el sistema de respaldos.
3. Se eliminará o cifrará la información confidencial almacenada localmente en el equipo, especialmente datos de clientes y credenciales de acceso.
4. Solo los **dueños** autorizarán el retiro de equipamiento corporativo; los equipos personales utilizados para trabajo deberán seguir el mismo procedimiento respecto de la información empresarial que contengan.

> **Situación actual:** no existe proceso definido para altas y bajas de equipos ni registro de salidas para mantenimiento. Su formalización es una acción prioritaria vinculada al inventario de activos del punto 5.1.

---

## 7.7. Desafectación Segura de los Equipos

La información puede verse comprometida por una desafectación o reutilización descuidada del equipamiento. En Inmemorian, donde los usuarios poseen **privilegios administrativos** en sus equipos y pueden **instalar software libremente**, el riesgo de residuos de información en discos desafectados es particularmente elevado.

### Procedimiento de desafectación

Antes de dar de baja, vender, donar o desechar cualquier equipo —corporativo o personal que haya almacenado información empresarial—:

1. El gerente del área o los dueños autorizarán la baja en el inventario de activos.
2. El **proveedor externo de sistemas** realizará la eliminación segura de los medios de almacenamiento:
   - **Sobrescritura segura** de discos que vayan a reutilizarse.
   - **Destrucción física** de discos o medios removibles que contengan Información Clasificada y no vayan a reutilizarse.
3. No se utilizarán las funciones de borrado estándar del sistema operativo como único método para equipos que hayan procesado datos de clientes, información financiera o credenciales de los ERP.
4. Se documentará el proceso de desafectación (equipo, fecha, método aplicado, responsable).

### Medios removibles

Los pen drives, discos externos u otros medios removibles utilizados para transferir información entre locaciones o hacia proveedores externos deberán ser inventariados y sometidos al mismo procedimiento de eliminación segura al dejar de utilizarse.

---

## 7.8. Políticas de Escritorios y Pantallas Limpias

Se adoptará una política de **escritorios limpios** para proteger documentos en papel, dispositivos de almacenamiento removibles y móviles corporativos, y una política de **pantallas limpias** en todas las instalaciones de procesamiento de información, a fin de reducir los riesgos de acceso no autorizado, pérdida y daño de la información.

Esta política es especialmente relevante en Inmemorian dado que:

- Los **locales comerciales reciben clientes** que podrían visualizar información en pantallas o documentos dejados a la vista.
- Los **móviles corporativos** contienen conversaciones de WhatsApp con datos de clientes, incluyendo en algunos casos **datos bancarios**.
- No existen controles sobre dispositivos personales que podrían quedar desatendidos en modalidad híbrida.

### Lineamientos obligatorios

- Cuando corresponda, los documentos en papel (pedidos, diseños de placas, comprobantes) y los medios informáticos removibles deben almacenarse bajo llave, **especialmente fuera del horario de trabajo** y en locales comerciales al cierre.
- La información sensible o confidencial, una vez impresa, debe retirarse de la impresora de inmediato.
- **Bloquear la pantalla** (Windows + L) o cerrar las aplicaciones al alejarse del escritorio, en todas las locaciones. Esto es crítico en los locales de ventas con atención al público.
- No dejar **pen drives** ni otros medios removibles conectados a los equipos.
- Los **móviles corporativos** no deben dejarse desbloqueados sobre mostradores; activar bloqueo automático por inactividad.
- Apagar el equipo al ausentarse por períodos prolongados, especialmente al cierre de los locales comerciales.
- **No escribir contraseñas** en notas adhesivas ni guardarlas visibles en la oficina —práctica de riesgo elevado dado que las contraseñas actualmente no poseen vencimiento y varias cuentas son compartidas.
- Borrar pizarras o superficies de escritura donde se hayan anotado datos de clientes, pedidos o credenciales.

### Lineamientos adicionales para modalidad híbrida

El personal administrativo que utilice las **2 laptops personales** para trabajo deberá:

- No trabajar con información de clientes en espacios públicos (cafeterías, transporte) sin protección de pantalla.
- No dejar la laptop desatendida en el vehículo o domicilio sin bloqueo de sesión.
- Almacenar documentación impresa de la organización en lugar seguro, no mezclada con documentación personal.

---

# 8. Gestión de Comunicaciones y Operaciones

Es conveniente establecer procedimientos que aseguren el funcionamiento correcto y seguro de las instalaciones de procesamiento de información y comunicaciones de Inmemorian, a fin de minimizar los riesgos de incidentes producidos por la manipulación indebida de información operativa.

El relevamiento evidenció brechas críticas en este ámbito: **ausencia total de respaldos**, **inexistencia de firewall perimetral** en las tres locaciones, **ausencia de mecanismos de monitoreo y registros centralizados**, **sin filtros anti-spam ni anti-phishing** en el correo electrónico, **instalación libre de software** por parte de los usuarios, **sistemas sin actualizaciones regulares**, y **dependencia operativa del proveedor externo de sistemas** sin acuerdos formales de nivel de servicio. La organización no desarrolla software propio, por lo que la separación de ambientes de desarrollo y producción aplica principalmente a los sistemas administrados por el proveedor externo (ERP, portales web).

## Objetivo

- Garantizar el funcionamiento correcto y seguro de las instalaciones de procesamiento de información y comunicaciones en las tres locaciones de Inmemorian.
- Establecer responsabilidades y procedimientos para su gestión y operación, incluyendo instrucciones operativas y segregación de funciones en la medida que la estructura organizacional lo permita.
- Implementar controles operativos que mitiguen las brechas identificadas en el relevamiento, con prioridad en respaldos, protección contra software malicioso y gestión de cambios.

## Alcance

Todas las instalaciones de procesamiento y transmisión de información de Inmemorian:

- **Infraestructura local:** 6 estaciones de trabajo, 2 laptops personales, 2 móviles corporativos, 3 routers WiFi en Parque Industrial, Local Inmemorian y Local La Roca.
- **Sistemas críticos:** 2 ERP, portales web, correo electrónico (administrado por los dueños).
- **Canales de comunicación:** WhatsApp, Instagram, Facebook utilizados operacionalmente por ventas, producción y logística.
- **Servicios administrados por terceros:** servidores, red, usuarios, accesos y sistemas bajo administración del proveedor externo de sistemas; información financiera del proveedor externo de finanzas; datos de importaciones del proveedor externo de importaciones.

## Responsabilidades

### Dueños de la organización

En su carácter de máxima autoridad y administradores del correo electrónico corporativo, tendrán a su cargo:

- Establecer criterios de aprobación para nuevos sistemas de información en materia de seguridad.
- Aprobar cambios e inversiones tecnológicas sobre la base de propuestas de las distintas áreas y del proveedor externo de sistemas.
- Definir y documentar la norma de uso del correo electrónico e Internet.
- Designar o asumir provisionalmente la función de **responsable formal de seguridad de la información**.
- Verificar el cumplimiento de las normas, procedimientos y controles establecidos.
- Evaluar, junto con el proveedor externo de sistemas, los contratos y acuerdos con terceros para garantizar la incorporación de consideraciones de seguridad de la información.

### Proveedor externo de sistemas

En su carácter de administrador de servidores, red, usuarios, accesos y los dos ERP, tendrá a su cargo:

- Controlar la existencia de documentación actualizada relacionada con los procedimientos de comunicaciones y operaciones bajo su gestión.
- Evaluar el posible impacto operativo de los cambios previstos a sistemas y equipamiento, y verificar su correcta implementación.
- **Implementar y controlar las copias de resguardo** de información, así como la prueba periódica de su restauración —actualmente inexistentes y de máxima prioridad.
- Asegurar el registro de las actividades realizadas en los sistemas bajo su administración.
- Implementar los controles de seguridad definidos: protección contra software malicioso, firewall perimetral, detección de accesos no autorizados.
- Definir e implementar procedimientos para la administración de medios informáticos de almacenamiento y su eliminación segura.
- Participar en el tratamiento de incidentes de seguridad, de acuerdo con los procedimientos establecidos en el punto 6.2.

### Gerentes de área

Como propietarios de la información de su área:

- Determinar, junto con el proveedor externo de sistemas y los dueños, los requerimientos de resguardo para el software y los datos bajo su gestión, en función de su criticidad (punto 5.2).
- Reportar de inmediato incidentes o anomalías detectadas en los equipos y sistemas de su locación.
- Velar por el cumplimiento de las normas de uso del correo electrónico, Internet y canales de comunicación en su equipo.

### Todo el personal

- Utilizar los sistemas y canales de comunicación conforme a las normas establecidas.
- No instalar software sin autorización de los dueños o el proveedor externo de sistemas.
- Reportar de inmediato cualquier comportamiento anómalo de los sistemas, sospecha de malware o correos fraudulentos.

---

## 8.1. Procedimientos y Responsabilidades Operativas

### 8.1.1. Control de Cambios en las Operaciones

Se definirán procedimientos para el control de los cambios en el ambiente operativo y de comunicaciones de Inmemorian. Actualmente, **las decisiones de cambios e inversiones tecnológicas son tomadas por los dueños** sobre la base de propuestas de las distintas áreas, sin un procedimiento formal documentado.

Todo cambio en componentes operativos —instalación de software, modificación de red, actualización de ERP, cambios en portales web, incorporación de nuevos equipos— deberá:

1. Ser **evaluado previamente** en aspectos técnicos y de seguridad por el proveedor externo de sistemas.
2. Ser **aprobado por los dueños** antes de su implementación.
3. Ser **comunicado al gerente del área** afectada.
4. Quedar registrado en un **registro de cambios** con fecha, descripción, solicitante, aprobador, evaluación de impacto y resultado.

Los cambios de mayor impacto —modificaciones en ERP, infraestructura de red, políticas de acceso, implementación de respaldos— requerirán evaluación explícita de su efecto sobre la seguridad de la información y la continuidad operativa.

| Tipo de cambio | Ejemplo en Inmemorian | Aprobación requerida |
|---|---|---|
| Cambio de red | Instalación de firewall, segmentación VLAN | Dueños + proveedor externo de sistemas |
| Cambio en ERP | Actualización de módulo, nueva integración | Dueños + gerente del área + proveedor externo |
| Alta de equipo | Incorporación de nueva PC en Local La Roca | Dueños + gerente de área |
| Cambio en portal web | Publicación de nuevo catálogo de mesadas | Dueños + gerencia de Ventas de Mesadas |
| Instalación de software | Antivirus, gestor de contraseñas | Proveedor externo de sistemas + dueños |

### 8.1.2. Procedimientos de Manejo de Incidentes

Se establecerán funciones y procedimientos de manejo de incidentes que garanticen una respuesta rápida, eficaz y sistemática a los incidentes relativos a seguridad de la información.

> **Situación actual:** no existe una definición formal de responsabilidades ante incidentes ni un procedimiento documentado para la comunicación interna. Las decisiones son tomadas por el dueño junto con los gerentes de forma ad-hoc.

El procedimiento detallado de reporte y escalamiento se encuentra definido en el **punto 6.2** del presente plan. En el ámbito de comunicaciones y operaciones, se complementa con las siguientes disposiciones:

- Ante un incidente que afecte sistemas, red, ERP o portales web, el **proveedor externo de sistemas** deberá ser contactado de inmediato por los dueños o el gerente que reciba el reporte.
- El proveedor documentará las acciones técnicas de contención y resolución, y las compartirá con los dueños para el registro centralizado de incidentes.
- Los incidentes que involucren **pérdida de datos** —especialmente crítico dado que no existen respaldos— o **filtración de datos de clientes** deberán tratarse con máxima prioridad, evaluando las obligaciones de la Ley N.º 25.326.

### 8.1.3. Separación entre Instalaciones de Desarrollo e Instalaciones Operativas

Inmemorian **no desarrolla software propio** ni cuenta con personal de desarrollo interno. Los sistemas críticos (2 ERP, portales web) son administrados por el proveedor externo de sistemas.

En este contexto:

- Los ambientes de **desarrollo, prueba y producción** de los ERP y portales web deberán estar separados en la infraestructura administrada por el proveedor externo de sistemas.
- El proveedor externo de sistemas deberá documentar las reglas para la transferencia de configuraciones o actualizaciones desde ambientes de prueba hacia producción.
- Ningún cambio en sistemas productivos deberá aplicarse sin haber sido probado previamente en un ambiente no productivo, salvo emergencia documentada y aprobada por los dueños.
- El personal de Inmemorian **no deberá realizar pruebas, instalaciones o modificaciones** en los ERP o portales web sin autorización y supervisión del proveedor externo de sistemas.

---

## 8.2. Protección Contra Software Malicioso

Los dueños, con el asesoramiento del responsable formal de seguridad de la información que se designe, definirán los controles de detección y prevención para la protección contra software malicioso. El **proveedor externo de sistemas** implementará dichos controles en servidores, red y estaciones de trabajo.

> **Situación actual:** no se relevó con certeza qué antivirus o soluciones de seguridad están instaladas en cada equipo. No existen filtros anti-spam ni anti-phishing. Los usuarios pueden instalar software libremente. Los sistemas no se actualizan regularmente.

### Controles a implementar

| Control | Responsable | Prioridad |
|---|---|---|
| **Antivirus corporativo** en las 6 estaciones de trabajo, 2 laptops y servidores | Proveedor externo de sistemas | Alta |
| **Actualización automática** de firmas de antivirus y parches de seguridad del sistema operativo Windows | Proveedor externo de sistemas | Alta |
| **Filtros anti-spam y anti-phishing** en el correo electrónico administrado por los dueños | Dueños + proveedor externo de sistemas | Alta |
| **Firewall perimetral (NGFW)** en cada una de las 3 locaciones | Proveedor externo de sistemas | Alta |
| **Restricción de instalación de software** por parte de usuarios | Dueños + gerentes de área | Media |
| **Capacitación** en identificación de phishing, archivos sospechosos y enlaces maliciosos | Gerentes de área (punto 6.1) | Alta |

El proveedor externo de sistemas deberá verificar periódicamente el estado de las protecciones implementadas y reportar a los dueños cualquier equipo sin antivirus activo, sin actualizaciones o con software no autorizado instalado.

---

## 8.3. Mantenimiento

### 8.3.1. Resguardo de la Información

El proveedor externo de sistemas, junto con los dueños y los **propietarios de información** (gerentes de área), determinarán los requerimientos para resguardar cada software o dato en función de su criticidad, conforme a la clasificación del punto 5.2.

> **Situación crítica identificada:** actualmente **no existen respaldos de ningún tipo**, **no se realizan copias de seguridad**, **no hay copias offline o inmutables**, y **nunca se probaron restauraciones**. Esta es la brecha operativa de mayor severidad identificada en el relevamiento.

#### Requerimientos de resguardo por criticidad

| Criticidad | Información / Sistema | Frecuencia mínima de respaldo | Retención |
|---|---|---|---|
| **Alta** | Datos personales y bancarios de clientes (ERP), registros contables (finanzas) | Diaria | 90 días mínimo; 1 copia offline mensual |
| **Alta** | Configuración y datos de los 2 ERP | Diaria | 90 días mínimo |
| **Media** | Pedidos, diseños de placas, portales web | Diaria o semanal según volumen | 60 días |
| **Media** | Datos de importaciones y proveedores | Semanal | 60 días |
| **Baja** | Material de marketing en redes sociales | Según necesidad | 30 días |

#### Implementación

- El **proveedor externo de sistemas** dispondrá y controlará la realización de las copias de resguardo, aplicando la estrategia **3-2-1** (tres copias, dos medios, una copia offline o fuera del sitio), conforme al plan técnico del capítulo de medidas técnicas.
- Se realizarán **pruebas de restauración** al menos **trimestralmente**, documentando fecha, alcance de la prueba, resultado y tiempo de recuperación.
- Los dueños serán informados del estado de los respaldos en un reporte mensual hasta que el sistema se encuentre estabilizado.

### 8.3.2. Registro de Actividades del Personal Operativo

El proveedor externo de sistemas asegurará el registro de las actividades relevantes realizadas en los sistemas bajo su administración (servidores, ERP, portales web, red).

> **Situación actual:** no poseen mecanismos de monitoreo ni registros centralizados.

#### Registros mínimos a implementar

- Accesos y acciones administrativas en servidores y ERP.
- Cambios de configuración en routers y firewall, una vez implementados.
- Ejecución y resultado de respaldos.
- Intentos de acceso fallidos a sistemas críticos.
- Instalación o desinstalación de software en estaciones de trabajo, una vez restringida la instalación libre.

Los registros deberán conservarse por un período mínimo de **6 meses** y estar protegidos contra modificación no autorizada. El acceso a los registros quedará limitado a los dueños y al proveedor externo de sistemas.

---

## 8.4. Administración y Seguridad de los Medios de Almacenamiento

### 8.4.1. Administración de Medios Informáticos Removibles

El proveedor externo de sistemas, con la asistencia de los dueños, implementará procedimientos para la administración y auditoría de medios informáticos removibles (pen drives, discos externos, tarjetas de memoria).

Dado que la organización opera con **tres locaciones independientes** y coordina operaciones mediante ERP y WhatsApp, es probable el uso de medios removibles para transferir archivos —especialmente diseños de placas e imágenes conmemorativas— entre sedes.

#### Lineamientos

- Todo medio removible utilizado para almacenar información de Inmemorian deberá registrarse en el inventario de activos.
- Los medios que contengan Información Clasificada deberán estar cifrados.
- Se prohibirá el uso de medios removibles personales no registrados para almacenar información de clientes o datos de los ERP.
- Los gerentes de área verificarán periódicamente que no existan pen drives conectados permanentemente a las estaciones de trabajo, conforme a la política de escritorios limpios (punto 7.8).

### 8.4.2. Eliminación de Medios de Información

El proveedor externo de sistemas, junto con los dueños, definirá procedimientos para la eliminación segura de los medios de información, respetando la normativa vigente —incluyendo la Ley N.º 25.326 en lo relativo a datos personales de clientes.

El procedimiento se coordinará con el punto 7.7 (Desafectación Segura de los Equipos) y contemplará:

- Eliminación segura de medios removibles al finalizar su vida útil.
- Borrado certificado de información de clientes cuando los medios dejen de ser necesarios.
- Registro de cada operación de eliminación (medio, fecha, método, responsable).

---

## 8.5. Intercambios de Información y Software

### 8.5.1. Seguridad del Correo Electrónico

La administración del correo electrónico corporativo está actualmente a cargo de los **dueños**. Se definirán controles y normas claras para su uso seguro.

#### Controles a implementar

- **Filtros anti-spam y anti-phishing**, actualmente inexistentes, como medida prioritaria.
- Restricción del envío de Información Clasificada —especialmente datos personales y bancarios de clientes— sin cifrado o por canales no autorizados.
- Prohibición de reenviar correos con datos de clientes a cuentas personales o a WhatsApp.
- Uso de contraseñas individuales con vencimiento periódico para las cuentas de correo corporativo.
- Implementación de **MFA** en las cuentas de correo de los dueños y gerentes, como primer paso hacia la autenticación multifactor en sistemas críticos.

#### Normas de uso del correo electrónico

| Permitido | Prohibido |
|---|---|
| Comunicación laboral con clientes, proveedores y entre áreas | Compartir credenciales de acceso al correo |
| Envío de pedidos y documentación comercial por canales autorizados | Enviar datos bancarios de clientes sin protección adecuada |
| Reportar incidentes de seguridad a los dueños | Abrir archivos adjuntos de remitentes desconocidos sin verificar |
| Uso de firma corporativa en comunicaciones oficiales | Utilizar el correo corporativo para fines personales no autorizados |

### 8.5.2. Sistemas de Acceso Público

Inmemorian mantiene **portales web** utilizados por las gerencias de ventas para la comercialización de placas conmemorativas, placas profesionales, placas para monumentos y mesadas. Asimismo, utiliza **Instagram, Facebook y WhatsApp** como canales de comunicación y comercialización con acceso público.

Se tomarán recaudos para la protección de la integridad de la información publicada electrónicamente, a fin de prevenir la modificación no autorizada que podría dañar la reputación de la organización.

#### Proceso de autorización para publicación

1. Todo contenido destinado a portales web o redes sociales deberá ser revisado y aprobado por el **gerente del área** correspondiente antes de su publicación.
2. Los dueños autorizarán contenido institucional, cambios en portales web y publicaciones que involucren información sensible.
3. **No se publicarán** datos personales de clientes, datos bancarios, información financiera interna ni credenciales de acceso en ningún canal público.
4. El proveedor externo de sistemas garantizará los controles de acceso administrativo sobre los portales web, de modo que solo personal autorizado pueda modificar el contenido publicado.
5. Ante sospecha de modificación no autorizada de un portal web o perfil de red social, se activará el procedimiento de incidentes (puntos 6.2 y 8.1.2).

#### Controles sobre canales de comunicación operativa

Dado el uso intensivo de **WhatsApp** para coordinar ventas, producción y logística:

- Se establecerán lineamientos sobre qué información puede compartirse por WhatsApp (información de criticidad baja o media sin datos personales sensibles) y qué información debe circular exclusivamente por ERP o correo electrónico (datos personales, datos bancarios —criticidad alta).
- Los **móviles corporativos** deberán tener bloqueo de pantalla, copia de seguridad periódica de conversaciones comerciales relevantes cuando sea técnicamente viable, y procedimiento de borrado seguro al cambio de titular del equipo.
- Las cuentas de Instagram y Facebook utilizadas comercialmente deberán tener contraseñas robustas, acceso limitado al personal autorizado y revisión periódica de permisos de publicación.

---

# 9. Control de Accesos

El acceso por medio de un sistema de restricciones y excepciones a la información es la base de todo sistema de seguridad de la información. Para impedir el acceso no autorizado a los sistemas de información de Inmemorian se deben implementar procedimientos formales para controlar la asignación de derechos de acceso a los sistemas, bases de datos y servicios de información (2 ERP, portales web, correo electrónico, redes sociales comerciales), los cuales deben estar claramente documentados, comunicados y controlados en cuanto a su cumplimiento.

El relevamiento de la situación actual evidenció brechas severas en esta materia: existen **credenciales compartidas** —especialmente en Producción y Ventas, debido a cambios de turno y rotación de personal—, **no se utiliza autenticación multifactor (MFA)**, las contraseñas **no poseen vencimiento**, los usuarios tienen **privilegios administrativos en sus equipos**, **no existen controles sobre la navegación web** y **no hay registros de acceso ni monitoreo centralizado**. Asimismo, la administración de usuarios y accesos está a cargo del **proveedor externo de sistemas**, mientras que la **autorización de permisos especiales recae en los dueños**, sin un procedimiento formal documentado entre ambos.

Los procedimientos que se definan deberán comprender todas las etapas del ciclo de vida de los accesos de los usuarios, desde el registro inicial de nuevos usuarios hasta la privación final de derechos de aquellos que ya no requieren acceso —situación particularmente relevante dada la rotación de personal en los locales comerciales.

La cooperación de los usuarios es esencial para la eficacia de la seguridad. Por lo tanto, es necesario concientizar a los aproximadamente 8 empleados de la organización acerca de sus responsabilidades en el mantenimiento de controles de acceso eficaces, en particular las relacionadas con el uso de contraseñas individuales y la seguridad del equipamiento.

## Objetivo

- Impedir el acceso no autorizado a los sistemas de información, bases de datos y servicios de información de Inmemorian (ERP, portales web, correo electrónico, redes sociales comerciales).
- Eliminar progresivamente el uso de cuentas compartidas, implementando identificadores únicos por usuario.
- Implementar seguridad en los accesos mediante técnicas de autenticación y autorización, incorporando MFA en los sistemas críticos.
- Controlar la seguridad en la conexión entre las redes de las tres locaciones e Internet.
- Registrar y revisar eventos y actividades críticas llevadas a cabo por los usuarios en los sistemas.
- Concientizar a los usuarios respecto de su responsabilidad frente a la utilización de contraseñas y equipos.
- Garantizar la seguridad de la información cuando se utilizan los móviles corporativos y las laptops personales en modalidad híbrida.

## Alcance

Esta política se aplica a todas las formas de acceso de aquellos a quienes se les haya otorgado permisos sobre los sistemas de información, bases de datos o servicios de información de Inmemorian, cualquiera sea la función que desempeñen:

- Los **8 empleados** de la organización, incluyendo el personal administrativo en modalidad híbrida.
- Los **dueños** y los **gerentes de área** (Ventas de Placas Conmemorativas y Profesionales, Ventas de Mesadas, Producción y Logística).
- El **personal tercerizado**: proveedores externos de Sistemas, Finanzas e Importaciones, en la medida en que acceden a sistemas o información de la organización.

Comprende los accesos a: los 2 ERP, los portales web, el correo electrónico corporativo, las cuentas comerciales de WhatsApp, Instagram y Facebook, las 6 estaciones de trabajo, las 2 laptops personales utilizadas para trabajo, los 2 móviles corporativos y los 3 routers WiFi de las locaciones Parque Industrial, Local Inmemorian y Local La Roca.

Asimismo, se aplica al proveedor externo de sistemas en su carácter de administrador de servidores, usuarios, accesos y conexiones de red.

## Responsabilidades

Dado que Inmemorian **no cuenta con un responsable formal del área de sistemas ni con un área de Seguridad de la Información dedicada**, las funciones se distribuyen de la siguiente manera:

### Dueños de la organización

En su carácter de autoridad que **autoriza permisos y accesos especiales**, tendrán a su cargo:

- Aprobar formalmente toda alta, modificación y baja de accesos a los sistemas críticos (ERP, portales web, correo electrónico).
- Definir, junto con el proveedor externo de sistemas, las normas y procedimientos para la gestión de accesos.
- Definir las pautas de utilización de Internet para todos los usuarios.
- Aprobar la asignación de privilegios administrativos, que deberán quedar limitados a los casos estrictamente necesarios.
- Verificar el cumplimiento de las pautas establecidas y concientizar a los usuarios sobre el uso apropiado de contraseñas y equipos.
- Asumir provisionalmente la función de **responsable formal de seguridad de la información** hasta que se formalice la designación.

### Proveedor externo de sistemas

En su carácter de administrador de servidores, usuarios y accesos:

- Implementar los métodos de autenticación y control de acceso definidos en los sistemas, bases de datos y servicios.
- Ejecutar las altas, modificaciones y bajas de usuarios **únicamente ante el pedido formal aprobado por los dueños**, conservando registro de cada solicitud.
- Implementar procedimientos para la activación y desactivación de derechos de acceso a las redes.
- Realizar una adecuada subdivisión de la red en cada locación e implementar el control de puertos y servicios.
- Definir e implementar los registros de eventos y actividades correspondientes a sistemas operativos y plataformas bajo su administración.
- Analizar e implementar, junto con los dueños, las medidas de control de acceso a Internet.
- Efectuar el control de los registros de auditoría generados por los sistemas, una vez implementados.

### Gerentes de área (propietarios de la información)

- Evaluar los riesgos a los cuales se expone la información de su área a fin de determinar los controles de acceso, autenticación y utilización a implementar en cada caso.
- Solicitar a los dueños la asignación o revocación de accesos para el personal a su cargo, informando de inmediato las desvinculaciones y cambios de funciones.
- Definir los eventos y actividades de usuarios a registrar en los sistemas de su incumbencia y la periodicidad de revisión.
- Llevar a cabo, junto con los dueños, un proceso formal y periódico —al menos **semestral**— de revisión de los derechos de acceso a la información de su área.

### Todo el personal

- Mantener en secreto sus credenciales individuales y no compartirlas bajo ninguna circunstancia, incluso ante cambios de turno.
- Cumplir las pautas de uso de contraseñas, Internet y equipos definidas en esta política.

---

## 9.1. Requerimientos para el Control de Acceso

### 9.1.1. Política de Control de Accesos

En la aplicación de controles de acceso se contemplarán los siguientes aspectos:

- Identificar los requerimientos de seguridad de cada una de las aplicaciones utilizadas: los 2 ERP, los portales web, el correo electrónico y las cuentas comerciales de redes sociales.
- Identificar toda la información relacionada con dichas aplicaciones, con especial atención a los **datos personales y bancarios de clientes** sujetos a obligaciones legales de protección (Ley N.º 25.326).
- Considerar la criticidad definida en la clasificación de activos (punto 5.2): las áreas de **Sistemas y Finanzas/Administración** manejan la información más sensible, y **todas las áreas excepto Producción** acceden a información crítica.

### 9.1.2. Reglas de Control de Acceso

Las reglas de control de acceso especificadas deberán:

- Indicar expresamente si las reglas son obligatorias u optativas.
- Establecerse sobre la premisa **"Todo debe estar prohibido a menos que se permita expresamente"**, en reemplazo de la situación actual donde los usuarios poseen privilegios administrativos y libertad de instalación de software.
- Controlar y registrar los cambios en los permisos de usuario, los cuales requerirán siempre aprobación de los dueños.

#### Matriz de acceso de referencia

| Rol | ERP | Portales web (administración) | Correo corporativo | Redes sociales comerciales | Datos bancarios de clientes |
|---|---|---|---|---|---|
| Dueños | Acceso total | Autorizan cambios | Administradores | Autorizan | Sí |
| Gerencias de Ventas | Módulos de ventas | Carga de contenido aprobado | Sí | Sí (cuentas de su área) | Limitado a su operación |
| Gerencia de Producción | Módulos de producción | No | No | No | No |
| Gerencia de Logística | Módulos de logística | No | Sí | No | No |
| Proveedor externo de sistemas | Administración técnica | Administración técnica | Soporte técnico | No | Solo con autorización expresa |
| Proveedores de Finanzas / Importaciones | Módulos de su incumbencia | No | Según necesidad | No | Según función, con autorización |

---

## 9.2. Administración de Accesos de Usuarios

Con el objetivo de impedir el acceso no autorizado a la información, se implementarán procedimientos formales para controlar la asignación de derechos de acceso a los sistemas, datos y servicios de información.

### 9.2.1. Registración de Usuarios

Los dueños, junto con el proveedor externo de sistemas, definirán un procedimiento formal de registro de usuarios para otorgar y revocar el acceso a todos los sistemas, bases de datos y servicios de información, el cual debe comprender:

- **Utilizar identificadores de usuario únicos** para cada uno de los 8 empleados, en cada sistema.
- **Eliminar progresivamente las cuentas compartidas** existentes en Producción y Ventas. El uso de identificadores grupales solo se permitirá cuando sea imprescindible por razones operativas documentadas (por ejemplo, la cuenta de atención de un local comercial), debiendo en tal caso registrarse qué persona la utilizó en cada turno.
- Verificar que el usuario tiene autorización del gerente de área (propietario de la información) y de los dueños para el uso del sistema, base de datos o servicio.
- Verificar que el nivel de acceso otorgado es adecuado para la función del usuario, conforme a la matriz de acceso del punto 9.1.2.
- Requerir que los usuarios firmen declaraciones señalando que comprenden y aceptan las condiciones de acceso.
- **Cancelar inmediatamente los derechos de acceso** de los usuarios que cambiaron de tareas, fueron desvinculados o cuya autorización fue revocada. Dada la rotación de personal en los locales, el gerente del área deberá comunicar la novedad a los dueños y al proveedor externo de sistemas **el mismo día** en que se produzca.
- Efectuar revisiones **semestrales** con el objeto de:
  - Cancelar identificadores y cuentas de usuario redundantes.
  - Inhabilitar y/o eliminar cuentas inactivas por un período mayor a 60 días.
  - Detectar y regularizar cuentas compartidas no autorizadas.

> **Situación actual:** existen credenciales individuales pero muchas son compartidas, principalmente en Producción y Ventas debido a cambios de turno y rotación de personal. La regularización de estas cuentas constituye una acción prioritaria, ya que impide atribuir las acciones realizadas en los sistemas a una persona determinada.

### 9.2.2. Administración de Contraseñas de Usuario

La asignación de contraseñas se controlará a través de un proceso de administración formal, mediante el cual deben respetarse los siguientes pasos:

- Requerir que los usuarios firmen una declaración por la cual se comprometen a mantener sus contraseñas personales en secreto.
- Garantizar que los usuarios cambien las contraseñas iniciales asignadas en el primer inicio de sesión.
- Almacenar las contraseñas solo en sistemas informáticos protegidos. Se evaluará la adopción de un **gestor de contraseñas corporativo** para reemplazar prácticas inseguras como anotarlas en papel (prohibidas por la política de escritorios limpios, punto 7.8).
- Configurar los sistemas de manera que permitan únicamente la utilización de **contraseñas robustas**: longitud mínima de 12 caracteres, combinación de mayúsculas, minúsculas, números y símbolos, y no reutilización de contraseñas anteriores.
- Establecer **vencimiento periódico** de contraseñas en los sistemas críticos —actualmente las contraseñas no poseen vencimiento— o, alternativamente, vencimiento ante cualquier indicio de compromiso, conforme a las buenas prácticas vigentes.
- Implementar **autenticación multifactor (MFA)**, comenzando por: cuentas de correo de dueños y gerentes, accesos administrativos a los ERP y portales web, y cuentas comerciales de redes sociales.

### 9.2.3. Administración de Contraseñas Críticas

Los dueños, junto con el proveedor externo de sistemas, definirán los procedimientos para la administración de las contraseñas críticas de la organización, entre ellas:

- Credenciales de administración de los 2 ERP y de los portales web.
- Credenciales de administración de los 3 routers WiFi (que deberán modificarse respecto de las de fábrica).
- Contraseña de administración del correo electrónico corporativo, hoy gestionada por los dueños.
- Credenciales de las cuentas comerciales de Instagram, Facebook y WhatsApp Business.

Estas contraseñas deberán resguardarse en sobre cerrado o gestor de contraseñas con acceso restringido a los dueños, de modo que la organización no dependa exclusivamente del proveedor externo para acceder a sus propios sistemas.

---

## 9.3. Responsabilidades del Usuario

### 9.3.1. Uso de Contraseñas

Los usuarios deben seguir buenas prácticas de seguridad en la selección y uso de contraseñas. Las contraseñas constituyen el principal medio de validación y autenticación de la identidad de un usuario en Inmemorian —actualmente el único, hasta tanto se implemente MFA— y, consecuentemente, un medio para establecer derechos de acceso a los sistemas.

Los usuarios deben cumplir las siguientes directivas:

- **Mantener las contraseñas en secreto.** No compartirlas con compañeros de turno, gerentes ni proveedores externos: si otra persona necesita acceso, debe solicitarse una cuenta propia.
- Cambiar la contraseña siempre que exista un posible indicio de compromiso del sistema, informando además a los dueños.
- Seleccionar contraseñas de calidad que:
  - Sean fáciles de recordar para el usuario.
  - No estén basadas en datos que otra persona pueda adivinar u obtener fácilmente (nombres de familiares, nombre de la empresa, fechas, "inmemorian2026", etc.).
  - Sean distintas para cada sistema: el ERP, el correo y las redes sociales no deben compartir la misma contraseña.
- Cambiar las contraseñas cada vez que el sistema lo solicite.
- No anotar contraseñas en papeles, notas adhesivas ni archivos sin protección, conforme a la política de escritorios y pantallas limpias (punto 7.8).

---

## 9.4. Control de Acceso a la Red

### 9.4.1. Política de Utilización de los Servicios de Red

Las conexiones no seguras a los servicios de red pueden afectar a toda la organización. Por lo tanto, se controlará el acceso a los servicios de red tanto internos como externos en las tres locaciones.

Los dueños, con la implementación técnica a cargo del proveedor externo de sistemas, tendrán a su cargo el otorgamiento del acceso a los servicios y recursos de red, únicamente de acuerdo con el pedido formal correspondiente.

Lineamientos específicos para Inmemorian:

- Las contraseñas de las redes WiFi de las tres locaciones deberán ser robustas, cambiarse periódicamente y ante cada desvinculación de personal.
- No se compartirá la contraseña de la red WiFi operativa con clientes o visitantes; de requerirse WiFi para terceros, se habilitará una **red de invitados separada**.
- La administración de los routers quedará restringida al proveedor externo de sistemas, con credenciales de administración distintas de las de fábrica.

### 9.4.2. Subdivisión de Redes

Para controlar la seguridad en redes, estas deberán dividirse en dominios lógicos separados, definiendo y documentando los perímetros de seguridad convenientes.

> **Situación actual:** cada locación opera con una red ad-hoc independiente sin segmentación interna ni firewall perimetral. Los equipos de dueños, producción y ventas comparten la misma red que cualquier dispositivo que se conecte al WiFi.

En la medida de las posibilidades técnicas de la infraestructura de cada locación, el proveedor externo de sistemas implementará:

| Locación | Segmentación mínima propuesta |
|---|---|
| Parque Industrial | Separación entre la red de PC de dueños (información crítica), la PC de producción y la red de invitados. |
| Local Inmemorian | Separación entre la red operativa (PC de ventas, móvil corporativo) y la red de invitados para clientes. |
| Local La Roca | Idem Local Inmemorian, contemplando las 2 PC de ventas. |

Esta subdivisión se coordinará con la incorporación del **firewall perimetral** prevista en el punto 8.2.

### 9.4.3. Acceso a Internet

El acceso a Internet será utilizado con propósitos autorizados o con el destino por el cual fue provisto. Se reconoce que las gerencias de ventas utilizan legítimamente **Instagram, Facebook, WhatsApp y portales web** como herramientas comerciales, por lo que el control de navegación deberá contemplar estas necesidades operativas.

Para todos los usuarios está prohibido el acceso a contenidos considerados inapropiados al propósito del negocio. A tal fin se considerarán inapropiados:

- Páginas de descargas de software no autorizado (riesgo agravado porque los usuarios hoy pueden instalar software libremente).
- Páginas de hacking.
- Páginas de juegos.
- Páginas con contenido de violencia, discriminación, odio racial, étnico o religioso.
- Páginas con contenido obsceno y/o pornográfico.

Adicionalmente, se implementará un **registro de los accesos de los usuarios a Internet**, con el objeto de realizar revisiones de los accesos efectuados o analizar casos particulares. Dicho control deberá ser **comunicado a los usuarios** antes de su puesta en marcha.

> **Situación actual:** no existen controles sobre la navegación web ni registros de acceso. Los dueños, junto con el proveedor externo de sistemas, analizarán las medidas a implementar (filtrado DNS, funciones del firewall perimetral) para efectivizar dicho control.

### 9.4.4. Seguridad de los Servicios de Red

Los dueños, junto con el proveedor externo de sistemas, definirán las pautas para garantizar la seguridad de los servicios de red de la organización, tanto públicos (portales web) como privados (ERP, red interna de cada locación).

Para ello se tendrán en cuenta las siguientes directivas:

- Mantener instalados y habilitados solo aquellos servicios que sean utilizados, deshabilitando en los routers funciones innecesarias (administración remota desde Internet, WPS, UPnP cuando no se requiera).
- Controlar el acceso lógico a los servicios, tanto a su uso como a su administración.
- Configurar cada servicio de manera segura, evitando las vulnerabilidades que pudieran presentar.
- **Instalar periódicamente las actualizaciones de seguridad** —los sistemas hoy no se actualizan regularmente—, incluyendo el firmware de los 3 routers WiFi.

---

## 9.5. Control de Acceso al Sistema Operativo

### 9.5.1. Procedimientos de Conexión de Equipos de Usuario

El acceso a los servicios de información solo será posible a través de un proceso de conexión seguro, diseñado para minimizar la oportunidad de acceso no autorizado.

En las 6 estaciones de trabajo (Windows), las 2 laptops personales utilizadas para trabajo y los 2 móviles corporativos:

- Todo equipo deberá requerir autenticación (contraseña, PIN o biometría) para iniciar sesión.
- Se configurará el **bloqueo automático de sesión por inactividad**, especialmente crítico en las PC de ventas de los locales con atención al público.
- El procedimiento de conexión divulgará la mínima información posible acerca del sistema, evitando mensajes que faciliten el accionar de un usuario no autorizado.
- Se priorizará la **regularización de los sistemas operativos obsoletos**: la mayoría de los equipos se encuentra sin soporte, lo que compromete la eficacia de cualquier control de acceso. Su actualización o reemplazo se gestionará conforme al procedimiento de control de cambios (punto 8.1.1).

### 9.5.2. Identificación y Autenticación de los Usuarios

Todos los usuarios tendrán un **identificador único (ID de usuario)** para su uso personal exclusivo, tanto en el sistema operativo de su equipo como en los ERP y demás sistemas, de manera que las actividades puedan rastrearse con posterioridad. Los identificadores de usuario no darán ningún indicio del nivel de privilegio otorgado.

En circunstancias excepcionales, cuando exista un claro beneficio para la organización —por ejemplo, la cuenta operativa de atención de un local comercial—, podrá utilizarse un identificador compartido para un grupo de usuarios o una tarea específica. En tales casos se documentará la justificación, la aprobación de los dueños y el registro de qué persona utilizó la cuenta en cada turno.

Asimismo, los **privilegios administrativos sobre los equipos** —que hoy poseen todos los usuarios— quedarán restringidos al proveedor externo de sistemas y a los dueños. Los usuarios operarán con cuentas estándar sin capacidad de instalar software, conforme al punto 8.2.

### 9.5.3. Limitación del Horario de Conexión

La limitación del período durante el cual se permiten las conexiones a los servicios informáticos reduce el espectro de oportunidades para el acceso no autorizado.

Dado que la operación de Inmemorian se desarrolla en horarios comerciales y productivos definidos, se evaluará junto con el proveedor externo de sistemas la restricción de inicio de sesión en los ERP y estaciones de trabajo fuera del horario laboral habitual de cada locación, contemplando excepciones autorizadas para los dueños y el personal administrativo en modalidad híbrida.

---

## 9.6. Monitoreo del Acceso y Uso de los Sistemas

### 9.6.1. Registro de Eventos

Se generarán registros de auditoría que contengan excepciones y otros eventos relativos a la seguridad.

> **Situación actual:** la organización no posee mecanismos de monitoreo ni registros centralizados, lo que impide detectar accesos no autorizados o reconstruir lo ocurrido ante un incidente. La implementación de registros es una acción prioritaria a cargo del proveedor externo de sistemas, conforme al punto 8.3.2.

Los registros de auditoría deberán incluir, como mínimo:

- Identificación del usuario.
- Fecha y hora de inicio y terminación de la sesión.
- Registros de intentos exitosos y fallidos de acceso al sistema.
- Registros de intentos exitosos y fallidos de acceso a datos y otros recursos, con prioridad en los módulos de los ERP que contienen **datos personales y bancarios de clientes**.

Los registros se conservarán por un período mínimo de **6 meses**, protegidos contra modificación, con acceso limitado a los dueños y al proveedor externo de sistemas. Los gerentes de área definirán, junto con los dueños, la periodicidad de revisión de los registros correspondientes a los sistemas de su incumbencia.

---

## 9.7. Computación Móvil y Trabajo Remoto

### 9.7.1. Computación Móvil y Trabajo Remoto

Cuando se utilicen dispositivos informáticos móviles propiedad de Inmemorian —los **2 móviles corporativos** de los locales— y/o equipos personales validados o autorizados para el trabajo —las **2 laptops personales** del personal administrativo en modalidad híbrida—, se deberá tener especial cuidado en garantizar que no se comprometa la información de la organización. Cada usuario garantizará que ningún tercero acceda a los dispositivos bajo su responsabilidad.

> **Situación actual:** no existen controles sobre los dispositivos personales utilizados para trabajar, la organización no utiliza VPN y no hay conexiones remotas formales a los sistemas. El trabajo híbrido del personal administrativo se realiza sin lineamientos de seguridad definidos.

Se desarrollarán procedimientos adecuados para estos dispositivos, que abarquen los siguientes conceptos:

- **Protección física:** los móviles corporativos no permanecerán desatendidos en mostradores; las laptops no se dejarán en vehículos o espacios públicos sin custodia (en coordinación con los puntos 7.2 y 7.8).
- **Acceso seguro a los dispositivos:** bloqueo por contraseña, PIN o biometría en todos los casos, con bloqueo automático por inactividad.
- **Utilización en lugares públicos:** prohibición de trabajar con datos de clientes en redes WiFi públicas sin protección; evitar la visualización de información por terceros.
- **Acceso a los sistemas de la organización:** si en el futuro se habilita acceso remoto a los ERP o a otros sistemas internos, este deberá realizarse exclusivamente mediante **VPN u otro canal cifrado** definido por el proveedor externo de sistemas, con MFA. Hasta entonces, queda prohibido exponer los sistemas internos directamente a Internet.
- **Técnicas criptográficas:** cifrado del almacenamiento de las laptops que contengan información de la organización, y de los medios removibles utilizados para transportar información entre locaciones (punto 8.4.1).
- **Resguardo de la información:** la información de la organización contenida en estos dispositivos —incluyendo conversaciones comerciales de WhatsApp en los móviles corporativos— se incorporará al esquema de respaldos del punto 8.3.1.
- **Protección contra software malicioso:** antivirus activo y actualizado también en las laptops personales utilizadas para el trabajo, como condición para su autorización.

---

# 10. Desarrollo y Mantenimiento de Sistemas

El desarrollo y mantenimiento de las aplicaciones es un punto crítico de la seguridad. Durante el análisis y diseño de los procesos que soportan las aplicaciones se deben identificar, documentar y aprobar los requerimientos de seguridad a incorporar durante las etapas de desarrollo e implementación.

**Inmemorian no desarrolla software propio ni cuenta con personal de desarrollo interno.** Sus sistemas críticos —los 2 ERP y los portales web— son productos desarrollados y mantenidos por terceros, administrados por el **proveedor externo de sistemas**. En consecuencia, esta política se orienta principalmente a: (a) exigir y verificar requerimientos de seguridad frente a los proveedores que desarrollan y mantienen los sistemas; (b) controlar los cambios, actualizaciones y datos de prueba de dichos sistemas; y (c) asegurar una adecuada administración de la infraestructura de base (sistemas operativos Windows y software de base) sobre la que operan.

Asimismo, es necesaria una adecuada administración de la infraestructura de base en las distintas plataformas para asegurar una correcta implementación de la seguridad, situación hoy comprometida por la existencia de **equipos con sistemas operativos obsoletos y sin gestión de actualizaciones**.

## Objetivo

- Asegurar la inclusión de controles de seguridad en los sistemas de información utilizados por Inmemorian, aun cuando su desarrollo y mantenimiento estén tercerizados.
- Definir y documentar las normas y procedimientos de seguridad que se aplicarán durante el ciclo de vida de los aplicativos (ERP, portales web) y en la infraestructura de base en la cual se apoyan.
- Establecer las exigencias contractuales y de control hacia los proveedores externos que desarrollan, mantienen o administran software para la organización.

## Alcance

Esta política se aplica a todos los sistemas informáticos utilizados por Inmemorian —en su totalidad desarrollos de terceros—, y a todos los sistemas operativos y/o software de base que integren cualquiera de los ambientes en donde residan dichos sistemas:

- Los **2 ERP** que soportan ventas, compras, producción, logística y finanzas.
- Los **portales web** utilizados para la comercialización de placas y mesadas.
- El **correo electrónico** corporativo y los servicios asociados.
- Los **sistemas operativos Windows** de las 6 estaciones de trabajo y las 2 laptops, y el software de base de los servidores administrados por el proveedor externo de sistemas.
- Cualquier desarrollo o personalización futura que se contrate a terceros (por ejemplo, modificaciones a los portales web o integraciones del ERP).

## Responsabilidades

**Los dueños**, junto con los **gerentes de área** (propietarios de la información) y el **proveedor externo de sistemas**, definirán los controles a ser implementados en los sistemas provistos por terceros.

**Los dueños**, en su rol provisional de responsables de seguridad de la información, verificarán el cumplimiento de los requerimientos de seguridad establecidos para el mantenimiento de los sistemas, pudiendo requerir al proveedor externo de sistemas la evidencia correspondiente.

**El proveedor externo de sistemas** cumplirá, respecto de los sistemas bajo su administración, las funciones de **"Implementador"** y **"Administrador de programas fuentes"** descriptas en este capítulo, en la medida en que resulten aplicables. Deberá documentar quién, dentro de su organización, ejerce cada función, y verificará el cumplimiento de las definiciones establecidas sobre los controles y medidas de seguridad incorporadas a los sistemas.

---

## 10.1. Análisis y Especificaciones de los Requerimientos de Seguridad

Esta política se implementa para incorporar seguridad a los sistemas de información utilizados por Inmemorian (todos de terceros) y a las mejoras o actualizaciones que se les incorporen.

Para ello, se definirá un procedimiento de modo de incorporar los requerimientos de seguridad durante la **evaluación, contratación y actualización** de sistemas:

- Antes de contratar o actualizar un sistema (ERP, portal web, herramienta complementaria), los dueños —con asesoramiento del proveedor externo de sistemas— evaluarán los requerimientos de seguridad: control de accesos por usuario individual, registro de auditoría, protección de datos personales de clientes, mecanismos de respaldo y soporte vigente del fabricante.
- Toda incorporación de sistemas seguirá el procedimiento de control de cambios del punto 8.1.1.
- Se priorizarán productos que permitan **MFA, perfiles de acceso diferenciados y registros de auditoría**, en línea con los objetivos del punto 9 y con la expectativa de la dirección de avanzar hacia una futura **certificación ISO 27001**.

## 10.2. Controles Criptográficos

Cuando sea necesario, se utilizarán sistemas y técnicas criptográficas para la protección de la información, con el fin de asegurar una adecuada protección de su confidencialidad e integridad. En el contexto de Inmemorian, se aplicarán como mínimo a:

- Los **datos personales y bancarios de clientes** almacenados o transmitidos por los ERP y el correo electrónico.
- Los **portales web**, que deberán operar exclusivamente sobre HTTPS con certificados vigentes, responsabilidad del proveedor externo de sistemas.
- Los **respaldos** de información crítica y los **medios removibles** que la transporten (puntos 8.3.1 y 8.4.1).
- El almacenamiento de las **laptops personales** autorizadas para trabajo híbrido (punto 9.7.1).

## 10.3. Seguridad de los Archivos del Sistema

Se garantizará que las actividades de soporte y mantenimiento de los sistemas se lleven a cabo de manera segura, controlando el acceso a los archivos de estos.

### 10.3.1. Control del Software Operativo

Se definen los siguientes controles a realizar durante la implementación y actualización del software en producción, a fin de minimizar el riesgo de alteración de los sistemas:

- El personal de Inmemorian **no accederá a los ambientes de administración técnica** de los ERP ni de los portales web; dicha administración corresponde exclusivamente al proveedor externo de sistemas.
- El proveedor externo de sistemas, en su función de **"Implementador"**, tendrá como responsabilidades principales:
  - Coordinar la implementación de modificaciones, actualizaciones o nuevos módulos en el ambiente de producción de los ERP y portales web.
  - Asegurar que los sistemas en uso en producción sean los autorizados y aprobados de acuerdo con el procedimiento de control de cambios (punto 8.1.1).
  - Instalar las modificaciones controlando previamente que hayan sido probadas y aprobadas por el gerente del área afectada (usuario final) y comunicadas a los dueños.
- Solo se instalará **software original y licenciado**: el relevamiento evidenció que no existe control de licenciamiento, situación que deberá regularizarse mediante un inventario de software y licencias a cargo del proveedor externo de sistemas.

### 10.3.2. Protección de los Datos de Prueba del Sistema

Cuando el proveedor externo de sistemas o cualquier tercero requiera realizar pruebas sobre los sistemas de Inmemorian, se establecerán normas y procedimientos que contemplen lo siguiente:

- **Prohibir el uso de bases de datos operativas** para pruebas. En caso de resultar imprescindible, los datos deberán **despersonalizarse** previamente, en particular los datos personales y bancarios de clientes protegidos por la Ley N.º 25.326.
- Solicitar **autorización formal de los dueños** para realizar una copia de la base operativa como base de prueba, llevando registro de tal autorización.
- **Eliminar inmediatamente**, una vez completadas las pruebas, la información operativa utilizada, dejando constancia de dicha eliminación.

### 10.3.3. Control de Cambios a Datos Operativos

La modificación, actualización o eliminación de los datos operativos serán realizadas a través de los sistemas que procesan dichos datos (los ERP) y de acuerdo con el esquema de control de accesos implementado en los mismos. Una modificación por fuera de los sistemas —por ejemplo, directamente sobre la base de datos por parte del proveedor externo— podría poner en riesgo la integridad de la información.

Los casos en los que no fuera posible la aplicación de la precedente política se considerarán **excepciones**, para las cuales se contemplará lo siguiente:

- Se generará una **solicitud formal** para la realización de la modificación, actualización o eliminación del dato, dirigida a los dueños.
- El **gerente del área afectada** (propietario de la información) y los **dueños** aprobarán la ejecución del cambio, evaluando las razones por las cuales se solicita.
- El proveedor externo de sistemas documentará la operación realizada (dato afectado, fecha, motivo, autorización) y, una vez implementado el esquema de respaldos, verificará la existencia de una copia previa al cambio.

### 10.3.4. Control de Acceso a Programas Fuentes

Inmemorian no posee programas fuentes propios. No obstante, para reducir la probabilidad de alteración de los sistemas que utiliza:

- El proveedor externo de sistemas, en su función de **"Administrador de programas fuentes"**, mantendrá la custodia y el control de versiones de cualquier código o personalización desarrollada para Inmemorian (por ejemplo, los portales web o adaptaciones de los ERP), manteniendo en todo momento la correlación entre versiones fuente y versiones en producción.
- Se prohibirá el acceso de todo operador y/o usuario de Inmemorian a los ambientes y herramientas que permitan la generación y/o manipulación de los programas fuentes.
- En los contratos con los proveedores se procurará establecer el derecho de Inmemorian a acceder a los fuentes o a un **acuerdo de custodia (escrow)** ante la discontinuidad del proveedor, conforme al punto 10.4.3.

## 10.4. Seguridad de los Procesos de Desarrollo y Soporte

Esta política provee seguridad al software y a la información de los sistemas de aplicación; por lo tanto, se controlarán los entornos y el soporte dado a los mismos.

### 10.4.1. Procedimiento de Control de Cambios

A fin de minimizar los riesgos de alteración de los sistemas de información, se implementarán controles durante la implementación de cambios, imponiendo el cumplimiento de procedimientos formales que garanticen la seguridad y el control, respetando la división de funciones en la medida en que la escala de la organización lo permita.

El procedimiento —coordinado con el punto 8.1.1— incluirá las siguientes consideraciones:

- Identificar todos los elementos que requieren modificaciones (software, bases de datos, hardware, configuración de red).
- Obtener **aprobación formal de los dueños** antes de que comiencen las tareas, sobre la base de la propuesta técnica del proveedor externo de sistemas.
- Verificar que el cambio no viole los requerimientos de seguridad definidos en la presente política.
- Efectuar las actividades relativas al cambio en un **ambiente de prueba** previo a producción (punto 8.1.3).
- Actualizar la documentación para cada cambio implementado, tanto los instructivos de usuario como la documentación operativa del proveedor.
- Mantener un **control de versiones** para todas las actualizaciones de software.
- Garantizar que la implementación se lleve a cabo minimizando la discontinuidad de las actividades —relevante dado que la dependencia operativa de los sistemas es del 75 % y la organización considera que todos sus servicios son importantes para la continuidad.
- Garantizar que sea el proveedor externo de sistemas, en su función de **"Implementador"**, quien efectúe el pasaje de los objetos modificados al ambiente operativo.

### 10.4.2. Revisión Técnica de los Cambios en el Sistema Operativo

Toda vez que sea necesario realizar un cambio en el sistema operativo —incluyendo la **actualización o reemplazo de los equipos Windows obsoletos**, acción prioritaria identificada en el relevamiento—, los sistemas serán revisados para asegurar que no se produzca un impacto en su funcionamiento o seguridad.

En particular, antes de actualizar el sistema operativo de las estaciones de trabajo, el proveedor externo de sistemas verificará la compatibilidad de los clientes de los ERP y demás software operativo, realizará el respaldo previo correspondiente (una vez implementado el esquema del punto 8.3.1) y documentará el resultado de la actualización.

### 10.4.3. Desarrollo Externo de Software

Dado que **todo el software utilizado por Inmemorian es de desarrollo externo**, y que existe dependencia operativa de los proveedores externos de Sistemas, Finanzas e Importaciones, se establecerán normas y procedimientos para toda contratación de desarrollo, personalización o mantenimiento de software, que contemplen los siguientes puntos:

- **Acuerdos de licencias, propiedad de código y derechos conferidos**, especialmente respecto de los portales web y cualquier personalización de los ERP.
- **Acuerdos de confidencialidad** con todos los proveedores que accedan a información de la organización, en particular a datos personales y bancarios de clientes.
- Definición del **acceso del proveedor a los entornos de desarrollo, prueba y producción**, limitado a lo estrictamente necesario y, en lo posible, con cuentas nominales y registro de actividad (punto 9.6.1).
- **Requerimientos contractuales con respecto a la calidad del código** y la existencia de garantías sobre el trabajo entregado.
- **Procedimientos de certificación de la calidad y precisión** del trabajo llevado a cabo por el proveedor, incluyendo la aprobación funcional por parte del gerente del área usuaria.
- **Acuerdos de custodia de los programas fuentes** (y cualquier otra información requerida) en caso de quiebra o discontinuidad del proveedor, de modo de no comprometer la continuidad operativa de la organización.
- Niveles de servicio (SLA) y compromisos de respuesta ante incidentes, hoy inexistentes con el proveedor externo de sistemas, cuya formalización constituye una acción prioritaria vinculada al punto 4 (Seguridad Frente al Acceso por Parte de Terceros).

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

*Documento elaborado en el marco del Plan de Seguridad de la Información de Inmemorian.*
*Versión unificada — Puntos 1 a 12.*
