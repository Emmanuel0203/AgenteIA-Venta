# AgenteIA-Venta

Proyecto de agentes para apoyo comercial en Sexmonions Shop.

## Estado implementado

Incluye la implementacion funcional de:

- Sprint 1: agente conversacional base + catalogo consultable.
- Sprint 2: agente recomendador con reglas por contexto y popularidad.
- Sprint 3: agente de ventas con upselling y cross-selling.

## Ejecutar en consola
PRINT 1 — Agente Conversacional Base + Catálogo
Objetivo: Crear el agente base que interactúe con el usuario y consulte productos.

Historias de usuario:

Como cliente, quiero buscar productos mediante conversación.
Como sistema, quiero responder preguntas básicas.
Tareas:

implementar agente conversacional
crear dataset de productos (mock o real)
implementar agente de catálogo
conectar catálogo con backend
detectar intención básica:
buscar producto
preguntar precio
construir respuestas simples
probar flujo en consola
Entregables:

agente conversacional funcional
catálogo consultable
respuestas básicas
Criterios de aceptación:

el usuario puede buscar productos
el sistema responde correctamente
no hay errores en flujo básico
Resultado visible: Ya existe un asistente funcional de productos.

SPRINT 2 — Agente Recomendador
Objetivo: Implementar recomendaciones inteligentes de productos.

Historias de usuario:

Como cliente, quiero que me recomienden productos.
Como sistema, quiero sugerir productos relevantes.
Tareas:

implementar agente recomendador
diseñar reglas simples:
por categoría
por popularidad
implementar embeddings (opcional)
integrar recomendador con conversación
manejar consultas como:
"recomiéndame algo"
"qué me sugieres"
Entregables:

agente recomendador funcional
sugerencias automáticas
Criterios de aceptación:

el sistema sugiere productos coherentes
las recomendaciones tienen sentido
Resultado visible: El agente ya no solo responde, también recomienda.

SPRINT 3 — Agente de Ventas (Upselling y flujo de compra)
Objetivo: Convertir el agente en una herramienta de ventas.

Historias de usuario:

Como cliente, quiero recibir sugerencias para complementar mi compra.
Como negocio, quiero aumentar ventas.
Tareas:

implementar agente de ventas
lógica de upselling:
productos premium
lógica de cross-selling:
productos relacionados
detectar intención de compra
guiar al usuario:
"quieres ver algo más?"
mejorar prompts comerciales
Entregables:

agente de ventas funcional
recomendaciones comerciales
Criterios de aceptación:

el sistema impulsa compras adicionales
respuestas orientadas a conversión
Resultado visible: El agente actúa como vendedor digital.
```bash
python -m app.cli
```

## Levantar API

```bash
uvicorn app.api:app --reload
```

Endpoint principal:

- `POST /chat` con body `{"message":"texto del usuario"}`

## Pruebas

```bash
python -m pytest -q
```
