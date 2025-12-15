---
layout: default
title: Conditional Coverage Diagnostics for Conformal Prediction
---

# Conditional Coverage Diagnostics for Conformal Prediction
**arXiv**：[2512.11779v1](https://arxiv.org/abs/2512.11779) · [PDF](https://arxiv.org/pdf/2512.11779.pdf)  
**作者**：Sacha Braun, David Holzmüller, Michael I. Jordan, Francis Bach  

**一句话要点**：提出ERT指标以解决共形预测中条件覆盖评估的样本低效和过拟合问题。

**关键词**：共形预测, 条件覆盖, 分类问题, 风险差, 统计评估, 开源工具

## 3 点简述
- 核心问题：共形预测方法无法保证条件覆盖，现有评估指标存在样本低效和过拟合。
- 方法要点：将条件覆盖估计转化为分类问题，通过风险差计算保守估计的ERT指标。
- 实验或效果：使用现代分类器提高统计功效，并用于基准测试不同共形预测方法。

## 摘要（原文）

> Evaluating conditional coverage remains one of the most persistent challenges in assessing the reliability of predictive systems. Although conformal methods can give guarantees on marginal coverage, no method can guarantee to produce sets with correct conditional coverage, leaving practitioners without a clear way to interpret local deviations. To overcome sample-inefficiency and overfitting issues of existing metrics, we cast conditional coverage estimation as a classification problem. Conditional coverage is violated if and only if any classifier can achieve lower risk than the target coverage. Through the choice of a (proper) loss function, the resulting risk difference gives a conservative estimate of natural miscoverage measures such as L1 and L2 distance, and can even separate the effects of over- and under-coverage, and non-constant target coverages. We call the resulting family of metrics excess risk of the target coverage (ERT). We show experimentally that the use of modern classifiers provides much higher statistical power than simple classifiers underlying established metrics like CovGap. Additionally, we use our metric to benchmark different conformal prediction methods. Finally, we release an open-source package for ERT as well as previous conditional coverage metrics. Together, these contributions provide a new lens for understanding, diagnosing, and improving the conditional reliability of predictive systems.

