---
layout: default
title: CycleChart: A Unified Consistency-Based Learning Framework for Bidirectional Chart Understanding and Generation
---

# CycleChart: A Unified Consistency-Based Learning Framework for Bidirectional Chart Understanding and Generation
**arXiv**：[2512.19173v1](https://arxiv.org/abs/2512.19173) · [PDF](https://arxiv.org/pdf/2512.19173.pdf)  
**作者**：Dazhen Deng, Sen Yang, Yuchen He, Yuan Tian, Yingcai Wu  

**一句话要点**：提出CycleChart框架，通过一致性学习统一双向图表理解与生成任务

**关键词**：图表理解, 图表生成, 一致性学习, 多任务学习, 模式预测, 数据解析

## 3 点简述
- 核心问题：现有图表任务孤立研究，缺乏共享语义学习，阻碍双向理解与生成
- 方法要点：采用模式中心化表述，构建多任务数据集，引入生成-解析一致性目标
- 实验或效果：在图表生成、解析和问答任务上取得强结果，提升跨任务泛化能力

## 摘要（原文）

> Current chart-specific tasks, such as chart question answering, chart parsing, and chart generation, are typically studied in isolation, preventing models from learning the shared semantics that link chart generation and interpretation. We introduce CycleChart, a consistency-based learning framework for bidirectional chart understanding and generation. CycleChart adopts a schema-centric formulation as a common interface across tasks. We construct a consistent multi-task dataset, where each chart sample includes aligned annotations for schema prediction, data parsing, and question answering. To learn cross-directional chart semantics, CycleChart introduces a generate-parse consistency objective: the model generates a chart schema from a table and a textual query, then learns to recover the schema and data from the generated chart, enforcing semantic alignment across directions. CycleChart achieves strong results on chart generation, chart parsing, and chart question answering, demonstrating improved cross-task generalization and marking a step toward more general chart understanding models.

