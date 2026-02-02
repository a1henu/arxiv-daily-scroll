---
layout: default
title: Uncertainty-Aware Extrapolation in Bayesian Oblique Trees
---

# Uncertainty-Aware Extrapolation in Bayesian Oblique Trees
**arXiv**：[2601.22899v1](https://arxiv.org/abs/2601.22899) · [PDF](https://arxiv.org/pdf/2601.22899.pdf)  
**作者**：Viktor Andonovikj, Sašo Džeroski, Pavle Boškoski  

**一句话要点**：提出贝叶斯斜决策树模型，通过GP叶节点解决回归任务中可靠外推和不确定性校准问题。

**关键词**：贝叶斯决策树, 高斯过程回归, 不确定性校准, 外推预测, 变分推理

## 3 点简述
- 决策树在回归任务中面临外推不可靠和不确定性校准不足的问题。
- 模型结合贝叶斯斜分裂和GP叶节点，实现不确定性感知分区和局部函数建模。
- 实验显示在基准回归任务中预测性能提升，外推场景下性能增益显著。

## 摘要（原文）

> Decision trees are widely used due to their interpretability and efficiency, but they struggle in regression tasks that require reliable extrapolation and well-calibrated uncertainty. Piecewise-constant leaf predictions are bounded by the training targets and often become overconfident under distribution shift. We propose a single-tree Bayesian model that extends VSPYCT by equipping each leaf with a GP predictor. Bayesian oblique splits provide uncertainty-aware partitioning of the input space, while GP leaves model local functional behaviour and enable principled extrapolation beyond the observed target range. We present an efficient inference and prediction scheme that combines posterior sampling of split parameters with \gls{gp} posterior predictions, and a gating mechanism that activates GP-based extrapolation when inputs fall outside the training support of a leaf. Experiments on benchmark regression tasks show improvements in the predictive performance compared to standard variational oblique trees, and substantial performance gains in extrapolation scenarios.

