---
layout: default
title: AGSP-DSA: An Adaptive Graph Signal Processing Framework for Robust Multimodal Fusion with Dynamic Semantic Alignment
---

# AGSP-DSA: An Adaptive Graph Signal Processing Framework for Robust Multimodal Fusion with Dynamic Semantic Alignment
**arXiv**：[2601.18589v1](https://arxiv.org/abs/2601.18589) · [PDF](https://arxiv.org/pdf/2601.18589.pdf)  
**作者**：KV Karthikeya, Ashok Kumar Das, Shantanu Pal, Vivekananda Bhat K, Arun Sekar Rajasekaran  

**一句话要点**：提出AGSP-DSA框架，通过自适应图信号处理与动态语义对齐实现鲁棒多模态融合。

**关键词**：多模态融合, 图信号处理, 动态语义对齐, 鲁棒学习, 情感分析

## 3 点简述
- 核心问题：异构多模态数据融合中，如何动态对齐语义并提升鲁棒性。
- 方法要点：采用双图构建学习模态内外关系，结合谱图滤波与多尺度GCN增强信号。
- 实验效果：在CMU-MOSEI等数据集上达到SOTA，准确率最高95.3%，缺失模态下表现稳健。

## 摘要（原文）

> In this paper, we introduce an Adaptive Graph Signal Processing with Dynamic Semantic Alignment (AGSP DSA) framework to perform robust multimodal data fusion over heterogeneous sources, including text, audio, and images. The requested approach uses a dual-graph construction to learn both intra-modal and inter-modal relations, spectral graph filtering to boost the informative signals, and effective node embedding with Multi-scale Graph Convolutional Networks (GCNs). Semantic aware attention mechanism: each modality may dynamically contribute to the context with respect to contextual relevance. The experimental outcomes on three benchmark datasets, including CMU-MOSEI, AVE, and MM-IMDB, show that AGSP-DSA performs as the state of the art. More precisely, it achieves 95.3% accuracy, 0.936 F1-score, and 0.924 mAP on CMU-MOSEI, improving MM-GNN by 2.6 percent in accuracy. It gets 93.4% accuracy and 0.911 F1-score on AVE and 91.8% accuracy and 0.886 F1-score on MM-IMDB, which demonstrate good generalization and robustness in the missing modality setting. These findings verify the efficiency of AGSP-DSA in promoting multimodal learning in sentiment analysis, event recognition and multimedia classification.

