---
layout: default
title: UniManip: General-Purpose Zero-Shot Robotic Manipulation with Agentic Operational Graph
---

# UniManip: General-Purpose Zero-Shot Robotic Manipulation with Agentic Operational Graph
**arXiv**：[2602.13086v1](https://arxiv.org/abs/2602.13086) · [PDF](https://arxiv.org/pdf/2602.13086.pdf)  
**作者**：Haichao Liu, Yuanjiang Xue, Yuheng Zhou, Haoyuan Deng, Yinan Liang, Lihua Xie, Ziwei Wang  

**一句话要点**：提出UniManip框架，通过双层智能操作图实现零样本机器人操作泛化

**关键词**：机器人操作, 零样本泛化, 智能操作图, 语义推理, 物理基础, 动态规划

## 3 点简述
- 核心问题：现有方法在零样本泛化中面临语义与物理交互的脱节，导致长时任务精度不足或语义僵化。
- 方法要点：采用双层智能操作图，高层代理层协调任务，低层场景层动态表示状态，实现语义推理与物理基础的统一。
- 实验或效果：在未见物体和任务上验证零样本能力，相比先进基线成功率提升22.5%和25.0%，支持固定基座到移动操作的直接迁移。

## 摘要（原文）

> Achieving general-purpose robotic manipulation requires robots to seamlessly bridge high-level semantic intent with low-level physical interaction in unstructured environments. However, existing approaches falter in zero-shot generalization: end-to-end Vision-Language-Action (VLA) models often lack the precision required for long-horizon tasks, while traditional hierarchical planners suffer from semantic rigidity when facing open-world variations. To address this, we present UniManip, a framework grounded in a Bi-level Agentic Operational Graph (AOG) that unifies semantic reasoning and physical grounding. By coupling a high-level Agentic Layer for task orchestration with a low-level Scene Layer for dynamic state representation, the system continuously aligns abstract planning with geometric constraints, enabling robust zero-shot execution. Unlike static pipelines, UniManip operates as a dynamic agentic loop: it actively instantiates object-centric scene graphs from unstructured perception, parameterizes these representations into collision-free trajectories via a safety-aware local planner, and exploits structured memory to autonomously diagnose and recover from execution failures. Extensive experiments validate the system's robust zero-shot capability on unseen objects and tasks, demonstrating a 22.5% and 25.0% higher success rate compared to state-of-the-art VLA and hierarchical baselines, respectively. Notably, the system enables direct zero-shot transfer from fixed-base setups to mobile manipulation without fine-tuning or reconfiguration. Our open-source project page can be found at https://henryhcliu.github.io/unimanip.

