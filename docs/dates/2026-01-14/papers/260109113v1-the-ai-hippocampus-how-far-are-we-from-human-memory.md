---
layout: default
title: The AI Hippocampus: How Far are We From Human Memory?
---

# The AI Hippocampus: How Far are We From Human Memory?
**arXiv**：[2601.09113v1](https://arxiv.org/abs/2601.09113) · [PDF](https://arxiv.org/pdf/2601.09113.pdf)  
**作者**：Zixia Jia, Jiaqi Li, Yipeng Kang, Yuxuan Wang, Tong Wu, Quansen Wang, Xiaobo Wang, Shuyi Zhang, Junzhe Shen, Qing Li, Siyuan Qi, Yitao Liang, Di He, Zilong Zheng, Song-Chun Zhu  

**一句话要点**：综述LLMs与MLLMs中的记忆机制，提出隐式、显式和代理记忆分类框架。

**关键词**：记忆机制, 大语言模型, 多模态大语言模型, 隐式记忆, 显式记忆, 代理记忆

## 3 点简述
- 核心问题：记忆机制如何增强大语言模型和多模态大语言模型的推理、适应性和上下文保真度。
- 方法要点：将记忆分为隐式（内部参数）、显式（外部存储）和代理（自主代理持久结构）三类。
- 实验或效果：讨论架构进展、基准任务及容量、对齐、事实一致性等开放挑战。

## 摘要（原文）

> Memory plays a foundational role in augmenting the reasoning, adaptability, and contextual fidelity of modern Large Language Models and Multi-Modal LLMs. As these models transition from static predictors to interactive systems capable of continual learning and personalized inference, the incorporation of memory mechanisms has emerged as a central theme in their architectural and functional evolution. This survey presents a comprehensive and structured synthesis of memory in LLMs and MLLMs, organizing the literature into a cohesive taxonomy comprising implicit, explicit, and agentic memory paradigms. Specifically, the survey delineates three primary memory frameworks. Implicit memory refers to the knowledge embedded within the internal parameters of pre-trained transformers, encompassing their capacity for memorization, associative retrieval, and contextual reasoning. Recent work has explored methods to interpret, manipulate, and reconfigure this latent memory. Explicit memory involves external storage and retrieval components designed to augment model outputs with dynamic, queryable knowledge representations, such as textual corpora, dense vectors, and graph-based structures, thereby enabling scalable and updatable interaction with information sources. Agentic memory introduces persistent, temporally extended memory structures within autonomous agents, facilitating long-term planning, self-consistency, and collaborative behavior in multi-agent systems, with relevance to embodied and interactive AI. Extending beyond text, the survey examines the integration of memory within multi-modal settings, where coherence across vision, language, audio, and action modalities is essential. Key architectural advances, benchmark tasks, and open challenges are discussed, including issues related to memory capacity, alignment, factual consistency, and cross-system interoperability.

