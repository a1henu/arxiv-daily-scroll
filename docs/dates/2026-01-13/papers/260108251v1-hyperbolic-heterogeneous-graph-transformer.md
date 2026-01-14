---
layout: default
title: Hyperbolic Heterogeneous Graph Transformer
---

# Hyperbolic Heterogeneous Graph Transformer
**arXiv**：[2601.08251v1](https://arxiv.org/abs/2601.08251) · [PDF](https://arxiv.org/pdf/2601.08251.pdf)  
**作者**：Jongmin Park, Seunghoon Han, Hyewon Lee, Won-Yong Shin, Sungsu Lim  

**一句话要点**：提出双曲异构图变换器以解决异构图表示学习中全局依赖捕获与计算效率问题

**关键词**：异构图表示学习, 双曲几何, 图变换器, 注意力机制, 节点分类

## 3 点简述
- 核心问题：现有双曲异构图方法依赖切空间操作导致映射失真，且消息传递架构难以捕获全局层次结构和长程依赖
- 方法要点：HypHGT完全在双曲空间中运行，基于变换器架构捕获局部和全局依赖，并引入关系特定双曲注意力机制实现线性时间复杂度
- 实验或效果：在节点分类任务中性能优于现有方法，同时显著减少训练时间和内存使用

## 摘要（原文）

> In heterogeneous graphs, we can observe complex structures such as tree-like or hierarchical structures. Recently, the hyperbolic space has been widely adopted in many studies to effectively learn these complex structures. Although these methods have demonstrated the advantages of the hyperbolic space in learning heterogeneous graphs, most existing methods still have several challenges. They rely heavily on tangent-space operations, which often lead to mapping distortions during frequent transitions. Moreover, their message-passing architectures mainly focus on local neighborhood information, making it difficult to capture global hierarchical structures and long-range dependencies between different types of nodes. To address these limitations, we propose Hyperbolic Heterogeneous Graph Transformer (HypHGT), which effectively and efficiently learns heterogeneous graph representations entirely within the hyperbolic space. Unlike previous message-passing based hyperbolic heterogeneous GNNs, HypHGT naturally captures both local and global dependencies through transformer-based architecture. Furthermore, the proposed relation-specific hyperbolic attention mechanism in HypHGT, which operates with linear time complexity, enables efficient computation while preserving the heterogeneous information across different relation types. This design allows HypHGT to effectively capture the complex structural properties and semantic information inherent in heterogeneous graphs. We conduct comprehensive experiments to evaluate the effectiveness and efficiency of HypHGT, and the results demonstrate that it consistently outperforms state-of-the-art methods in node classification task, with significantly reduced training time and memory usage.

