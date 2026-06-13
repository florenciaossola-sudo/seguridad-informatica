# Medidas de Implementación y Plan de Acción

## 1 Seguridad de la Información

### Medidas Técnicas

La implementación de una política de Seguridad de la Información requiere la adopción de controles técnicos que permitan proteger los activos críticos de la organización frente a amenazas internas y externas.

Considerando que durante el relevamiento se identificó una alta dependencia de los sistemas informáticos y la inexistencia de controles formales de seguridad, se propone implementar un inventario centralizado de activos de información, herramientas de monitoreo de eventos y mecanismos de respaldo que permitan garantizar la disponibilidad de la información.

Asimismo, se recomienda la adopción de herramientas de registro y auditoría que permitan detectar accesos indebidos, modificaciones no autorizadas e incidentes de seguridad.

### Procedimientos

La organización deberá formalizar un procedimiento de gestión de riesgos que permita identificar, analizar y tratar periódicamente las amenazas que afectan a sus activos.

Además, deberán documentarse procedimientos para la gestión de incidentes de seguridad, gestión de cambios tecnológicos y control documental, permitiendo que todas las acciones relacionadas con la seguridad sean ejecutadas de forma consistente y trazable.

### Hardware

* NAS (Network Attached Storage (Almacenamiento Conectado a la Red)) para almacenamiento seguro de respaldos: Durante el relevamiento se detectó que la empresa no posee mecanismos formales de respaldo. Un NAS permite centralizar la información y almacenar copias de seguridad automáticas, reduciendo significativamente el riesgo de pérdida total de información ante fallas técnicas, errores humanos o ataques de ransomware.
Imagen:practico/Inmemorian/politica de seguridad/NAS.png
Ventajas
    ✔ Centralización de información.
    ✔ Backups automáticos.
    ✔ Recuperación ante incidentes.
    ✔ Protección frente a ransomware.
* Disco Externo USB para Backup Offline: Permite mantener copias de seguridad desconectadas de la red, disminuyendo el impacto de ataques de ransomware y cumpliendo con la estrategia de respaldo 3-2-1 recomendada para la protección de la información.
* Equipamiento de red protegido.

### Software

* Wazuh para monitoreo y correlación de eventos: Permite monitorear eventos de seguridad, detectar actividades sospechosas y generar alertas tempranas frente a posibles incidentes.
Imagen: practico/Inmemorian/politica de seguridad/wazuh.png
Ventajas
✔ Detección temprana de incidentes.
✔ Monitoreo centralizado.
✔ Auditoría de accesos.
✔ Cumplimiento de buenas prácticas ISO 27001.
* Soluciones de respaldo automatizado como ser Veeam Backup Community Edition el cual automatiza la realización de copias de seguridad y facilita la recuperación de información ante incidentes de seguridad o fallas operativas y Microsoft Defender for Business que brinda protección contra malware, ransomware y amenazas avanzadas, complementando las medidas de seguridad implementadas en los equipos de la organización.
* Microsoft Defender for Business o ESET Protect: Permite proteger los equipos frente a malware, ransomware, spyware y otras amenazas que pueden ingresar mediante correos electrónicos, descargas maliciosas o dispositivos externos.
* Microsoft Defender for Office 365 (opcional): Proporciona protección contra phishing, enlaces maliciosos y archivos adjuntos peligrosos recibidos por correo electrónico.

### Plan de Acción

#### Corto Plazo

* Identificar y registrar los activos de información.
* Determinar responsables para cada activo crítico.
* Definir criterios de clasificación de información.

#### Mediano Plazo

* Implementar herramientas de monitoreo.
* Formalizar la gestión de riesgos.
* Implementar procedimientos documentados.

#### Largo Plazo

* Realizar auditorías internas periódicas.
* Avanzar hacia la adopción de un Sistema de Gestión de Seguridad de la Información alineado con ISO 27001.

---

## 2 Política de Seguridad de la Información

### Medidas Técnicas

La Política de Seguridad de la Información constituye el marco normativo que orienta todas las actividades relacionadas con la protección de la información.

Para asegurar su cumplimiento, deberá mantenerse disponible en formato digital para todo el personal, asegurando el control de versiones y la disponibilidad de la documentación vigente.

### Procedimientos

La organización deberá establecer un proceso formal para la aprobación, difusión y revisión de la política.

Asimismo, cada modificación deberá ser comunicada oportunamente a todos los empleados y registrada para fines de auditoría.

### Hardware

No se requiere equipamiento específico para la implementación de esta política, la política constituye un documento de gobierno y gestión organizacional, por lo que su implementación no demanda equipamiento físico dedicado.

### Software

* Google Workspace: Facilita la difusión y disponibilidad permanente de políticas, procedimientos y documentación institucional.
* Microsoft 365: Permite gestionar documentación, controlar versiones y distribuir las políticas organizacionales de manera centralizada.
* Repositorio documental centralizado.

### Plan de Acción

#### Corto Plazo

