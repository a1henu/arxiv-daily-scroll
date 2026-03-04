---
layout: default
title: SPARC: Spatial-Aware Path Planning via Attentive Robot Communication
---

# SPARC: Spatial-Aware Path Planning via Attentive Robot Communication
**arXiv**：[2603.02845v1](https://arxiv.org/abs/2603.02845) · [PDF](https://arxiv.org/pdf/2603.02845.pdf)  
**作者**：Sayang Mu, Xiangyu Wu, Bo An  

**一句话要点**：提出关系增强多头注意力机制，以解决多机器人路径规划中空间邻近性忽略导致的通信效率低下问题。

**关键词**：多机器人路径规划, 图注意力机制, 多头注意力, 通信优化, 协作决策

## 3 点简述
- 核心问题：现有学习通信方法在去中心化多机器人路径规划中忽视空间邻近性，导致拥堵区域协调不足。
- 方法要点：通过嵌入曼哈顿距离到注意力权重计算，动态优先处理空间相关邻居消息，结合距离约束掩码和GRU门控融合。
- 实验或效果：在40x40网格上从8个训练机器人零样本泛化到128个测试机器人，在30%障碍密度下成功率约75%，优于基线超过25个百分点。

## 摘要（原文）

> Efficient communication is critical for decentralized Multi-Robot Path Planning (MRPP), yet existing learned communication methods treat all neighboring robots equally regardless of their spatial proximity, leading to diluted attention in congested regions where coordination matters most. We propose Relation enhanced Multi Head Attention (RMHA), a communication mechanism that explicitly embeds pairwise Manhattan distances into the attention weight computation, enabling each robot to dynamically prioritize messages from spatially relevant neighbors. Combined with a distance-constrained attention mask and GRU gated message fusion, RMHA integrates seamlessly with MAPPO for stable end-to-end training. In zero-shot generalization from 8 training robots to 128 test robots on 40x40 grids, RMHA achieves approximately 75 percent success rate at 30 percent obstacle density outperforming the best baseline by over 25 percentage points. Ablation studies confirm that distance-relation encoding is the key contributor to success rate improvement in high-density environments. Index Terms-Multi-robot path planning, graph attention mechanism, multi-head attention, communication optimization, cooperative decision-making

