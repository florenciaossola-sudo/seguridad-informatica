# Plan de Seguridad de la Información
## Inmemorian
### Puntos 5 y 6 — Clasificación y Control de Activos / Seguridad del Personal

---

# 5. Clasificación y Control de Activos

Todo activo de información de Inmemorian tiene valor para la organización y debe ser identificado, clasificado y protegido de manera proporcional a su criticidad. El relevamiento de la situación actual evidenció que **no existe ningún inventario formal de activos tecnológicos ni de información**, que no hay un proceso definido para la gestión de altas y bajas de equipos, y que tampoco existe control sobre las licencias de software. Esta situación impide conocer con exactitud qué se debe proteger y en qué medida.

## Objetivo

Identificar, clasificar y proteger adecuadamente los activos de información de Inmemorian, asignando a cada uno un responsable y un nivel de protección acorde a su criticidad e impacto potencial sobre la operación.

## Alcance

Esta política se aplica a todos los activos de información de la organización, incluyendo hardware, software, datos e información, y a todos sus usuarios, independientemente de la locación en que operen o de su modalidad de trabajo.

## Responsabilidades

- Los **dueños** son los responsables últimos de la definición de criterios de clasificación y de la aprobación del inventario consolidado de activos.
- Los **gerentes de cada área** actúan como propietarios de los activos de información bajo su gestión, siendo responsables de clasificarlos y mantener actualizado su inventario.
- El **proveedor externo de sistemas** es responsable del inventario técnico de la infraestructura que administra (servidores, equipos de red, estaciones de trabajo) y de informar a los dueños ante cualquier alta, baja o modificación de activos tecnológicos.
- **Todos los usuarios** son responsables de cuidar los activos que les sean asignados y de informar ante cualquier pérdida, robo, daño o mal funcionamiento.

---

## 5.1. Inventario de Activos

Se deberá confeccionar y mantener actualizado un **inventario de activos de información** que incluya, como mínimo, los siguientes tipos de activos identificados en el relevamiento:

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

> **Acción prioritaria:** el inventario de activos deberá confeccionarse como una de las primeras acciones del plan, dado que actualmente no existe ningún registro formal. Sin inventario, no es posible gestionar adecuadamente las protecciones descritas en los puntos siguientes.

---

## 5.2. Clasificación de la Información

Toda la información de Inmemorian deberá clasificarse según su nivel de sensibilidad y el impacto que su divulgación, alteración o pérdida podría generar sobre la organización, sus clientes o sus operaciones. Se establecen los siguientes niveles:

### Nivel 1 — Confidencial

Información cuya divulgación no autorizada podría generar daño significativo a la organización, sus clientes o sus relaciones comerciales.

Incluye:
- Datos personales de clientes (nombre, dirección, datos de contacto), alcanzados por la **Ley N.º 25.326 de Protección de Datos Personales**.
- Datos bancarios de clientes compartidos en el marco de operaciones comerciales.
- Información financiera y contable de la organización.
- Credenciales de acceso a sistemas y contraseñas.
- Información contractual con proveedores externos.
- Datos de importaciones y compras internacionales.

**Controles mínimos:** acceso restringido a usuarios autorizados con necesidad demostrada; prohibición de transmisión por canales no seguros (WhatsApp, redes sociales); obligación de confidencialidad para quienes accedan a ella.

### Nivel 2 — De Uso Interno

Información generada en el marco de la operación diaria, cuya divulgación no autorizada podría afectar la operación pero no causa daño directo a terceros.

Incluye:
- Registros operativos de producción y logística en el ERP.
- Diseños de placas conmemorativas en elaboración.
- Comunicaciones internas entre áreas.
- Información de pedidos y presupuestos en curso.

**Controles mínimos:** acceso restringido al personal del área responsable; no debe compartirse fuera de la organización sin autorización explícita.

### Nivel 3 — Pública

Información destinada a la difusión externa o cuya divulgación no genera impacto sobre la organización.

Incluye:
- Catálogos de productos publicados en portales web.
- Información de contacto institucional.
- Publicaciones en redes sociales corporativas.

**Controles mínimos:** verificación de que no contiene información confidencial antes de su publicación.

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

El factor humano representa uno de los principales vectores de riesgo para la seguridad de la información. En Inmemorian, el relevamiento evidenció que **no existe capacitación formal en ciberseguridad**, que los usuarios poseen privilegios administrativos en sus equipos, que utilizan cuentas compartidas, que instalan software libremente y que transmiten información sensible de clientes por canales informales como WhatsApp y redes sociales. Estas prácticas, producto de la ausencia de políticas formales, generan riesgos significativos que requieren ser abordados desde la gestión del personal.

