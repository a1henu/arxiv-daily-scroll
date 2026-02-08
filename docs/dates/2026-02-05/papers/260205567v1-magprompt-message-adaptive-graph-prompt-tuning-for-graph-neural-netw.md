---
layout: default
title: MAGPrompt: Message-Adaptive Graph Prompt Tuning for Graph Neural Networks
---

# MAGPrompt: Message-Adaptive Graph Prompt Tuning for Graph Neural Networks
**arXiv**：[2602.05567v1](https://arxiv.org/abs/2602.05567) · [PDF](https://arxiv.org/pdf/2602.05567.pdf)  
**作者**：Long D. Nguyen, Binh P. Nguyen  

**一句话要点**：提出消息自适应图提示调优方法，以增强图神经网络在下游任务中的适应性。

**关键词**：图神经网络, 提示调优, 消息传递, 参数高效, 下游任务适应

## 3 点简述
- 核心问题：预训练图神经网络在下游任务中因目标不匹配而适应性受限，现有图提示方法未充分调整邻居交互。
- 方法要点：在消息传递步骤注入可学习提示，重加权邻居消息并添加任务特定向量，保持骨干网络冻结。
- 实验或效果：在少样本设置中优于先前图提示方法，在全样本设置中性能与微调相当。

## 摘要（原文）

> Pre-trained graph neural networks (GNNs) transfer well, but adapting them to downstream tasks remains challenging due to mismatches between pre-training objectives and task requirements. Graph prompt tuning offers a parameter-efficient alternative to fine-tuning, yet most methods only modify inputs or representations and leave message passing unchanged, limiting their ability to adapt neighborhood interactions. We propose message-adaptive graph prompt tuning, which injects learnable prompts into the message passing step to reweight incoming neighbor messages and add task-specific prompt vectors during message aggregation, while keeping the backbone GNN frozen. The approach is compatible with common GNN backbones and pre-training strategies, and applicable across downstream settings. Experiments on diverse node- and graph-level datasets show consistent gains over prior graph prompting methods in few-shot settings, while achieving performance competitive with fine-tuning in full-shot regimes.

