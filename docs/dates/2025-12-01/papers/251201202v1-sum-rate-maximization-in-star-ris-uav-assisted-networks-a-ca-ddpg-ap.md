---
layout: default
title: Sum Rate Maximization in STAR-RIS-UAV-Assisted Networks: A CA-DDPG Approach for Joint Optimization
---

# Sum Rate Maximization in STAR-RIS-UAV-Assisted Networks: A CA-DDPG Approach for Joint Optimization
**arXiv**：[2512.01202v1](https://arxiv.org/abs/2512.01202) · [PDF](https://arxiv.org/pdf/2512.01202.pdf)  
**作者**：Yujie Huang, Haibin Wan, Xiangcheng Li, Tuanfa Qin, Yun Li, Jun Li, Wen Chen  

**一句话要点**：提出CA-DDPG算法以优化STAR-RIS-UAV辅助网络的总速率

**关键词**：STAR-RIS, 无人机辅助网络, 深度强化学习, 总速率最大化, 联合优化, CA-DDPG算法

## 3 点简述
- 核心问题：在STAR-RIS-UAV辅助无线通信系统中，联合优化波束成形、相移和无人机位置以最大化总速率。
- 方法要点：基于DDPG算法，引入随机扰动增强探索，并采用卷积增强评估，提出CA-DDPG算法进行迭代优化。
- 实验或效果：仿真显示CA-DDPG算法有效优化系统参数，提升系统容量，性能优于其他算法。

## 摘要（原文）

> With the rapid advances in programmable materials, reconfigurable intelligent surfaces (RIS) have become a pivotal technology for future wireless communications. The simultaneous transmitting and reflecting reconfigurable intelligent surfaces (STAR-RIS) can both transmit and reflect signals, enabling comprehensive signal control and expanding application scenarios. This paper introduces an unmanned aerial vehicle (UAV) to further enhance system flexibility and proposes an optimization design for the spectrum efficiency of the STAR-RIS-UAV-assisted wireless communication system. We present a deep reinforcement learning (DRL) algorithm capable of iteratively optimizing beamforming, phase shifts, and UAV positioning to maximize the system's sum rate through continuous interactions with the environment. To improve exploration in deterministic policies, we introduce a stochastic perturbation factor, which enhances exploration capabilities. As exploration is strengthened, the algorithm's ability to accurately evaluate the state-action value function becomes critical. Thus, based on the deep deterministic policy gradient (DDPG) algorithm, we propose a convolution-augmented deep deterministic policy gradient (CA-DDPG) algorithm that balances exploration and evaluation to improve the system's sum rate. The simulation results demonstrate that the CA-DDPG algorithm effectively interacts with the environment, optimizing the beamforming matrix, phase shift matrix, and UAV location, thereby improving system capacity and achieving better performance than other algorithms.

