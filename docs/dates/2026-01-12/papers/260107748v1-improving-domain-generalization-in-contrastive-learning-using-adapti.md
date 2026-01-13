---
layout: default
title: Improving Domain Generalization in Contrastive Learning using Adaptive Temperature Control
---

# Improving Domain Generalization in Contrastive Learning using Adaptive Temperature Control
**arXiv**：[2601.07748v1](https://arxiv.org/abs/2601.07748) · [PDF](https://arxiv.org/pdf/2601.07748.pdf)  
**作者**：Robert Lewis, Katie Matton, Rosalind W. Picard, John Guttag  

**一句话要点**：提出自适应温度控制对比学习方法以提升多域训练下的分布外泛化能力

**关键词**：对比学习, 域泛化, 自适应温度控制, 分布外泛化, 自监督预训练

## 3 点简述
- 研究对比学习在训练与测试数据分布偏移时性能下降的问题
- 方法利用域标签调整InfoNCE损失温度，增强表示域不变性
- 在MNIST变体数据集上验证，优于基线并保持域内性能

## 摘要（原文）

> Self-supervised pre-training with contrastive learning is a powerful method for learning from sparsely labeled data. However, performance can drop considerably when there is a shift in the distribution of data from training to test time. We study this phenomenon in a setting in which the training data come from multiple domains, and the test data come from a domain not seen at training that is subject to significant covariate shift. We present a new method for contrastive learning that incorporates domain labels to increase the domain invariance of learned representations, leading to improved out-of-distribution generalization. Our method adjusts the temperature parameter in the InfoNCE loss -- which controls the relative weighting of negative pairs -- using the probability that a negative sample comes from the same domain as the anchor. This upweights pairs from more similar domains, encouraging the model to discriminate samples based on domain-invariant attributes. Through experiments on a variant of the MNIST dataset, we demonstrate that our method yields better out-of-distribution performance than domain generalization baselines. Furthermore, our method maintains strong in-distribution task performance, substantially outperforming baselines on this measure.

