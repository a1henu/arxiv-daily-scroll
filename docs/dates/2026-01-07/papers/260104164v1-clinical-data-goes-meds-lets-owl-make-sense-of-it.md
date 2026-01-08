---
layout: default
title: Clinical Data Goes MEDS? Let's OWL make sense of it
---

# Clinical Data Goes MEDS? Let's OWL make sense of it
**arXiv**：[2601.04164v1](https://arxiv.org/abs/2601.04164) · [PDF](https://arxiv.org/pdf/2601.04164.pdf)  
**作者**：Alberto Marfoglia, Jong Ho Jhee, Adrien Coulet  

**一句话要点**：提出MEDS-OWL本体和meds2rdf工具，将医疗事件数据标准与语义网集成以提升互操作性。

**关键词**：医疗事件数据标准, 语义网集成, RDF转换, 本体设计, 数据互操作性, 临床数据分析

## 3 点简述
- 医疗数据缺乏标准化语义表示，阻碍机器学习应用和跨数据集互操作性。
- 开发轻量级OWL本体MEDS-OWL和Python库meds2rdf，将MEDS事件转换为RDF图。
- 在合成颅内动脉瘤数据集上验证，支持FAIR数据转换和基于图的分析基础。

## 摘要（原文）

> The application of machine learning on healthcare data is often hindered by the lack of standardized and semantically explicit representation, leading to limited interoperability and reproducibility across datasets and experiments. The Medical Event Data Standard (MEDS) addresses these issues by introducing a minimal, event-centric data model designed for reproducible machine-learning workflows from health data. However, MEDS is defined as a data-format specification and does not natively provide integration with the Semantic Web ecosystem. In this article, we introduce MEDS-OWL, a lightweight OWL ontology that provides formal concepts and relations to enable representing MEDS datasets as RDF graphs. Additionally, we implemented meds2rdf, a Python conversion library that transforms MEDS events into RDF graphs, ensuring conformance with the ontology. We demonstrate the approach on a synthetic clinical dataset that describes patient care pathways for ruptured intracranial aneurysms and validate the resulting graph using SHACL constraints. The first release of MEDS-OWL comprises 13 classes, 10 object properties, 20 data properties, and 24 OWL axioms. Combined with meds2rdf, it enables data transformation into FAIR-aligned datasets, provenance-aware publishing, and interoperability of event-based clinical data. By bridging MEDS with the Semantic Web, this work contributes a reusable semantic layer for event-based clinical data and establishes a robust foundation for subsequent graph-based analytics.

