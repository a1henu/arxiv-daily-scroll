---
layout: default
title: SALT-KG: A Benchmark for Semantics-Aware Learning on Enterprise Tables
---

# SALT-KG: A Benchmark for Semantics-Aware Learning on Enterprise Tables
**arXiv**：[2601.07638v1](https://arxiv.org/abs/2601.07638) · [PDF](https://arxiv.org/pdf/2601.07638.pdf)  
**作者**：Isaiah Onando Mulang, Felix Sasaki, Tassilo Klein, Jonas Kolk, Nikolay Grechanov, Johannes Hoffart  

**一句话要点**：提出SALT-KG基准，通过元数据知识图谱增强企业表格的语义感知学习能力。

**关键词**：企业表格学习, 语义感知基准, 元数据知识图谱, 结构化数据推理, 语义条件预测

## 3 点简述
- 核心问题：企业表格数据缺乏语义上下文，限制模型在结构化数据上的推理能力。
- 方法要点：扩展SALT基准，链接多表事务数据与元数据知识图谱，捕获字段描述和业务对象类型。
- 实验或效果：实证分析显示元数据特征提升有限，但揭示模型在语义利用上的差距，推动语义条件推理。

## 摘要（原文）

> Building upon the SALT benchmark for relational prediction (Klein et al., 2024), we introduce SALT-KG, a benchmark for semantics-aware learning on enterprise tables. SALT-KG extends SALT by linking its multi-table transactional data with a structured Operational Business Knowledge represented in a Metadata Knowledge Graph (OBKG) that captures field-level descriptions, relational dependencies, and business object types. This extension enables evaluation of models that jointly reason over tabular evidence and contextual semantics, an increasingly critical capability for foundation models on structured data. Empirical analysis reveals that while metadata-derived features yield modest improvements in classical prediction metrics, these metadata features consistently highlight gaps in the ability of models to leverage semantics in relational context. By reframing tabular prediction as semantics-conditioned reasoning, SALT-KG establishes a benchmark to advance tabular foundation models grounded in declarative knowledge, providing the first empirical step toward semantically linked tables in structured data at enterprise scale.

