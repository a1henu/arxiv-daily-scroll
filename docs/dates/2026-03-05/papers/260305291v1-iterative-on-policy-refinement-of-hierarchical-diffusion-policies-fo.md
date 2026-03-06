---
layout: default
title: Iterative On-Policy Refinement of Hierarchical Diffusion Policies for Language-Conditioned Manipulation
---

# Iterative On-Policy Refinement of Hierarchical Diffusion Policies for Language-Conditioned Manipulation
**arXiv**：[2603.05291v1](https://arxiv.org/abs/2603.05291) · [PDF](https://arxiv.org/pdf/2603.05291.pdf)  
**作者**：Clemence Grislain, Olivier Sigaud, Mohamed Chetouani  

**一句话要点**：提出HD-ExpIt框架，通过环境反馈迭代微调分层扩散策略以解决语言条件操作中的规划-控制器不匹配问题。

**关键词**：分层策略, 扩散模型, 语言条件操作, 迭代微调, 自增强学习, CALVIN基准

## 3 点简述
- 核心问题：分层策略中高层规划器生成子目标时未考虑低层控制器的实际限制，导致任务失败。
- 方法要点：采用自增强循环训练，利用扩散规划自主发现成功行为，并蒸馏回分层策略以隐式对齐规划与控制能力。
- 实验或效果：在CALVIN基准测试中，相比仅离线训练的方法，HD-ExpIt显著提升性能，达到从头训练方法中的最优水平。

## 摘要（原文）

> Hierarchical policies for language-conditioned manipulation decompose tasks into subgoals, where a high-level planner guides a low-level controller. However, these hierarchical agents often fail because the planner generates subgoals without considering the actual limitations of the controller. Existing solutions attempt to bridge this gap via intermediate modules or shared representations, but they remain limited by their reliance on fixed offline datasets. We propose HD-ExpIt, a framework for iterative fine-tuning of hierarchical diffusion policies via environment feedback. HD-ExpIt organizes training into a self-reinforcing cycle: it utilizes diffusion-based planning to autonomously discover successful behaviors, which are then distilled back into the hierarchical policy. This loop enables both components to improve while implicitly grounding the planner in the controller's actual capabilities without requiring explicit proxy models. Empirically, HD-ExpIt significantly improves hierarchical policies trained solely on offline data, achieving state-of-the-art performance on the long-horizon CALVIN benchmark among methods trained from scratch.

