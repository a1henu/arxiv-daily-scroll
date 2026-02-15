---
layout: default
title: Protein Circuit Tracing via Cross-layer Transcoders
---

# Protein Circuit Tracing via Cross-layer Transcoders
**arXiv**：[2602.12026v1](https://arxiv.org/abs/2602.12026) · [PDF](https://arxiv.org/pdf/2602.12026.pdf)  
**作者**：Darin Tsui, Kunal Talreja, Daniel Saeedi, Amirali Aghazadeh  

**一句话要点**：提出ProtoMech框架，通过跨层转码器解决蛋白质语言模型计算电路理解不足的问题。

**关键词**：蛋白质语言模型, 计算电路追踪, 跨层转码器, 蛋白质设计, 稀疏表示

## 3 点简述
- 核心问题：蛋白质语言模型预测背后的计算电路难以理解，现有方法因独立处理各层而无法捕捉跨层计算。
- 方法要点：引入跨层转码器，学习稀疏潜在表示以联合捕获模型全计算电路。
- 实验或效果：在ESM2上恢复82-89%性能，识别压缩电路保留79%准确度，并用于蛋白质设计超越基线方法。

## 摘要（原文）

> Protein language models (pLMs) have emerged as powerful predictors of protein structure and function. However, the computational circuits underlying their predictions remain poorly understood. Recent mechanistic interpretability methods decompose pLM representations into interpretable features, but they treat each layer independently and thus fail to capture cross-layer computation, limiting their ability to approximate the full model. We introduce ProtoMech, a framework for discovering computational circuits in pLMs using cross-layer transcoders that learn sparse latent representations jointly across layers to capture the model's full computational circuitry. Applied to the pLM ESM2, ProtoMech recovers 82-89% of the original performance on protein family classification and function prediction tasks. ProtoMech then identifies compressed circuits that use <1% of the latent space while retaining up to 79% of model accuracy, revealing correspondence with structural and functional motifs, including binding, signaling, and stability. Steering along these circuits enables high-fitness protein design, surpassing baseline methods in more than 70% of cases. These results establish ProtoMech as a principled framework for protein circuit tracing.

