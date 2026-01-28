---
layout: default
title: Regularized $f$-Divergence Kernel Tests
---

# Regularized $f$-Divergence Kernel Tests
**arXiv**：[2601.19755v1](https://arxiv.org/abs/2601.19755) · [PDF](https://arxiv.org/pdf/2601.19755.pdf)  
**作者**：Mónica Ribero, Antonin Schrab, Arthur Gretton  

**一句话要点**：提出正则化f-散度核检验框架，用于两样本测试和机器去学习评估。

**关键词**：f-散度检验, 核方法, 两样本测试, 机器去学习, Hockey-Stick散度, 正则化变分表示

## 3 点简述
- 核心问题：基于f-散度构建实用的核方法两样本检验，适应超参数如核带宽和正则化参数。
- 方法要点：利用散度的正则化变分表示，通过核方法估计见证函数计算检验统计量。
- 实验或效果：实验显示不同f-散度对局部差异敏感，并针对机器去学习提出相对检验区分失败与安全变化。

## 摘要（原文）

> We propose a framework to construct practical kernel-based two-sample tests from the family of $f$-divergences. The test statistic is computed from the witness function of a regularized variational representation of the divergence, which we estimate using kernel methods. The proposed test is adaptive over hyperparameters such as the kernel bandwidth and the regularization parameter. We provide theoretical guarantees for statistical test power across our family of $f$-divergence estimates. While our test covers a variety of $f$-divergences, we bring particular focus to the Hockey-Stick divergence, motivated by its applications to differential privacy auditing and machine unlearning evaluation. For two-sample testing, experiments demonstrate that different $f$-divergences are sensitive to different localized differences, illustrating the importance of leveraging diverse statistics. For machine unlearning, we propose a relative test that distinguishes true unlearning failures from safe distributional variations.

