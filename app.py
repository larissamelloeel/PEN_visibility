from __future__ import annotations # "__future__" is a special Python module that enables language features from newer Python versions while maintaining compatibility with older versions.
#postpones the evaluation of type annotations, allowing them to reference types that may not yet be defined.

import json #json.dumps() converts the Python structure into text that follows JavaScript-compatible syntax.

import streamlit as st #streamlit library
import streamlit.components.v1 as components #allows the Streamlit application to embed and execute custom HTML, CSS, and JavaScript. Without it, this line would not work: components.html(app_html(), height=1080, scrolling=False)

st.set_page_config( #This configures the general appearance of the Streamlit page.
    page_title="PEN visibility",
    page_icon="ons.jpg", #small icon shown in the browser tab
    layout="wide", #to correct: maybe make better use of the space
)


MONTHS = [ #it is creating a list containing the names of the months.
    "janeiro",
    "fevereiro",
    "março",
    "abril",
    "maio",
    "junho",
    "julho",
    "agosto",
    "setembro",
    "outubro",
    "novembro",
    "dezembro",
]

BASE_VALUES = [ #example list of datas to test the filters in the chart
    {"month": "janeiro", "scheduled": 233, "additional": 180},
    {"month": "fevereiro", "scheduled": 107, "additional": 181},
    {"month": "março", "scheduled": 53, "additional": 118},
    {"month": "abril", "scheduled": 129, "additional": 162},
    {"month": "maio", "scheduled": 447, "additional": 405},
    {"month": "junho", "scheduled": 651, "additional": 535},
    {"month": "julho", "scheduled": 787, "additional": 641},
    {"month": "agosto", "scheduled": 1100, "additional": 854},
    {"month": "setembro", "scheduled": 1651, "additional": 1174},
    {"month": "outubro", "scheduled": 1560, "additional": 1057},
    {"month": "novembro", "scheduled": 564, "additional": 541},
    {"month": "dezembro", "scheduled": 288, "additional": 370},
]


