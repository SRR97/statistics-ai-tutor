# Phase 0 — Project Definition

## Statistics AI Tutor

**Proyecto:** Asistente académico basado en Inteligencia Artificial Generativa para un curso de Estadística  
**Tipo de proyecto:** Aplicación web con IA Generativa y Retrieval-Augmented Generation (RAG)  
**Estado:** En desarrollo  

---

## 1. Contexto del proyecto

El presente proyecto surge en el contexto de un curso académico de Estadística, en el cual los estudiantes disponen de notas de clase y material proporcionado por la asignatura como fuente principal para el estudio y consulta de los conceptos desarrollados durante el curso.

A medida que aumenta la cantidad de contenido, localizar información específica, relacionar conceptos y resolver dudas a partir de las notas puede requerir revisar manualmente diferentes secciones del material. En este contexto, las herramientas de Inteligencia Artificial Generativa ofrecen la posibilidad de desarrollar mecanismos de consulta más interactivos, mediante los cuales un estudiante pueda formular preguntas en lenguaje natural y recibir explicaciones relacionadas con el contenido estudiado.

Este proyecto propone el desarrollo de un asistente académico basado en Inteligencia Artificial Generativa, orientado específicamente a la consulta y comprensión del material del curso de Estadística. El sistema utilizará las notas de clase como fuente de conocimiento y empleará una arquitectura de Retrieval-Augmented Generation (RAG), con el propósito de recuperar fragmentos relevantes del material antes de generar una respuesta.

De esta manera, el proyecto busca explorar la aplicación de técnicas modernas de Inteligencia Artificial Generativa en un contexto educativo, manteniendo como principio fundamental que las respuestas del asistente estén sustentadas en el material académico proporcionado.

## 2. Planteamiento del problema

Los cursos de Estadística integran conceptos teóricos, expresiones matemáticas, supuestos, procedimientos de estimación e interpretación de resultados que se encuentran distribuidos a lo largo de diferentes materiales y notas de clase. Esta característica puede dificultar la consulta eficiente de la información cuando un estudiante necesita resolver una duda específica, recordar la definición de un concepto o relacionar contenidos estudiados en diferentes momentos del curso.

Los mecanismos tradicionales de consulta requieren que el estudiante identifique manualmente el documento y la sección en la que se encuentra la información relevante. A medida que aumenta la cantidad de material académico disponible, este proceso puede requerir más tiempo y dificultar la localización de contenidos relacionados entre sí.

Por otra parte, los modelos de lenguaje de gran escala (LLM) permiten realizar consultas mediante lenguaje natural y generar explicaciones sobre una amplia variedad de temas. Sin embargo, utilizar un modelo de lenguaje de propósito general como mecanismo de consulta académica introduce una dificultad adicional: sus respuestas no necesariamente se encuentran fundamentadas en las notas, definiciones, notación o enfoque utilizado específicamente en el curso.

Esto resulta especialmente relevante en Estadística, donde una respuesta aparentemente correcta puede depender de determinados supuestos, definiciones o convenciones. Por ejemplo, las notas utilizadas inicialmente en este proyecto establecen explícitamente supuestos para el modelo de Regresión Lineal Simple y distinguen entre conceptos como parámetros, estimadores, valores ajustados y residuos. Por lo tanto, una herramienta de apoyo académico debe procurar conservar el contexto y la terminología del material proporcionado por la asignatura.

En consecuencia, se identifica la necesidad de desarrollar un mecanismo de consulta que permita a los estudiantes formular preguntas en lenguaje natural y obtener respuestas sustentadas prioritariamente en el material académico del curso, recuperando la información relevante antes de generar la respuesta y proporcionando referencias que permitan al estudiante verificar su procedencia.

A partir de este problema se plantea la siguiente pregunta:

**¿Cómo desarrollar un asistente académico basado en Inteligencia Artificial Generativa que permita consultar mediante lenguaje natural los contenidos de un curso de Estadística y generar respuestas relevantes, comprensibles y sustentadas en las notas de clase proporcionadas?**

