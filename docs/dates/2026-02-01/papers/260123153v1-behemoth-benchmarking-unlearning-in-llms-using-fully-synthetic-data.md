---
layout: default
title: Behemoth: Benchmarking Unlearning in LLMs Using Fully Synthetic Data
---

# Behemoth: Benchmarking Unlearning in LLMs Using Fully Synthetic Data
**arXiv**：[2601.23153v1](https://arxiv.org/abs/2601.23153) · [PDF](https://arxiv.org/pdf/2601.23153.pdf)  
**作者**：Eugenia Iofinova, Dan Alistarh  

**一句话要点**：提出Behemoth框架，使用全合成数据基准化大语言模型中的遗忘编辑效果。

**关键词**：模型编辑, 合成数据, 大语言模型, 遗忘基准, 训练数据分布, 权重调整

## 3 点简述
- 核心问题：模型编辑在真实数据上难以评估与理解其与训练数据分布的交互。
- 方法要点：开发全合成数据生成框架，以可控方式研究模型编辑的机制。
- 实验或效果：在表格数据上探索编辑，发现限制更新秩有时能提升编辑效果。

## 摘要（原文）

> As artificial neural networks, and specifically large language models, have improved rapidly in capabilities and quality, they have increasingly been deployed in real-world applications, from customer service to Google search, despite the fact that they frequently make factually incorrect or undesirable statements. This trend has inspired practical and academic interest in model editing, that is, in adjusting the weights of the model to modify its likely outputs for queries relating to a specific fact or set of facts. This may be done either to amend a fact or set of facts, for instance, to fix a frequent error in the training data, or to suppress a fact or set of facts entirely, for instance, in case of dangerous knowledge. Multiple methods have been proposed to do such edits. However, at the same time, it has been shown that such model editing can be brittle and incomplete. Moreover the effectiveness of any model editing method necessarily depends on the data on which the model is trained, and, therefore, a good understanding of the interaction of the training data distribution and the way it is stored in the network is necessary and helpful to reliably perform model editing. However, working with large language models trained on real-world data does not allow us to understand this relationship or fully measure the effects of model editing. We therefore propose Behemoth, a fully synthetic data generation framework. To demonstrate the practical insights from the framework, we explore model editing in the context of simple tabular data, demonstrating surprising findings that, in some cases, echo real-world results, for instance, that in some cases restricting the update rank results in a more effective update. The code is available at https://github.com/IST-DASLab/behemoth.git.

