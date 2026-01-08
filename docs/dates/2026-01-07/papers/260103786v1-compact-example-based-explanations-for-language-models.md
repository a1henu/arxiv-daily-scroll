---
layout: default
title: Compact Example-Based Explanations for Language Models
---

# Compact Example-Based Explanations for Language Models
**arXiv**：[2601.03786v1](https://arxiv.org/abs/2601.03786) · [PDF](https://arxiv.org/pdf/2601.03786.pdf)  
**作者**：Loris Schoenegger, Benjamin Roth  

**一句话要点**：提出选择相关性分数以优化语言模型的示例解释选择策略

**关键词**：语言模型解释, 训练数据影响估计, 示例选择策略, 选择相关性分数, 模型可解释性

## 3 点简述
- 核心问题：训练数据影响估计方法生成大量示例，但人类无法处理，需选择子集，而现有研究忽视选择策略对解释质量的影响。
- 方法要点：提出无需重训练的选择相关性分数，量化示例集对模型输出的解释有用性，并通过微调实验验证其预测能力。
- 实验或效果：发现常见选择策略常劣于随机选择，提出平衡影响力和代表性的策略，能更有效利用选择预算。

## 摘要（原文）

> Training data influence estimation methods quantify the contribution of training documents to a model's output, making them a promising source of information for example-based explanations. As humans cannot interpret thousands of documents, only a small subset of the training data can be presented as an explanation. Although the choice of which documents to include directly affects explanation quality, previous evaluations of such systems have largely ignored any selection strategies. To address this, we propose a novel selection relevance score, a retraining-free metric that quantifies how useful a set of examples is for explaining a model's output. We validate this score through fine-tuning experiments, confirming that it can predict whether a set of examples supports or undermines the model's predictions. Using this metric, we further show that common selection strategies often underperform random selection. Motivated by this finding, we propose a strategy that balances influence and representativeness, enabling better use of selection budgets than naively selecting the highest-ranking examples.

