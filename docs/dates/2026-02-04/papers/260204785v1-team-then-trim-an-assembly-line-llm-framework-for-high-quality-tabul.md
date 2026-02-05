---
layout: default
title: Team, Then Trim: An Assembly-Line LLM Framework for High-Quality Tabular Data Generation
---

# Team, Then Trim: An Assembly-Line LLM Framework for High-Quality Tabular Data Generation
**arXiv**：[2602.04785v1](https://arxiv.org/abs/2602.04785) · [PDF](https://arxiv.org/pdf/2602.04785.pdf)  
**作者**：Congjing Zhang, Ryan Feng Lin, Ruoxuan Bao, Shuai Huang  

**一句话要点**：提出Team-then-Trim框架，通过LLM协作与质量控制生成高质量表格数据以解决数据稀缺问题。

**关键词**：表格数据生成, 大语言模型协作, 数据质量控制, 机器学习应用, 合成数据

## 3 点简述
- 核心问题：表格数据获取成本高，常存在类别不平衡、选择偏差和低保真度等缺陷。
- 方法要点：采用流水线式LLM团队协作生成数据，并集成三阶段插件式质量控制管道。
- 实验或效果：在模拟和真实数据集上优于现有方法，支持下游模型应用。

## 摘要（原文）

> While tabular data is fundamental to many real-world machine learning (ML) applications, acquiring high-quality tabular data is usually labor-intensive and expensive. Limited by the scarcity of observations, tabular datasets often exhibit critical deficiencies, such as class imbalance, selection bias, and low fidelity. To address these challenges, building on recent advances in Large Language Models (LLMs), this paper introduces Team-then-Trim (T$^2$), a framework that synthesizes high-quality tabular data through a collaborative team of LLMs, followed by a rigorous three-stage plug-in data quality control (QC) pipeline. In T$^2$, tabular data generation is conceptualized as a manufacturing process: specialized LLMs, guided by domain knowledge, are tasked with generating different data components sequentially, and the resulting products, i.e., the synthetic data, are systematically evaluated across multiple dimensions of QC. Empirical results on both simulated and real-world datasets demonstrate that T$^2$ outperforms state-of-the-art methods in producing high-quality tabular data, highlighting its potential to support downstream models when direct data collection is practically infeasible.

