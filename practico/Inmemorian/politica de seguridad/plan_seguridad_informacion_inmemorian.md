# Plan de Seguridad de la Información — Inmemorian

---

## Índice

1. [Alcance](#1-alcance)
2. [Seguridad de la Información](#2-seguridad-de-la-información)
3. [Política de Seguridad de la Información](#3-política-de-seguridad-de-la-información)
4. [Seguridad Frente al Acceso por Parte de Terceros](#4-seguridad-frente-al-acceso-por-parte-de-terceros)
5. [Clasificación y Control de Activos](#5-clasificación-y-control-de-activos)
6. [Seguridad del Personal](#6-seguridad-del-personal)

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

*Documento elaborado en el marco del Plan de Seguridad de la Información de Inmemorian.*
*Versión unificada — Puntos 1 a 6.*
