---
layout: default
title: Graph-based Agent Memory: Taxonomy, Techniques, and Applications
---

# Graph-based Agent Memory: Taxonomy, Techniques, and Applications
**arXiv**：[2602.05665v1](https://arxiv.org/abs/2602.05665) · [PDF](https://arxiv.org/pdf/2602.05665.pdf)  
**作者**：Chang Yang, Chuang Zhou, Yilin Xiao, Su Dong, Luyao Zhuang, Yujing Zhang, Zhu Wang, Zijin Hong, Zheng Yuan, Zhishang Xiang, Shengyuan Chen, Huachi Zhou, Qinggang Zhang, Ninghao Liu, Jinsong Su, Xinrun Wang, Yi Chang, Xiao Huang  

**一句话要点**：综述基于图的智能体记忆，涵盖分类、技术与应用，以支持长时复杂任务。

**关键词**：智能体记忆, 图结构, 长时任务, 知识积累, 自进化系统, 检索技术

## 3 点简述
- 核心问题：基于大语言模型的智能体在长时复杂任务中需要高效记忆模块以积累知识、推理和自进化。
- 方法要点：提出基于图的记忆分类，包括短期/长期、知识/经验、非结构/结构记忆，并分析提取、存储、检索和进化技术。
- 实验或效果：总结开源库和基准，支持自进化记忆的开发与评估，并探讨应用场景和未来方向。

## 摘要（原文）

> Memory emerges as the core module in the Large Language Model (LLM)-based agents for long-horizon complex tasks (e.g., multi-turn dialogue, game playing, scientific discovery), where memory can enable knowledge accumulation, iterative reasoning and self-evolution. Among diverse paradigms, graph stands out as a powerful structure for agent memory due to the intrinsic capabilities to model relational dependencies, organize hierarchical information, and support efficient retrieval. This survey presents a comprehensive review of agent memory from the graph-based perspective. First, we introduce a taxonomy of agent memory, including short-term vs. long-term memory, knowledge vs. experience memory, non-structural vs. structural memory, with an implementation view of graph-based memory. Second, according to the life cycle of agent memory, we systematically analyze the key techniques in graph-based agent memory, covering memory extraction for transforming the data into the contents, storage for organizing the data efficiently, retrieval for retrieving the relevant contents from memory to support reasoning, and evolution for updating the contents in the memory. Third, we summarize the open-sourced libraries and benchmarks that support the development and evaluation of self-evolving agent memory. We also explore diverse application scenarios. Finally, we identify critical challenges and future research directions. This survey aims to offer actionable insights to advance the development of more efficient and reliable graph-based agent memory systems. All the related resources, including research papers, open-source data, and projects, are collected for the community in https://github.com/DEEP-PolyU/Awesome-GraphMemory.

