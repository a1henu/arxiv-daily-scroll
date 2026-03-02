---
layout: default
title: Fixed Anchors Are Not Enough: Dynamic Retrieval and Persistent Homology for Dataset Distillation
---

# Fixed Anchors Are Not Enough: Dynamic Retrieval and Persistent Homology for Dataset Distillation
**arXiv**：[2602.24144v1](https://arxiv.org/abs/2602.24144) · [PDF](https://arxiv.org/pdf/2602.24144.pdf)  
**作者**：Muquan Li, Hang Gou, Yingyi Ma, Rongzheng Wang, Ke Qin, Tao He  

**一句话要点**：提出RETA框架，通过动态检索和拓扑对齐解决解耦数据集蒸馏中的拟合-复杂度差距和锚点效应问题。

**关键词**：数据集蒸馏, 动态检索, 拓扑对齐, 解耦学习, 泛化能力

## 3 点简述
- 核心问题：现有解耦数据集蒸馏方法依赖静态真实补丁，导致拟合-复杂度差距和锚点效应，降低类内多样性和泛化能力。
- 方法要点：引入动态检索连接选择真实补丁以优化拟合-复杂度，并采用持久拓扑对齐正则化合成数据，缓解锚点效应。
- 实验或效果：在多个数据集上超越基线，ImageNet-1K上达到64.3% top-1准确率，比先前最佳提升3.1%。

## 摘要（原文）

> Decoupled dataset distillation (DD) compresses large corpora into a few synthetic images by matching a frozen teacher's statistics. However, current residual-matching pipelines rely on static real patches, creating a fit-complexity gap and a pull-to-anchor effect that reduce intra-class diversity and hurt generalization. To address these issues, we introduce RETA -- a Retrieval and Topology Alignment framework for decoupled DD. First, Dynamic Retrieval Connection (DRC) selects a real patch from a prebuilt pool by minimizing a fit-complexity score in teacher feature space; the chosen patch is injected via a residual connection to tighten feature fit while controlling injected complexity. Second, Persistent Topology Alignment (PTA) regularizes synthesis with persistent homology: we build a mutual k-NN feature graph, compute persistence images of components and loops, and penalize topology discrepancies between real and synthetic sets, mitigating pull-to-anchor effect. Across CIFAR-100, Tiny-ImageNet, ImageNet-1K, and multiple ImageNet subsets, RETA consistently outperforms various baselines under comparable time and memory, especially reaching 64.3% top-1 accuracy on ImageNet-1K with ResNet-18 at 50 images per class, +3.1% over the best prior.

