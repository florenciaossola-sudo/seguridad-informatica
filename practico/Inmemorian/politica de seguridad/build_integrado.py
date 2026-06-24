#!/usr/bin/env python3
"""Genera plan_seguridad_integrado_inmemorian.md a partir de plan + propuesta."""

import re
from pathlib import Path

BASE = Path(__file__).parent
PLAN = BASE / "plan_seguridad_informacion_inmemorian.md"
PROP = BASE / "politica_seguridad_propuesta.md"
PROBLEMATICA = BASE / "problematica_inmemorian.md"
OUT = BASE / "plan_seguridad_integrado_inmemorian.md"

# Referencias inline: heading exacto del plan -> bullets de correlación
INLINE_REFS: dict[str, list[str]] = {
    "## 2.1. Confidencialidad": [
        "Wazuh para auditoría de accesos y detección de accesos indebidos.",
        "Procedimiento formal de gestión de riesgos (ver bloque final).",
    ],
    "## 2.2. Integridad": [
        "Wazuh para detectar modificaciones no autorizadas.",
        "Procedimientos de control documental e incidentes.",
    ],
    "## 2.3. Disponibilidad": [
        "NAS Synology, disco USB offline y Veeam Backup.",
        "Microsoft Defender for Business en endpoints.",
    ],
    "## 2.4. Gestión de Riesgos": [
        "Formalización del procedimiento de gestión de riesgos.",
        "Plan de acción corto, mediano y largo plazo del capítulo 2.",
    ],
    "## 2.5. Cultura de Seguridad": [
        "Capacitación continua con KnowBe4/GoPhish (cap. 6).",
        "Simulaciones de phishing y campañas de concientización.",
    ],
    "## 2.6. Objetivos Generales del Plan": [
        "Roadmap hacia ISO/IEC 27001 (plan de acción largo plazo).",
    ],
    "## 3.1. Principios Rectores": [
        "Google Workspace / Microsoft 365 para difusión y control de versiones.",
        "Repositorio documental centralizado.",
    ],
    "## 3.2. Gestión de Riesgos": [
        "Aprobar, difundir y revisar anualmente la política.",
        "Evidencia de lectura y aceptación del personal.",
    ],
    "## 3.3. Cultura de Seguridad": [
        "Capacitación sobre contenido de la política (cap. 6).",
    ],
    "## 3.4. Objetivos Específicos del Plan": [
        "Plan de acción: aprobar, difundir, capacitar y revisar anualmente.",
    ],
    "## 4.1. Identificación de Riesgos de Acceso de Terceros": [
        "MFA, mínimo privilegio y mecanismos de auditoría.",
    ],
    "## 4.2. Requerimientos de Seguridad en Contratos con Terceros": [
        "Formalizar NDA y SLA (plan de acción corto plazo).",
    ],
    "## 4.3. Acceso Remoto y Monitoreo": [
        "VPN corporativa, FortiGate, AnyDesk Empresarial, Microsoft Authenticator.",
    ],
    "## 4.4. Revisión y Auditoría de Accesos de Terceros": [
        "Wazuh para registro de actividades; auditorías periódicas.",
    ],
    "## 5.1. Inventario de Activos": [
        "GLPI + OCS Inventory; etiquetas patrimoniales.",
    ],
    "## 5.2. Clasificación de la Información": [
        "Criterios CIA; clasificación por criticidad (plan mediano plazo).",
    ],
    "## 5.3. Etiquetado y Manejo de la Información": [
        "Etiquetas patrimoniales y archivadores con llave.",
    ],
    "## 5.4. Control de Activos de Hardware y Software": [
        "GLPI para ciclo de vida; armarios para documentación sensible.",
    ],
    "## 6.1. Capacitación del Usuario": [
        "KnowBe4 / GoPhish; plan de acción corto, mediano y largo plazo.",
    ],
    "## 6.2. Respuesta a Incidentes y Anomalías en Materia de Seguridad": [
        "Procedimientos documentados; Wazuh (detalle operativo en cap. 8).",
    ],
    "## 7.1. Perímetro de Seguridad Física": [
        "Gabinetes de protección industrial; armarios con llave.",
    ],
    "## 7.2. Controles de Acceso Físico": [
        "Control de acceso a áreas críticas; registro de visitantes.",
    ],
    "## 7.3. Ubicación y Protección del Equipamiento y Copias de Seguridad": [
        "NAS para resguardo físico de copias (ver también cap. 8 y 11).",
    ],
    "## 7.4. Suministros de Energía": [
        "UPS APC Easy UPS en equipamiento crítico.",
    ],
    "## 7.5. Seguridad del Cableado": [
        "Sin hardware específico en propuesta — a definir con proveedor externo.",
    ],
    "## 7.6. Mantenimiento de Equipos": [
        "Procedimientos de mantenimiento y retiro de equipos.",
    ],
    "## 7.7. Desafectación Segura de los Equipos": [
        "BitLocker para borrado seguro; procedimiento de baja de activos.",
    ],
    "## 7.8. Políticas de Escritorios y Pantallas Limpias": [
        "Política de escritorios limpios; Microsoft Intune.",
    ],
    "## 8.1. Procedimientos y Responsabilidades Operativas": [
        "Gestión de cambios, incidentes y separación de ambientes.",
    ],
    "## 8.2. Protección Contra Software Malicioso": [
        "Microsoft Defender for Business, FortiGate 40F, Wazuh.",
    ],
    "## 8.3. Mantenimiento": [
        "NAS DS923+, Veeam, disco USB offline; pruebas de restauración trimestrales.",
    ],
    "## 8.4. Administración y Seguridad de los Medios de Almacenamiento": [
        "Disco USB offline; cifrado BitLocker en medios removibles.",
    ],
    "## 8.5. Intercambios de Información y Software": [
        "Defender for Office 365 / gateway de correo (cap. 4); MFA en correo (cap. 9).",
    ],
    "## 9.1. Requerimientos para el Control de Acceso": [
        "Política de contraseñas; Bitwarden Enterprise.",
    ],
    "## 9.2. Administración de Accesos de Usuarios": [
        "Alta, baja y modificación de usuarios; eliminar cuentas compartidas.",
    ],
    "## 9.3. Responsabilidades del Usuario": [
        "Bitwarden; capacitación en cap. 6.",
    ],
    "## 9.4. Control de Acceso a la Red": [
        "FortiGate; segmentación VLAN.",
    ],
    "## 9.5. Control de Acceso al Sistema Operativo": [
        "Restricción de privilegios admin; Microsoft Intune.",
    ],
    "## 9.6. Monitoreo del Acceso y Uso de los Sistemas": [
        "Wazuh para registro y detección de comportamientos anómalos.",
    ],
    "## 9.7. Computación Móvil y Trabajo Remoto": [
        "Microsoft Authenticator (MFA); Intune para BYOD.",
    ],
    "## 10.1. Análisis y Especificaciones de los Requerimientos de Seguridad": [
        "GLPI + Jira Service Management para trazabilidad.",
    ],
    "## 10.2. Controles Criptográficos": [
        "BitLocker para cifrado de discos (cap. 7).",
    ],
    "## 10.3. Seguridad de los Archivos del Sistema": [
        "Gestión de cambios documentada en GLPI/Jira.",
    ],
    "## 10.4. Seguridad de los Procesos de Desarrollo y Soporte": [
        "Jira Service Management: aprobación de cambios e incidencias.",
    ],
    "## 11.1. Continuidad de las Actividades y Análisis de los Impactos": [
        "BIA; identificar procesos críticos (plan corto plazo).",
    ],
    "## 11.2. Elaboración e Implementación de los Planes de Continuidad": [
        "NAS, UPS APC, Veeam, disco offline; simulacros periódicos.",
        "Wazuh para monitoreo de disponibilidad.",
    ],
    "## 12.1. Cumplimiento de Requisitos Legales": [
        "Ley 25.326; Microsoft Purview (opcional).",
    ],
    "## 12.2. Cumplimiento de la Política de Seguridad": [
        "Wazuh + GLPI como evidencia; auditorías internas.",
    ],
}

