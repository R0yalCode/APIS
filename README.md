# MenuBoard - Integración de APIs

## Introducción

Este documento detalla la integración de APIs públicas en la aplicación MenuBoard, enfocada en la gestión de pedidos de restaurantes. Se han investigado y analizado dos APIs relevantes para mejorar la funcionalidad del sistema: Google Maps API y Weather API. A continuación, se describen sus características, requisitos y limitaciones, así como la propuesta de integración de una de ellas en la aplicación.

---

## APIs Investigadas

### 1. Google Maps API

#### Descripción

Google Maps API proporciona herramientas para la geolocalización, búsqueda de lugares, cálculo de rutas y estimación de tiempos de viaje. Es útil para aplicaciones de restaurantes al facilitar la ubicación de sucursales, optimizar rutas de entrega y permitir a los clientes encontrar el local más cercano.

#### Principales funcionalidades

- _Places API_: Permite buscar restaurantes cercanos y obtener detalles de ubicación.
- _Directions API_: Calcula rutas entre puntos, ideal para entregas.
- _Geocoding API_: Convierte direcciones en coordenadas geográficas y viceversa.
- _Distance Matrix API_: Estima tiempos y distancias entre ubicaciones.

#### Requisitos y limitaciones

- Se necesita una clave API proporcionada por Google Cloud.
- Algunos servicios son gratuitos con límites de uso; a partir de cierto punto, se requiere pago.
- Restricciones geográficas pueden aplicar en algunas funcionalidades.

---

### 2. Weather API

#### Descripción

Weather API proporciona información meteorológica en tiempo real y pronósticos para distintas ubicaciones. Es ideal para integrar en aplicaciones de restaurantes para adaptar promociones, recomendar platos según el clima y mejorar la planificación de entregas.

#### Principales funcionalidades

- _Clima en tiempo real_: Datos de temperatura, humedad, precipitaciones y viento.
- _Pronóstico a corto y largo plazo_: Predicciones del clima para los próximos días.
- _Alertas meteorológicas_: Notificaciones sobre condiciones climáticas adversas.
- _Historial climático_: Datos de clima pasados para análisis de tendencias.

#### Requisitos y limitaciones

- Se necesita una clave API para acceder a los servicios.
- Algunas funciones avanzadas requieren suscripción de pago.
- Disponibilidad y precisión pueden variar según la ubicación.

---

## API Seleccionada para la Integración

Se ha elegido la _Google Maps API_ para integrarla en MenuBoard, dado su impacto directo en la optimización de pedidos y entregas.

### Propuesta de Integración

Se integrará Google Maps API en el módulo de pedidos del restaurante con las siguientes funcionalidades:

- _Ubicación de restaurantes_: Mostrar en un mapa todas las sucursales disponibles para que los clientes elijan la más cercana.
- _Cálculo de rutas de entrega_: Utilizar Directions API para planificar rutas eficientes.
- _Estimación de tiempos de entrega_: Distance Matrix API calculará tiempos de llegada en función del tráfico en tiempo real.

### Beneficios para la Aplicación

- _Mejora la experiencia del cliente_, permitiendo encontrar restaurantes cercanos de forma rápida.
- _Optimiza las entregas_, reduciendo tiempos y costos de distribución.
- _Aumenta la eficiencia del restaurante_, ayudando a la logística de pedidos.

---

## Implementación

Para integrar Google Maps API, se han seguido los siguientes pasos:

1. _Obtención de clave API_ desde Google Cloud Console.
2. _Configuración del módulo de pedidos_ para incluir mapas interactivos.
3. _Implementación de Distance Matrix API_ para mostrar tiempos estimados de entrega.
4. _Pruebas de integración_ en entornos de desarrollo y producción.

### Capturas de Pantalla sobre los resultados de aplicacion de APIS

#### API de Google Maps

![Image](https://github.com/user-attachments/assets/747f871d-eec3-4cdf-878c-0ade794c7c6e)

#### Weather API

![Image](https://github.com/user-attachments/assets/a2e7727f-53c7-4512-84e0-6bd5215cab43)

![Image](https://github.com/user-attachments/assets/d45dae8f-3d8e-44e1-ae08-5584c4fb6586)

![Image](https://github.com/user-attachments/assets/6a2cf9d6-a27c-4736-897b-8a1ac24a3126)

![Image](https://github.com/user-attachments/assets/d643bddd-633a-4bfb-bb36-1fd8e73a4ac9)

## Conclusión

La integración de Google Maps API en MenuBoard ha mejorado significativamente la gestión de pedidos y la experiencia del usuario. En futuras actualizaciones, se podría combinar con la Weather API para ofrecer recomendaciones climáticas que influyan en promociones y menús personalizados.

---

## Repositorio del Proyecto

[Enlace al repositorio](https://github.com/R0yalCode/APIS.git)
