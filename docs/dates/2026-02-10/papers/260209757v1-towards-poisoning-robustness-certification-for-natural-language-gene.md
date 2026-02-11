---
layout: default
title: Towards Poisoning Robustness Certification for Natural Language Generation
---

# Towards Poisoning Robustness Certification for Natural Language Generation
**arXiv**：[2602.09757v1](https://arxiv.org/abs/2602.09757) · [PDF](https://arxiv.org/pdf/2602.09757.pdf)  
**作者**：Mihnea Ghitu, Matthew Wicker  

**一句话要点**：提出Targeted Partition Aggregation算法，为自然语言生成提供可证明的投毒鲁棒性认证框架。

**关键词**：自然语言生成, 投毒鲁棒性认证, Targeted Partition Aggregation, 混合整数线性规划, 安全属性

## 3 点简述
- 核心问题：现有认证防御无法处理自回归生成的序列预测和指数级输出空间。
- 方法要点：形式化稳定性和有效性安全属性，引入TPA算法计算最小投毒预算以认证目标攻击。
- 实验或效果：在代理工具调用和偏好对齐等场景中实证TPA的有效性，但推理延迟未知。

## 摘要（原文）

> Understanding the reliability of natural language generation is critical for deploying foundation models in security-sensitive domains. While certified poisoning defenses provide provable robustness bounds for classification tasks, they are fundamentally ill-equipped for autoregressive generation: they cannot handle sequential predictions or the exponentially large output space of language models. To establish a framework for certified natural language generation, we formalize two security properties: stability (robustness to any change in generation) and validity (robustness to targeted, harmful changes in generation). We introduce Targeted Partition Aggregation (TPA), the first algorithm to certify validity/targeted attacks by computing the minimum poisoning budget needed to induce a specific harmful class, token, or phrase. Further, we extend TPA to provide tighter guarantees for multi-turn generations using mixed integer linear programming (MILP). Empirically, we demonstrate TPA's effectiveness across diverse settings including: certifying validity of agent tool-calling when adversaries modify up to 0.5% of the dataset and certifying 8-token stability horizons in preference-based alignment. Though inference-time latency remains an open challenge, our contributions enable certified deployment of language models in security-critical applications.

