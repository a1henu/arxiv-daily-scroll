---
layout: default
title: Metanetworks as Regulatory Operators: Learning to Edit for Requirement Compliance
---

# Metanetworks as Regulatory Operators: Learning to Edit for Requirement Compliance
**arXiv**：[2512.15469v1](https://arxiv.org/abs/2512.15469) · [PDF](https://arxiv.org/pdf/2512.15469.pdf)  
**作者**：Ioannis Kalogeropoulos, Giorgos Bouritsas, Yannis Panagakis  

**一句话要点**：提出图元网络框架，以数据驱动方式编辑神经网络，在满足合规要求的同时保持模型效用。

**关键词**：模型编辑, 图元网络, 合规要求, 数据驱动, 神经网络优化, 公平性

## 3 点简述
- 核心问题：高风险部署中，模型需满足合规、公平等要求，但传统后处理或重训练方法效率低且易牺牲性能。
- 方法要点：训练图元网络作为编辑器，通过单次推理步骤编辑神经网络，平衡要求满足与效用保留。
- 实验或效果：在数据最小化、偏见缓解和权重剪枝任务中，相比后处理或重训练，提升了性能、要求满足和时间效率的权衡。

## 摘要（原文）

> As machine learning models are increasingly deployed in high-stakes settings, e.g. as decision support systems in various societal sectors or in critical infrastructure, designers and auditors are facing the need to ensure that models satisfy a wider variety of requirements (e.g. compliance with regulations, fairness, computational constraints) beyond performance. Although most of them are the subject of ongoing studies, typical approaches face critical challenges: post-processing methods tend to compromise performance, which is often counteracted by fine-tuning or, worse, training from scratch, an often time-consuming or even unavailable strategy. This raises the following question: "Can we efficiently edit models to satisfy requirements, without sacrificing their utility?" In this work, we approach this with a unifying framework, in a data-driven manner, i.e. we learn to edit neural networks (NNs), where the editor is an NN itself - a graph metanetwork - and editing amounts to a single inference step. In particular, the metanetwork is trained on NN populations to minimise an objective consisting of two terms: the requirement to be enforced and the preservation of the NN's utility. We experiment with diverse tasks (the data minimisation principle, bias mitigation and weight pruning) improving the trade-offs between performance, requirement satisfaction and time efficiency compared to popular post-processing or re-training alternatives.

