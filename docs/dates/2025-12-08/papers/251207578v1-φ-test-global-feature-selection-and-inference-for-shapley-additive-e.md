---
layout: default
title: $φ$-test: Global Feature Selection and Inference for Shapley Additive Explanations
---

# $φ$-test: Global Feature Selection and Inference for Shapley Additive Explanations
**arXiv**：[2512.07578v1](https://arxiv.org/abs/2512.07578) · [PDF](https://arxiv.org/pdf/2512.07578.pdf)  
**作者**：Dongseok Kim, Hyoungsun Choi, Mohamed Jismy Aashik Rasool, Gisung Oh  

**一句话要点**：提出φ-test，结合Shapley归因与选择性推断，用于黑盒预测器的全局特征选择与显著性检验。

**关键词**：Shapley归因, 选择性推断, 全局特征选择, 黑盒解释, 显著性检验, 代理模型

## 3 点简述
- 核心问题：黑盒预测器中全局特征选择与显著性推断缺乏统计保证，难以稳定解释。
- 方法要点：基于SHAP引导筛选特征，通过选择性推断拟合线性代理模型，输出p值和置信区间。
- 实验或效果：在表格回归任务中，使用少量特征保持预测能力，特征集在重采样和模型间较稳定。

## 摘要（原文）

> We propose $φ$-test, a global feature-selection and significance procedure for black-box predictors that combines Shapley attributions with selective inference. Given a trained model and an evaluation dataset, $φ$-test performs SHAP-guided screening and fits a linear surrogate on the screened features via a selection rule with a tractable selective-inference form. For each retained feature, it outputs a Shapley-based global score, a surrogate coefficient, and post-selection $p$-values and confidence intervals in a global feature-importance table. Experiments on real tabular regression tasks with tree-based and neural backbones suggest that $φ$-test can retain much of the predictive ability of the original model while using only a few features and producing feature sets that remain fairly stable across resamples and backbone classes. In these settings, $φ$-test acts as a practical global explanation layer linking Shapley-based importance summaries with classical statistical inference.