* Aprobar formalmente la política.
* Difundirla entre todo el personal.

#### Mediano Plazo

* Capacitar a los empleados sobre su contenido.
* Obtener evidencia de lectura y aceptación.

#### Largo Plazo

* Revisar anualmente la política.
* Actualizarla según cambios tecnológicos y organizacionales.

---

## 3 Seguridad Frente al Acceso por Parte de Terceros

### Medidas Técnicas

Durante el relevamiento se identificó una fuerte dependencia del proveedor externo de sistemas, quien posee acceso privilegiado a los recursos tecnológicos de la organización.

Para minimizar los riesgos asociados a terceros, se recomienda implementar autenticación multifactor, accesos restringidos según funciones específicas y mecanismos de auditoría que registren todas las actividades realizadas por personal externo.

Asimismo, se deberán limitar los permisos otorgados bajo el principio de mínimo privilegio.

### Procedimientos

Deberán establecerse procedimientos formales para la gestión de proveedores y terceros, incluyendo autorización, revisión periódica de accesos y revocación inmediata una vez finalizada la relación contractual.

Toda intervención realizada por terceros deberá quedar documentada.

### Hardware

* Firewall perimetral: Permite controlar, registrar y filtrar los accesos externos realizados por proveedores o terceros, reduciendo el riesgo de accesos no autorizados.
Imagen: practico/Inmemorian/politica de seguridad/Firewall Perimetral.png
Ventajas
    ✔ Bloquea accesos no autorizados.
    ✔ Permite VPN segura.
    ✔ Registra eventos de seguridad.
    ✔ Filtra sitios maliciosos.
* Equipamiento de comunicaciones seguro como ser UPS para Equipos de Red que nos garantiza la disponibilidad de los servicios de red y comunicaciones frente a cortes eléctricos o fluctuaciones de tensión.


### Software

* VPN corporativa: Proporciona acceso remoto seguro mediante cifrado de las comunicaciones.
Imagen: practico/Inmemorian/politica de seguridad/vpn_corporativa.png
Ventajas
    ✔ Comunicación cifrada.
    ✔ Acceso remoto seguro.
    ✔ Control de proveedores.
* Microsoft Authenticator: Permite implementar autenticación multifactor (MFA), reduciendo el riesgo de robo o compromiso de credenciales.
Imagen:practico/Inmemorian/politica de seguridad/MFA.png
Ventajas
    ✔ Reduce robo de credenciales.
    ✔ Protege contra phishing.
    ✔ Aumenta la seguridad de acceso.
* Sistemas de auditoría de accesos como ser AnyDesk Empresarial:Facilita la asistencia remota de proveedores de forma controlada y auditable.
* Gateway de Correo Seguro como ser Proofpoint Essentials,Microsoft Defender for Office 365,SpamTitan que nos permite reducir el riesgo de ataques de phishing dirigidos a empleados o proveedores mediante el filtrado de correos maliciosos antes de que lleguen a los usuarios.

### Plan de Acción

#### Corto Plazo

* Formalizar acuerdos de confidencialidad (NDA).
* Formalizar acuerdos de nivel de servicio (SLA).

#### Mediano Plazo

* Implementar MFA para accesos externos.
* Revisar permisos actuales de terceros.

#### Largo Plazo

* Realizar auditorías periódicas de accesos externos.

---

## 4 Clasificación y Control de Activos

### Medidas Técnicas

La correcta identificación y clasificación de los activos constituye uno de los pilares fundamentales de la seguridad de la información.

Durante el relevamiento se observó la inexistencia de un inventario formal de activos tecnológicos y de información.

Por ello, se propone implementar un sistema de gestión de activos que permita identificar, clasificar y controlar todos los recursos utilizados por la organización.

La clasificación deberá contemplar criterios de confidencialidad, integridad y disponibilidad.

### Procedimientos

Se deberá documentar un procedimiento de alta, modificación y baja de activos.

Asimismo, cada activo deberá contar con un responsable designado que garantice su correcta utilización y protección.

### Hardware

* Etiquetas patrimoniales: Permiten identificar físicamente cada activo tecnológico y facilitar su seguimiento durante todo su ciclo de vida.
* Armarios para documentación sensible (Archivadores con Llave): Protegen documentación física sensible relacionada con clientes, proveedores y operaciones administrativas.
* Dispositivos de almacenamiento para respaldos.

### Software
        Equipos Inmemorian
                 │
                 ▼
         OCS Inventory
      (Descubrimiento)
                 │
                 ▼
              GLPI
       (Administración)
                 │
 ┌───────────────┼───────────────┐
 ▼               ▼               ▼
Hardware      Software      Responsables
 │                │                │
 ▼                ▼                ▼
PCs          Licencias      Responsables
Servidores   Aplicaciones   Asignaciones
Impresoras
Ventajas
                 │
                 ▼
          Reportes y Auditorías
