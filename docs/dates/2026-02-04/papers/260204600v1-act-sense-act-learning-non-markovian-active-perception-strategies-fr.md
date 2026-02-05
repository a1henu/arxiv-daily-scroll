---
layout: default
title: Act, Sense, Act: Learning Non-Markovian Active Perception Strategies from Large-Scale Egocentric Human Data
---

# Act, Sense, Act: Learning Non-Markovian Active Perception Strategies from Large-Scale Egocentric Human Data
**arXiv**：[2602.04600v1](https://arxiv.org/abs/2602.04600) · [PDF](https://arxiv.org/pdf/2602.04600.pdf)  
**作者**：Jialiang Li, Yi Qiao, Yunhan Guo, Changwen Chen, Wenzhao Lian  

**一句话要点**：提出CoMe-VLA框架，利用人类第一视角数据学习非马尔可夫主动感知策略以提升机器人通用操作能力。

**关键词**：主动感知, 非马尔可夫过程, 第一视角数据, 视觉-语言-动作框架, 长时程任务, 机器人操作

## 3 点简述
- 核心问题：现有主动感知方法局限于有限感知行为，难以适应复杂环境中的信息不确定性。
- 方法要点：基于信息增益和决策分支形式化非马尔可夫主动感知，集成认知辅助头和双轨记忆系统。
- 实验或效果：在轮式人形机器人上验证了方法在多种长时程任务中的强鲁棒性和适应性。

## 摘要（原文）

> Achieving generalizable manipulation in unconstrained environments requires the robot to proactively resolve information uncertainty, i.e., the capability of active perception. However, existing methods are often confined in limited types of sensing behaviors, restricting their applicability to complex environments. In this work, we formalize active perception as a non-Markovian process driven by information gain and decision branching, providing a structured categorization of visual active perception paradigms. Building on this perspective, we introduce CoMe-VLA, a cognitive and memory-aware vision-language-action (VLA) framework that leverages large-scale human egocentric data to learn versatile exploration and manipulation priors. Our framework integrates a cognitive auxiliary head for autonomous sub-task transitions and a dual-track memory system to maintain consistent self and environmental awareness by fusing proprioceptive and visual temporal contexts. By aligning human and robot hand-eye coordination behaviors in a unified egocentric action space, we train the model progressively in three stages. Extensive experiments on a wheel-based humanoid have demonstrated strong robustness and adaptability of our proposed method across diverse long-horizon tasks spanning multiple active perception scenarios.