CHAPTER_TITLES = {
    1: "Alcance",
    2: "Seguridad de la Información",
    3: "Política de Seguridad de la Información",
    4: "Seguridad Frente al Acceso por Parte de Terceros",
    5: "Clasificación y Control de Activos",
    6: "Seguridad del Personal",
    7: "Seguridad Física y Ambiental",
    8: "Gestión de Comunicaciones y Operaciones",
    9: "Control de Accesos",
    10: "Desarrollo y Mantenimiento de Sistemas",
    11: "Administración de la Continuidad de las Actividades de la Organización",
    12: "Cumplimiento",
}

SYNTHESIS = """## Síntesis de medidas transversales de implementación

El capítulo 1 define el alcance del plan; las medidas concretas de implementación se distribuyen en los capítulos 2 a 12. A continuación se presenta una síntesis transversal agrupada por dominio, extraída de la propuesta de implementación.

### Gobierno y cumplimiento

- Aprobación, difusión y revisión anual de la política (cap. 3).
- Auditorías internas, gestión de evidencias y alineación con ISO/IEC 27001 (cap. 2, 12).
- Cumplimiento de la Ley N.º 25.326 de Protección de Datos Personales (cap. 12).

### Activos e inventario

- GLPI + OCS Inventory para inventario centralizado y ciclo de vida (cap. 5).
- Etiquetas patrimoniales y archivadores con llave (cap. 5).

### Identidad y acceso

- Eliminación de cuentas compartidas; cuentas individuales (cap. 6, 9).
- MFA con Microsoft Authenticator; Bitwarden Enterprise (cap. 4, 6, 9).
- Revisión semestral de permisos y privilegios (cap. 9).

### Infraestructura y red

- FortiGate 40F como firewall perimetral y segmentación VLAN (cap. 4, 8, 9).
- VPN corporativa para acceso remoto de terceros (cap. 4).

### Protección de endpoints

- Microsoft Defender for Business (cap. 2, 8).
- Microsoft Intune para dispositivos corporativos y BYOD (cap. 6, 7, 9).
- BitLocker para cifrado de discos (cap. 7, 8).

### Respaldo y continuidad

- Estrategia 3-2-1: NAS Synology DS923+, Veeam Backup, disco USB offline (cap. 2, 7, 8, 11).
- UPS APC para continuidad eléctrica (cap. 4, 7, 11).
- Plan de continuidad, BIA y simulacros periódicos (cap. 11).

### Monitoreo y respuesta

- Wazuh para monitoreo, correlación de eventos y evidencia de auditoría (cap. 2, 4, 8, 9, 11, 12).

### Personas y cultura

- KnowBe4 / GoPhish para capacitación y simulaciones de phishing (cap. 6).
- Política BYOD formalizada (cap. 6).

### Operaciones

- Gestión de cambios, incidentes y software autorizado (cap. 8, 10).
- GLPI + Jira Service Management para tickets y trazabilidad (cap. 5, 10, 12).

### Tabla resumen: Medida → Capítulos del plan

| Medida / herramienta | Capítulos del plan |
|---|---|
| Wazuh | 2, 4, 8, 9, 11, 12 |
| NAS Synology | 2, 7, 8, 11 |
| FortiGate 40F | 4, 8, 9 |
| Veeam Backup | 2, 8, 11 |
| Microsoft Defender for Business | 2, 8 |
| Microsoft Authenticator (MFA) | 4, 6, 9 |
| Bitwarden | 6, 9 |
| Microsoft Intune | 6, 7, 9 |
| BitLocker | 7, 8 |
| GLPI | 5, 10, 12 |
| OCS Inventory | 5 |
| Jira Service Management | 10 |
| KnowBe4 / GoPhish | 6 |
| UPS APC | 4, 7, 11 |
| Google Workspace / M365 | 3, 12 |
| Microsoft Purview (opcional) | 12 |
| Disco USB offline | 2, 8, 11 |

> **Nota de coherencia:** El plan teórico exige respaldos diarios para información de criticidad alta (cap. 8.3). La propuesta práctica implementa esta exigencia mediante NAS + Veeam + copia offline mensual (cap. 8 y 11), en línea con la estrategia 3-2-1.

---
"""

