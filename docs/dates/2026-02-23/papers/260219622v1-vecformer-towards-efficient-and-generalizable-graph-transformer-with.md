---
layout: default
title: VecFormer: Towards Efficient and Generalizable Graph Transformer with Graph Token Attention
---

# VecFormer: Towards Efficient and Generalizable Graph Transformer with Graph Token Attention
**arXiv**：[2602.19622v1](https://arxiv.org/abs/2602.19622) · [PDF](https://arxiv.org/pdf/2602.19622.pdf)  
**作者**：Jingbo Zhou, Jun Xia, Siyuan Li, Yunfan Liu, Wenjun Wang, Yufei Huang, Changxi Chi, Mutian Hong, Zhuoli Ouyang, Shu Wang, Zhongqi Wang, Xingyu Wu, Chang Yu, Stan Z. Li  

**一句话要点**：提出VecFormer以解决图Transformer的计算复杂度和泛化性能问题

**关键词**：图Transformer, 向量量化, 泛化性能, 节点分类, 计算效率, 图表示学习

## 3 点简述
- 现有图Transformer面临计算复杂度指数增长和泛化性能差的问题
- VecFormer采用两阶段训练，通过代码本重构节点特征和图结构学习Graph Codes
- 实验表明VecFormer在性能和速度上优于现有模型，尤其在OOD场景

## 摘要（原文）

> Graph Transformer has demonstrated impressive capabilities in the field of graph representation learning. However, existing approaches face two critical challenges: (1) most models suffer from exponentially increasing computational complexity, making it difficult to scale to large graphs; (2) attention mechanisms based on node-level operations limit the flexibility of the model and result in poor generalization performance in out-of-distribution (OOD) scenarios. To address these issues, we propose \textbf{VecFormer} (the \textbf{Vec}tor Quantized Graph Trans\textbf{former}), an efficient and highly generalizable model for node classification, particularly under OOD settings. VecFormer adopts a two-stage training paradigm. In the first stage, two codebooks are used to reconstruct the node features and the graph structure, aiming to learn the rich semantic \texttt{Graph Codes}. In the second stage, attention mechanisms are performed at the \texttt{Graph Token} level based on the transformed cross codebook, reducing computational complexity while enhancing the model's generalization capability. Extensive experiments on datasets of various sizes demonstrate that VecFormer outperforms the existing Graph Transformer in both performance and speed.

