# Plan de Seguridad de la Información
## Inmemorian
### Puntos 5 y 6 — Clasificación y Control de Activos / Seguridad del Personal

---

# 5. Clasificación y Control de Activos

Inmemorian debe conocer y documentar los activos de información y tecnología que utiliza en su operación diaria como parte fundamental de la administración de riesgos. Los activos de información deben ser clasificados de acuerdo con la sensibilidad y criticidad de la información que contienen, o bien de acuerdo a la funcionalidad que cumplen, con el objeto de señalar cómo ha de ser tratada y protegida dicha información.

El relevamiento de la situación actual evidenció que **no existe un inventario formal de activos informáticos**, **no hay proceso definido para altas y bajas de equipos** y **no se controla el licenciamiento de software**. Asimismo, la información crítica —incluyendo datos personales y bancarios de clientes— circula por canales informales como WhatsApp, Instagram y Facebook, sin criterios de clasificación ni controles acordes a su sensibilidad. Esta situación incrementa el riesgo de exposición, pérdida o uso indebido de la información organizacional.

## Objetivo

Garantizar que los activos de información y tecnología de Inmemorian reciban un nivel de protección acorde a su criticidad y sensibilidad.

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

Se identificarán los activos importantes asociados a cada sistema de información, sus respectivos propietarios y su ubicación, para elaborar un inventario con dicha información. El inventario será actualizado ante cualquier modificación —incorporación, reemplazo, baja o traslado de equipos—.

> **Situación actual:** no existe un proceso definido para la gestión de altas y bajas de equipos. La implementación del inventario constituye una acción prioritaria del presente plan.

El encargado de elaborar el inventario de cada área y mantenerlo actualizado es el **gerente responsable del sector**, en coordinación con el proveedor externo de sistemas para los activos técnicos centralizados.

Como mínimo, el inventario deberá registrar:

| Campo | Descripción |
|---|---|
| Identificación del activo | Nombre, tipo y número de serie o identificador único |
| Categoría | Hardware, software, servicio, información o medio de almacenamiento |
| Propietario | Gerente o área responsable del activo |
| Ubicación | Parque Industrial, Local Inmemorian o Local La Roca |
| Criticidad | Baja, media o alta (según clasificación del punto 5.2) |
| Usuarios autorizados | Personas o roles con acceso legítimo |
| Estado | Activo, obsoleto, en reemplazo o dado de baja |

A continuación se detalla el inventario preliminar de activos tecnológicos relevados, que deberá ser formalizado y completado por cada gerente:

| Activo | Tipo | Ubicación | Propietario | Observación |
|---|---|---|---|---|
| PC producción | Estación de trabajo | Parque Industrial | Gerencia de Producción | Cuenta compartida; privilegios administrativos |
| 2 PC dueños | Estación de trabajo | Parque Industrial | Dueños | Administran correo electrónico corporativo |
| PC ventas | Estación de trabajo | Local Inmemorian | Gerencia Ventas Placas | Cuenta compartida; uso de WhatsApp y redes sociales |
| 2 PC ventas | Estación de trabajo | Local La Roca | Gerencia Ventas Mesadas | Cuentas compartidas |
| 2 laptops personales | Equipo BYOD | Variable | Según usuario | Sin controles de seguridad |
| 2 móviles corporativos | Dispositivo móvil | Locales comerciales | Gerencias de ventas | Uso de WhatsApp para datos de clientes |
| 3 módem/router WiFi | Infraestructura de red | Cada locación | Proveedor de sistemas | Sin firewall perimetral |
| 2 ERP | Sistema de negocio | Servidor (administrado externamente) | Proveedor de sistemas | Dependencia crítica (~75 % operación) |
| Portales web | Aplicación | Servidor (administrado externamente) | Proveedor de sistemas | Ventas y gestión comercial |
| Correo electrónico | Servicio | Administrado por dueños | Dueños | Sin filtros anti-spam ni anti-phishing |
| WhatsApp / redes sociales | Canal de comunicación | Móviles y PCs | Gerencias de ventas y logística | Intercambio de datos sensibles de clientes |

El inventario deberá incluir asimismo el registro de software instalado en cada equipo, con el fin de revertir la **ausencia actual de control sobre el licenciamiento de software** y la práctica habitual de instalación libre de programas por parte de los usuarios.

---

## 5.2. Clasificación de la Información

Para clasificar un activo de información, se evaluarán las tres características en las cuales se basa la seguridad: **Confidencialidad, Integridad y Disponibilidad**.

A continuación se establece el criterio de clasificación en función de cada una de dichas características:

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

*Documento elaborado en el marco del Plan de Seguridad de la Información de Inmemorian. Complementa y debe ser leído en conjunto con los puntos 1 (Alcance), 2 (Seguridad de la Información), 3 (Política de Seguridad de la Información) y 4 (Seguridad Frente al Acceso por Parte de Terceros) del mismo plan.*
