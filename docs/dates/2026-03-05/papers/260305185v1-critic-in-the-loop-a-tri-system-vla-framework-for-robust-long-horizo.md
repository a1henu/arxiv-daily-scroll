---
layout: default
title: Critic in the Loop: A Tri-System VLA Framework for Robust Long-Horizon Manipulation
---

# Critic in the Loop: A Tri-System VLA Framework for Robust Long-Horizon Manipulation
**arXiv**：[2603.05185v1](https://arxiv.org/abs/2603.05185) · [PDF](https://arxiv.org/pdf/2603.05185.pdf)  
**作者**：Pengfei Yi, Yingjie Ma, Wenjiang Xu, Yanan Hao, Shuai Gan, Wanting Li, Shanlin Zhong  

**一句话要点**：提出Critic in the Loop框架，通过动态调度VLM和VLA以解决长时程机器人操作中的语义推理与实时控制平衡问题。

**关键词**：视觉语言模型, 机器人操作, 动态调度, 长时程任务, 鲁棒性增强, 仿生架构

## 3 点简述
- 核心问题：视觉机器人操作中，高语义推理与低层实时控制难以平衡，VLM延迟高而VLA语义深度不足。
- 方法要点：采用仿生三系统架构，包括VLM大脑、VLA小脑和轻量视觉Critic，Critic动态监控并调度控制权。
- 实验或效果：在长时程操作基准测试中实现先进性能，增强OOD场景下的鲁棒性和自主性。

## 摘要（原文）

> Balancing high-level semantic reasoning with low-level reactive control remains a core challenge in visual robotic manipulation. While Vision-Language Models (VLMs) excel at cognitive planning, their inference latency precludes real-time execution. Conversely, fast Vision-Language-Action (VLA) models often lack the semantic depth required for complex, long-horizon tasks. To bridge this gap, we introduce Critic in the Loop, an adaptive hierarchical framework driven by dynamic VLM-Expert scheduling. At its core is a bionic Tri-System architecture comprising a VLM brain for global reasoning, a VLA cerebellum for reactive execution, and a lightweight visual Critic. By continuously monitoring the workspace, the Critic dynamically routes control authority. It sustains rapid closed-loop execution via the VLA for routine subtasks, and adaptively triggers the VLM for replanning upon detecting execution anomalies such as task stagnation or failures. Furthermore, our architecture seamlessly integrates human-inspired rules to intuitively break infinite retry loops. This visually-grounded scheduling minimizes expensive VLM queries, while substantially enhancing system robustness and autonomy in out-of-distribution (OOD) scenarios. Comprehensive experiments on challenging, long-horizon manipulation benchmarks reveal that our approach achieves state-of-the-art performance.

