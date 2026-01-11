---
layout: default
title: CAOS: Conformal Aggregation of One-Shot Predictors
---

# CAOS: Conformal Aggregation of One-Shot Predictors
**arXiv**：[2601.05219v1](https://arxiv.org/abs/2601.05219) · [PDF](https://arxiv.org/pdf/2601.05219.pdf)  
**作者**：Maja Waldron  

**一句话要点**：提出CAOS框架以解决单样本预测中不确定性量化效率低的问题

**关键词**：共形预测, 单样本学习, 不确定性量化, 预测集, 自适应聚合, 留一校准

## 3 点简述
- 单样本预测缺乏不确定性量化，标准共形预测方法因数据分割和单一预测器而效率低下
- CAOS通过自适应聚合多个单样本预测器并采用留一校准方案，充分利用稀缺标注数据
- 实验表明CAOS在保持可靠覆盖的同时，预测集大小显著小于基线方法

## 摘要（原文）

> One-shot prediction enables rapid adaptation of pretrained foundation models to new tasks using only one labeled example, but lacks principled uncertainty quantification. While conformal prediction provides finite-sample coverage guarantees, standard split conformal methods are inefficient in the one-shot setting due to data splitting and reliance on a single predictor. We propose Conformal Aggregation of One-Shot Predictors (CAOS), a conformal framework that adaptively aggregates multiple one-shot predictors and uses a leave-one-out calibration scheme to fully exploit scarce labeled data. Despite violating classical exchangeability assumptions, we prove that CAOS achieves valid marginal coverage using a monotonicity-based argument. Experiments on one-shot facial landmarking and RAFT text classification tasks show that CAOS produces substantially smaller prediction sets than split conformal baselines while maintaining reliable coverage.

