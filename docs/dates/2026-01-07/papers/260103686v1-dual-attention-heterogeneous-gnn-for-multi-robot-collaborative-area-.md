---
layout: default
title: Dual-Attention Heterogeneous GNN for Multi-robot Collaborative Area Search via Deep Reinforcement Learning
---

# Dual-Attention Heterogeneous GNN for Multi-robot Collaborative Area Search via Deep Reinforcement Learning
**arXiv**：[2601.03686v1](https://arxiv.org/abs/2601.03686) · [PDF](https://arxiv.org/pdf/2601.03686.pdf)  
**作者**：Lina Zhu, Jiyu Cheng, Yuehu Liu, Wei Zhang  

**一句话要点**：提出双注意力异构图神经网络，通过深度强化学习解决多机器人协作区域搜索中的探索与覆盖平衡问题。

**关键词**：多机器人协作, 区域搜索, 异构图神经网络, 深度强化学习, 注意力机制, 模拟验证

## 3 点简述
- 核心问题：多机器人协作区域搜索中，动态平衡探索未知区域与覆盖特定救援目标的挑战。
- 方法要点：构建包含机器人、前沿点和兴趣点的异构图，采用关系感知和类型感知双注意力机制解耦任务。
- 实验或效果：在iGibson模拟器中基于Gibson和MatterPort3D数据集验证，展示优越的可扩展性和泛化能力。

## 摘要（原文）

> In multi-robot collaborative area search, a key challenge is to dynamically balance the two objectives of exploring unknown areas and covering specific targets to be rescued. Existing methods are often constrained by homogeneous graph representations, thus failing to model and balance these distinct tasks. To address this problem, we propose a Dual-Attention Heterogeneous Graph Neural Network (DA-HGNN) trained using deep reinforcement learning. Our method constructs a heterogeneous graph that incorporates three entity types: robot nodes, frontier nodes, and interesting nodes, as well as their historical states. The dual-attention mechanism comprises the relational-aware attention and type-aware attention operations. The relational-aware attention captures the complex spatio-temporal relationships among robots and candidate goals. Building on this relational-aware heterogeneous graph, the type-aware attention separately computes the relevance between robots and each goal type (frontiers vs. points of interest), thereby decoupling the exploration and coverage from the unified tasks. Extensive experiments conducted in interactive 3D scenarios within the iGibson simulator, leveraging the Gibson and MatterPort3D datasets, validate the superior scalability and generalization capability of the proposed approach.

