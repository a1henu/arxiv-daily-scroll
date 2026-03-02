---
layout: default
title: Efficient Discovery of Approximate Causal Abstractions via Neural Mechanism Sparsification
---

# Efficient Discovery of Approximate Causal Abstractions via Neural Mechanism Sparsification
**arXiv**：[2602.24266v1](https://arxiv.org/abs/2602.24266) · [PDF](https://arxiv.org/pdf/2602.24266.pdf)  
**作者**：Amir Asiaee  

**一句话要点**：提出基于神经机制稀疏化的近似因果抽象发现方法，以高效提取预训练网络的干预忠实抽象

**关键词**：因果抽象, 神经机制稀疏化, 结构化剪枝, 干预风险, 预训练网络, 可解释性

## 3 点简述
- 核心问题：验证神经网络是否实现可解释因果机制需发现因果抽象，但传统方法需暴力干预或重训练，效率低
- 方法要点：将结构化剪枝视为近似抽象搜索，推导干预风险目标，基于二阶展开获得闭式准则替换或合并单元
- 实验或效果：方法高效提取稀疏且干预忠实的抽象，通过交换干预验证，统一曲率下简化为基于方差的剪枝

## 摘要（原文）

> Neural networks are hypothesized to implement interpretable causal mechanisms, yet verifying this requires finding a causal abstraction -- a simpler, high-level Structural Causal Model (SCM) faithful to the network under interventions. Discovering such abstractions is hard: it typically demands brute-force interchange interventions or retraining. We reframe the problem by viewing structured pruning as a search over approximate abstractions. Treating a trained network as a deterministic SCM, we derive an Interventional Risk objective whose second-order expansion yields closed-form criteria for replacing units with constants or folding them into neighbors. Under uniform curvature, our score reduces to activation variance, recovering variance-based pruning as a special case while clarifying when it fails. The resulting procedure efficiently extracts sparse, intervention-faithful abstractions from pretrained networks, which we validate via interchange interventions.

