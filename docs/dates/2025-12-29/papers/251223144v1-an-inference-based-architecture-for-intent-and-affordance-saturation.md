---
layout: default
title: An Inference-Based Architecture for Intent and Affordance Saturation in Decision-Making
---

# An Inference-Based Architecture for Intent and Affordance Saturation in Decision-Making
**arXiv**：[2512.23144v1](https://arxiv.org/abs/2512.23144) · [PDF](https://arxiv.org/pdf/2512.23144.pdf)  
**作者**：Wendyam Eric Lionel Ilboudo, Saori C Tanaka  

**一句话要点**：提出基于推理的意图与可供性饱和模型，以解释决策瘫痪现象。

**关键词**：决策瘫痪, 推理模型, KL目标, 意图饱和, 可供性饱和, 自闭症研究

## 3 点简述
- 核心问题：决策瘫痪源于层次决策过程中的收敛失败，尤其在自闭症研究中显著。
- 方法要点：分离意图与可供性选择，使用反向和正向KL目标混合进行推理形式化承诺。
- 实验或效果：模拟多选项任务重现决策惯性和关闭特征，将自闭症视为推理决策连续体的极端状态。

## 摘要（原文）

> Decision paralysis, i.e. hesitation, freezing, or failure to act despite full knowledge and motivation, poses a challenge for choice models that assume options are already specified and readily comparable. Drawing on qualitative reports in autism research that are especially salient, we propose a computational account in which paralysis arises from convergence failure in a hierarchical decision process. We separate intent selection (what to pursue) from affordance selection (how to pursue the goal) and formalize commitment as inference under a mixture of reverse- and forward-Kullback-Leibler (KL) objectives. Reverse KL is mode-seeking and promotes rapid commitment, whereas forward KL is mode-covering and preserves multiple plausible goals or actions. In static and dynamic (drift-diffusion) models, forward-KL-biased inference yields slow, heavy-tailed response times and two distinct failure modes, intent saturation and affordance saturation, when values are similar. Simulations in multi-option tasks reproduce key features of decision inertia and shutdown, treating autism as an extreme regime of a general, inference-based, decision-making continuum.

