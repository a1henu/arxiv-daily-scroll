---
layout: default
title: A Large-Scale Dataset for Molecular Structure-Language Description via a Rule-Regularized Method
---

# A Large-Scale Dataset for Molecular Structure-Language Description via a Rule-Regularized Method
**arXiv**：[2602.02320v1](https://arxiv.org/abs/2602.02320) · [PDF](https://arxiv.org/pdf/2602.02320.pdf)  
**作者**：Feiyang Cai, Guijuan He, Yi Hu, Jingjing Wang, Joshua Luo, Tianyu Zhu, Srikanth Pilla, Gang Li, Ling Liu, Feng Luo  

**一句话要点**：提出基于规则正则化的自动化框架，构建大规模分子结构-语言描述数据集以支持分子-语言对齐。

**关键词**：分子结构描述, 自动化标注, 大语言模型, 化学命名解析, 数据集构建, 分子-语言对齐

## 3 点简述
- 核心问题：人工标注成本高，难以构建大规模高质量分子结构-语言描述数据集。
- 方法要点：扩展基于规则的化学命名解析器，从IUPAC名称生成结构化XML元数据，指导大语言模型生成精确描述。
- 实验或效果：构建约163k对数据集，验证子集显示描述精度达98.6%，为下游化学任务提供可靠基础。

## 摘要（原文）

> Molecular function is largely determined by structure. Accurately aligning molecular structure with natural language is therefore essential for enabling large language models (LLMs) to reason about downstream chemical tasks. However, the substantial cost of human annotation makes it infeasible to construct large-scale, high-quality datasets of structure-grounded descriptions. In this work, we propose a fully automated annotation framework for generating precise molecular structure descriptions at scale. Our approach builds upon and extends a rule-based chemical nomenclature parser to interpret IUPAC names and construct enriched, structured XML metadata that explicitly encodes molecular structure. This metadata is then used to guide LLMs in producing accurate natural-language descriptions. Using this framework, we curate a large-scale dataset of approximately $163$k molecule-description pairs. A rigorous validation protocol combining LLM-based and expert human evaluation on a subset of $2,000$ molecules demonstrates a high description precision of $98.6\%$. The resulting dataset provides a reliable foundation for future molecule-language alignment, and the proposed annotation method is readily extensible to larger datasets and broader chemical tasks that rely on structural descriptions.

