---
layout: default
title: Quantifying Epistemic Predictive Uncertainty in Conformal Prediction
---

# Quantifying Epistemic Predictive Uncertainty in Conformal Prediction
**arXiv**：[2602.01667v1](https://arxiv.org/abs/2602.01667) · [PDF](https://arxiv.org/pdf/2602.01667.pdf)  
**作者**：Siu Lun Chau, Soroush H. Zargarbashi, Yusuf Sale, Michele Caprio  

**一句话要点**：提出基于最大平均不精确度的不确定性度量，以量化共形预测中的认知预测不确定性。

**关键词**：共形预测, 认知不确定性, 置信集, 不确定性量化, 主动学习, 选择性分类

## 3 点简述
- 研究共形预测中认知预测不确定性的量化问题，即因存在多个合理预测模型而产生的不确定性。
- 证明共形预测区域与诱导的置信集分布概率至少为1-α的标签集一致，并基于最大平均不精确度提出高效不确定性度量。
- 实验表明，该度量在主动学习和选择性分类中提供比仅依赖预测区域大小更精细的不确定性评估。

## 摘要（原文）

> We study the problem of quantifying epistemic predictive uncertainty (EPU) -- that is, uncertainty faced at prediction time due to the existence of multiple plausible predictive models -- within the framework of conformal prediction (CP). To expose the implicit model multiplicity underlying CP, we build on recent results showing that, under a mild assumption, any full CP procedure induces a set of closed and convex predictive distributions, commonly referred to as a credal set. Importantly, the conformal prediction region (CPR) coincides exactly with the set of labels to which all distributions in the induced credal set assign probability at least $1-α$. As our first contribution, we prove that this characterisation also holds in split CP. Building on this connection, we then propose a computationally efficient and analytically tractable uncertainty measure, based on \emph{Maximum Mean Imprecision}, to quantify the EPU by measuring the degree of conflicting information within the induced credal set. Experiments on active learning and selective classification demonstrate that the quantified EPU provides substantially more informative and fine-grained uncertainty assessments than reliance on CPR size alone. More broadly, this work highlights the potential of CP serving as a principled basis for decision-making under epistemic uncertainty.

