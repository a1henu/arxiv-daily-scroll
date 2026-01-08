---
layout: default
title: Learning Shrinks the Hard Tail: Training-Dependent Inference Scaling in a Solvable Linear Model
---

# Learning Shrinks the Hard Tail: Training-Dependent Inference Scaling in a Solvable Linear Model
**arXiv**：[2601.03764v1](https://arxiv.org/abs/2601.03764) · [PDF](https://arxiv.org/pdf/2601.03764.pdf)  
**作者**：Noam Levi  

**一句话要点**：提出潜在实例难度模型，分析训练依赖的推理缩放，揭示学习缩小误差分布硬尾现象。

**关键词**：神经缩放定律, 推理失败率, 潜在实例难度, 重尾分布, 训练依赖缩放, 计算分配

## 3 点简述
- 核心问题：在目标具有内在异质难度的可解模型中，分析神经缩放定律与推理失败率的关系。
- 方法要点：基于重尾分布建模实例精度，推导训练样本量影响推理指数β_eff的闭式预测。
- 实验或效果：通过模拟和CIFAR-10H、数学蒸馏任务验证模型预测，包括计算分配规则。

## 摘要（原文）

> We analyze neural scaling laws in a solvable model of last-layer fine-tuning where targets have intrinsic, instance-heterogeneous difficulty. In our Latent Instance Difficulty (LID) model, each input's target variance is governed by a latent ``precision'' drawn from a heavy-tailed distribution. While generalization loss recovers standard scaling laws, our main contribution connects this to inference. The pass@$k$ failure rate exhibits a power-law decay, $k^{-β_\text{eff}}$, but the observed exponent $β_\text{eff}$ is training-dependent. It grows with sample size $N$ before saturating at an intrinsic limit $β$ set by the difficulty distribution's tail. This coupling reveals that learning shrinks the ``hard tail'' of the error distribution: improvements in the model's generalization error steepen the pass@$k$ curve until irreducible target variance dominates. The LID model yields testable, closed-form predictions for this behavior, including a compute-allocation rule that favors training before saturation and inference attempts after. We validate these predictions in simulations and in two real-data proxies: CIFAR-10H (human-label variance) and a maths teacher-student distillation task.

