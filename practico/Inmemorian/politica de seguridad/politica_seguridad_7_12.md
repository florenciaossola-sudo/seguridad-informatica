# Plan de Seguridad de la Información para Inmemorian
## Puntos 7 al 12

---

## 7. Seguridad Física y Ambiental

### Objetivo

Prevenir e impedir accesos no autorizados, daños e interferencia a las sedes, instalaciones e información de Inmemorian, protegiendo el equipamiento de procesamiento de información y controlando los factores ambientales que puedan afectar su correcto funcionamiento.

### Alcance

Esta política se aplica a los recursos físicos relativos a los sistemas de información de las tres locaciones de la organización: Parque Industrial, Local Inmemorian y Local La Roca. Comprende instalaciones, equipamiento, cableado y medios de almacenamiento.

### Responsabilidad

Los dueños de la organización son responsables de definir y aprobar las medidas de seguridad física en cada sede. El proveedor externo de sistemas coordinará la implementación de medidas técnicas sobre el equipamiento informático.

### 7.1. Perímetro de Seguridad Física

Cada una de las tres locaciones deberá contar con controles de acceso físico diferenciados según el nivel de criticidad de la información que allí se procese. El Parque Industrial, por concentrar la mayor cantidad de equipos (incluidas las computadoras de los dueños), requiere especial atención en el control de acceso a las áreas donde se encuentran los equipos de procesamiento.

### 7.2. Controles de Acceso Físico

Se deberán implementar los siguientes controles en cada sede:

- Restringir el acceso físico a los equipos de procesamiento únicamente al personal autorizado.
- Registrar el ingreso de personas externas (proveedores, técnicos, visitas) a las áreas donde se encuentren equipos con información sensible.
- Revisar periódicamente los derechos de acceso físico a las áreas críticas.

### 7.3. Ubicación y Protección del Equipamiento

El equipamiento informático deberá ubicarse en lugares que minimicen el riesgo de acceso no autorizado, daño físico o robo. Dado que actualmente no existen copias de seguridad, se deberá prestar especial atención a la protección física de los equipos que contienen información crítica del negocio.

### 7.4. Suministros de Energía

Se deberá evaluar la incorporación de protectores de tensión y, en equipos críticos, sistemas de alimentación ininterrumpida (UPS), para proteger el equipamiento ante fallas eléctricas en las tres sedes. Las interrupciones eléctricas constituyen un riesgo identificado para la continuidad operativa.

### 7.5. Seguridad del Cableado

El cableado de red y energía en cada locación deberá estar protegido para evitar daños físicos e interceptaciones. Se revisará el estado del cableado de los módems/routers wifi en cada sede.

### 7.6. Mantenimiento de Equipos

Se establecerá un plan de mantenimiento preventivo del equipamiento, considerando que la mayoría de los equipos actuales se encuentran sin soporte o con sistemas operativos obsoletos. Ante el retiro de equipos para mantenimiento externo, se deberá eliminar previamente la información confidencial que contengan y registrar su salida.

### 7.7. Desafectación Segura de los Equipos

Cuando un equipo sea dado de baja o reutilizado, los medios de almacenamiento deberán ser sobrescritos de forma segura o destruidos físicamente. No se deberá utilizar el borrado estándar del sistema operativo para información sensible.

### 7.8. Políticas de Escritorios y Pantallas Limpias

Todo el personal deberá cumplir las siguientes pautas:

- Bloquear la pantalla al alejarse del puesto de trabajo.
- No dejar documentación con información sensible de clientes (datos personales, bancarios) a la vista en el escritorio.
- No almacenar contraseñas escritas en papeles cerca del equipo.
- Apagar los equipos al finalizar la jornada laboral.
- No dejar pendrives o medios removibles conectados a los equipos sin supervisión.
- Retirar inmediatamente de la impresora los documentos que contengan información confidencial.

---

## 8. Gestión de Comunicaciones y Operaciones

### Objetivo

Garantizar el funcionamiento correcto y seguro de las instalaciones de procesamiento de la información y comunicaciones en las tres locaciones de Inmemorian, estableciendo responsabilidades y procedimientos para su gestión y operación.

### Alcance

