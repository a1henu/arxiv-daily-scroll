---
layout: default
title: Cumulative Path-Level Semantic Reasoning for Inductive Knowledge Graph Completion
---

# Cumulative Path-Level Semantic Reasoning for Inductive Knowledge Graph Completion
**arXiv**：[2601.05629v1](https://arxiv.org/abs/2601.05629) · [PDF](https://arxiv.org/pdf/2601.05629.pdf)  
**作者**：Jiapu Wang, Xinghe Cheng, Zezheng Wu, Ruiqi Ma, Rui Wang, Zhichao Yan, Haoran Luo, Yuhao Jiang, Kai Sun  

**一句话要点**：提出CPSR框架以解决归纳知识图谱补全中的噪声结构和长距离依赖问题

**关键词**：归纳知识图谱补全, 路径级语义推理, 噪声结构过滤, 全局语义评分, 动态适应性

## 3 点简述
- 核心问题：现有归纳KGC方法易受噪声结构干扰且难以捕获推理路径的长距离依赖
- 方法要点：采用查询依赖掩码模块自适应过滤噪声，并引入全局语义评分模块评估路径节点贡献
- 实验或效果：实验结果显示CPSR在归纳KGC任务上达到最先进性能

## 摘要（原文）

> Conventional Knowledge Graph Completion (KGC) methods aim to infer missing information in incomplete Knowledge Graphs (KGs) by leveraging existing information, which struggle to perform effectively in scenarios involving emerging entities. Inductive KGC methods can handle the emerging entities and relations in KGs, offering greater dynamic adaptability. While existing inductive KGC methods have achieved some success, they also face challenges, such as susceptibility to noisy structural information during reasoning and difficulty in capturing long-range dependencies in reasoning paths. To address these challenges, this paper proposes the Cumulative Path-Level Semantic Reasoning for inductive knowledge graph completion (CPSR) framework, which simultaneously captures both the structural and semantic information of KGs to enhance the inductive KGC task. Specifically, the proposed CPSR employs a query-dependent masking module to adaptively mask noisy structural information while retaining important information closely related to the targets. Additionally, CPSR introduces a global semantic scoring module that evaluates both the individual contributions and the collective impact of nodes along the reasoning path within KGs. The experimental results demonstrate that CPSR achieves state-of-the-art performance.

