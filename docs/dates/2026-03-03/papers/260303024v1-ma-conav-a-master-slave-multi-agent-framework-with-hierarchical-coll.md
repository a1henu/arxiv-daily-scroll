---
layout: default
title: MA-CoNav: A Master-Slave Multi-Agent Framework with Hierarchical Collaboration and Dual-Level Reflection for Long-Horizon Embodied VLN
---

# MA-CoNav: A Master-Slave Multi-Agent Framework with Hierarchical Collaboration and Dual-Level Reflection for Long-Horizon Embodied VLN
**arXiv**：[2603.03024v1](https://arxiv.org/abs/2603.03024) · [PDF](https://arxiv.org/pdf/2603.03024.pdf)  
**作者**：Ling Luo, Qianqian Bai  

**一句话要点**：提出MA-CoNav多智能体框架以解决长距离视觉语言导航中的认知过载问题

**关键词**：视觉语言导航, 多智能体协作, 主从架构, 分层协作, 双阶段反思, 长距离导航

## 3 点简述
- 核心问题：单智能体在复杂长距离任务中易受感知扭曲和决策漂移影响
- 方法要点：采用主从分层架构，分配感知、规划、执行和记忆功能给专门智能体
- 实验或效果：在真实室内数据集上全面超越现有主流方法，无需场景微调

## 摘要（原文）

> Vision-Language Navigation (VLN) aims to empower robots with the ability to perform long-horizon navigation in unfamiliar environments based on complex linguistic instructions. Its success critically hinges on establishing an efficient ``language-understanding -- visual-perception -- embodied-execution'' closed loop. Existing methods often suffer from perceptual distortion and decision drift in complex, long-distance tasks due to the cognitive overload of a single agent. Inspired by distributed cognition theory, this paper proposes MA-CoNav, a Multi-Agent Collaborative Navigation framework. This framework adopts a ``Master-Slave'' hierarchical agent collaboration architecture, decoupling and distributing the perception, planning, execution, and memory functions required for navigation tasks to specialized agents. Specifically, the Master Agent is responsible for global orchestration, while the Subordinate Agent group collaborates through a clear division of labor: an Observation Agent generates environment descriptions, a Planning Agent performs task decomposition and dynamic verification, an Execution Agent handles simultaneous mapping and action, and a Memory Agent manages structured experiences. Furthermore, the framework introduces a ``Local-Global'' dual-stage reflection mechanism to dynamically optimize the entire navigation pipeline. Empirical experiments were conducted using a real-world indoor dataset collected by a Limo Pro robot, with no scene-specific fine-tuning performed on the models throughout the process. The results demonstrate that MA-CoNav comprehensively outperforms existing mainstream VLN methods across multiple metrics.

