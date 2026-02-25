---
layout: default
title: Buffer Matters: Unleashing the Power of Off-Policy Reinforcement Learning in Large Language Model Reasoning
---

# Buffer Matters: Unleashing the Power of Off-Policy Reinforcement Learning in Large Language Model Reasoning
**arXiv**：[2602.20722v1](https://arxiv.org/abs/2602.20722) · [PDF](https://arxiv.org/pdf/2602.20722.pdf)  
**作者**：Xu Wan, Yansheng Wang, Wenqi Huang, Mingyang Sun  

**一句话要点**：提出BAPO框架以解决大语言模型后训练中经验浪费和奖励同质化问题

**关键词**：大语言模型后训练, 离线强化学习, 策略优化, 经验重用, 推理任务

## 3 点简述
- 核心问题：传统RLVR框架存在经验浪费和奖励同质化，影响困难样本学习效率
- 方法要点：BAPO通过动态选择训练批次，重用高质量样本并保证策略改进下界
- 实验或效果：在数学、规划和视觉推理任务上平均提升12.5%，解决40.7%基础模型失败问题

## 摘要（原文）

> Traditional on-policy Reinforcement Learning with Verifiable Rewards (RLVR) frameworks suffer from experience waste and reward homogeneity, which directly hinders learning efficiency on difficult samples during large language models post-training. In this paper, we introduce Batch Adaptation Policy Optimization (BAPO), an off-policy RLVR framework to improve the data efficiency in large language models post-training. It dynamically selects training batches by re-evaluating historically difficult samples and reusing high-quality ones, while holding a lower bound guarantee for policy improvement. Extensive experiments further demonstrate that BAPO achieves an average 12.5% improvement over GRPO across mathematics, planning, and visual reasoning tasks. Crucially, BAPO successfully resolves 40.7% of problems that base models consistently fail to solve.

