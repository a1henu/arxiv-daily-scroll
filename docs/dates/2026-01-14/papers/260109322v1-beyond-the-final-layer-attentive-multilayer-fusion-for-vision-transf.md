---
layout: default
title: Beyond the final layer: Attentive multilayer fusion for vision transformers
---

# Beyond the final layer: Attentive multilayer fusion for vision transformers
**arXiv**：[2601.09322v1](https://arxiv.org/abs/2601.09322) · [PDF](https://arxiv.org/pdf/2601.09322.pdf)  
**作者**：Laure Ciernik, Marco Morik, Lukas Thede, Luca Eyring, Shinichi Nakajima, Zeynep Akata, Lukas Muttenthaler  

**一句话要点**：提出多层注意力融合方法，以提升视觉Transformer在下游任务中的线性探测性能。

**关键词**：视觉Transformer, 线性探测, 多层融合, 注意力机制, 下游任务适应

## 3 点简述
- 核心问题：线性探测仅利用最后一层表示，忽略了任务相关信息在网络层次中的分布。
- 方法要点：通过注意力机制动态融合所有层表示，学习识别任务相关层并组合低层结构线索与高层语义抽象。
- 实验或效果：在20个数据集和多个预训练模型上，相比标准线性探测获得一致显著提升。

## 摘要（原文）

> With the rise of large-scale foundation models, efficiently adapting them to downstream tasks remains a central challenge. Linear probing, which freezes the backbone and trains a lightweight head, is computationally efficient but often restricted to last-layer representations. We show that task-relevant information is distributed across the network hierarchy rather than solely encoded in any of the last layers. To leverage this distribution of information, we apply an attentive probing mechanism that dynamically fuses representations from all layers of a Vision Transformer. This mechanism learns to identify the most relevant layers for a target task and combines low-level structural cues with high-level semantic abstractions. Across 20 diverse datasets and multiple pretrained foundation models, our method achieves consistent, substantial gains over standard linear probes. Attention heatmaps further reveal that tasks different from the pre-training domain benefit most from intermediate representations. Overall, our findings underscore the value of intermediate layer information and demonstrate a principled, task aware approach for unlocking their potential in probing-based adaptation.

