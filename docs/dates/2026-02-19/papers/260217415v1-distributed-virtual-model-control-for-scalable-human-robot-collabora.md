---
layout: default
title: Distributed Virtual Model Control for Scalable Human-Robot Collaboration in Shared Workspace
---

# Distributed Virtual Model Control for Scalable Human-Robot Collaboration in Shared Workspace
**arXiv**：[2602.17415v1](https://arxiv.org/abs/2602.17415) · [PDF](https://arxiv.org/pdf/2602.17415.pdf)  
**作者**：Yi Zhang, Omar Faris, Chapa Sirithunge, Kai-Fung Chu, Fumiya Iida, Fulvio Forni  

**一句话要点**：提出分布式虚拟模型控制框架，实现共享工作空间中可扩展的人机协作

**关键词**：虚拟模型控制, 人机协作, 分布式控制, 死锁检测, 共享工作空间

## 3 点简述
- 核心问题：人机协作中机器人易陷入死锁，影响任务效率和安全性。
- 方法要点：基于虚拟模型控制，通过虚拟弹簧和阻尼器实现运动，无需显式轨迹规划。
- 实验或效果：实验中将死锁概率从61.2%降至零，支持多机器人协作，保持约20厘米间距。

## 摘要（原文）

> We present a decentralized, agent agnostic, and safety-aware control framework for human-robot collaboration based on Virtual Model Control (VMC). In our approach, both humans and robots are embedded in the same virtual-component-shaped workspace, where motion is the result of the interaction with virtual springs and dampers rather than explicit trajectory planning. A decentralized, force-based stall detector identifies deadlocks, which are resolved through negotiation. This reduces the probability of robots getting stuck in the block placement task from up to 61.2% to zero in our experiments. The framework scales without structural changes thanks to the distributed implementation: in experiments we demonstrate safe collaboration with up to two robots and two humans, and in simulation up to four robots, maintaining inter-agent separation at around 20 cm. Results show that the method shapes robot behavior intuitively by adjusting control parameters and achieves deadlock-free operation across team sizes in all tested scenarios.

