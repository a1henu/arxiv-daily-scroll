---
layout: default
title: SynCABEL: Synthetic Contextualized Augmentation for Biomedical Entity Linking
---

# SynCABEL: Synthetic Contextualized Augmentation for Biomedical Entity Linking
**arXiv**：[2601.19667v1](https://arxiv.org/abs/2601.19667) · [PDF](https://arxiv.org/pdf/2601.19667.pdf)  
**作者**：Adam Remaki, Christel Gérardin, Eulàlia Farré-Maduell, Martin Krallinger, Xavier Tannier  

**一句话要点**：提出SynCABEL框架，利用大语言模型生成合成训练数据，解决生物医学实体链接中标注数据稀缺问题。

**关键词**：生物医学实体链接, 合成数据生成, 大语言模型, 多语言基准, 数据效率, 临床有效性评估

## 3 点简述
- 核心问题：生物医学实体链接中专家标注训练数据稀缺，是监督学习的主要瓶颈。
- 方法要点：基于大语言模型为目标知识库中所有候选概念生成上下文丰富的合成训练示例，无需人工标注。
- 实验或效果：在三个多语言基准测试中达到新SOTA，数据效率提升，减少对专家标注的依赖。

## 摘要（原文）

> We present SynCABEL (Synthetic Contextualized Augmentation for Biomedical Entity Linking), a framework that addresses a central bottleneck in supervised biomedical entity linking (BEL): the scarcity of expert-annotated training data. SynCABEL leverages large language models to generate context-rich synthetic training examples for all candidate concepts in a target knowledge base, providing broad supervision without manual annotation. We demonstrate that SynCABEL, when combined with decoder-only models and guided inference establish new state-of-the-art results across three widely used multilingual benchmarks: MedMentions for English, QUAERO for French, and SPACCC for Spanish. Evaluating data efficiency, we show that SynCABEL reaches the performance of full human supervision using up to 60% less annotated data, substantially reducing reliance on labor-intensive and costly expert labeling. Finally, acknowledging that standard evaluation based on exact code matching often underestimates clinically valid predictions due to ontology redundancy, we introduce an LLM-as-a-judge protocol. This analysis reveals that SynCABEL significantly improves the rate of clinically valid predictions. Our synthetic datasets, models, and code are released to support reproducibility and future research.

