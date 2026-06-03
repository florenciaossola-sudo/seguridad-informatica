# Plan de Seguridad de la Información
## Inmemorian
### Puntos 3 y 4 — Política de Seguridad y Acceso de Terceros

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

*Documento elaborado en el marco del Plan de Seguridad de la Información de Inmemorian. Complementa y debe ser leído en conjunto con los puntos 1 (Alcance) y 2 (Seguridad de la Información) del mismo plan.*