def app_html() -> str: #def app_html (function) that returns a string
    data = json.dumps(BASE_VALUES, ensure_ascii=False) #This line converts BASE_VALUES from a Python structure into JSON text and stores the result in the variable data
    months = json.dumps(MONTHS, ensure_ascii=False) #likewise to months. "Ensure_ascii" preserve non-ASCII characters, such as accents and ç.

    return f"""
<style>             /*block of CSS that only controls the content inside the iframe.*/
    * {{
        box-sizing: border-box;
    }}

    html,
    body {{
        width: 100%;
        height: 100%;
        margin: 0;
        overflow-x: hidden;
        overflow-y: auto;
        font-family: Arial, Helvetica, sans-serif;
        color: #2d3327;
        background:
            radial-gradient(circle at 4% 92%, rgba(49, 77, 22, 0.13) 0 1px, transparent 1px) 0 0 / 10px 10px,
            linear-gradient(115deg, #f5f7f1 0%, #fbfcf9 42%, #eef3e8 100%);
    }}

    .pen-app {{
        width: 100vw;
        min-height: 100vh;
        overflow-x: hidden;
        background:
            radial-gradient(circle at 5% 89%, rgba(49, 77, 22, 0.12) 0 1px, transparent 1px) 0 0 / 9px 9px,
            linear-gradient(116deg, #f4f7f0 0%, #fbfcf9 48%, #edf3e7 100%);
    }}

    .pen-header {{
        position: fixed;
        inset: 0 0 auto 0;
        z-index: 20;
        height: 102px;
        display: grid;
        grid-template-columns: 1fr;
        align-items: center;
        gap: 28px;
        padding: 0 38px;
        color: #fff;
        background: linear-gradient(90deg, #263d11, #314d16);
        box-shadow: 0 7px 20px rgba(38, 61, 17, 0.28);
    }}

    .brand {{
        display: flex;
        align-items: center;
        gap: 16px;
        min-width: 0;
    }}

    .logo {{
        font-size: 40px;
        line-height: 1;
        font-weight: 800;
        letter-spacing: 0;
    }}

    .brand-line {{
        width: 1px;
        height: 44px;
        background: rgba(255, 255, 255, 0.42);
    }}

    .brand-name {{
        font-size: 14px;
        line-height: 1.25;
        font-weight: 600;
        color: rgba(255, 255, 255, 0.86);
    }}

    .page {{
        min-height: calc(100vh - 102px);
        margin-top: 102px;
        display: grid;
        grid-template-columns: minmax(760px, 1fr);
        place-items: center;
        padding: 22px 38px 28px;
    }}

    .center-stage {{
        width: min(920px, 100%);
        min-width: 0;
        align-self: center;
    }}

    .map-title {{
        width: min(500px, 68%);
        margin: 0 auto 8px;
        padding: 10px 16px;
        font-size: 22px;
        font-weight: 800;
        color: #2d3327;
        background: rgba(255, 255, 255, 0.50);
    }}

    .filters {{
        width: min(540px, 76%);
        margin: 0 auto 10px;
        display: grid;
        grid-template-columns: repeat(3, minmax(0, 1fr));
        gap: 10px;
    }}

    label {{
        display: grid;
        gap: 3px;
        font-size: 10px;
        font-weight: 800;
        color: #48513f;
    }}

    select {{
        width: 100%;
        height: 29px;
        border: 1px solid rgba(49, 77, 22, 0.16);
        border-radius: 4px;
        padding: 0 8px;
        background: rgba(255, 255, 255, 0.92);
        color: #2d3327;
        font-size: 11px;
    }}

    .chart-card {{
        position: relative;
        width: min(860px, 100%);
        height: 454px;
        margin: 0 auto;
        padding: 20px 22px 8px;
        border: 1px solid rgba(49, 77, 22, 0.08);
        border-radius: 8px;
        background: rgba(255, 255, 255, 0.92);
        box-shadow: 0 8px 24px rgba(57, 72, 38, 0.16);
    }}

    .legend {{
        height: 24px;
        display: flex;
        justify-content: center;
        gap: 26px;
        align-items: center;
        font-size: 11px;
        color: #343b2f;
    }}

    .legend span {{
        display: inline-flex;
        align-items: center;
        gap: 8px;
    }}

    .dot {{
        width: 10px;
        height: 10px;
        border-radius: 50%;
        display: inline-block;
    }}

    .green {{
        background: #11823e;
    }}

    .yellow {{
        background: #d9b400;
    }}

    svg {{
        display: block;
        width: 100%;
        height: 380px;
    }}

    .axis.text,
    .axis text,
    .bar-label,
    .total-label {{
        font-family: Arial, Helvetica, sans-serif;
    }}

    .axis.text,
    .axis text {{
        fill: #343b2f;
        font-size: 11px;
    }}

    .axis-title {{
        fill: #343b2f;
        font-size: 13px;
        font-weight: 700;
    }}

    .grid-line {{
        stroke: #e4e9de;
        stroke-width: 1;
    }}

    .axis-line {{
        stroke: #d7ddcf;
        stroke-width: 1;
    }}

    .bar-label {{
        fill: #fff;
        font-size: 11px;
        font-weight: 800;
        pointer-events: none;
    }}

    .total-label {{
        fill: #2c3128;
        font-size: 12px;
        font-weight: 800;
        pointer-events: none;
    }}

    .year {{
        margin-top: -6px;
        text-align: center;
        font-size: 18px;
        font-weight: 800;
        color: #3b3f36;
    }}

    .tooltip {{
        position: absolute;
        min-width: 210px;
        padding: 13px 16px;
        border: 1px solid rgba(49, 77, 22, 0.10);
        border-radius: 8px;
        background: rgba(255, 255, 255, 0.98);
        box-shadow: 0 6px 18px rgba(57, 72, 38, 0.17);
        color: #2d3327;
        font-size: 11px;
        pointer-events: none;
        opacity: 0;
        transform: translate(-50%, -100%);
        transition: opacity 120ms ease;
    }}

    .tooltip.visible {{
        opacity: 1;
    }}

    .tooltip-title {{
        margin-bottom: 10px;
        font-weight: 800;
        font-size: 13px;
    }}

    .tooltip-row {{
        display: flex;
        justify-content: space-between;
        gap: 22px;
        margin: 7px 0;
    }}

    .tooltip-total {{
        margin-top: 9px;
        padding-top: 9px;
        border-top: 1px solid rgba(49, 77, 22, 0.12);
        font-weight: 800;
    }}

    @media (max-width: 1120px) {{
        html,
        body,
        .pen-app {{
            height: auto;
            min-height: 100vh;
            overflow-x: hidden;
            overflow-y: auto;
        }}

        .pen-header {{
            height: auto;
            min-height: 96px;
            grid-template-columns: 1fr;
            gap: 12px;
            padding: 18px;
        }}

        .page {{
            height: auto;
            margin-top: 120px;
            grid-template-columns: 1fr;
            align-items: start;
            padding: 24px 18px;
        }}

        .filters,
        .map-title {{
            width: 100%;
        }}

        .chart-card {{
            height: auto;
        }}
    }}
</style>

<div class="pen-app">
    <header class="pen-header">
        <div class="brand">
            <div class="logo">ONS</div>
            <div class="brand-line"></div>
            <div class="brand-name">Operador Nacional<br>do Sistema Elétrico</div>
        </div>
    </header>

    <main class="page">
        <section class="center-stage">
            <div class="map-title">título do mapa</div>
            <div class="filters">
                <label>nome do filtro
                    <select id="submarket">
                        <option>Filtro submenu</option>
                        <option>Sudeste/Centro-Oeste</option>
                        <option>Sul</option>
                        <option>Nordeste</option>
                        <option>Norte</option>
                    </select>
                </label>
                <label>nome do filtro
                    <select id="source">
                        <option>Todas as fontes</option>
                        <option>Hidráulica</option>
                        <option>Térmica</option>
                        <option>Eólica/Solar</option>
                    </select>
                </label>
                <label>nome do filtro
                    <select id="scenario">
                        <option>Cenário base</option>
                        <option>Carga alta</option>
                        <option>Carga baixa</option>
                    </select>
                </label>
            </div>

            <div class="chart-card" id="chartCard">
                <div class="legend">
                    <span><i class="dot green"></i>Geração Programada (MWmed)</span>
                    <span><i class="dot yellow"></i>Geração Adicional (MWmed)</span>
                </div>
                <svg id="chart" viewBox="0 0 860 380" role="img" aria-label="Gráfico empilhado mensal de geração programada e adicional"></svg>
                <div class="year">2029</div>
                <div class="tooltip" id="tooltip" aria-hidden="true"></div>
            </div>
        </section>
    </main>
</div>

<script>
(() => {{
    const baseValues = {data};
    const months = {months};
    const svg = document.getElementById("chart");
    const tooltip = document.getElementById("tooltip");
    const chartCard = document.getElementById("chartCard");
    const filters = {{
        submarket: document.getElementById("submarket"),
        source: document.getElementById("source"),
        scenario: document.getElementById("scenario"),
    }};

    const factors = {{
        submarket: {{
            "Filtro submenu": 1,
            "Sudeste/Centro-Oeste": 1.08,
            "Sul": 0.72,
            "Nordeste": 0.86,
            "Norte": 0.64,
        }},
        source: {{
            "Todas as fontes": 1,
            "Hidráulica": 0.82,
            "Térmica": 0.38,
            "Eólica/Solar": 0.51,
        }},
        scenario: {{
            "Cenário base": 1,
            "Carga alta": 1.12,
            "Carga baixa": 0.88,
        }},
    }};

    let zoomStart = 0;
    let zoomEnd = months.length - 1;

    function fmt(value) {{
        return Number(value).toLocaleString("pt-BR");
    }}

    function currentMultiplier() {{
        return factors.submarket[filters.submarket.value] *
            factors.source[filters.source.value] *
            factors.scenario[filters.scenario.value];
    }}

    function filteredData() {{
        const multiplier = currentMultiplier();
        return baseValues.map((item) => {{
            const scheduled = Math.round(item.scheduled * multiplier);
            const additional = Math.round(item.additional * multiplier);
            return {{
                month: item.month,
                scheduled,
                additional,
                total: scheduled + additional,
            }};
        }}).slice(zoomStart, zoomEnd + 1);
    }}

    function clearSvg() {{
        while (svg.firstChild) {{
            svg.removeChild(svg.firstChild);
        }}
    }}

    function el(name, attrs = {{}}, parent = svg) {{
        const node = document.createElementNS("http://www.w3.org/2000/svg", name);
        Object.entries(attrs).forEach(([key, value]) => node.setAttribute(key, value));
        parent.appendChild(node);
        return node;
    }}

    function showTooltip(event, item) {{
        tooltip.innerHTML = `
            <div class="tooltip-title">${{item.month}}</div>
            <div class="tooltip-row"><span><i class="dot green"></i>Geração Programada</span><strong>${{fmt(item.scheduled)}}</strong></div>
            <div class="tooltip-row"><span><i class="dot yellow"></i>Geração Adicional</span><strong>${{fmt(item.additional)}}</strong></div>
            <div class="tooltip-total">Total: ${{fmt(item.total)}} MWmed</div>
        `;
        const cardRect = chartCard.getBoundingClientRect();
        const x = Math.min(Math.max(event.clientX - cardRect.left, 130), cardRect.width - 130);
        const y = Math.max(event.clientY - cardRect.top - 18, 86);
        tooltip.style.left = `${{x}}px`;
        tooltip.style.top = `${{y}}px`;
        tooltip.classList.add("visible");
        tooltip.setAttribute("aria-hidden", "false");
    }}

    function hideTooltip() {{
        tooltip.classList.remove("visible");
        tooltip.setAttribute("aria-hidden", "true");
    }}

    function renderChart() {{
        clearSvg();
        const data = filteredData();
        const width = 860;
        const height = 380;
        const plot = {{ left: 70, right: 20, top: 38, bottom: 48 }};
        const plotWidth = width - plot.left - plot.right;
        const plotHeight = height - plot.top - plot.bottom;
        const maxTotal = Math.max(...data.map((item) => item.total), 1);
        const yMax = Math.ceil((maxTotal * 1.12) / 500) * 500;
        const tickStep = yMax <= 1500 ? 250 : 500;
        const ticks = [];

        for (let tick = 0; tick <= yMax; tick += tickStep) {{
            ticks.push(tick);
        }}

        const y = (value) => plot.top + plotHeight - (value / yMax) * plotHeight;
        const band = plotWidth / data.length;
        const barWidth = Math.min(44, band * 0.58);

        ticks.forEach((tick) => {{
            const yy = y(tick);
            el("line", {{ x1: plot.left, x2: width - plot.right, y1: yy, y2: yy, class: "grid-line" }});
            const text = el("text", {{ x: plot.left - 18, y: yy + 4, "text-anchor": "end", class: "axis text" }});
            text.textContent = fmt(tick);
        }});

        el("line", {{ x1: plot.left, x2: width - plot.right, y1: y(0), y2: y(0), class: "axis-line" }});
        el("line", {{ x1: plot.left, x2: plot.left, y1: plot.top, y2: y(0), class: "axis-line" }});

        const axisTitle = el("text", {{
            x: 18,
            y: plot.top + plotHeight / 2,
            transform: `rotate(-90 18 ${{plot.top + plotHeight / 2}})`,
            "text-anchor": "middle",
            class: "axis-title",
        }});
        axisTitle.textContent = "MWmed";

        data.forEach((item, index) => {{
            const x = plot.left + index * band + band / 2 - barWidth / 2;
            const scheduledHeight = y(0) - y(item.scheduled);
            const additionalHeight = y(item.scheduled) - y(item.total);
            const group = el("g");

            const scheduledBar = el("rect", {{
                x,
                y: y(item.scheduled),
                width: barWidth,
                height: Math.max(0, scheduledHeight),
                fill: "#11823e",
                rx: 1,
            }}, group);

            const additionalBar = el("rect", {{
                x,
                y: y(item.total),
                width: barWidth,
                height: Math.max(0, additionalHeight),
                fill: "#d9b400",
                rx: 1,
            }}, group);

            [scheduledBar, additionalBar].forEach((bar) => {{
                bar.style.cursor = "default";
                bar.addEventListener("mousemove", (event) => showTooltip(event, item));
                bar.addEventListener("mouseleave", hideTooltip);
            }});

            const scheduledLabel = el("text", {{
                x: x + barWidth / 2,
                y: y(item.scheduled / 2) + 4,
                "text-anchor": "middle",
                class: "bar-label",
            }});
            scheduledLabel.textContent = fmt(item.scheduled);

            const additionalLabel = el("text", {{
                x: x + barWidth / 2,
                y: y(item.scheduled + item.additional / 2) + 4,
                "text-anchor": "middle",
                class: "bar-label",
            }});
            additionalLabel.textContent = fmt(item.additional);

            const totalLabel = el("text", {{
                x: x + barWidth / 2,
                y: y(item.total) - 10,
                "text-anchor": "middle",
                class: "total-label",
            }});
            totalLabel.textContent = fmt(item.total);

            const monthLabel = el("text", {{
                x: x + barWidth / 2,
                y: height - 14,
                "text-anchor": "middle",
                class: "axis text",
            }});
            monthLabel.textContent = item.month;
        }});
    }}

    function clampZoom(direction) {{
        const visible = zoomEnd - zoomStart + 1;
        if (direction > 0 && visible > 6) {{
            zoomStart += 1;
            zoomEnd -= 1;
        }}
        if (direction < 0 && visible < months.length) {{
            zoomStart = Math.max(0, zoomStart - 1);
            zoomEnd = Math.min(months.length - 1, zoomEnd + 1);
        }}
        renderChart();
    }}

    Object.values(filters).forEach((select) => select.addEventListener("change", renderChart));

    chartCard.addEventListener("wheel", (event) => {{
        event.preventDefault();
        clampZoom(event.deltaY > 0 ? 1 : -1);
    }}, {{ passive: false }});

    chartCard.addEventListener("dblclick", () => {{
        zoomStart = 0;
        zoomEnd = months.length - 1;
        renderChart();
    }});

    renderChart();
}})();
</script>
"""


st.markdown(
    """
    <style>
        html,
        body,
        .stApp,
        [data-testid="stAppViewContainer"],
        [data-testid="stAppViewContainer"] > .main {
            margin: 0;
            padding: 0;
            overflow: hidden;
            background: #263d11;
        }

        [data-testid="stHeader"],
        [data-testid="stToolbar"],
        [data-testid="stSidebar"],
        [data-testid="stDecoration"],
        #MainMenu,
        footer {
            display: none;
        }

        .block-container {
            max-width: 100%;
            padding: 0;
        }

        [data-testid="stVerticalBlock"],
        [data-testid="stElementContainer"],
        [data-testid="stIFrame"] {
            gap: 0;
            margin: 0;
            padding: 0;
        }

        iframe {
            display: block;
            height: 100vh !important;
            min-height: 100vh;
            border: 0;
            margin: 0;
            padding: 0;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

components.html(app_html(), height=1080, scrolling=False)
