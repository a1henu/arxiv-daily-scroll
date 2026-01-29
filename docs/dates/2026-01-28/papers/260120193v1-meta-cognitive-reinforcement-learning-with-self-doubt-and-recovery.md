---
layout: default
title: Meta-Cognitive Reinforcement Learning with Self-Doubt and Recovery
---

# Meta-Cognitive Reinforcement Learning with Self-Doubt and Recovery
**arXiv**：[2601.20193v1](https://arxiv.org/abs/2601.20193) · [PDF](https://arxiv.org/pdf/2601.20193.pdf)  
**作者**：Zhipeng Zhang, Wenting Ma, Kai Li, Meng Guo, Lei Yang, Wei Yu, Hongji Cui, Yichen Zhang, Mo Zhang, Jinzhe Lin, Zhenjie Yao  

**一句话要点**：提出元认知强化学习框架，通过自疑与恢复机制解决奖励污染下的鲁棒性问题。

**关键词**：元认知强化学习, 奖励污染, 鲁棒性, 价值预测误差稳定性, 故障安全调节, 信任恢复

## 3 点简述
- 核心问题：现有鲁棒强化学习方法缺乏对自身学习过程可靠性的推理能力，易过度保守或灾难性失败。
- 方法要点：引入基于价值预测误差稳定性的元信任变量，通过故障安全调节和渐进信任恢复调控学习动态。
- 实验或效果：在奖励污染的连续控制基准测试中，实现更高平均回报并显著减少后期训练失败。

## 摘要（原文）

> Robust reinforcement learning methods typically focus on suppressing unreliable experiences or corrupted rewards, but they lack the ability to reason about the reliability of their own learning process. As a result, such methods often either overreact to noise by becoming overly conservative or fail catastrophically when uncertainty accumulates.
>   In this work, we propose a meta-cognitive reinforcement learning framework that enables an agent to assess, regulate, and recover its learning behavior based on internally estimated reliability signals. The proposed method introduces a meta-trust variable driven by Value Prediction Error Stability (VPES), which modulates learning dynamics via fail-safe regulation and gradual trust recovery.
>   Experiments on continuous-control benchmarks with reward corruption demonstrate that recovery-enabled meta-cognitive control achieves higher average returns and significantly reduces late-stage training failures compared to strong robustness baselines.

