---
layout: default
title: Multimodal Graph Representation Learning with Dynamic Information Pathways
---

# Multimodal Graph Representation Learning with Dynamic Information Pathways
**arXiv**：[2603.09258v1](https://arxiv.org/abs/2603.09258) · [PDF](https://arxiv.org/pdf/2603.09258.pdf)  
**作者**：Xiaobin Hong, Mingkai Lin, Xiaoli Wang, Chaoqun Wang, Wenzhong Li  

**一句话要点**：提出动态信息路径框架以解决多模态图表示学习中的灵活性与表达性问题

**关键词**：多模态图表示学习, 动态信息路径, 伪节点交互, 稀疏消息传播, 线性复杂度, 链接预测

## 3 点简述
- 核心问题：现有方法依赖静态结构或密集注意力，限制多模态图节点嵌入的灵活学习
- 方法要点：引入模态特定伪节点，通过邻近引导交互和共享状态空间路径实现动态稀疏消息传播
- 实验或效果：在多个基准测试中，DiP在线性复杂度下优于基线，验证了链接预测和节点分类性能

## 摘要（原文）

> Multimodal graphs, where nodes contain heterogeneous features such as images and text, are increasingly common in real-world applications. Effectively learning on such graphs requires both adaptive intra-modal message passing and efficient inter-modal aggregation. However, most existing approaches to multimodal graph learning are typically extended from conventional graph neural networks and rely on static structures or dense attention, which limit flexibility and expressive node embedding learning. In this paper, we propose a novel multimodal graph representation learning framework with Dynamic information Pathways (DiP). By introducing modality-specific pseudo nodes, DiP enables dynamic message routing within each modality via proximity-guided pseudo-node interactions and captures inter-modality dependence through efficient information pathways in a shared state space. This design achieves adaptive, expressive, and sparse message propagation across modalities with linear complexity. We conduct the link prediction and node classification tasks to evaluate performance and carry out full experimental analyses. Extensive experiments across multiple benchmarks demonstrate that DiP consistently outperforms baselines.

