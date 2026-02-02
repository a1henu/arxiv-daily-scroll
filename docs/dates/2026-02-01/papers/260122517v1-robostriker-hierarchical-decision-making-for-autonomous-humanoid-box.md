---
layout: default
title: RoboStriker: Hierarchical Decision-Making for Autonomous Humanoid Boxing
---

# RoboStriker: Hierarchical Decision-Making for Autonomous Humanoid Boxing
**arXiv**：[2601.22517v1](https://arxiv.org/abs/2601.22517) · [PDF](https://arxiv.org/pdf/2601.22517.pdf)  
**作者**：Kangning Yin, Zhe Cao, Wentao Dong, Weishuai Zeng, Tianyi Zhang, Qiang Zhang, Jingbo Wang, Jiangmiao Pang, Ming Zhou, Weinan Zhang  

**一句话要点**：提出RoboStriker分层框架，通过解耦策略推理与物理执行实现自主人形机器人拳击。

**关键词**：人形机器人控制, 分层决策, 潜空间强化学习, 多智能体交互, 仿真到现实迁移

## 3 点简述
- 核心问题：人形机器人拳击任务中，高维接触动力学和缺乏运动先验阻碍多智能体强化学习直接应用。
- 方法要点：采用三阶段框架，包括技能学习、潜空间正则化和潜空间神经虚拟自博弈，以稳定训练。
- 实验或效果：在仿真中实现优越竞争性能，并展示仿真到现实的迁移能力。

## 摘要（原文）

> Achieving human-level competitive intelligence and physical agility in humanoid robots remains a major challenge, particularly in contact-rich and highly dynamic tasks such as boxing. While Multi-Agent Reinforcement Learning (MARL) offers a principled framework for strategic interaction, its direct application to humanoid control is hindered by high-dimensional contact dynamics and the absence of strong physical motion priors. We propose RoboStriker, a hierarchical three-stage framework that enables fully autonomous humanoid boxing by decoupling high-level strategic reasoning from low-level physical execution. The framework first learns a comprehensive repertoire of boxing skills by training a single-agent motion tracker on human motion capture data. These skills are subsequently distilled into a structured latent manifold, regularized by projecting the Gaussian-parameterized distribution onto a unit hypersphere. This topological constraint effectively confines exploration to the subspace of physically plausible motions. In the final stage, we introduce Latent-Space Neural Fictitious Self-Play (LS-NFSP), where competing agents learn competitive tactics by interacting within the latent action space rather than the raw motor space, significantly stabilizing multi-agent training. Experimental results demonstrate that RoboStriker achieves superior competitive performance in simulation and exhibits sim-to-real transfer. Our website is available at RoboStriker.

