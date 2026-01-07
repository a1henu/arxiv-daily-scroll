---
layout: default
title: Fast Conformal Prediction using Conditional Interquantile Intervals
---

# Fast Conformal Prediction using Conditional Interquantile Intervals
**arXiv**：[2601.02769v1](https://arxiv.org/abs/2601.02769) · [PDF](https://arxiv.org/pdf/2601.02769.pdf)  
**作者**：Naixin Guo, Rui Luo, Zhixin Zhou  

**一句话要点**：提出CIR和CIR+方法，通过条件分位数区间高效构建最小化预测区间，保证覆盖率和计算效率。

**关键词**：保形预测, 条件分位数回归, 预测区间构建, 计算效率优化, 分布估计

## 3 点简述
- 核心问题：现有分布性保形预测方法在处理偏斜分布时效果有限，且计算效率低。
- 方法要点：CIR利用黑盒模型估计分位数区间，转换为紧凑预测区间；CIR+引入宽度选择规则进一步优化。
- 实验或效果：在合成和真实数据集上验证，平衡预测准确性和计算效率，优于现有方法。

## 摘要（原文）

> We introduce Conformal Interquantile Regression (CIR), a conformal regression method that efficiently constructs near-minimal prediction intervals with guaranteed coverage. CIR leverages black-box machine learning models to estimate outcome distributions through interquantile ranges, transforming these estimates into compact prediction intervals while achieving approximate conditional coverage. We further propose CIR+ (Conditional Interquantile Regression with More Comparison), which enhances CIR by incorporating a width-based selection rule for interquantile intervals. This refinement yields narrower prediction intervals while maintaining comparable coverage, though at the cost of slightly increased computational time. Both methods address key limitations of existing distributional conformal prediction approaches: they handle skewed distributions more effectively than Conformalized Quantile Regression, and they achieve substantially higher computational efficiency than Conformal Histogram Regression by eliminating the need for histogram construction. Extensive experiments on synthetic and real-world datasets demonstrate that our methods optimally balance predictive accuracy and computational efficiency compared to existing approaches.

