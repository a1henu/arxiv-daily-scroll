---
layout: default
title: Asymptotic Theory of Iterated Empirical Risk Minimization, with Applications to Active Learning
---

# Asymptotic Theory of Iterated Empirical Risk Minimization, with Applications to Active Learning
**arXiv**：[2601.23031v1](https://arxiv.org/abs/2601.23031) · [PDF](https://arxiv.org/pdf/2601.23031.pdf)  
**作者**：Hugo Cui, Yue M. Lu  

**一句话要点**：提出迭代经验风险最小化的渐近理论，应用于主动学习以优化标注预算分配。

**关键词**：迭代经验风险最小化, 渐近理论, 主动学习, 高维统计, 数据选择, 双下降现象

## 3 点简述
- 研究迭代经验风险最小化，其中第一阶段预测作为第二阶段损失函数的输入，引入复杂统计依赖性。
- 针对高斯混合数据上的线性模型，推导高维比例缩放下测试误差的精确渐近表征。
- 应用于主动学习，揭示标注预算分配的权衡，并展示由数据选择驱动的双下降行为。

## 摘要（原文）

> We study a class of iterated empirical risk minimization (ERM) procedures in which two successive ERMs are performed on the same dataset, and the predictions of the first estimator enter as an argument in the loss function of the second. This setting, which arises naturally in active learning and reweighting schemes, introduces intricate statistical dependencies across samples and fundamentally distinguishes the problem from classical single-stage ERM analyses. For linear models trained with a broad class of convex losses on Gaussian mixture data, we derive a sharp asymptotic characterization of the test error in the high-dimensional regime where the sample size and ambient dimension scale proportionally. Our results provide explicit, fully asymptotic predictions for the performance of the second-stage estimator despite the reuse of data and the presence of prediction-dependent losses. We apply this theory to revisit a well-studied pool-based active learning problem, removing oracle and sample-splitting assumptions made in prior work. We uncover a fundamental tradeoff in how the labeling budget should be allocated across stages, and demonstrate a double-descent behavior of the test error driven purely by data selection, rather than model size or sample count.

