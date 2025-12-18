---
layout: default
title: Behavior Tokens Speak Louder: Disentangled Explainable Recommendation with Behavior Vocabulary
---

# Behavior Tokens Speak Louder: Disentangled Explainable Recommendation with Behavior Vocabulary
**arXiv**：[2512.15614v1](https://arxiv.org/abs/2512.15614) · [PDF](https://arxiv.org/pdf/2512.15614.pdf)  
**作者**：Xinshun Feng, Mingzhe Liu, Yi Qiao, Tongyu Zhu, Leilei Sun, Shuai Wang  

**一句话要点**：提出BEAT框架，通过行为词汇表将用户-物品交互转化为可解释序列，以提升零样本推荐性能与解释生成。

**关键词**：可解释推荐, 行为词汇表, 语义对齐, 零样本学习, 语言模型集成

## 3 点简述
- 现有可解释推荐方法依赖ID表示，语义模糊且限制语言模型在开放场景的应用。
- BEAT使用向量量化自编码构建行为词汇表，解耦宏观兴趣与微观意图，并引入语义对齐正则化。
- 在三个公开数据集上，BEAT提升零样本推荐性能，生成连贯解释，行为令牌捕获细粒度语义。

## 摘要（原文）

> Recent advances in explainable recommendations have explored the integration of language models to analyze natural language rationales for user-item interactions. Despite their potential, existing methods often rely on ID-based representations that obscure semantic meaning and impose structural constraints on language models, thereby limiting their applicability in open-ended scenarios. These challenges are intensified by the complex nature of real-world interactions, where diverse user intents are entangled and collaborative signals rarely align with linguistic semantics. To overcome these limitations, we propose BEAT, a unified and transferable framework that tokenizes user and item behaviors into discrete, interpretable sequences. We construct a behavior vocabulary via a vector-quantized autoencoding process that disentangles macro-level interests and micro-level intentions from graph-based representations. We then introduce multi-level semantic supervision to bridge the gap between behavioral signals and language space. A semantic alignment regularization mechanism is designed to embed behavior tokens directly into the input space of frozen language models. Experiments on three public datasets show that BEAT improves zero-shot recommendation performance while generating coherent and informative explanations. Further analysis demonstrates that our behavior tokens capture fine-grained semantics and offer a plug-and-play interface for integrating complex behavior patterns into large language models.

