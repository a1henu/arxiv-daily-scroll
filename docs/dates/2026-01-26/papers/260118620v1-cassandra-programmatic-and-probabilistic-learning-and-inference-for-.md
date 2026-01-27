---
layout: default
title: CASSANDRA: Programmatic and Probabilistic Learning and Inference for Stochastic World Modeling
---

# CASSANDRA: Programmatic and Probabilistic Learning and Inference for Stochastic World Modeling
**arXiv**：[2601.18620v1](https://arxiv.org/abs/2601.18620) · [PDF](https://arxiv.org/pdf/2601.18620.pdf)  
**作者**：Panagiotis Lymperopoulos, Abhiramon Rajasekharan, Ian Berlot-Attwell, Stéphane Aroca-Ouellette, Kaheer Suleman  

**一句话要点**：提出CASSANDRA神经符号世界建模方法，利用LLM先验知识构建轻量转换模型以提升商业规划性能。

**关键词**：神经符号建模, 世界建模, 概率图模型, LLM引导学习, 商业规划, 转换预测

## 3 点简述
- 核心问题：在商业等现实领域，从有限数据建模复杂动作效果和因果关系以支持规划。
- 方法要点：结合LLM合成代码建模确定性特征，并引导概率图模型结构学习捕捉随机变量因果关系。
- 实验或效果：在咖啡店和主题公园模拟器中，相比基线显著提升转换预测和规划效果。

## 摘要（原文）

> Building world models is essential for planning in real-world domains such as businesses. Since such domains have rich semantics, we can leverage world knowledge to effectively model complex action effects and causal relationships from limited data. In this work, we propose CASSANDRA, a neurosymbolic world modeling approach that leverages an LLM as a knowledge prior to construct lightweight transition models for planning. CASSANDRA integrates two components: (1) LLM-synthesized code to model deterministic features, and (2) LLM-guided structure learning of a probabilistic graphical model to capture causal relationships among stochastic variables. We evaluate CASSANDRA in (i) a small-scale coffee-shop simulator and (ii) a complex theme park business simulator, where we demonstrate significant improvements in transition prediction and planning over baselines.

