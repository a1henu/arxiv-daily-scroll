---
layout: default
title: Decoder-Free Supervoxel GNN for Accurate Brain-Tumor Localization in Multi-Modal MRI
---

# Decoder-Free Supervoxel GNN for Accurate Brain-Tumor Localization in Multi-Modal MRI
**arXiv**：[2601.14055v1](https://arxiv.org/abs/2601.14055) · [PDF](https://arxiv.org/pdf/2601.14055.pdf)  
**作者**：Andrea Protani, Marc Molina Van Den Bosch, Lorenzo Giusti, Heloisa Barbosa Da Silva, Paolo Cacace, Albert Sund Aillet, Miguel Angel Gonzalez Ballester, Friedhelm Hummel, Luigi Serio  

**一句话要点**：提出解码器自由的超体素图神经网络，用于多模态MRI中脑肿瘤的精准定位。

**关键词**：3D医学影像, 图神经网络, 超体素分割, 脑肿瘤定位, 多模态MRI, 解码器自由架构

## 3 点简述
- 核心问题：传统3D医学影像模型参数冗余，过多用于空间重建而非特征学习。
- 方法要点：通过内容感知分组构建语义图，结合Transformer和图注意力网络进行分层编码。
- 实验或效果：在BraTS数据集上，分类模型F1分数0.875，回归模型MAE 0.028，验证了框架的有效性。

## 摘要（原文）

> Modern vision backbones for 3D medical imaging typically process dense voxel grids through parameter-heavy encoder-decoder structures, a design that allocates a significant portion of its parameters to spatial reconstruction rather than feature learning. Our approach introduces SVGFormer, a decoder-free pipeline built upon a content-aware grouping stage that partitions the volume into a semantic graph of supervoxels. Its hierarchical encoder learns rich node representations by combining a patch-level Transformer with a supervoxel-level Graph Attention Network, jointly modeling fine-grained intra-region features and broader inter-regional dependencies. This design concentrates all learnable capacity on feature encoding and provides inherent, dual-scale explainability from the patch to the region level. To validate the framework's flexibility, we trained two specialized models on the BraTS dataset: one for node-level classification and one for tumor proportion regression. Both models achieved strong performance, with the classification model achieving a F1-score of 0.875 and the regression model a MAE of 0.028, confirming the encoder's ability to learn discriminative and localized features. Our results establish that a graph-based, encoder-only paradigm offers an accurate and inherently interpretable alternative for 3D medical image representation.

