---
layout: default
title: Robust Domain Generalization under Divergent Marginal and Conditional Distributions
---

# Robust Domain Generalization under Divergent Marginal and Conditional Distributions
**arXiv**：[2602.02015v1](https://arxiv.org/abs/2602.02015) · [PDF](https://arxiv.org/pdf/2602.02015.pdf)  
**作者**：Jewon Yeom, Kyubyung Chae, Hyunggyu Lim, Yoonna Oh, Dongyoon Yang, Taesup Kim  

**一句话要点**：提出统一框架以解决域泛化中边际与条件分布同时偏移的鲁棒性问题

**关键词**：域泛化, 分布偏移, 风险界, 元学习, 长尾识别, 鲁棒学习

## 3 点简述
- 核心问题：现实多域场景常涉及边际标签分布和条件分布同时偏移，现有方法主要假设条件分布偏移而忽略边际分布变化。
- 方法要点：通过分解联合分布并推导新风险界，设计元学习过程最小化风险界，确保对未见域的强泛化能力。
- 实验或效果：在传统域泛化基准和具有显著边际与条件偏移的多域长尾识别设置中实现最先进性能。

## 摘要（原文）

> Domain generalization (DG) aims to learn predictive models that can generalize to unseen domains. Most existing DG approaches focus on learning domain-invariant representations under the assumption of conditional distribution shift (i.e., primarily addressing changes in $P(X\mid Y)$ while assuming $P(Y)$ remains stable). However, real-world scenarios with multiple domains often involve compound distribution shifts where both the marginal label distribution $P(Y)$ and the conditional distribution $P(X\mid Y)$ vary simultaneously. To address this, we propose a unified framework for robust domain generalization under divergent marginal and conditional distributions. We derive a novel risk bound for unseen domains by explicitly decomposing the joint distribution into marginal and conditional components and characterizing risk gaps arising from both sources of divergence. To operationalize this bound, we design a meta-learning procedure that minimizes and validates the proposed risk bound across seen domains, ensuring strong generalization to unseen ones. Empirical evaluations demonstrate that our method achieves state-of-the-art performance not only on conventional DG benchmarks but also in challenging multi-domain long-tailed recognition settings where both marginal and conditional shifts are pronounced.