TOOL_CROSS_NOTES = {
    2: {"Wazuh": "2, 4, 8, 9, 11, 12", "NAS": "2, 7, 8, 11"},
    4: {"FortiGate": "4, 8, 9", "Wazuh": "2, 4, 8, 9, 11, 12"},
    8: {"Wazuh": "2, 4, 8, 9, 11, 12", "NAS": "2, 7, 8, 11", "FortiGate": "4, 8, 9"},
    9: {"Wazuh": "2, 4, 8, 9, 11, 12", "FortiGate": "4, 8, 9"},
    11: {"NAS": "2, 7, 8, 11", "Wazuh": "2, 4, 8, 9, 11, 12", "Veeam": "2, 8, 11"},
    12: {"Wazuh": "2, 4, 8, 9, 11, 12", "GLPI": "5, 10, 12"},
}


def split_plan_chapters(text: str) -> dict[int, str]:
    pattern = re.compile(r"^# (\d+)\. ", re.MULTILINE)
    matches = list(pattern.finditer(text))
    chapters: dict[int, str] = {}
    for i, m in enumerate(matches):
        num = int(m.group(1))
        start = m.start()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(text)
        chapters[num] = text[start:end].rstrip()
    return chapters


def split_propuesta_chapters(text: str) -> dict[int, str]:
    lines = text.splitlines()
    # Skip title line
    content = "\n".join(lines[1:]).lstrip()
    pattern = re.compile(r"^(?:#|##) (\d+)\.?\s+", re.MULTILINE)
    matches = list(pattern.finditer(content))
    chapters: dict[int, str] = {}
    for i, m in enumerate(matches):
        num = int(m.group(1))
        start = m.start()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(content)
        block = content[start:end].strip()
        # Remove chapter header line
        block_lines = block.splitlines()
        if block_lines:
            block = "\n".join(block_lines[1:]).strip()
        chapters[num] = block
    return chapters


