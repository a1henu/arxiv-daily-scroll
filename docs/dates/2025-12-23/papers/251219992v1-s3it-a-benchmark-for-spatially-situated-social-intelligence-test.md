---
layout: default
title: S$^3$IT: A Benchmark for Spatially Situated Social Intelligence Test
---

# S$^3$IT: A Benchmark for Spatially Situated Social Intelligence Test
**arXiv**：[2512.19992v1](https://arxiv.org/abs/2512.19992) · [PDF](https://arxiv.org/pdf/2512.19992.pdf)  
**作者**：Zhe Sun, Xueyuan Yang, Yujie Lu, Zhenliang Zhang  

**一句话要点**：提出S^3IT基准以评估具身社交智能，通过座位排序任务整合物理与社交约束。

**关键词**：具身社交智能, 基准测试, 座位排序任务, 多目标优化, 大语言模型评估, 空间智能

## 3 点简述
- 核心问题：现有评估无法整合具身社交智能，缺乏物理与社交约束的联合推理。
- 方法要点：设计可扩展框架，生成多样场景，要求代理通过对话、探索和优化完成任务。
- 实验或效果：评估先进大语言模型，发现其在空间智能方面存在不足，但在文本线索冲突解决中接近人类水平。

## 摘要（原文）

> The integration of embodied agents into human environments demands embodied social intelligence: reasoning over both social norms and physical constraints. However, existing evaluations fail to address this integration, as they are limited to either disembodied social reasoning (e.g., in text) or socially-agnostic physical tasks. Both approaches fail to assess an agent's ability to integrate and trade off both physical and social constraints within a realistic, embodied context. To address this challenge, we introduce Spatially Situated Social Intelligence Test (S$^{3}$IT), a benchmark specifically designed to evaluate embodied social intelligence. It is centered on a novel and challenging seat-ordering task, requiring an agent to arrange seating in a 3D environment for a group of large language model-driven (LLM-driven) NPCs with diverse identities, preferences, and intricate interpersonal relationships. Our procedurally extensible framework generates a vast and diverse scenario space with controllable difficulty, compelling the agent to acquire preferences through active dialogue, perceive the environment via autonomous exploration, and perform multi-objective optimization within a complex constraint network. We evaluate state-of-the-art LLMs on S$^{3}$IT and found that they still struggle with this problem, showing an obvious gap compared with the human baseline. Results imply that LLMs have deficiencies in spatial intelligence, yet simultaneously demonstrate their ability to achieve near human-level competence in resolving conflicts that possess explicit textual cues.

