---
layout: default
title: Return of the Schema: Building Complete Datasets for Machine Learning and Reasoning on Knowledge Graphs
---

# Return of the Schema: Building Complete Datasets for Machine Learning and Reasoning on Knowledge Graphs
**arXiv**：[2602.14795v1](https://arxiv.org/abs/2602.14795) · [PDF](https://arxiv.org/pdf/2602.14795.pdf)  
**作者**：Ivan Diliso, Roberto Barile, Claudia d'Amato, Nicola Fanizzi  

**一句话要点**：提出资源与工作流以构建包含模式与事实的完整知识图谱数据集，支持机器学习与推理评估。

**关键词**：知识图谱数据集, 模式提取, 推理服务, 机器学习评估, OWL序列化, 张量表示

## 3 点简述
- 核心问题：现有知识图谱精炼数据集通常仅含事实，缺乏模式信息，限制了依赖约束或推理的方法评估。
- 方法要点：提供工作流提取包含模式和事实的完整数据集，处理不一致性并利用推理推导隐式知识。
- 实验或效果：生成新数据集并丰富现有数据集，以OWL序列化支持推理，并提供张量表示工具。

## 摘要（原文）

> Datasets for the experimental evaluation of knowledge graph refinement algorithms typically contain only ground facts, retaining very limited schema level knowledge even when such information is available in the source knowledge graphs. This limits the evaluation of methods that rely on rich ontological constraints, reasoning or neurosymbolic techniques and ultimately prevents assessing their performance in large-scale, real-world knowledge graphs. In this paper, we present \resource{} the first resource that provides a workflow for extracting datasets including both schema and ground facts, ready for machine learning and reasoning services, along with the resulting curated suite of datasets. The workflow also handles inconsistencies detected when keeping both schema and facts and also leverage reasoning for entailing implicit knowledge. The suite includes newly extracted datasets from KGs with expressive schemas while simultaneously enriching existing datasets with schema information. Each dataset is serialized in OWL making it ready for reasoning services. Moreover, we provide utilities for loading datasets in tensor representations typical of standard machine learning libraries.