def normalize_propuesta_block(block: str, chapter: int) -> str:
    """Normalize headings, images, and add cross-ref notes."""
    block = re.sub(
        r"^## (Medidas Técnicas|Procedimientos|Hardware|Software|Plan de Acción)\s*$",
        r"### \1",
        block,
        flags=re.MULTILINE,
    )
    block = re.sub(r"^### (Corto Plazo|Mediano Plazo|Largo Plazo)\s*$", r"#### \1", block, flags=re.MULTILINE)

    image_map = {
        "NAS.png": "imagenes/NAS.png",
        "wazuh.png": "imagenes/wazuh.png",
        "Firewall Perimetral.png": "imagenes/Firewall Perimetral.png",
        "vpn_corporativa.png": "imagenes/vpn_corporativa.png",
        "MFA.png": "imagenes/MFA.png",
    }

    for key, val in image_map.items():
        block = re.sub(
            rf"Imagen:\s*[^\n]*{re.escape(key)}[^\n]*\n",
            f"\n\n![{key}]({val})\n\n",
            block,
            flags=re.IGNORECASE,
        )

    def diagram_after_imagen(m: re.Match) -> str:
        content = m.group(1).rstrip()
        if any(c in content for c in "│▼┌┐└┘┼──") or content.startswith(("Internet", "Red Eléctrica")):
            return f"\n\n```\n{content}\n```\n\n"
        return m.group(0)

    block = re.sub(r"Imagen:\s*\n((?:.*\n)+?)(?=Ventajas)", diagram_after_imagen, block)

    block = re.sub(
        r"(### Software\n)(        Equipos Inmemorian\n(?:.*\n)+?)(\* GLPI:)",
        lambda m: f"{m.group(1)}```\n{m.group(2).rstrip()}\n```\n\n{m.group(3)}",
        block,
    )
    block = re.sub(
        r"(### Software\n)(                    Empleado\n(?:.*\n)+?)(\* Gestores)",
        lambda m: f"{m.group(1)}```\n{m.group(2).rstrip()}\n```\n\n{m.group(3)}",
        block,
    )

    notes = TOOL_CROSS_NOTES.get(chapter, {})
    if notes:
        note_lines = [
            "> **Referencias cruzadas:** "
            + "; ".join(f"{tool} (cap. {caps})" for tool, caps in notes.items())
            + "."
        ]
        block = "\n".join(note_lines) + "\n\n" + block

    return block


def format_implementation_block(chapter: int, raw: str) -> str:
    normalized = normalize_propuesta_block(raw, chapter)
    return f"""
---

## Implementación propuesta

*Fuente: Medidas de Implementación y Plan de Acción — Capítulo {chapter}*

{normalized}
"""


def inject_inline_refs(chapter_text: str) -> str:
    lines = chapter_text.splitlines()
    out: list[str] = []
    i = 0
    while i < len(lines):
        line = lines[i]
        if line in INLINE_REFS:
            out.append(line)
            level = len(line) - len(line.lstrip("#"))
            j = i + 1
            section_lines: list[str] = []
            while j < len(lines):
                nxt = lines[j]
                if nxt.startswith("#"):
                    nxt_level = len(nxt) - len(nxt.lstrip("#"))
                    if nxt_level <= level:
                        break
                section_lines.append(nxt)
                j += 1
            trailing_sep: list[str] = []
            while section_lines and section_lines[-1].strip() == "---":
                trailing_sep.insert(0, section_lines.pop())
            out.extend(section_lines)
            out.append("")
            out.append("> **Correlación con implementación:**")
            for b in INLINE_REFS[line]:
                out.append(f"> - {b}")
            out.append("")
            out.extend(trailing_sep)
            i = j
            continue
        out.append(line)
        i += 1
    return "\n".join(out)