Todas las instalaciones de procesamiento y transmisión de información de la organización, incluyendo los dos ERP, portales web, correo electrónico, dispositivos móviles corporativos y canales de comunicación digital (WhatsApp, redes sociales).

### Responsabilidad

El proveedor externo de sistemas administra la infraestructura tecnológica. Los dueños aprueban cambios y decisiones tecnológicas. Todo el personal es responsable del uso adecuado de los sistemas y canales de comunicación.

### 8.1. Procedimientos y Responsabilidades Operativas

#### 8.1.1. Control de Cambios en las Operaciones

Todo cambio en los sistemas, configuraciones de red o equipamiento deberá ser evaluado previamente y autorizado por los dueños. Se llevará un registro de los cambios implementados, incluyendo fecha, responsable y descripción del cambio.

#### 8.1.2. Procedimientos de Manejo de Incidentes

Se establecerá un procedimiento formal de gestión de incidentes — actualmente inexistente — que defina cómo reportar, escalar y resolver situaciones de seguridad. Ante cualquier incidente, los dueños deberán ser notificados de forma inmediata.

### 8.2. Protección Contra Software Malicioso

Se deberá implementar una solución antivirus homogénea en todos los equipos de la organización. Actualmente no se ha verificado la existencia de antivirus en todos los equipos, lo que constituye una brecha crítica. Se deberán establecer actualizaciones automáticas de definiciones de virus y análisis periódicos programados.

Adicionalmente, se implementarán filtros anti-spam y anti-phishing en el correo electrónico, considerando que actualmente no existen tales controles.

### 8.3. Resguardo de la Información

Dado que actualmente no existen respaldos de ningún tipo, se deberá implementar con carácter urgente un sistema de copias de seguridad que incluya:

- Backups automáticos periódicos de los dos ERP y demás sistemas críticos.
- Copias offline o en almacenamiento inmutable para protección ante ransomware.
- Pruebas periódicas de restauración para verificar la integridad de los respaldos.
- Definición de responsables de la ejecución y verificación de los backups.

### 8.4. Administración de Medios de Almacenamiento

Se establecerán procedimientos para la administración de medios removibles (pendrives, discos externos) y para su eliminación segura cuando ya no sean necesarios. El uso de medios removibles deberá estar controlado y registrado.

### 8.5. Seguridad del Correo Electrónico y Canales de Comunicación

Se establecerán pautas claras para el uso del correo electrónico, haciendo énfasis en:

- No compartir datos personales o bancarios de clientes por canales no seguros como WhatsApp.
- No abrir adjuntos o enlaces de remitentes desconocidos.
- Reportar mensajes sospechosos.

El uso de WhatsApp, Instagram y Facebook para comunicación comercial deberá estar regulado para evitar la exposición de información sensible de clientes.

---

## 9. Control de Accesos

### Objetivo

Impedir el acceso no autorizado a los sistemas de información, bases de datos y servicios de información de Inmemorian. Implementar seguridad en los accesos de usuarios mediante técnicas de autenticación y autorización adecuadas.

### Alcance

Esta política se aplica a todos los usuarios internos y externos que accedan a los sistemas de la organización, incluyendo los dos ERP, portales web, correo electrónico y dispositivos corporativos.

### Responsabilidad

Los dueños autorizan los permisos y accesos especiales. El proveedor externo de sistemas implementa los controles técnicos de acceso.

### 9.1. Gestión de Usuarios y Credenciales

Se deberá avanzar progresivamente en la eliminación de cuentas compartidas, especialmente en las áreas de Producción y Ventas donde esta práctica es actualmente frecuente. Cada usuario deberá contar con credenciales únicas e intransferibles.

Se establecerán las siguientes políticas de contraseñas:

- Contraseñas de longitud mínima de 8 caracteres, combinando letras, números y caracteres especiales.
- Vencimiento periódico de contraseñas (se recomienda cada 90 días).
- Prohibición de reutilización de contraseñas anteriores.
- Cambio obligatorio de contraseñas iniciales o provisorias.

### 9.2. Autenticación Multifactor (MFA)

Se deberá implementar autenticación multifactor en los sistemas críticos de la organización, especialmente en los ERP y en el correo electrónico de los dueños. Actualmente la organización no utiliza MFA, lo que representa un riesgo significativo.

