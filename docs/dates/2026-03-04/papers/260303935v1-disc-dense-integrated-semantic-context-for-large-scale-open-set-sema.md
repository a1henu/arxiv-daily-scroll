---
layout: default
title: DISC: Dense Integrated Semantic Context for Large-Scale Open-Set Semantic Mapping
---

# DISC: Dense Integrated Semantic Context for Large-Scale Open-Set Semantic Mapping
**arXiv**：[2603.03935v1](https://arxiv.org/abs/2603.03935) · [PDF](https://arxiv.org/pdf/2603.03935.pdf)  
**作者**：Felix Igelbrink, Lennart Niecksch, Martin Atzmueller, Joachim Hertzberg  

**一句话要点**：提出DISC方法以解决开放集语义映射中基于裁剪的特征提取瓶颈问题

**关键词**：开放集语义映射, 密集语义上下文, 零样本学习, 实时语义建图, CLIP嵌入, GPU加速架构

## 3 点简述
- 核心问题：现有开放集语义映射方法依赖裁剪式特征提取，导致上下文缺失和计算开销大
- 方法要点：引入单次距离加权提取机制，直接从视觉变换器中间层获取高保真CLIP嵌入，避免裁剪延迟和域偏移
- 实验或效果：在标准基准和新大规模数据集上评估，DISC在语义准确性和查询检索方面显著优于当前零样本方法

## 摘要（原文）

> Open-set semantic mapping enables language-driven robotic perception, but current instance-centric approaches are bottlenecked by context-depriving and computationally expensive crop-based feature extraction. To overcome this fundamental limitation, we introduce DISC (Dense Integrated Semantic Context), featuring a novel single-pass, distance-weighted extraction mechanism. By deriving high-fidelity CLIP embeddings directly from the vision transformer's intermediate layers, our approach eliminates the latency and domain-shift artifacts of traditional image cropping, yielding pure, mask-aligned semantic representations. To fully leverage these features in large-scale continuous mapping, DISC is built upon a fully GPU-accelerated architecture that replaces periodic offline processing with precise, on-the-fly voxel-level instance refinement. We evaluate our approach on standard benchmarks (Replica, ScanNet) and a newly generated large-scale-mapping dataset based on Habitat-Matterport 3D (HM3DSEM) to assess scalability across complex scenes in multi-story buildings. Extensive evaluations demonstrate that DISC significantly surpasses current state-of-the-art zero-shot methods in both semantic accuracy and query retrieval, providing a robust, real-time capable framework for robotic deployment. The full source code, data generation and evaluation pipelines will be made available at https://github.com/DFKI-NI/DISC.

