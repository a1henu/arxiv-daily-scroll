---
layout: default
title: LLM-Guided Decentralized Exploration with Self-Organizing Robot Teams
---

# LLM-Guided Decentralized Exploration with Self-Organizing Robot Teams
**arXiv**：[2603.04762v1](https://arxiv.org/abs/2603.04762) · [PDF](https://arxiv.org/pdf/2603.04762.pdf)  
**作者**：Hiroaki Kawashima, Shun Ikejima, Takeshi Takai, Mikita Miyaguchi, Yasuharu Kunii  

**一句话要点**：提出基于LLM引导的自组织机器人团队探索方法，以增强多机器人探索的自主性和效率。

**关键词**：多机器人探索, 自组织团队, LLM引导决策, 分散控制, 仿真验证

## 3 点简述
- 核心问题：多机器人探索中，个体感知有限且需团队协作，传统集中控制缺乏鲁棒性和灵活性。
- 方法要点：结合自组织算法动态形成团队，并利用LLM为各团队自主确定探索目标。
- 实验或效果：通过数十至数百机器人的仿真验证了方法的有效性。

## 摘要（原文）

> When individual robots have limited sensing capabilities or insufficient fault tolerance, it becomes necessary for multiple robots to form teams during exploration, thereby increasing the collective observation range and reliability. Traditionally, swarm formation has often been managed by a central controller; however, from the perspectives of robustness and flexibility, it is preferable for the swarm to operate autonomously even in the absence of centralized control. In addition, the determination of exploration targets for each team is crucial for efficient exploration in such multi-team exploration scenarios. This study therefore proposes an exploration method that combines (1) an algorithm for self-organization, enabling the autonomous and dynamic formation of multiple teams, and (2) an algorithm that allows each team to autonomously determine its next exploration target (destination). In particular, for (2), this study explores a novel strategy based on large language models (LLMs), while classical frontier-based methods and deep reinforcement learning approaches have been widely studied. The effectiveness of the proposed method was validated through simulations involving tens to hundreds of robots.