### 9.3. Privilegios Administrativos

Se deberá eliminar el acceso con privilegios administrativos en las estaciones de trabajo de usuarios que no requieran dicho nivel de acceso para sus tareas diarias. El principio de mínimo privilegio deberá aplicarse en todos los sistemas.

### 9.4. Control de Acceso a la Red

Dado que las tres sedes utilizan redes ad-hoc sin segmentación, se deberá implementar progresivamente:

- Separación de la red WiFi de uso interno respecto de la red de acceso a invitados o visitantes.
- Firewall perimetral en cada locación — actualmente inexistente.
- Controles de acceso a Internet para prevenir el acceso a contenidos no relacionados con el negocio.

### 9.5. Acceso de Dispositivos Personales (BYOD)

Actualmente existen al menos dos computadoras personales utilizadas para tareas laborales sin ningún control. Se deberán establecer políticas mínimas de seguridad para estos dispositivos, incluyendo obligatoriedad de antivirus, contraseña de inicio de sesión y cifrado de datos sensibles.

### 9.6. Baja y Revocación de Accesos

Se deberá establecer un proceso formal para revocar accesos de usuarios que cambien de rol o se desvinculen de la organización, tanto para sistemas internos como para cuentas de redes sociales y portales web.

---

## 10. Desarrollo y Mantenimiento de Sistemas

### Objetivo

Asegurar la inclusión de controles de seguridad en el desarrollo y mantenimiento de los sistemas de información utilizados por Inmemorian, y garantizar una adecuada gestión de los sistemas provistos por terceros.

### Alcance

Esta política aplica a todos los sistemas informáticos de la organización: los dos ERP, portales web y cualquier otro sistema desarrollado internamente o por proveedores externos.

### Responsabilidad

El proveedor externo de sistemas es responsable del mantenimiento y actualización de los sistemas. Los dueños aprueban los cambios significativos. Todo el personal reporta fallas o comportamientos anómalos en los sistemas.

### 10.1. Gestión de Actualizaciones y Parches

Se establecerá un proceso formal de gestión de actualizaciones de sistemas operativos y aplicaciones. Actualmente los sistemas no se actualizan regularmente, lo que representa una brecha de seguridad crítica. El proveedor externo deberá ser responsable de aplicar parches de seguridad de forma periódica y documentada.

### 10.2. Control de Software Instalado

Dado que actualmente los usuarios pueden instalar software libremente, se deberá implementar una política que restrinja la instalación de software no autorizado. Solo el proveedor externo de sistemas podrá instalar software en los equipos corporativos.

### 10.3. Licenciamiento de Software

Se deberá realizar un relevamiento del software instalado en todos los equipos y verificar el cumplimiento de licencias. Actualmente no existe control de licenciamiento, lo que expone a la organización a riesgos legales.

### 10.4. Contratos con Proveedores de Sistemas

Los contratos con el proveedor externo de sistemas deberán incluir cláusulas referidas a:

- Acuerdo de nivel de servicio (SLA).
- Acuerdo de confidencialidad sobre la información de clientes y datos del negocio.
- Derecho de auditoría por parte de la organización.
- Propiedad de los datos y programas fuentes.
- Responsabilidades ante incidentes de seguridad.

### 10.5. Seguridad en Portales Web

Los portales web de la organización deberán mantenerse actualizados y contar con controles de seguridad básicos, incluyendo cifrado HTTPS, protección contra accesos no autorizados y proceso de autorización formal para la publicación de contenidos.

---

## 11. Administración de la Continuidad de las Actividades de la Organización

### Objetivo

Minimizar los efectos de posibles interrupciones de las actividades de Inmemorian, protegiendo los procesos críticos mediante controles preventivos y acciones de recuperación, considerando la alta dependencia tecnológica (aproximadamente 75%) de la organización.

### Alcance

Esta política se aplica a todos los procesos críticos identificados: Ventas, Compras, Logística, Finanzas, Sistemas y Producción, en las tres locaciones.

### Responsabilidad

Los dueños y gerentes son responsables de la toma de decisiones ante emergencias e interrupciones. El proveedor externo de sistemas apoya la recuperación tecnológica.

### 11.1. Identificación de Riesgos y Análisis de Impacto

