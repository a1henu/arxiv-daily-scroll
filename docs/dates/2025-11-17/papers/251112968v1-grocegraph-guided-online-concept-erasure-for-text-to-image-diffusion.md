---
layout: default
title: GrOCE:Graph-Guided Online Concept Erasure for Text-to-Image Diffusion Models
---

# GrOCE:Graph-Guided Online Concept Erasure for Text-to-Image Diffusion Models
**arXiv**：[2511.12968v1](https://arxiv.org/abs/2511.12968) · [PDF](https://arxiv.org/pdf/2511.12968.pdf)  
**作者**：Ning Han, Zhenyu Ge, Feng Han, Yuhua Sun, Chengqing Li, Jingjing Chen  

**一句话要点**：提出GrOCE框架以解决文本到图像扩散模型中的概念擦除问题

**关键词**：概念擦除, 文本到图像扩散模型, 图推理, 训练无关方法, 语义图构建

## 3 点简述
- 现有概念擦除方法依赖微调或粗语义分离，易损害无关概念且适应性差
- GrOCE基于动态语义图进行训练无关的精确推理，实现细粒度概念隔离
- 实验在CS和FID指标上达到SOTA，无需重训练即可高效稳定擦除概念

## 摘要（原文）

> Concept erasure aims to remove harmful, inappropriate, or copyrighted content from text-to-image diffusion models while preserving non-target semantics. However, existing methods either rely on costly fine-tuning or apply coarse semantic separation, often degrading unrelated concepts and lacking adaptability to evolving concept sets. To alleviate this issue, we propose Graph-Guided Online Concept Erasure (GrOCE), a training-free framework that performs precise and adaptive concept removal through graph-based semantic reasoning. GrOCE models concepts and their interrelations as a dynamic semantic graph, enabling principled reasoning over dependencies and fine-grained isolation of undesired content. It comprises three components: (1) Dynamic Topological Graph Construction for incremental graph building, (2) Adaptive Cluster Identification for multi-hop traversal with similarity-decay scoring, and (3) Selective Edge Severing for targeted edge removal while preserving global semantics. Extensive experiments demonstrate that GrOCE achieves state-of-the-art performance on Concept Similarity (CS) and Fréchet Inception Distance (FID) metrics, offering efficient, accurate, and stable concept erasure without retraining.

