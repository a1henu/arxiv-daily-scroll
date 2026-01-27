---
layout: default
title: Enhancing Control Policy Smoothness by Aligning Actions with Predictions from Preceding States
---

# Enhancing Control Policy Smoothness by Aligning Actions with Predictions from Preceding States
**arXiv**：[2601.18479v1](https://arxiv.org/abs/2601.18479) · [PDF](https://arxiv.org/pdf/2601.18479.pdf)  
**作者**：Kyoleen Kwak, Hyoseok Hwang  

**一句话要点**：提出ASAP方法以解决深度强化学习中动作振荡问题，提升控制策略平滑性。

**关键词**：深度强化学习, 动作平滑, 控制策略, 转移诱导相似状态, 高频振荡抑制

## 3 点简述
- 核心问题：深度强化学习在控制任务中产生高频动作振荡，限制实际应用。
- 方法要点：基于转移诱导相似状态定义，通过动作对齐和二阶差分惩罚来平滑动作。
- 实验或效果：在Gymnasium和Isaac-Lab环境中验证，ASAP能有效减少振荡并提升策略性能。

## 摘要（原文）

> Deep reinforcement learning has proven to be a powerful approach to solving control tasks, but its characteristic high-frequency oscillations make it difficult to apply in real-world environments. While prior methods have addressed action oscillations via architectural or loss-based methods, the latter typically depend on heuristic or synthetic definitions of state similarity to promote action consistency, which often fail to accurately reflect the underlying system dynamics. In this paper, we propose a novel loss-based method by introducing a transition-induced similar state. The transition-induced similar state is defined as the distribution of next states transitioned from the previous state. Since it utilizes only environmental feedback and actually collected data, it better captures system dynamics. Building upon this foundation, we introduce Action Smoothing by Aligning Actions with Predictions from Preceding States (ASAP), an action smoothing method that effectively mitigates action oscillations. ASAP enforces action smoothness by aligning the actions with those taken in transition-induced similar states and by penalizing second-order differences to suppress high-frequency oscillations. Experiments in Gymnasium and Isaac-Lab environments demonstrate that ASAP yields smoother control and improved policy performance over existing methods.