Las principales amenazas identificadas que podrían interrumpir las operaciones de Inmemorian son:

- Pérdida total de información por ausencia de respaldos (riesgo crítico e inmediato).
- Fallas de hardware en equipos sin soporte o con sistemas operativos obsoletos.
- Interrupciones eléctricas o de conectividad en alguna de las tres locaciones.
- Ataques de ransomware o malware, facilitados por la falta de antivirus y actualizaciones.
- Dependencia crítica del proveedor externo de sistemas sin acuerdos formales de nivel de servicio.
- Pérdida o robo de dispositivos móviles corporativos.

### 11.2. Plan de Continuidad

Se deberá elaborar e implementar un plan de continuidad que contemple como mínimo:

- **Respaldo de información**: Implementación urgente de backups automáticos con copias fuera de las instalaciones (offsite o nube), dado que actualmente no existen respaldos de ningún tipo.
- **Contingencia ante falla de equipos**: Identificar equipos de reemplazo o procedimientos manuales temporales para los procesos críticos.
- **Contingencia ante falla de conectividad**: Definir procedimientos de operación ante la pérdida de acceso a internet en alguna de las sedes.
- **Recuperación ante pérdida del proveedor de sistemas**: Documentar accesos, credenciales y configuraciones críticas para no depender exclusivamente del proveedor externo.

### 11.3. Prueba y Actualización del Plan

El plan de continuidad deberá revisarse y probarse al menos una vez al año, o ante cambios significativos en la infraestructura tecnológica de la organización.

---

## 12. Cumplimiento

### Objetivo

Garantizar que Inmemorian cumpla con las disposiciones legales y contractuales vigentes relacionadas con la protección de la información, especialmente en lo referido a datos personales y bancarios de clientes, y avanzar hacia los estándares requeridos para una futura certificación ISO/IEC 27001.

### Alcance

Esta política aplica a todo el personal de la organización y a los sistemas de información, normas, procedimientos y plataformas tecnológicas utilizadas.

### Responsabilidad

Los dueños son responsables de garantizar el cumplimiento normativo de la organización. Todo el personal debe conocer y cumplir las políticas de seguridad establecidas.

### 12.1. Cumplimiento de Requisitos Legales

#### 12.1.1. Protección de Datos Personales

Inmemorian maneja datos personales y bancarios de clientes, lo que genera obligaciones bajo la Ley 25.326 de Protección de Datos Personales de Argentina. Se deberá:

- Garantizar que los datos personales de clientes (incluyendo datos bancarios compartidos) sean almacenados y tratados con los controles de seguridad adecuados.
- Evitar la exposición de datos de clientes a través de canales informales como WhatsApp o redes sociales.
- Asegurar que los proveedores externos que accedan a datos de clientes cuenten con acuerdos de confidencialidad.

#### 12.1.2. Licenciamiento de Software

Se deberá verificar que todo el software instalado en los equipos de la organización cuente con las licencias correspondientes, en cumplimiento de la Ley 11.723 de Propiedad Intelectual.

### 12.2. Cumplimiento de la Política de Seguridad

Todos los empleados deberán conocer, cumplir y hacer cumplir la presente política. Los dueños y gerentes son responsables de comunicar esta política dentro de sus áreas y de reportar cualquier desvío o incumplimiento detectado.

Se realizarán revisiones periódicas del cumplimiento de la política, especialmente en lo referido a:

- Uso de contraseñas y cuentas compartidas.
- Manejo de datos de clientes en canales digitales.
- Uso de software no autorizado.
- Estado de actualizaciones y antivirus en los equipos.

### 12.3. Orientación hacia ISO/IEC 27001

La dirección ha expresado el objetivo de avanzar hacia una futura certificación ISO/IEC 27001. El presente plan constituye el punto de partida para ese proceso. Se recomienda:

- Designar formalmente un Responsable de Seguridad de la Información dentro de la organización.
- Implementar un registro de incidentes de seguridad.
- Establecer revisiones anuales del plan y sus controles.
- Documentar formalmente todos los procesos y procedimientos de seguridad implementados.

---

*Documento elaborado en el marco del Trabajo Práctico Integrador — Seguridad Informática — Maestría en Informática, UNSa.*
