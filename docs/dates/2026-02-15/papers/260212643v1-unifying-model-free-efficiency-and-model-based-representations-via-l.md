---
layout: default
title: Unifying Model-Free Efficiency and Model-Based Representations via Latent Dynamics
---

# Unifying Model-Free Efficiency and Model-Based Representations via Latent Dynamics
**arXiv**：[2602.12643v1](https://arxiv.org/abs/2602.12643) · [PDF](https://arxiv.org/pdf/2602.12643.pdf)  
**作者**：Jashaswimalya Acharjee, Balaraman Ravindran  

**一句话要点**：提出统一潜在动力学算法，结合无模型效率与基于模型表示，实现跨领域强化学习。

**关键词**：强化学习, 潜在表示, 模型融合, 跨领域学习, 值函数近似, 样本效率

## 3 点简述
- 核心问题：强化学习中无模型方法效率高但表示能力弱，基于模型方法反之，需平衡两者。
- 方法要点：将状态-动作对嵌入潜在空间，使值函数近似线性，同步更新编码器、值和策略网络。
- 实验或效果：在80个环境中评估，性能匹配或超越基线，跨领域适应性强，参数少且调优少。

## 摘要（原文）

> We present Unified Latent Dynamics (ULD), a novel reinforcement learning algorithm that unifies the efficiency of model-free methods with the representational strengths of model-based approaches, without incurring planning overhead. By embedding state-action pairs into a latent space in which the true value function is approximately linear, our method supports a single set of hyperparameters across diverse domains -- from continuous control with low-dimensional and pixel inputs to high-dimensional Atari games. We prove that, under mild conditions, the fixed point of our embedding-based temporal-difference updates coincides with that of a corresponding linear model-based value expansion, and we derive explicit error bounds relating embedding fidelity to value approximation quality. In practice, ULD employs synchronized updates of encoder, value, and policy networks, auxiliary losses for short-horizon predictive dynamics, and reward-scale normalization to ensure stable learning under sparse rewards. Evaluated on 80 environments spanning Gym locomotion, DeepMind Control (proprioceptive and visual), and Atari, our approach matches or exceeds the performance of specialized model-free and general model-based baselines -- achieving cross-domain competence with minimal tuning and a fraction of the parameter footprint. These results indicate that value-aligned latent representations alone can deliver the adaptability and sample efficiency traditionally attributed to full model-based planning.

