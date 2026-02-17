---
layout: default
title: Coverage Guarantees for Pseudo-Calibrated Conformal Prediction under Distribution Shift
---

# Coverage Guarantees for Pseudo-Calibrated Conformal Prediction under Distribution Shift
**arXiv**：[2602.14913v1](https://arxiv.org/abs/2602.14913) · [PDF](https://arxiv.org/pdf/2602.14913.pdf)  
**作者**：Farbod Siahkali, Ashwin Verma, Vijay Gupta  

**一句话要点**：提出伪校准方法以在分布偏移下保持保形预测的目标覆盖率

**关键词**：保形预测, 分布偏移, 伪校准, 覆盖率保证, 域适应, Wasserstein距离

## 3 点简述
- 核心问题：保形预测在数据分布偏移时覆盖率保证失效
- 方法要点：基于有界标签条件协变量偏移模型，推导目标覆盖率下界并设计伪校准集
- 实验或效果：数值实验显示方法能缓解覆盖率下降并保持预测集大小

## 摘要（原文）

> Conformal prediction (CP) offers distribution-free marginal coverage guarantees under an exchangeability assumption, but these guarantees can fail if the data distribution shifts. We analyze the use of pseudo-calibration as a tool to counter this performance loss under a bounded label-conditional covariate shift model. Using tools from domain adaptation, we derive a lower bound on target coverage in terms of the source-domain loss of the classifier and a Wasserstein measure of the shift. Using this result, we provide a method to design pseudo-calibrated sets that inflate the conformal threshold by a slack parameter to keep target coverage above a prescribed level. Finally, we propose a source-tuned pseudo-calibration algorithm that interpolates between hard pseudo-labels and randomized labels as a function of classifier uncertainty. Numerical experiments show that our bounds qualitatively track pseudo-calibration behavior and that the source-tuned scheme mitigates coverage degradation under distribution shift while maintaining nontrivial prediction set sizes.

