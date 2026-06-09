# Plan de Seguridad de la Información
## Inmemorian
### Puntos 7 y 8 — Seguridad Física y Ambiental / Gestión de Comunicaciones y Operaciones

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

*Documento elaborado en el marco del Plan de Seguridad de la Información de Inmemorian. Complementa y debe ser leído en conjunto con los puntos 1 (Alcance), 2 (Seguridad de la Información), 3 (Política de Seguridad de la Información), 4 (Seguridad Frente al Acceso por Parte de Terceros), 5 (Clasificación y Control de Activos) y 6 (Seguridad del Personal) del mismo plan.*
