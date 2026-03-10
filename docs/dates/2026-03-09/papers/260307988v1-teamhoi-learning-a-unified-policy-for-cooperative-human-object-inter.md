---
layout: default
title: TeamHOI: Learning a Unified Policy for Cooperative Human-Object Interactions with Any Team Size
---

# TeamHOI: Learning a Unified Policy for Cooperative Human-Object Interactions with Any Team Size
**arXiv**：[2603.07988v1](https://arxiv.org/abs/2603.07988) · [PDF](https://arxiv.org/pdf/2603.07988.pdf)  
**作者**：Stefan Lionar, Gim Hee Lee  

**一句话要点**：提出TeamHOI框架，使单一去中心化策略能处理任意团队规模的协作人-物交互任务。

**关键词**：协作人-物交互, 去中心化策略, Transformer网络, 对抗运动先验, 物理模拟控制

## 3 点简述
- 核心问题：基于物理的人形控制难以扩展到协作人-物交互，且数据稀缺。
- 方法要点：使用基于Transformer的策略网络和掩码对抗运动先验，实现可扩展协调与运动真实性。
- 实验或效果：在2至8个代理的协作搬运任务中，实现高成功率与连贯合作。

## 摘要（原文）

> Physics-based humanoid control has achieved remarkable progress in enabling realistic and high-performing single-agent behaviors, yet extending these capabilities to cooperative human-object interaction (HOI) remains challenging. We present TeamHOI, a framework that enables a single decentralized policy to handle cooperative HOIs across any number of cooperating agents. Each agent operates using local observations while attending to other teammates through a Transformer-based policy network with teammate tokens, allowing scalable coordination across variable team sizes. To enforce motion realism while addressing the scarcity of cooperative HOI data, we further introduce a masked Adversarial Motion Prior (AMP) strategy that uses single-human reference motions while masking object-interacting body parts during training. The masked regions are then guided through task rewards to produce diverse and physically plausible cooperative behaviors. We evaluate TeamHOI on a challenging cooperative carrying task involving two to eight humanoid agents and varied object geometries. Finally, to promote stable carrying, we design a team-size- and shape-agnostic formation reward. TeamHOI achieves high success rates and demonstrates coherent cooperation across diverse configurations with a single policy.

