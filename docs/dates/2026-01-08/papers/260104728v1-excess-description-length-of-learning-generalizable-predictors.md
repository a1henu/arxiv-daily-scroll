---
layout: default
title: Excess Description Length of Learning Generalizable Predictors
---

# Excess Description Length of Learning Generalizable Predictors
**arXiv**：[2601.04728v1](https://arxiv.org/abs/2601.04728) · [PDF](https://arxiv.org/pdf/2601.04728.pdf)  
**作者**：Elizabeth Donoway, Hailey Joren, Fabien Roger, Jan Leike  

**一句话要点**：提出超额描述长度框架，量化微调中从训练数据提取预测结构的信息量。

**关键词**：信息论框架, 微调量化, 泛化分析, 预序编码, 语言模型评估

## 3 点简述
- 核心问题：微调是激发潜在能力还是教授新能力，对语言模型评估与安全至关重要。
- 方法要点：基于信息论，通过预序编码定义超额描述长度，衡量在线训练与最终模型的编码成本差距。
- 实验或效果：通过玩具模型澄清学习中的信息混淆，如随机标签的超额描述长度接近零，提供泛化增益的界限。

## 摘要（原文）

> Understanding whether fine-tuning elicits latent capabilities or teaches new ones is a fundamental question for language model evaluation and safety. We develop a formal information-theoretic framework for quantifying how much predictive structure fine-tuning extracts from the train dataset and writes into a model's parameters. Our central quantity, Excess Description Length (EDL), is defined via prequential coding and measures the gap between the bits required to encode training labels sequentially using an evolving model (trained online) and the residual encoding cost under the final trained model. We establish that EDL is non-negative in expectation, converges to surplus description length in the infinite-data limit, and provides bounds on expected generalization gain. Through a series of toy models, we clarify common confusions about information in learning: why random labels yield EDL near zero, how a single example can eliminate many bits of uncertainty about the underlying rule(s) that describe the data distribution, why structure learned on rare inputs contributes proportionally little to expected generalization, and how format learning creates early transients distinct from capability acquisition. This framework provides rigorous foundations for the empirical observation that capability elicitation and teaching exhibit qualitatively distinct scaling signatures.