## 3. Justificación

El desarrollo de este proyecto se justifica por la necesidad de facilitar el acceso y la consulta del material académico de un curso de Estadística mediante herramientas que permitan una interacción más natural con la información. En lugar de depender exclusivamente de búsquedas manuales dentro de las notas de clase, un asistente conversacional puede proporcionar un mecanismo complementario mediante el cual los estudiantes formulen preguntas directamente sobre los contenidos estudiados.

Desde el punto de vista académico, el proyecto busca apoyar el proceso de aprendizaje proporcionando respuestas contextualizadas a partir del material suministrado por la asignatura. La posibilidad de recuperar los fragmentos relevantes de las notas antes de generar una respuesta permite conservar, en la medida de lo posible, la terminología, las definiciones y los supuestos utilizados durante el curso, además de ofrecer al estudiante referencias que le permitan consultar directamente la fuente original.

Desde el punto de vista tecnológico, el proyecto permite explorar la aplicación de modelos de lenguaje de gran escala (LLM) junto con técnicas de Retrieval-Augmented Generation (RAG). Esta arquitectura permite combinar las capacidades de generación y comprensión de lenguaje natural de los modelos generativos con una fuente de conocimiento externa y delimitada, en este caso las notas académicas del curso.

Adicionalmente, el desarrollo del sistema permitirá abordar diferentes componentes propios de una aplicación moderna de Inteligencia Artificial, incluyendo el procesamiento de documentos, segmentación de texto, generación de embeddings, recuperación de información, integración con modelos de lenguaje, desarrollo de servicios mediante una API y construcción de una interfaz de interacción con el usuario.

Finalmente, el proyecto permitirá evaluar experimentalmente el comportamiento del asistente mediante un conjunto de preguntas relacionadas con los contenidos del curso. Esto permitirá analizar aspectos como la capacidad de recuperación de información relevante, la correspondencia de las respuestas con el material académico y el desempeño de diferentes configuraciones del sistema.

Por estas razones, el proyecto no se limita a la implementación de un chatbot, sino que constituye un ejercicio aplicado de diseño, construcción y evaluación de un sistema de Inteligencia Artificial Generativa orientado a un contexto académico específico.

## 4. Objetivo general

Desarrollar un asistente académico conversacional basado en Inteligencia Artificial Generativa y Retrieval-Augmented Generation (RAG) que permita a los estudiantes consultar mediante lenguaje natural los contenidos de un curso de Estadística y obtener respuestas comprensibles y sustentadas en las notas de clase proporcionadas, incluyendo referencias a las fuentes utilizadas.

## 5. Objetivos específicos

1. Procesar y estructurar las notas de clase del curso de Estadística para que puedan ser utilizadas como fuente de conocimiento por el sistema.

2. Implementar un mecanismo de segmentación del contenido que permita dividir los documentos académicos en fragmentos adecuados para su posterior recuperación.

3. Generar representaciones vectoriales (embeddings) de los fragmentos del material académico y almacenarlas en un sistema que permita realizar búsquedas por similitud semántica.

4. Implementar un mecanismo de recuperación de información que permita identificar los fragmentos del material académico más relevantes para una pregunta formulada por el usuario.

5. Integrar el mecanismo de recuperación con un modelo de lenguaje de gran escala mediante una arquitectura Retrieval-Augmented Generation (RAG), utilizando la información recuperada como contexto para la generación de respuestas.

6. Incorporar referencias a las fuentes utilizadas en las respuestas generadas, permitiendo identificar el material académico del cual fue recuperada la información.

7. Desarrollar una interfaz conversacional que permita a los estudiantes realizar consultas en lenguaje natural e interactuar con el asistente académico.

8. Implementar mecanismos para la resolución de cálculos estadísticos cuando las consultas requieran operaciones matemáticas, utilizando herramientas computacionales apropiadas en lugar de depender exclusivamente del modelo de lenguaje.

9. Diseñar un conjunto de pruebas que permita evaluar el desempeño del sistema en aspectos como recuperación de información relevante, correspondencia de las respuestas con el material académico y capacidad para responder adecuadamente a preguntas relacionadas con el contenido del curso.

