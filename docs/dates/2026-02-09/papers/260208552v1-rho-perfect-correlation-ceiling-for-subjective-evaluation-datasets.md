---
layout: default
title: Rho-Perfect: Correlation Ceiling For Subjective Evaluation Datasets
---

# Rho-Perfect: Correlation Ceiling For Subjective Evaluation Datasets
**arXiv**：[2602.08552v1](https://arxiv.org/abs/2602.08552) · [PDF](https://arxiv.org/pdf/2602.08552.pdf)  
**作者**：Fredrik Cumlin  

**一句话要点**：提出ρ-Perfect以估计主观评价数据集上模型可达到的最高相关性，量化数据可靠性问题。

**关键词**：主观评价, 相关性估计, 数据可靠性, 异方差噪声, 语音质量评估

## 3 点简述
- 核心问题：主观评分存在固有噪声，限制模型与人类相关性，但可靠性问题很少被量化。
- 方法要点：定义ρ-Perfect为完美预测器与人类评分的相关性，基于异方差噪声场景推导估计值。
- 实验或效果：在语音质量数据集上演示ρ-Perfect，区分模型限制与数据质量问题。

## 摘要（原文）

> Subjective ratings contain inherent noise that limits the model-human correlation, but this reliability issue is rarely quantified. In this paper, we present $ρ$-Perfect, a practical estimation of the highest achievable correlation of a model on subjectively rated datasets. We define $ρ$-Perfect to be the correlation between a perfect predictor and human ratings, and derive an estimate of the value based on heteroscedastic noise scenarios, a common occurrence in subjectively rated datasets. We show that $ρ$-Perfect squared estimates test-retest correlation and use this to validate the estimate. We demonstrate the use of $ρ$-Perfect on a speech quality dataset and show how the measure can distinguish between model limitations and data quality issues.

