---
layout: default
title: ClusIR: Towards Cluster-Guided All-in-One Image Restoration
---

# ClusIR: Towards Cluster-Guided All-in-One Image Restoration
**arXiv**：[2512.10948v1](https://arxiv.org/abs/2512.10948) · [PDF](https://arxiv.org/pdf/2512.10948.pdf)  
**作者**：Shengkai Hu, Jiaqi Ma, Jun Wan, Wenwen Min, Yongcheng Jing, Lefei Zhang, Dacheng Tao  

**一句话要点**：提出ClusIR框架，通过聚类引导解决多退化图像恢复中的自适应问题。

**关键词**：图像恢复, 聚类引导, 频率调制, 多退化处理, 自适应框架

## 3 点简述
- 核心问题：现有方法难以显式建模退化类型，对复杂或混合退化适应能力不足。
- 方法要点：引入概率聚类引导路由机制和退化感知频率调制模块，实现语义与频域协同恢复。
- 实验或效果：在多个基准测试中验证了ClusIR在广泛退化场景下的竞争性性能。

## 摘要（原文）

> All-in-One Image Restoration (AiOIR) aims to recover high-quality images from diverse degradations within a unified framework. However, existing methods often fail to explicitly model degradation types and struggle to adapt their restoration behavior to complex or mixed degradations. To address these issues, we propose ClusIR, a Cluster-Guided Image Restoration framework that explicitly models degradation semantics through learnable clustering and propagates cluster-aware cues across spatial and frequency domains for adaptive restoration. Specifically, ClusIR comprises two key components: a Probabilistic Cluster-Guided Routing Mechanism (PCGRM) and a Degradation-Aware Frequency Modulation Module (DAFMM). The proposed PCGRM disentangles degradation recognition from expert activation, enabling discriminative degradation perception and stable expert routing. Meanwhile, DAFMM leverages the cluster-guided priors to perform adaptive frequency decomposition and targeted modulation, collaboratively refining structural and textural representations for higher restoration fidelity. The cluster-guided synergy seamlessly bridges semantic cues with frequency-domain modulation, empowering ClusIR to attain remarkable restoration results across a wide range of degradations. Extensive experiments on diverse benchmarks validate that ClusIR reaches competitive performance under several scenarios.

