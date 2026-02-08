---
layout: default
title: DFPO: Scaling Value Modeling via Distributional Flow towards Robust and Generalizable LLM Post-Training
---

# DFPO: Scaling Value Modeling via Distributional Flow towards Robust and Generalizable LLM Post-Training
**arXiv**：[2602.05890v1](https://arxiv.org/abs/2602.05890) · [PDF](https://arxiv.org/pdf/2602.05890.pdf)  
**作者**：Dingwei Zhu, Zhiheng Xi, Shihan Dou, Jiahan Li, Chenhao Huang, Junjie Ye, Sixian Li, Mingxu Chai, Yuhui Wang, Yajie Yang, Ming Zhang, Jiazheng Zhang, Shichun Liu, Caishuang Huang, Yunke Zhang, Yuran Wang, Tao Gui, Xipeng Qiu, Qi Zhang, Xuanjing Huang  

**一句话要点**：提出DFPO以增强LLM后训练中强化学习的鲁棒性和泛化能力

**关键词**：强化学习, 分布强化学习, LLM后训练, 值流建模, 鲁棒性优化, 泛化能力

## 3 点简述
- 核心问题：强化学习在真实环境中面临噪声监督和域外泛化差的问题，现有分布方法值表示粗糙。
- 方法要点：DFPO通过建模值流场替代孤立分位数预测，捕获更丰富状态信息，并集成条件风险控制和一致性约束。
- 实验或效果：在对话、数学推理和科学任务上优于PPO和FlowRL等基线，提升训练稳定性和泛化性能。

## 摘要（原文）

> Training reinforcement learning (RL) systems in real-world environments remains challenging due to noisy supervision and poor out-of-domain (OOD) generalization, especially in LLM post-training. Recent distributional RL methods improve robustness by modeling values with multiple quantile points, but they still learn each quantile independently as a scalar. This results in rough-grained value representations that lack fine-grained conditioning on state information, struggling under complex and OOD conditions. We propose DFPO (Distributional Value Flow Policy Optimization with Conditional Risk and Consistency Control), a robust distributional RL framework that models values as continuous flows across time steps. By scaling value modeling through learning of a value flow field instead of isolated quantile predictions, DFPO captures richer state information for more accurate advantage estimation. To stabilize training under noisy feedback, DFPO further integrates conditional risk control and consistency constraints along value flow trajectories. Experiments on dialogue, math reasoning, and scientific tasks show that DFPO outperforms PPO, FlowRL, and other robust baselines under noisy supervision, achieving improved training stability and generalization.