* GLPI: Permite gestionar inventarios de hardware, software y responsables asignados a cada activo.
Ventajas
    ✔ Inventario centralizado.
    ✔ Control de responsables por activo.
    ✔ Gestión de incidencias y tickets.
    ✔ Seguimiento del ciclo de vida de los equipos.
    ✔ Facilita auditorías de seguridad.
* OCS Inventory: Automatiza el descubrimiento y actualización del inventario tecnológico de la organización.
Ventajas
    ✔ Descubrimiento automático de equipos.
    ✔ Inventario de hardware y software.
    ✔ Actualización automática de cambios.
    ✔ Detección de software no autorizado.
    ✔ Reducción del trabajo manual.
* Herramientas de inventario automatizado.

### Plan de Acción

#### Corto Plazo

* Inventariar hardware y software.
* Identificar propietarios de activos.

#### Mediano Plazo

* Clasificar la información según criticidad.
* Implementar una herramienta de gestión de activos.

#### Largo Plazo

* Realizar revisiones periódicas del inventario.

---

## 5 Seguridad del Personal

### Medidas Técnicas

El factor humano representa uno de los principales vectores de riesgo dentro de cualquier organización.

Durante el relevamiento se detectó la existencia de cuentas compartidas, privilegios excesivos y ausencia de controles sobre dispositivos personales utilizados para actividades laborales.

Para reducir estos riesgos se recomienda implementar autenticación multifactor, cuentas individuales, restricciones de privilegios administrativos y herramientas de protección para dispositivos corporativos y personales autorizados.

### Procedimientos

La organización deberá formalizar procedimientos de incorporación, modificación y desvinculación de usuarios.

Asimismo, deberá implementar programas permanentes de concientización y capacitación en seguridad de la información.

También se recomienda formalizar una política BYOD que regule el uso de dispositivos personales.

Política BYOD (Bring Your Own Device): La organización permitirá el uso de dispositivos personales para actividades laborales únicamente cuando cumplan los requisitos mínimos de seguridad definidos por la empresa. Los dispositivos deberán contar con sistema operativo actualizado, antivirus activo, mecanismos de bloqueo de acceso y autenticación multifactor para acceder a recursos corporativos. El objetivo es reducir los riesgos de fuga de información, accesos no autorizados y compromisos de seguridad asociados al uso de dispositivos personales.

### Hardware

* Equipos corporativos administrados (Notebooks Corporativas):Permiten aplicar configuraciones homogéneas de seguridad y reducen los riesgos asociados al uso de dispositivos personales.
* Tokens de autenticación para usuarios privilegiados (Llaves de Seguridad FIDO2 (YubiKey)):Proporcionan autenticación fuerte para usuarios con privilegios elevados y reducen el riesgo de robo de credenciales.

### Software
                    Empleado
                        │
        ┌───────────────┼───────────────┐
        ▼               ▼               ▼
 Bitwarden         Antivirus        Capacitación
   Teams           Corporativo      KnowBe4
        │               │               │
        └───────┬───────┴───────┬───────┘
                ▼               ▼
                Microsoft Intune
            (Control de dispositivos)
                        │
                        ▼
            Entorno de Trabajo Seguro
* Gestores de contraseñas como ser Bitwarden Teams que nos facilita la gestión segura de contraseñas y evita prácticas inseguras como reutilización o almacenamiento en papel.
Ventajas
    ✔ Generación de contraseñas robustas.
    ✔ Almacenamiento cifrado.
    ✔ Compartición segura entre usuarios autorizados.
    ✔ Reducción del riesgo de robo de credenciales.
    ✔ Facilita la implementación de MFA.
* Microsoft Intune: Permite administrar dispositivos corporativos y BYOD, aplicando políticas de seguridad centralizadas.
Ventajas
    ✔ Administración centralizada.
    ✔ Aplicación de políticas de seguridad.
    ✔ Control de dispositivos personales (BYOD).
    ✔ Borrado remoto de información corporativa.
    ✔ Verificación de cumplimiento de seguridad.
* Antivirus corporativo.
Ventajas
    ✔ Protección en tiempo real.
    ✔ Detección de ransomware.
    ✔ Protección contra malware.
    ✔ Análisis de archivos y correos.
    ✔ Administración centralizada.
* Plataformas de capacitación como ser KnowBe4 o GoPhish que facilitan la capacitación continua del personal y la realización de simulaciones de phishing para fortalecer la concientización.
Ventajas
    ✔ Reduce el riesgo de phishing.
    ✔ Mejora la concientización.
    ✔ Disminuye errores humanos.
    ✔ Permite medir el nivel de seguridad del personal.
    ✔ Fortalece la cultura organizacional de seguridad.

### Plan de Acción

#### Corto Plazo

* Eliminar cuentas compartidas.
* Revisar privilegios administrativos.
* Capacitar al personal.

#### Mediano Plazo

* Implementar MFA.
* Formalizar política BYOD.

#### Largo Plazo

* Realizar campañas periódicas de concientización.
* Ejecutar simulaciones de phishing.
