---
layout: default
title: DyGnROLE: Modeling Asymmetry in Dynamic Graphs with Node-Role-Oriented Latent Encoding
---

# DyGnROLE: Modeling Asymmetry in Dynamic Graphs with Node-Role-Oriented Latent Encoding
**arXiv**：[2602.23135v1](https://arxiv.org/abs/2602.23135) · [PDF](https://arxiv.org/pdf/2602.23135.pdf)  
**作者**：Tyler Bonnet, Marek Rei  

**一句话要点**：提出DyGnROLE以解决动态图中节点角色不对称建模问题

**关键词**：动态图学习, 节点角色建模, Transformer架构, 自监督预训练, 边分类

## 3 点简述
- 核心问题：现有动态图模型缺乏对源节点和目标节点不对称行为的系统建模
- 方法要点：基于Transformer，使用分离嵌入和角色语义位置编码来解耦节点表示
- 实验或效果：在未标注数据上通过自监督预训练，未来边分类任务中显著优于基线

## 摘要（原文）

> Real-world dynamic graphs are often directed, with source and destination nodes exhibiting asymmetrical behavioral patterns and temporal dynamics. However, existing dynamic graph architectures largely rely on shared parameters for processing source and destination nodes, with limited or no systematic role-aware modeling. We propose DyGnROLE (Dynamic Graph Node-Role-Oriented Latent Encoding), a transformer-based architecture that explicitly disentangles source and destination representations. By using separate embedding vocabularies and role-semantic positional encodings, the model captures the distinct structural and temporal contexts unique to each role. Critical to the effectiveness of these specialized embeddings in low-label regimes is a self-supervised pretraining objective we introduce: Temporal Contrastive Link Prediction (TCLP). The pretraining uses the full unlabeled interaction history to encode informative structural biases, enabling the model to learn role-specific representations without requiring annotated data. Evaluation on future edge classification demonstrates that DyGnROLE substantially outperforms a diverse set of state-of-the-art baselines, establishing role-aware modeling as an effective strategy for dynamic graph learning.

