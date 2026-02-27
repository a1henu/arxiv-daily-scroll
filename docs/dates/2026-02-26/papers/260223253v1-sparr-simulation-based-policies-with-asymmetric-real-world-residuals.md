---
layout: default
title: SPARR: Simulation-based Policies with Asymmetric Real-world Residuals for Assembly
---

# SPARR: Simulation-based Policies with Asymmetric Real-world Residuals for Assembly
**arXiv**：[2602.23253v1](https://arxiv.org/abs/2602.23253) · [PDF](https://arxiv.org/pdf/2602.23253.pdf)  
**作者**：Yijie Guo, Iretiayo Akinola, Lars Johannsmeier, Hugo Hadfield, Abhishek Gupta, Yashraj Narang  

**一句话要点**：提出SPARR方法，结合仿真与真实世界策略以解决机器人装配中的仿真到现实差距问题。

**关键词**：机器人装配, 仿真到现实迁移, 强化学习, 混合策略, 视觉观察, 稀疏奖励

## 3 点简述
- 核心问题：机器人装配因精确接触操作需求，仿真训练策略在真实部署时性能下降。
- 方法要点：使用仿真训练的基础策略提供先验，真实世界学习的残差策略补偿动态和传感器差异。
- 实验或效果：在真实世界实验中，SPARR提高成功率38.4%，减少周期时间29.7%，无需人类监督。

## 摘要（原文）

> Robotic assembly presents a long-standing challenge due to its requirement for precise, contact-rich manipulation. While simulation-based learning has enabled the development of robust assembly policies, their performance often degrades when deployed in real-world settings due to the sim-to-real gap. Conversely, real-world reinforcement learning (RL) methods avoid the sim-to-real gap, but rely heavily on human supervision and lack generalization ability to environmental changes. In this work, we propose a hybrid approach that combines a simulation-trained base policy with a real-world residual policy to efficiently adapt to real-world variations. The base policy, trained in simulation using low-level state observations and dense rewards, provides strong priors for initial behavior. The residual policy, learned in the real world using visual observations and sparse rewards, compensates for discrepancies in dynamics and sensor noise. Extensive real-world experiments demonstrate that our method, SPARR, achieves near-perfect success rates across diverse two-part assembly tasks. Compared to the state-of-the-art zero-shot sim-to-real methods, SPARR improves success rates by 38.4% while reducing cycle time by 29.7%. Moreover, SPARR requires no human expertise, in contrast to the state-of-the-art real-world RL approaches that depend heavily on human supervision.