10. Analizar los resultados obtenidos durante la evaluación para identificar limitaciones del sistema y oportunidades de mejora.

## 6. Alcance del proyecto

La primera versión del sistema estará orientada a la consulta y comprensión de los contenidos académicos proporcionados en las notas de un curso de Estadística.

El proyecto comprenderá las siguientes funcionalidades:

- Procesamiento de documentos académicos en formato PDF para extraer y estructurar su contenido textual.

- Segmentación del contenido de los documentos en fragmentos adecuados para su posterior recuperación.

- Generación y almacenamiento de embeddings que permitan representar semánticamente los fragmentos del material académico.

- Recuperación de fragmentos relevantes del material a partir de preguntas formuladas por los usuarios en lenguaje natural.

- Integración con un modelo de lenguaje de gran escala mediante una arquitectura Retrieval-Augmented Generation (RAG).

- Generación de respuestas utilizando como contexto la información recuperada de las notas de clase.

- Presentación de referencias que permitan identificar el documento y, cuando la información disponible lo permita, la página de donde proviene el contenido utilizado para generar la respuesta.

- Implementación de una interfaz web conversacional desde la cual el usuario pueda realizar preguntas e interactuar con el asistente.

- Implementación de funciones computacionales para apoyar la resolución de determinados cálculos estadísticos relacionados con los contenidos del curso.

- Desarrollo de un conjunto de preguntas de evaluación para analizar el comportamiento del sistema y comparar diferentes configuraciones del proceso de recuperación.

El sistema se desarrollará inicialmente utilizando como primera fuente de conocimiento las notas disponibles de la asignatura y su arquitectura permitirá incorporar posteriormente nuevos documentos del mismo curso.

## 7. Fuera de alcance

Para mantener el proyecto dentro de unos límites técnicos y académicos manejables, la primera versión del sistema no contempla las siguientes funcionalidades:

- Entrenamiento desde cero de un modelo de lenguaje de gran escala.

- Modificación de los parámetros internos de un LLM mediante procesos de entrenamiento o fine-tuning.

- Desarrollo de aplicaciones móviles nativas para Android o iOS.

- Interacción mediante reconocimiento o generación de voz.

- Integración directa con plataformas institucionales de gestión académica.

- Consulta automática de fuentes externas de Internet para complementar las respuestas académicas.

- Sustitución del docente o de los mecanismos formales de evaluación del curso.

- Garantía absoluta de exactitud en todas las respuestas generadas por el modelo.

- Resolución automática de cualquier tipo de problema matemático o estadístico fuera de los contenidos y funcionalidades implementadas en el sistema.

- Uso del asistente como fuente académica primaria en reemplazo de las notas, bibliografía o material oficial de la asignatura.

## 8. Usuarios objetivo

### 8.1 Usuario principal: estudiante

El usuario principal del sistema será el estudiante del curso de Estadística que requiera consultar, comprender o relacionar conceptos presentes en el material académico proporcionado por la asignatura.

El estudiante podrá interactuar con el asistente mediante lenguaje natural sin necesidad de conocer la estructura interna de los documentos ni las tecnologías utilizadas por el sistema.

Entre sus principales necesidades se encuentran:

- Consultar definiciones y conceptos estadísticos.
- Solicitar explicaciones de conceptos presentes en las notas de clase.
- Consultar fórmulas, supuestos y procedimientos.
- Identificar en qué documento o página se encuentra determinada información.
- Relacionar conceptos distribuidos en diferentes partes del material académico.
- Resolver determinados cálculos estadísticos soportados por el sistema.
- Obtener explicaciones de los resultados de dichos cálculos.

### 8.2 Usuario secundario: desarrollador o evaluador

Como usuario secundario se considera al responsable del desarrollo y evaluación del sistema, quien podrá analizar su comportamiento mediante un conjunto de preguntas de prueba, revisar la información recuperada y comparar diferentes configuraciones del proceso de recuperación.

