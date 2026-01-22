---
layout: default
title: M2I2HA: A Multi-modal Object Detection Method Based on Intra- and Inter-Modal Hypergraph Attention
---

# M2I2HA: A Multi-modal Object Detection Method Based on Intra- and Inter-Modal Hypergraph Attention
**arXiv**：[2601.14776v1](https://arxiv.org/abs/2601.14776) · [PDF](https://arxiv.org/pdf/2601.14776.pdf)  
**作者**：Xiaofan Yang, Yubin Liu, Wei Pan, Guoqing Chu, Junming Zhang, Jie Zhao, Zhuoqi Man, Xuanming Cao  

**一句话要点**：提出基于超图注意力的多模态目标检测方法M2I2HA，以解决模态内外高阶关系建模与跨模态对齐问题。

**关键词**：多模态目标检测, 超图注意力, 跨模态融合, 高阶关系建模, 自适应融合

## 3 点简述
- 核心问题：现有方法在模态内外信息提取、跨模态对齐及高阶依赖建模方面存在局限，如CNN感受野受限、Transformer计算复杂度高、SSM破坏空间结构。
- 方法要点：引入超图理论，设计模态内超图增强模块捕获全局多对多高阶关系，模态间超图融合模块对齐并融合跨模态特征，M2-FullPAD模块实现自适应多级融合。
- 实验或效果：在多个公开数据集上进行目标检测实验，相比基线方法，M2I2HA在多模态目标检测任务中达到最先进性能。

## 摘要（原文）

> Recent advances in multi-modal detection have significantly improved detection accuracy in challenging environments (e.g., low light, overexposure). By integrating RGB with modalities such as thermal and depth, multi-modal fusion increases data redundancy and system robustness. However, significant challenges remain in effectively extracting task-relevant information both within and across modalities, as well as in achieving precise cross-modal alignment. While CNNs excel at feature extraction, they are limited by constrained receptive fields, strong inductive biases, and difficulty in capturing long-range dependencies. Transformer-based models offer global context but suffer from quadratic computational complexity and are confined to pairwise correlation modeling. Mamba and other State Space Models (SSMs), on the other hand, are hindered by their sequential scanning mechanism, which flattens 2D spatial structures into 1D sequences, disrupting topological relationships and limiting the modeling of complex higher-order dependencies. To address these issues, we propose a multi-modal perception network based on hypergraph theory called M2I2HA. Our architecture includes an Intra-Hypergraph Enhancement module to capture global many-to-many high-order relationships within each modality, and an Inter-Hypergraph Fusion module to align, enhance, and fuse cross-modal features by bridging configuration and spatial gaps between data sources. We further introduce a M2-FullPAD module to enable adaptive multi-level fusion of multi-modal enhanced features within the network, meanwhile enhancing data distribution and flow across the architecture. Extensive object detection experiments on multiple public datasets against baselines demonstrate that M2I2HA achieves state-of-the-art performance in multi-modal object detection tasks.

