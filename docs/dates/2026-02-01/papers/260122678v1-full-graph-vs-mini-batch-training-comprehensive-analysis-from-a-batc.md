---
layout: default
title: Full-Graph vs. Mini-Batch Training: Comprehensive Analysis from a Batch Size and Fan-Out Size Perspective
---

# Full-Graph vs. Mini-Batch Training: Comprehensive Analysis from a Batch Size and Fan-Out Size Perspective
**arXiv**：[2601.22678v1](https://arxiv.org/abs/2601.22678) · [PDF](https://arxiv.org/pdf/2601.22678.pdf)  
**作者**：Mengfan Liu, Da Zheng, Junwei Su, Chuan Wu  

**一句话要点**：从批大小和扇出大小视角系统分析全图与迷你批训练，揭示非各向同性效应并提供调参指导

**关键词**：图神经网络训练, 批大小分析, 扇出大小, 泛化理论, 计算效率, 超参数调优

## 3 点简述
- 核心问题：比较全图与迷你批GNN训练的性能和效率，批大小和扇出大小影响未充分探索
- 方法要点：使用Wasserstein距离进行泛化分析，研究图结构特别是扇出大小的影响
- 实验或效果：发现批大小和扇出大小在收敛和泛化中的非各向同性效应，全图训练不一定优于调优迷你批

## 摘要（原文）

> Full-graph and mini-batch Graph Neural Network (GNN) training approaches have distinct system design demands, making it crucial to choose the appropriate approach to develop. A core challenge in comparing these two GNN training approaches lies in characterizing their model performance (i.e., convergence and generalization) and computational efficiency. While a batch size has been an effective lens in analyzing such behaviors in deep neural networks (DNNs), GNNs extend this lens by introducing a fan-out size, as full-graph training can be viewed as mini-batch training with the largest possible batch size and fan-out size. However, the impact of the batch and fan-out size for GNNs remains insufficiently explored. To this end, this paper systematically compares full-graph vs. mini-batch training of GNNs through empirical and theoretical analyses from the view points of the batch size and fan-out size. Our key contributions include: 1) We provide a novel generalization analysis using the Wasserstein distance to study the impact of the graph structure, especially the fan-out size. 2) We uncover the non-isotropic effects of the batch size and the fan-out size in GNN convergence and generalization, providing practical guidance for tuning these hyperparameters under resource constraints. Finally, full-graph training does not always yield better model performance or computational efficiency than well-tuned smaller mini-batch settings. The implementation can be found in the github link: https://github.com/LIUMENGFAN-gif/GNN_fullgraph_minibatch_training.

