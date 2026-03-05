---
layout: default
title: TaxonRL: Reinforcement Learning with Intermediate Rewards for Interpretable Fine-Grained Visual Reasoning
---

# TaxonRL: Reinforcement Learning with Intermediate Rewards for Interpretable Fine-Grained Visual Reasoning
**arXiv**：[2603.04380v1](https://arxiv.org/abs/2603.04380) · [PDF](https://arxiv.org/pdf/2603.04380.pdf)  
**作者**：Maximilian von Klinski, Maximilian Schall  

**一句话要点**：提出TaxonRL强化学习方法，通过中间奖励实现可解释的细粒度视觉推理

**关键词**：细粒度视觉推理, 强化学习, 中间奖励, 层级分类, 可解释性, 跨领域泛化

## 3 点简述
- 传统视觉语言模型在区分视觉相似物种时存在困难，TaxonRL将推理过程分解为层级分类预测
- 使用Group Relative Policy Optimization和中间奖励，激励模型在最终分类前显式推理物种、属、科级特征
- 在Birds-to-Words数据集上达到91.7%准确率，超越人类表现，并展示跨领域泛化能力

## 摘要（原文）

> Traditional vision-language models struggle with contrastive fine-grained taxonomic reasoning, particularly when distinguishing between visually similar species within the same genus or family. We introduce TaxonRL, a reinforcement learning approach using Group Relative Policy Optimization with intermediate rewards that decomposes the reasoning process into hierarchical taxonomic predictions. Our method incentivizes models to explicitly reason about species-level, genus-level, and family-level features before making final classifications. This structured approach is designed not only to boost accuracy but also to yield a transparent, verifiable decision-making process. On the challenging Birds-to-Words dataset, TaxonRL achieves 91.7\% average accuracy, exceeding human performance (77.3\%) while generating interpretable reasoning traces. We demonstrate strong cross-domain generalization, showing substantial gains in primate and marine species verification. Our results establish that enforcing structured, hierarchical reasoning provides a powerful and transferable framework for fine-grained visual discrimination.