## Objetivo

Reducir los riesgos de seguridad de la información derivados del factor humano, mediante la concientización, capacitación y definición de responsabilidades claras para todos los usuarios de los sistemas de Inmemorian, desde el proceso de incorporación hasta la desvinculación.

## Alcance

Esta política se aplica a todos los usuarios de los sistemas de la organización:

- Dueños y gerentes.
- Empleados permanentes.
- Personal administrativo en modalidad presencial o híbrida.
- Personal tercerizado y proveedores externos con acceso a sistemas e información de la organización.

## Responsabilidades

- Los **dueños** son responsables de aprobar y comunicar las políticas de seguridad del personal, y de autorizar los accesos correspondientes a cada rol.
- Los **gerentes** son responsables de asegurar que su personal conozca y cumpla las políticas de seguridad, y de informar al proveedor externo de sistemas sobre cualquier alta, baja o cambio de funciones que requiera modificar accesos.
- El **proveedor externo de sistemas** es responsable de ejecutar técnicamente las altas, bajas y modificaciones de accesos solicitadas por los dueños o gerentes.
- **Todos los usuarios** son responsables de conocer y cumplir las políticas de seguridad de la información, y de reportar cualquier incidente o sospecha de vulneración.

---

## 6.1. Incorporación de Personal

Ante el ingreso de un nuevo empleado, personal administrativo o trabajador tercerizado, deberán realizarse las siguientes acciones antes de que el usuario acceda a los sistemas:

- **Definición del perfil de acceso:** los dueños o el gerente del área correspondiente determinarán a qué sistemas, información y recursos el nuevo usuario necesita acceder para cumplir sus funciones, aplicando el principio de **mínimo privilegio**.
- **Alta formal en sistemas:** el proveedor externo de sistemas creará las credenciales individuales del nuevo usuario, con privilegios acordes al perfil definido. **No se crearán ni reutilizarán cuentas compartidas.**
- **Firma de compromiso de confidencialidad:** todo nuevo usuario deberá suscribir un compromiso de confidencialidad y de cumplimiento de la presente Política de Seguridad de la Información antes de acceder a los sistemas.
- **Capacitación inicial en seguridad:** el nuevo usuario recibirá una inducción básica en seguridad de la información, cubriendo como mínimo: manejo de contraseñas, prohibición de compartir credenciales, uso aceptable de sistemas y equipos, y procedimiento de reporte de incidentes.

> **Contexto actual:** no existe ninguno de estos procesos formalizados. La incorporación de personal no sigue un procedimiento definido, y los accesos se otorgan sin criterios documentados de mínimo privilegio.

---

## 6.2. Durante la Relación Laboral

### Capacitación y Concientización

Se implementará un programa de **capacitación periódica en ciberseguridad** para todo el personal, que incluya:

- **Riesgos del uso de WhatsApp, Instagram y Facebook** para el intercambio de información de clientes, con énfasis en las gerencias de ventas y logística, donde este uso es intensivo y cotidiano.
- **Manejo seguro de contraseñas:** creación de contraseñas robustas, prohibición de compartirlas, obligación de cambio periódico.
- **Reconocimiento de phishing y correo malicioso**, dado que no existen filtros anti-spam ni anti-phishing implementados.
- **Uso aceptable de equipos corporativos y personales**, incluyendo la prohibición de instalación libre de software.
- **Protección de datos personales de clientes** en cumplimiento de la Ley N.º 25.326, con especial atención al manejo de datos bancarios.
- **Procedimientos de reporte de incidentes**, cuya cadena de comunicación deberá ser conocida por todos los usuarios.

La capacitación deberá realizarse **al menos una vez al año** para todo el personal, con sesiones adicionales ante cambios significativos en el entorno tecnológico o ante la ocurrencia de incidentes relevantes.

### Uso Aceptable de Sistemas y Equipos

Todos los usuarios deberán cumplir las siguientes pautas de uso aceptable:

- Utilizar los sistemas y equipos **exclusivamente para fines laborales autorizados**.
- **No instalar software** sin autorización expresa de los dueños o del proveedor externo de sistemas.
- **No compartir credenciales** de acceso bajo ninguna circunstancia, eliminando la práctica actual de cuentas compartidas en producción y ventas.
- **No transmitir información Confidencial** —datos de clientes, datos bancarios, información financiera— a través de WhatsApp, Instagram, Facebook u otros canales no autorizados.
- Reportar **de inmediato** cualquier pérdida, robo o daño de equipos asignados.
- Reportar **de inmediato** cualquier incidente, anomalía o sospecha de vulneración de la seguridad a los dueños o al gerente del área.
- No conectar dispositivos de almacenamiento externos —pendrives, discos portátiles— sin autorización previa.

