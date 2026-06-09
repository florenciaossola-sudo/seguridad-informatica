# Plan de Seguridad de la Información
## Inmemorian
### Puntos 9 y 10 — Control de Accesos / Desarrollo y Mantenimiento de Sistemas

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

*Documento elaborado en el marco del Plan de Seguridad de la Información de Inmemorian. Complementa y debe ser leído en conjunto con los puntos 1 (Alcance), 2 (Seguridad de la Información), 3 (Política de Seguridad de la Información), 4 (Seguridad Frente al Acceso por Parte de Terceros), 5 (Clasificación y Control de Activos), 6 (Seguridad del Personal), 7 (Seguridad Física y Ambiental) y 8 (Gestión de Comunicaciones y Operaciones) del mismo plan.*