Este usuario tendrá como objetivo identificar errores, limitaciones y oportunidades de mejora en el funcionamiento del asistente.

## 9. Casos de uso

Los siguientes casos de uso representan las principales formas de interacción previstas para la primera versión del sistema.

| ID | Caso de uso | Descripción |
|---|---|---|
| UC-01 | Consultar un concepto | El estudiante formula una pregunta sobre un concepto estadístico y el sistema genera una explicación basada en el material académico disponible. |
| UC-02 | Consultar una fórmula | El estudiante solicita una fórmula o expresión matemática incluida en las notas y el sistema recupera la información correspondiente. |
| UC-03 | Consultar supuestos | El estudiante pregunta por los supuestos asociados a un modelo o procedimiento estadístico presentado en el curso. |
| UC-04 | Solicitar una explicación | El estudiante solicita que un concepto del material sea explicado de una manera más comprensible conservando su significado estadístico. |
| UC-05 | Localizar información | El estudiante pregunta dónde se encuentra determinado contenido y el sistema proporciona referencias al documento y, cuando sea posible, a la página correspondiente. |
| UC-06 | Relacionar conceptos | El estudiante realiza una pregunta que requiere recuperar información relacionada disponible en diferentes fragmentos del material académico. |
| UC-07 | Realizar un cálculo estadístico | El estudiante proporciona los datos necesarios para un cálculo soportado por el sistema y recibe el resultado junto con una explicación. |
| UC-08 | Consultar la fuente de una respuesta | El estudiante puede identificar qué fragmentos o referencias del material académico fueron utilizados para construir la respuesta. |
| UC-09 | Preguntar por información no disponible | Cuando el material recuperado no proporciona información suficiente para responder una pregunta, el sistema debe indicarlo en lugar de presentar la respuesta como si estuviera sustentada en las notas. |

## 10. Requisitos funcionales

Los requisitos funcionales describen las capacidades que deberá proporcionar el sistema para cumplir con los objetivos y casos de uso definidos.

| ID | Requisito funcional |
|---|---|
| RF-01 | El sistema deberá permitir la incorporación y procesamiento de documentos académicos en formato PDF como fuentes de conocimiento. |
| RF-02 | El sistema deberá extraer y estructurar el contenido textual de los documentos incorporados, conservando metadatos relevantes como el nombre del documento y, cuando sea posible, el número de página. |
| RF-03 | El sistema deberá segmentar el contenido extraído en fragmentos adecuados para su posterior recuperación. |
| RF-04 | El sistema deberá generar representaciones vectoriales (embeddings) de los fragmentos y almacenarlas para permitir búsquedas por similitud semántica. |
| RF-05 | El sistema deberá permitir al usuario formular preguntas relacionadas con el contenido académico mediante lenguaje natural. |
| RF-06 | El sistema deberá recuperar fragmentos del material académico relacionados con la pregunta realizada por el usuario. |
| RF-07 | El sistema deberá utilizar la información recuperada como contexto para la generación de respuestas mediante un modelo de lenguaje. |
| RF-08 | El sistema deberá proporcionar referencias que permitan identificar las fuentes académicas utilizadas para generar una respuesta. |
| RF-09 | El sistema deberá indicar cuando la información recuperada del material académico no sea suficiente para sustentar una respuesta. |
| RF-10 | El sistema deberá proporcionar una interfaz web conversacional para la interacción entre el estudiante y el asistente. |
| RF-11 | El sistema deberá permitir la incorporación posterior de nuevos documentos pertenecientes al mismo curso sin requerir rediseñar la arquitectura completa. |
| RF-12 | El sistema deberá permitir ejecutar determinados cálculos estadísticos mediante funciones computacionales implementadas para este propósito. |
| RF-13 | El sistema deberá presentar los resultados de los cálculos junto con una explicación comprensible para el estudiante. |

## 11. Requisitos no funcionales

Los requisitos no funcionales establecen características de calidad, mantenibilidad, seguridad y desempeño esperadas para el sistema.

