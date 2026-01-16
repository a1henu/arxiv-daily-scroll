---
layout: default
title: CoCoPlan: Adaptive Coordination and Communication for Multi-robot Systems in Dynamic and Unknown Environments
---

# CoCoPlan: Adaptive Coordination and Communication for Multi-robot Systems in Dynamic and Unknown Environments
**arXiv**：[2601.10116v1](https://arxiv.org/abs/2601.10116) · [PDF](https://arxiv.org/pdf/2601.10116.pdf)  
**作者**：Xintong Zhang, Junfeng Chen, Yuxiao Zhu, Bing Luo, Meng Guo  

**一句话要点**：提出CoCoPlan框架，通过联合优化任务规划与间歇通信，解决动态未知环境中多机器人系统在有限通信下的协调问题。

**关键词**：多机器人系统, 任务规划, 间歇通信, 动态环境, 协调优化

## 3 点简述
- 核心问题：现有方法在动态时空任务分布下，无法有效适应有限通信，导致协调效率低下。
- 方法要点：采用分支定界架构联合编码任务分配与通信事件，自适应目标函数平衡任务效率与通信延迟。
- 实验或效果：实验显示任务完成率提升22.4%，通信开销降低58.6%，支持100个机器人在动态环境中扩展。

## 摘要（原文）

> Multi-robot systems can greatly enhance efficiency through coordination and collaboration, yet in practice, full-time communication is rarely available and interactions are constrained to close-range exchanges. Existing methods either maintain all-time connectivity, rely on fixed schedules, or adopt pairwise protocols, but none adapt effectively to dynamic spatio-temporal task distributions under limited communication, resulting in suboptimal coordination. To address this gap, we propose CoCoPlan, a unified framework that co-optimizes collaborative task planning and team-wise intermittent communication. Our approach integrates a branch-and-bound architecture that jointly encodes task assignments and communication events, an adaptive objective function that balances task efficiency against communication latency, and a communication event optimization module that strategically determines when, where and how the global connectivity should be re-established. Extensive experiments demonstrate that it outperforms state-of-the-art methods by achieving a 22.4% higher task completion rate, reducing communication overhead by 58.6%, and improving the scalability by supporting up to 100 robots in dynamic environments. Hardware experiments include the complex 2D office environment and large-scale 3D disaster-response scenario.