### Gestión de Cambios de Funciones

Ante el cambio de funciones de un empleado dentro de la organización:

- El gerente del área deberá comunicar el cambio al proveedor externo de sistemas para que ajuste los permisos de acceso al nuevo perfil.
- Se revocarán inmediatamente los accesos correspondientes a las funciones anteriores.
- Se otorgarán únicamente los accesos necesarios para las nuevas funciones, aplicando el principio de mínimo privilegio.

---

## 6.3. Desvinculación de Personal

La desvinculación de un empleado, ya sea por renuncia, despido, finalización de contrato o cualquier otro motivo, representa un momento de riesgo significativo para la seguridad de la información. El procedimiento de desvinculación deberá incluir obligatoriamente:

- **Revocación inmediata de accesos:** el proveedor externo de sistemas deberá dar de baja todas las credenciales del usuario desvinculado en todos los sistemas —ERP, portales web, correo electrónico— el mismo día en que se produzca la desvinculación, o antes si la situación lo requiere.
- **Devolución de equipos y activos:** el usuario deberá entregar todos los equipos corporativos, teléfonos móviles, llaves de acceso físico y cualquier otro activo de la organización que tenga en su poder.
- **Eliminación de información corporativa** en dispositivos personales: en el caso del personal administrativo que utilice dispositivos personales para el trabajo, deberá verificarse la eliminación de información corporativa —especialmente datos de clientes— de dichos dispositivos.
- **Recordatorio de obligaciones de confidencialidad:** el usuario desvinculado deberá ser notificado formalmente de que las obligaciones de confidencialidad suscritas al inicio de la relación laboral se mantienen vigentes tras la desvinculación.

> **Contexto actual:** no existe un proceso formal de desvinculación. La ausencia de este procedimiento implica que, ante una baja de personal, los accesos podrían permanecer activos indefinidamente, representando un riesgo directo sobre la confidencialidad e integridad de la información.

---

## 6.4. Personal en Modalidad Híbrida

Inmemorian cuenta con **2 personas de personal administrativo** que trabajan bajo modalidad híbrida, utilizando equipos personales para acceder a los sistemas de la organización desde fuera de las locaciones. Esta situación requiere controles adicionales:

- Los equipos personales utilizados para trabajo deberán contar con **solución antivirus activa y actualizada**.
- El acceso a los sistemas desde equipos personales deberá realizarse a través de canales seguros. Cuando se implementen accesos remotos, deberá utilizarse VPN corporativa.
- La información Confidencial **no deberá almacenarse en los equipos personales** más allá del tiempo estrictamente necesario para la tarea.
- Los usuarios en modalidad híbrida deberán aplicar las mismas pautas de uso aceptable descriptas en el punto 6.2, incluyendo la prohibición de compartir información de clientes por WhatsApp u otros canales informales.
- Los dueños deberán evaluar, en el mediano plazo, la provisión de equipos corporativos a este personal, eliminando la dependencia de dispositivos personales para el acceso a información organizacional.

---

## 6.5. Gestión de Incidentes Relacionados con el Personal

Todo usuario que detecte o sospeche un incidente de seguridad —incluyendo pérdida de credenciales, acceso no autorizado, envío accidental de información confidencial o comportamiento anómalo de los sistemas— deberá:

1. **Reportarlo de inmediato** al dueño o gerente del área, sin demora y sin intentar resolverlo por cuenta propia.
2. El dueño o gerente lo comunicará al **proveedor externo de sistemas** para la evaluación técnica y contención del incidente.
3. Se documentará el incidente con la mayor cantidad de detalles posible: fecha, hora, descripción del evento, sistemas afectados y acciones tomadas.

> **Contexto actual:** no existe ningún procedimiento formal de reporte y escalamiento de incidentes. La cadena de comunicación ante un evento de seguridad es informal y depende de la iniciativa individual. La formalización de este proceso es una de las acciones prioritarias del presente plan.

---

*Documento elaborado en el marco del Plan de Seguridad de la Información de Inmemorian. Complementa y debe ser leído en conjunto con los puntos 1 (Alcance), 2 (Seguridad de la Información), 3 (Política de Seguridad) y 4 (Seguridad Frente al Acceso por Parte de Terceros) del mismo plan.*