| ID | Categoría | Requisito no funcional |
|---|---|---|
| RNF-01 | Usabilidad | La interfaz deberá permitir que un estudiante realice consultas sin necesidad de poseer conocimientos técnicos sobre Inteligencia Artificial o sobre la arquitectura interna del sistema. |
| RNF-02 | Claridad | Las respuestas deberán presentarse utilizando un lenguaje comprensible y una estructura adecuada para un contexto académico. |
| RNF-03 | Trazabilidad | Siempre que una respuesta se encuentre sustentada en el material académico recuperado, el sistema deberá permitir identificar la fuente utilizada. |
| RNF-04 | Mantenibilidad | El código deberá organizarse de manera modular, separando responsabilidades como procesamiento de documentos, recuperación de información, interacción con el LLM, cálculos estadísticos y API. |
| RNF-05 | Extensibilidad | La arquitectura deberá facilitar la incorporación de nuevos documentos y funcionalidades sin requerir modificaciones significativas en los componentes existentes. |
| RNF-06 | Seguridad | Las credenciales y claves utilizadas para acceder a servicios externos no deberán almacenarse directamente en el código fuente ni publicarse en el repositorio. |
| RNF-07 | Privacidad | El sistema deberá evitar enviar información innecesaria a servicios externos y utilizar únicamente el contexto requerido para procesar las consultas. |
| RNF-08 | Confiabilidad | El sistema deberá diferenciar, en la medida de lo posible, entre respuestas sustentadas por el material recuperado y situaciones en las que no existe suficiente información disponible. |
| RNF-09 | Rendimiento | El sistema deberá proporcionar tiempos de respuesta adecuados para permitir una interacción conversacional fluida durante su uso académico. |
| RNF-10 | Evaluabilidad | El funcionamiento del sistema deberá poder analizarse mediante un conjunto reproducible de preguntas y métricas de evaluación. |

## 12. Fuentes de conocimiento

El asistente utilizará como fuente primaria de conocimiento los documentos académicos proporcionados en el curso de Estadística. Estos documentos serán procesados e incorporados a la base de conocimiento del sistema para permitir posteriormente la recuperación de información mediante técnicas de búsqueda semántica.

### 12.1 Fuente inicial

La primera fuente de conocimiento incorporada al proyecto corresponde al siguiente material académico:

| ID | Documento | Tipo | Contenido principal | Estado |
|---|---|---|---|---|
| DOC-001 | Análisis de regresión — Clase 2 | Notas de clase en PDF | Regresión Lineal Simple, estimación, propiedades de los estimadores e inferencia | Disponible |

Este documento será utilizado inicialmente para desarrollar y validar el flujo completo de procesamiento, segmentación, generación de embeddings, recuperación de información y generación de respuestas.

### 12.2 Incorporación de nuevas fuentes

La arquitectura del sistema deberá permitir incorporar progresivamente nuevos documentos del mismo curso. Cada documento será identificado mediante metadatos que permitan conservar información sobre su procedencia.

Como mínimo, se buscará conservar los siguientes metadatos:

- Identificador del documento.
- Nombre del documento.
- Número de página, cuando pueda ser identificado.
- Fragmento de contenido recuperado.
- Información adicional necesaria para rastrear la procedencia del contenido.

### 12.3 Política de utilización de las fuentes

Las respuestas académicas del asistente deberán construirse prioritariamente utilizando la información recuperada de las fuentes de conocimiento incorporadas al sistema.

Cuando el material disponible no proporcione información suficiente para responder una pregunta, el sistema deberá comunicar esta limitación al usuario en lugar de presentar como sustentada en las notas una respuesta obtenida exclusivamente del conocimiento general del modelo de lenguaje.

Las fuentes externas de Internet no formarán parte de la base de conocimiento de la primera versión del sistema.

## 13. Restricciones del proyecto

El desarrollo del proyecto estará sujeto a las siguientes restricciones:

- La calidad de las respuestas dependerá de la calidad, estructura y cantidad de información disponible en los documentos académicos incorporados al sistema.

