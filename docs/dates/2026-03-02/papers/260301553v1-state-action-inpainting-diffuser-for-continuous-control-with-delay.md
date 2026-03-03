---
layout: default
title: State-Action Inpainting Diffuser for Continuous Control with Delay
---

# State-Action Inpainting Diffuser for Continuous Control with Delay
**arXiv**：[2603.01553v1](https://arxiv.org/abs/2603.01553) · [PDF](https://arxiv.org/pdf/2603.01553.pdf)  
**作者**：Dongqi Han, Wei Wang, Enze Zhang, Dongsheng Li  

**一句话要点**：提出状态-动作修复扩散器以解决延迟连续控制问题

**关键词**：延迟控制, 序列修复, 扩散模型, 强化学习, 连续控制

## 3 点简述
- 核心问题：信号延迟在连续控制中引入感知与交互的时间差，挑战强化学习性能。
- 方法要点：通过联合序列修复任务，结合动力学学习与策略优化，生成一致计划。
- 实验或效果：在延迟连续控制基准测试中实现最先进且鲁棒的性能。

## 摘要（原文）

> Signal delay poses a fundamental challenge in continuous control and reinforcement learning (RL) by introducing a temporal gap between interaction and perception. Current solutions have largely evolved along two distinct paradigms: model-free approaches which utilize state augmentation to preserve Markovian properties, and model-based methods which focus on inferring latent beliefs via dynamics modeling. In this paper, we bridge these perspectives by introducing State-Action Inpainting Diffuser (SAID), a framework that integrates the inductive bias of dynamics learning with the direct decision-making capability of policy optimization. By formulating the problem as a joint sequence inpainting task, SAID implicitly captures environmental dynamics while directly generating consistent plans, effectively operating at the intersection of model-based and model-free paradigms. Crucially, this generative formulation allows SAID to be seamlessly applied to both online and offline RL. Extensive experiments on delayed continuous control benchmarks demonstrate that SAID achieves state-of-the-art and robust performance. Our study suggests a new methodology to advance the field of RL with delay.

