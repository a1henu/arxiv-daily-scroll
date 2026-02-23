---
layout: default
title: Generating adversarial inputs for a graph neural network model of AC power flow
---

# Generating adversarial inputs for a graph neural network model of AC power flow
**arXiv**：[2602.17975v1](https://arxiv.org/abs/2602.17975) · [PDF](https://arxiv.org/pdf/2602.17975.pdf)  
**作者**：Robert Parker  

**一句话要点**：提出优化方法生成对抗输入，以评估图神经网络交流潮流模型的误差与脆弱性。

**关键词**：图神经网络, 交流潮流, 对抗攻击, 模型验证, 电力系统, 优化问题

## 3 点简述
- 核心问题：图神经网络交流潮流模型预测与物理方程解间存在高误差，需评估其对抗鲁棒性。
- 方法要点：通过优化问题生成对抗输入点，最小化扰动以满足对抗约束，验证模型脆弱性。
- 实验或效果：在14节点测试网格上，对抗点导致无功功率误差达3.4标幺值，电压幅值误差0.08标幺值；单节点电压幅值扰动0.04标幺值即可触发高误差。

## 摘要（原文）

> This work formulates and solves optimization problems to generate input points that yield high errors between a neural network's predicted AC power flow solution and solutions to the AC power flow equations. We demonstrate this capability on an instance of the CANOS-PF graph neural network model, as implemented by the PF$Δ$ benchmark library, operating on a 14-bus test grid. Generated adversarial points yield errors as large as 3.4 per-unit in reactive power and 0.08 per-unit in voltage magnitude. When minimizing the perturbation from a training point necessary to satisfy adversarial constraints, we find that the constraints can be met with as little as an 0.04 per-unit perturbation in voltage magnitude on a single bus. This work motivates the development of rigorous verification and robust training methods for neural network surrogate models of AC power flow.

