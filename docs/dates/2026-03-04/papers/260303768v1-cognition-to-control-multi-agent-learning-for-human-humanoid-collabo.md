---
layout: default
title: Cognition to Control - Multi-Agent Learning for Human-Humanoid Collaborative Transport
---

# Cognition to Control - Multi-Agent Learning for Human-Humanoid Collaborative Transport
**arXiv**：[2603.03768v1](https://arxiv.org/abs/2603.03768) · [PDF](https://arxiv.org/pdf/2603.03768.pdf)  
**作者**：Hao Zhang, Ding Zhao, H. Eric Tseng  

**一句话要点**：提出认知到控制（C2C）分层框架，用于人形机器人与人类协作搬运任务。

**关键词**：人机协作, 多智能体强化学习, 分层控制, 视觉语言模型, 全身控制, 马尔可夫势游戏

## 3 点简述
- 核心问题：现有视觉-语言-动作系统缺乏系统2式深思与低延迟连续控制的整合，影响多智能体人机协作。
- 方法要点：采用三层架构，包括视觉语言模型基础层、基于马尔可夫势游戏的分散式多智能体强化学习深思层，以及全身控制层。
- 实验或效果：在协作操作任务中，相比单智能体和端到端基线，表现出更高成功率和鲁棒性，并涌现出领导者-跟随者行为。

## 摘要（原文）

> Effective human-robot collaboration (HRC) requires translating high-level intent into contact-stable whole-body motion while continuously adapting to a human partner. Many vision-language-action (VLA) systems learn end-to-end mappings from observations and instructions to actions, but they often emphasize reactive (System 1-like) behavior and leave under-specified how sustained System 2-style deliberation can be integrated with reliable, low-latency continuous control. This gap is acute in multi-agent HRC, where long-horizon coordination decisions and physical execution must co-evolve under contact, feasibility, and safety constraints. We address this limitation with cognition-to-control (C2C), a three-layer hierarchy that makes the deliberation-to-control pathway explicit: (i) a VLM-based grounding layer that maintains persistent scene referents and infers embodiment-aware affordances/constraints; (ii) a deliberative skill/coordination layer-the System 2 core-that optimizes long-horizon skill choices and sequences under human-robot coupling via decentralized MARL cast as a Markov potential game with a shared potential encoding task progress; and (iii) a whole-body control layer that executes the selected skills at high frequency while enforcing kinematic/dynamic feasibility and contact stability. The deliberative layer is realized as a residual policy relative to a nominal controller, internalizing partner dynamics without explicit role assignment. Experiments on collaborative manipulation tasks show higher success and robustness than single-agent and end-to-end baselines, with stable coordination and emergent leader-follower behaviors.

