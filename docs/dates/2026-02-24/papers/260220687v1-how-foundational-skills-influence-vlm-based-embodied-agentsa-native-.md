---
layout: default
title: How Foundational Skills Influence VLM-based Embodied Agents:A Native Perspective
---

# How Foundational Skills Influence VLM-based Embodied Agents:A Native Perspective
**arXiv**：[2602.20687v1](https://arxiv.org/abs/2602.20687) · [PDF](https://arxiv.org/pdf/2602.20687.pdf)  
**作者**：Bo Peng, Pi Bu, Keyu Pan, Xinrun Xu, Yinxiu Zhao, Miao Chen, Yang Du, Lin Li, Jun Song, Tong Xu  

**一句话要点**：提出NativeEmbodied基准，以原生低层动作空间评估VLM驱动的具身智能体

**关键词**：具身智能体, 视觉语言模型, 基准评估, 低层动作空间, 技能解耦, 模拟场景

## 3 点简述
- 现有基准依赖高层命令或离散动作空间，与真实控制差异大，缺乏高低层联合评估
- 构建NativeEmbodied基准，使用统一原生低层动作空间，包含高层任务和低层技能任务
- 实验揭示当前VLM在基础技能上存在缺陷，这些瓶颈显著限制高层任务性能

## 摘要（原文）

> Recent advances in vision-language models (VLMs) have shown promise for human-level embodied intelligence. However, existing benchmarks for VLM-driven embodied agents often rely on high-level commands or discretized action spaces, which are non-native settings that differ markedly from real-world control. In addition, current benchmarks focus primarily on high-level tasks and lack joint evaluation and analysis at both low and high levels. To address these limitations, we present NativeEmbodied, a challenging benchmark for VLM-driven embodied agents that uses a unified, native low-level action space. Built on diverse simulated scenes, NativeEmbodied includes three representative high-level tasks in complex scenarios to evaluate overall performance. For more detailed analysis, we further decouple the skills required by complex tasks and construct four types of low-level tasks, each targeting a fundamental embodied skill. This joint evaluation across task and skill granularities enables fine-grained assessment of embodied agents. Experiments with state-of-the-art VLMs reveal clear deficiencies in several fundamental embodied skills, and further analysis shows that these bottlenecks significantly limit performance on high-level tasks. NativeEmbodied highlights key challenges for current VLM-driven embodied agents and provides insights to guide future research.

