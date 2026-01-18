---
layout: default
title: Process-Guided Concept Bottleneck Model
---

# Process-Guided Concept Bottleneck Model
**arXiv**：[2601.10562v1](https://arxiv.org/abs/2601.10562) · [PDF](https://arxiv.org/pdf/2601.10562.pdf)  
**作者**：Reza M. Asiyabi, SEOSAW Partnership, Steven Hancock, Casey Ryan  

**一句话要点**：提出过程引导概念瓶颈模型以解决科学领域稀疏监督下的可解释性问题

**关键词**：概念瓶颈模型, 过程引导学习, 可解释人工智能, 地球观测, 稀疏监督, 因果机制

## 3 点简述
- 标准概念瓶颈模型忽略领域特定关系和因果机制，依赖完整概念标签
- PG-CBM通过生物物理意义中间概念约束学习遵循领域定义因果机制
- 以地球观测数据生物量密度估计为例，PG-CBM减少误差和偏差，提升可解释性

## 摘要（原文）

> Concept Bottleneck Models (CBMs) improve the explainability of black-box Deep Learning (DL) by introducing intermediate semantic concepts. However, standard CBMs often overlook domain-specific relationships and causal mechanisms, and their dependence on complete concept labels limits applicability in scientific domains where supervision is sparse but processes are well defined. To address this, we propose the Process-Guided Concept Bottleneck Model (PG-CBM), an extension of CBMs which constrains learning to follow domain-defined causal mechanisms through biophysically meaningful intermediate concepts. Using above ground biomass density estimation from Earth Observation data as a case study, we show that PG-CBM reduces error and bias compared to multiple benchmarks, whilst leveraging multi-source heterogeneous training data and producing interpretable intermediate outputs. Beyond improved accuracy, PG-CBM enhances transparency, enables detection of spurious learning, and provides scientific insights, representing a step toward more trustworthy AI systems in scientific applications.

