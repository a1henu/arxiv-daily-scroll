---
layout: default
title: Tabular Foundation Models Can Learn Association Rules
---

# Tabular Foundation Models Can Learn Association Rules
**arXiv**：[2602.14622v1](https://arxiv.org/abs/2602.14622) · [PDF](https://arxiv.org/pdf/2602.14622.pdf)  
**作者**：Erkan Karabulut, Daniel Daza, Paul Groth, Martijn C. Schut, Victoria Degeler  

**一句话要点**：提出TabProbe框架，利用表格基础模型学习关联规则，解决传统方法规则爆炸与低数据性能差问题。

**关键词**：关联规则挖掘, 表格基础模型, 条件概率估计, 模型无关框架, 低数据稳健性

## 3 点简述
- 核心问题：传统关联规则挖掘方法存在规则爆炸和可扩展性差，神经方法在低数据下性能下降。
- 方法要点：引入模型无关框架，利用表格基础模型作为条件概率估计器，无需频繁项集挖掘。
- 实验或效果：在多种数据集上评估，表格基础模型能生成简洁高质量规则，在低数据下保持稳健。

## 摘要（原文）

> Association Rule Mining (ARM) is a fundamental task for knowledge discovery in tabular data and is widely used in high-stakes decision-making. Classical ARM methods rely on frequent itemset mining, leading to rule explosion and poor scalability, while recent neural approaches mitigate these issues but suffer from degraded performance in low-data regimes. Tabular foundation models (TFMs), pretrained on diverse tabular data with strong in-context generalization, provide a basis for addressing these limitations. We introduce a model-agnostic association rule learning framework that extracts association rules from any conditional probabilistic model over tabular data, enabling us to leverage TFMs. We then introduce TabProbe, an instantiation of our framework that utilizes TFMs as conditional probability estimators to learn association rules out-of-the-box without frequent itemset mining. We evaluate our approach on tabular datasets of varying sizes based on standard ARM rule quality metrics and downstream classification performance. The results show that TFMs consistently produce concise, high-quality association rules with strong predictive performance and remain robust in low-data settings without task-specific training. Source code is available at https://github.com/DiTEC-project/tabprobe.

