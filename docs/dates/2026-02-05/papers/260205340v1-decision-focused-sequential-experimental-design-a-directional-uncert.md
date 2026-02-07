---
layout: default
title: Decision-Focused Sequential Experimental Design: A Directional Uncertainty-Guided Approach
---

# Decision-Focused Sequential Experimental Design: A Directional Uncertainty-Guided Approach
**arXiv**：[2602.05340v1](https://arxiv.org/abs/2602.05340) · [PDF](https://arxiv.org/pdf/2602.05340.pdf)  
**作者**：Beichen Wan, Mo Liu, Paul Grigas, Zuo-Jun Max Shen  

**一句话要点**：提出基于方向性不确定性的顺序实验设计方法，以优化预测-优化范式中的决策损失。

**关键词**：顺序实验设计, 预测-优化范式, 决策损失, 方向性不确定性, LLM任务分配

## 3 点简述
- 核心问题：传统顺序实验设计在预测-优化范式中因忽视决策损失而效率低下。
- 方法要点：引入方向性不确定性度量，无需优化求解器，计算高效且具一致性保证。
- 实验或效果：在LLM任务分配等实验中，该方法比决策盲设计更早停止，提升效率。

## 摘要（原文）

> We consider the sequential experimental design problem in the predict-then-optimize paradigm. In this paradigm, the outputs of the prediction model are used as coefficient vectors in a downstream linear optimization problem. Traditional sequential experimental design aims to control the input variables (features) so that the improvement in prediction accuracy from each experimental outcome (label) is maximized. However, in the predict-then-optimize setting, performance is ultimately evaluated based on the decision loss induced by the downstream optimization, rather than by prediction error. This mismatch between prediction accuracy and decision loss renders traditional decision-blind designs inefficient. To address this issue, we propose a directional-based metric to quantify predictive uncertainty. This metric does not require solving an optimization oracle and is therefore computationally tractable. We show that the resulting sequential design criterion enjoys strong consistency and convergence guarantees. Under a broad class of distributions, we demonstrate that our directional uncertainty-based design attains an earlier stopping time than decision-blind designs. This advantage is further supported by real-world experiments on an LLM job allocation problem.

