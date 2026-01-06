---
layout: default
title: CausalNav: A Long-term Embodied Navigation System for Autonomous Mobile Robots in Dynamic Outdoor Scenarios
---

# CausalNav: A Long-term Embodied Navigation System for Autonomous Mobile Robots in Dynamic Outdoor Scenarios
**arXiv**：[2601.01872v1](https://arxiv.org/abs/2601.01872) · [PDF](https://arxiv.org/pdf/2601.01872.pdf)  
**作者**：Hongbo Duan, Shangyi Luo, Zhiyuan Deng, Yanbo Chen, Yuanhao Chiang, Yi Liu, Fangming Liu, Xueqian Wang  

**一句话要点**：提出CausalNav，首个基于场景图的语义导航框架，用于动态户外环境中的自主移动机器人。

**关键词**：语义导航, 场景图, 动态户外环境, 检索增强生成, 长期稳定性, 自主移动机器人

## 3 点简述
- 核心问题：户外大规模环境中的自主语言导航面临语义推理、动态条件和长期稳定性挑战。
- 方法要点：利用LLM构建多级语义场景图（Embodied Graph），结合RAG实现开放词汇查询下的语义导航和长程规划。
- 实验或效果：在仿真和真实世界实验中展示出优越的鲁棒性和效率。

## 摘要（原文）

> Autonomous language-guided navigation in large-scale outdoor environments remains a key challenge in mobile robotics, due to difficulties in semantic reasoning, dynamic conditions, and long-term stability. We propose CausalNav, the first scene graph-based semantic navigation framework tailored for dynamic outdoor environments. We construct a multi-level semantic scene graph using LLMs, referred to as the Embodied Graph, that hierarchically integrates coarse-grained map data with fine-grained object entities. The constructed graph serves as a retrievable knowledge base for Retrieval-Augmented Generation (RAG), enabling semantic navigation and long-range planning under open-vocabulary queries. By fusing real-time perception with offline map data, the Embodied Graph supports robust navigation across varying spatial granularities in dynamic outdoor environments. Dynamic objects are explicitly handled in both the scene graph construction and hierarchical planning modules. The Embodied Graph is continuously updated within a temporal window to reflect environmental changes and support real-time semantic navigation. Extensive experiments in both simulation and real-world settings demonstrate superior robustness and efficiency.

