---
layout: default
title: ManiLong-Shot: Interaction-Aware One-Shot Imitation Learning for Long-Horizon Manipulation
---

# ManiLong-Shot: Interaction-Aware One-Shot Imitation Learning for Long-Horizon Manipulation
**arXiv**：[2512.16302v1](https://arxiv.org/abs/2512.16302) · [PDF](https://arxiv.org/pdf/2512.16302.pdf)  
**作者**：Zixuan Chen, Chongkai Gao, Lin Shao, Jieqi Shi, Jing Huo, Yang Gao  

**一句话要点**：提出ManiLong-Shot框架，通过交互感知原语序列化实现长时程操作任务的一次性模仿学习。

**关键词**：一次性模仿学习, 长时程操作, 交互感知原语, 视觉语言模型, 机器人操作

## 3 点简述
- 核心问题：现有一次性模仿学习方法局限于短时程任务，难以应用于复杂长时程操作。
- 方法要点：基于物理交互事件分解任务为原语，利用视觉语言模型或规则启发式驱动，预测不变区域并建立对应关系。
- 实验或效果：在模拟实验中，仅用10个短时程任务训练，泛化至20个未见长时程任务，相对SOTA提升22.8%；真实机器人实验验证了鲁棒性。

## 摘要（原文）

> One-shot imitation learning (OSIL) offers a promising way to teach robots new skills without large-scale data collection. However, current OSIL methods are primarily limited to short-horizon tasks, thus limiting their applicability to complex, long-horizon manipulations. To address this limitation, we propose ManiLong-Shot, a novel framework that enables effective OSIL for long-horizon prehensile manipulation tasks. ManiLong-Shot structures long-horizon tasks around physical interaction events, reframing the problem as sequencing interaction-aware primitives instead of directly imitating continuous trajectories. This primitive decomposition can be driven by high-level reasoning from a vision-language model (VLM) or by rule-based heuristics derived from robot state changes. For each primitive, ManiLong-Shot predicts invariant regions critical to the interaction, establishes correspondences between the demonstration and the current observation, and computes the target end-effector pose, enabling effective task execution. Extensive simulation experiments show that ManiLong-Shot, trained on only 10 short-horizon tasks, generalizes to 20 unseen long-horizon tasks across three difficulty levels via one-shot imitation, achieving a 22.8% relative improvement over the SOTA. Additionally, real-robot experiments validate ManiLong-Shot's ability to robustly execute three long-horizon manipulation tasks via OSIL, confirming its practical applicability.

