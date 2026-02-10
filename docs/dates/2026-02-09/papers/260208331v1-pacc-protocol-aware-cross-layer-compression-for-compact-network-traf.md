---
layout: default
title: PACC: Protocol-Aware Cross-Layer Compression for Compact Network Traffic Representation
---

# PACC: Protocol-Aware Cross-Layer Compression for Compact Network Traffic Representation
**arXiv**：[2602.08331v1](https://arxiv.org/abs/2602.08331) · [PDF](https://arxiv.org/pdf/2602.08331.pdf)  
**作者**：Zhaochen Guo, Tianyufei Zhou, Honghao Wang, Ronghua Li, Shinan Liu  

**一句话要点**：提出PACC协议感知跨层压缩框架，以紧凑表示网络流量，提升分类性能与效率。

**关键词**：网络流量分类, 协议感知压缩, 跨层表示学习, 冗余去除, 加密流量分析, 紧凑表示

## 3 点简述
- 核心问题：网络流量分类面临加密和协议演化挑战，现有表示方法存在冗余、容量浪费和泛化差问题。
- 方法要点：将协议栈作为多视图输入，学习层间共享和层内私有组件，通过重构、对比学习和监督损失优化表示。
- 实验或效果：在加密应用分类、IoT设备识别和入侵检测数据集上，PACC优于特征工程和原始比特基线，提升准确率并提高效率。

## 摘要（原文）

> Network traffic classification is a core primitive for network security and management, yet it is increasingly challenged by pervasive encryption and evolving protocols. A central bottleneck is representation: hand-crafted flow statistics are efficient but often too lossy, raw-bit encodings can be accurate but are costly, and recent pre-trained embeddings provide transfer but frequently flatten the protocol stack and entangle signals across layers. We observe that real traffic contains substantial redundancy both across network layers and within each layer; existing paradigms do not explicitly identify and remove this redundancy, leading to wasted capacity, shortcut learning, and degraded generalization. To address this, we propose PACC, a redundancy-aware, layer-aware representation framework. PACC treats the protocol stack as multi-view inputs and learns compact layer-wise projections that remain faithful to each layer while explicitly factorizing representations into shared (cross-layer) and private (layer-specific) components. We operationalize these goals with a joint objective that preserves layer-specific information via reconstruction, captures shared structure via contrastive mutual-information learning, and maximizes task-relevant information via supervised losses, yielding compact latents suitable for efficient inference. Across datasets covering encrypted application classification, IoT device identification, and intrusion detection, PACC consistently outperforms feature-engineered and raw-bit baselines. On encrypted subsets, it achieves up to a 12.9% accuracy improvement over nPrint. PACC matches or surpasses strong foundation-model baselines. At the same time, it improves end-to-end efficiency by up to 3.16x.