- La primera versión utilizará principalmente documentos en formato PDF correspondientes a las notas del curso.

- El sistema dependerá de servicios externos para acceder al modelo de lenguaje y, cuando corresponda, a modelos de embeddings.

- El uso de servicios externos podrá estar sujeto a límites de utilización, disponibilidad, latencia y costos asociados a las APIs utilizadas.

- El proyecto será desarrollado con recursos computacionales convencionales, por lo que no se contempla infraestructura especializada para el entrenamiento de modelos de Inteligencia Artificial de gran escala.

- Las capacidades del sistema estarán limitadas inicialmente a los contenidos académicos incorporados a su base de conocimiento.

- La correcta recuperación de información dependerá de decisiones técnicas como la estrategia de segmentación, el modelo de embeddings y la configuración del mecanismo de recuperación.

- Las respuestas generadas por un modelo de lenguaje pueden presentar errores, por lo que el sistema será diseñado como una herramienta de apoyo académico y no como sustituto del material oficial o del criterio docente.

- El desarrollo se realizará de manera incremental, priorizando inicialmente una versión funcional mínima antes de incorporar funcionalidades adicionales.

## 14. Criterios de éxito

El proyecto se considerará funcionalmente exitoso cuando se cumplan, como mínimo, los siguientes criterios:

1. El sistema puede procesar correctamente al menos un documento académico del curso y convertir su contenido en información utilizable por el mecanismo de recuperación.

2. El sistema puede segmentar el contenido y generar las representaciones necesarias para realizar búsquedas semánticas.

3. Ante una pregunta relacionada con el material disponible, el sistema puede recuperar fragmentos relevantes de las notas de clase.

4. El sistema puede utilizar los fragmentos recuperados como contexto para generar una respuesta comprensible relacionada con la pregunta realizada.

5. Las respuestas permiten identificar la fuente académica utilizada y, cuando sea técnicamente posible, la página correspondiente.

6. Ante preguntas cuya respuesta no se encuentre suficientemente sustentada en el material disponible, el sistema puede comunicar esta limitación al usuario.

7. El estudiante puede interactuar con el sistema mediante una interfaz web conversacional sin necesidad de utilizar directamente herramientas de programación.

8. Los cálculos estadísticos implementados mediante funciones computacionales producen resultados verificables mediante casos de prueba conocidos.

9. El sistema puede ser evaluado utilizando un conjunto reproducible de preguntas relacionadas con los contenidos del curso.

10. Los resultados de la evaluación pueden almacenarse y analizarse para comparar el comportamiento de diferentes configuraciones del sistema.

## 15. Entregables

Al finalizar el proyecto se espera disponer de los siguientes entregables:

1. **Repositorio del proyecto:** código fuente organizado y versionado mediante Git.

2. **Documentación técnica:** descripción del problema, arquitectura, configuración, instalación y funcionamiento del sistema.

3. **Pipeline de procesamiento documental:** componentes para cargar, extraer, estructurar y segmentar las notas académicas.

4. **Sistema de recuperación:** mecanismo de embeddings, almacenamiento vectorial y recuperación semántica de información.

5. **Pipeline RAG:** integración entre el mecanismo de recuperación y el modelo de lenguaje para generar respuestas sustentadas en el material académico.

6. **Módulo de cálculos estadísticos:** funciones computacionales implementadas para los cálculos soportados por el asistente.

7. **API del sistema:** servicio que permita comunicar la lógica del asistente con la interfaz de usuario.

8. **Interfaz web conversacional:** aplicación desde la cual los estudiantes puedan realizar consultas al asistente.

9. **Conjunto de evaluación:** colección estructurada de preguntas y respuestas o criterios esperados para evaluar el funcionamiento del sistema.

10. **Resultados de evaluación:** métricas y análisis del comportamiento del asistente bajo diferentes tipos de preguntas o configuraciones.

11. **Aplicación funcional:** versión integrada del sistema que permita demostrar el flujo completo desde la pregunta del estudiante hasta la generación de una respuesta con sus respectivas fuentes.