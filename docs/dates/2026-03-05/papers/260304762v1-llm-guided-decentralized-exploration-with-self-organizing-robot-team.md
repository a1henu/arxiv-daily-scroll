---
layout: default
title: LLM-Guided Decentralized Exploration with Self-Organizing Robot Teams
---

# LLM-Guided Decentralized Exploration with Self-Organizing Robot Teams
**arXiv**：[2603.04762v1](https://arxiv.org/abs/2603.04762) · [PDF](https://arxiv.org/pdf/2603.04762.pdf)  
**作者**：Hiroaki Kawashima, Shun Ikejima, Takeshi Takai, Mikita Miyaguchi, Yasuharu Kunii  

**一句话要点**：提出基于LLM的自组织多机器人团队探索方法，以增强去中心化探索的效率和鲁棒性。

**关键词**：多机器人探索, 自组织团队, LLM引导决策, 去中心化控制, 仿真验证

## 3 点简述
- 核心问题：在去中心化多机器人探索中，如何动态组队并自主确定探索目标以提高效率和可靠性。
- 方法要点：结合自组织算法实现动态团队形成，并利用LLM为每个团队自主决策探索目的地。
- 实验或效果：通过数十至数百机器人的仿真验证了方法的有效性，未知具体性能指标。

## 摘要（原文）

> When individual robots have limited sensing capabilities or insufficient fault tolerance, it becomes necessary for multiple robots to form teams during exploration, thereby increasing the collective observation range and reliability. Traditionally, swarm formation has often been managed by a central controller; however, from the perspectives of robustness and flexibility, it is preferable for the swarm to operate autonomously even in the absence of centralized control. In addition, the determination of exploration targets for each team is crucial for efficient exploration in such multi-team exploration scenarios. This study therefore proposes an exploration method that combines (1) an algorithm for self-organization, enabling the autonomous and dynamic formation of multiple teams, and (2) an algorithm that allows each team to autonomously determine its next exploration target (destination). In particular, for (2), this study explores a novel strategy based on large language models (LLMs), while classical frontier-based methods and deep reinforcement learning approaches have been widely studied. The effectiveness of the proposed method was validated through simulations involving tens to hundreds of robots.

