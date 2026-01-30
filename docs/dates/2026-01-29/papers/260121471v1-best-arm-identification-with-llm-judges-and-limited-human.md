---
layout: default
title: Best Arm Identification with LLM Judges and Limited Human
---

# Best Arm Identification with LLM Judges and Limited Human
**arXiv**：[2601.21471v1](https://arxiv.org/abs/2601.21471) · [PDF](https://arxiv.org/pdf/2601.21471.pdf)  
**作者**：Ruicheng Ao, Hongyu Chen, Siyang Gao, Hanwei Li, David Simchi-Levi  

**一句话要点**：提出基于LLM代理和选择性审计的算法，以解决带偏置代理的最佳臂识别问题。

**关键词**：最佳臂识别, 多保真度学习, LLM代理, 选择性审计, 置信序列, 逆概率加权

## 3 点简述
- 研究带偏置代理（如LLM）和选择性地面真值审计的最佳臂识别问题。
- 开发结合代理分数和逆概率加权残差的估计器及置信序列。
- 算法自适应审计不可靠上下文和接近臂，实验验证其高效性和理论保证。

## 摘要（原文）

> We study fixed-confidence best-arm identification (BAI) where a cheap but potentially biased proxy (e.g., LLM judge) is available for every sample, while an expensive ground-truth label can only be acquired selectively when using a human for auditing. Unlike classical multi-fidelity BAI, the proxy is biased (arm- and context-dependent) and ground truth is selectively observed. Consequently, standard multi-fidelity methods can mis-select the best arm, and uniform auditing, though accurate, wastes scarce resources and is inefficient. We prove that without bias correction and propensity adjustment, mis-selection probability may not vanish (even with unlimited proxy data). We then develop an estimator for the mean of each arm that combines proxy scores with inverse-propensity-weighted residuals and form anytime-valid confidence sequences for that estimator. Based on the estimator and confidence sequence, we propose an algorithm that adaptively selects and audits arms. The algorithm concentrates audits on unreliable contexts and close arms and we prove that a plug-in Neyman rule achieves near-oracle audit efficiency. Numerical experiments confirm the theoretical guarantees and demonstrate the superior empirical performance of the proposed algorithm.