FOOTER = """
*Documento integrado elaborado en el marco del Plan de Seguridad de la Información de Inmemorian.*
*Versión unificada — marco teórico + medidas de implementación.*
"""


def strip_plan_footer(text: str) -> str:
    marker = "*Documento elaborado en el marco del Plan de Seguridad de la Información de Inmemorian.*"
    idx = text.find(marker)
    if idx == -1:
        return text
    prefix = text[:idx].rstrip()
    if prefix.endswith("---"):
        prefix = prefix[:-3].rstrip()
    return prefix


def strip_trailing_separator(text: str) -> str:
    text = text.rstrip()
    if text.endswith("---"):
        text = text[: text.rfind("---")].rstrip()
    return text


def build_index() -> str:
    lines = [
        "## Índice",
        "",
        "### Marco teórico e implementación",
        "",
    ]
    for n, title in CHAPTER_TITLES.items():
        anchor = title.lower().replace(" ", "-").replace("ó", "ó").replace("í", "í")
        slug = re.sub(r"[^a-z0-9\-áéíóúñ]", "", anchor)
        lines.append(f"{n}. [{title}](#{n}-{slug.split('-')[0] if n == 1 else n}-{title.split()[0].lower()})")
    lines.extend([
        "",
        "### Secciones de implementación por capítulo",
        "",
    ])
    for n in range(2, 13):
        lines.append(f"- [Cap. {n} — Implementación propuesta](#implementación-propuesta)")
    lines.extend([
        "",
        "- [Cap. 1 — Síntesis transversal de medidas](#síntesis-de-medidas-transversales-de-implementación)",
        "",
        "---",
        "",
    ])
    return "\n".join(lines)


def build_problematica_section(text: str) -> str:
    body = text.strip()
    if body.startswith("#"):
        body = "\n".join(body.splitlines()[1:]).strip()
    return f"""# Problemática de Inmemorian

*Fuente: `problematica_inmemorian.md` — antecedente del relevamiento que originó el plan de seguridad*

{body}

> Esta problemática constituye el antecedente que motivó la elaboración del presente Plan de Seguridad de la Información, desarrollado a partir del capítulo 1 en adelante.
"""


def build_header() -> str:
    chapters_index = [
        "- [Problemática de Inmemorian](#problemática-de-inmemorian)",
        "",
    ]
    for n, title in CHAPTER_TITLES.items():
        anchor = title.lower().replace(" ", "-")
        chapters_index.append(f"{n}. [{title}](#{n}-{title.split()[0].lower()})")
        if n == 1:
            chapters_index.append("   - [Síntesis transversal](#síntesis-de-medidas-transversales-de-implementación)")
        elif n >= 2:
            chapters_index.append("   - Implementación propuesta (al final del capítulo)")

    return f"""# Plan Integrado de Seguridad de la Información — Inmemorian

*Documento unificado: problemática identificada + marco teórico y normativo + medidas de implementación y plan de acción*

**Fuentes integradas:**
- Problemática: `problematica_inmemorian.md`
- Plan teórico: `plan_seguridad_informacion_inmemorian.md`
- Implementación práctica: `politica_seguridad_propuesta.md`

---

## Índice

{chr(10).join(chapters_index)}

---
"""


def main() -> None:
    plan_text = PLAN.read_text(encoding="utf-8")
    prop_text = PROP.read_text(encoding="utf-8")
    problematica_text = PROBLEMATICA.read_text(encoding="utf-8")

    plan_chapters = split_plan_chapters(plan_text)
    prop_chapters = split_propuesta_chapters(prop_text)

    parts: list[str] = [build_header(), build_problematica_section(problematica_text), "\n---\n"]

    for n in range(1, 13):
        if n not in plan_chapters:
            continue
        raw_chapter = plan_chapters[n]
        if n == 12:
            raw_chapter = strip_plan_footer(raw_chapter)
        chapter_body = strip_trailing_separator(inject_inline_refs(raw_chapter))
        parts.append(chapter_body)

        if n == 1:
            parts.append("\n" + SYNTHESIS.strip())
        elif n in prop_chapters:
            parts.append(format_implementation_block(n, prop_chapters[n]))

        parts.append("\n---\n")

    parts.append(FOOTER)

    OUT.write_text("\n".join(parts), encoding="utf-8")
    print(f"Generado: {OUT} ({OUT.stat().st_size} bytes)")


if __name__ == "__main__":
    main()
