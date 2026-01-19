---
layout: default
title: SoLA-Vision: Fine-grained Layer-wise Linear Softmax Hybrid Attention
---

# SoLA-Vision: Fine-grained Layer-wise Linear Softmax Hybrid Attention
**arXiv**：[2601.11164v1](https://arxiv.org/abs/2601.11164) · [PDF](https://arxiv.org/pdf/2601.11164.pdf)  
**作者**：Ruibang Li, Guan Luo, Yiwei Zhang, Jin Gao, Bing Li, Weiming Hu  

**一句话要点**：提出SoLA-Vision，通过细粒度层间混合注意力在视觉任务中平衡精度与计算成本。

**关键词**：视觉注意力机制, 层间混合设计, 计算复杂度优化, 图像分类, 密集预测任务, 线性注意力

## 3 点简述
- 标准softmax注意力计算复杂度高，线性注意力压缩表示可能损害建模能力。
- 分析层间混合模式，提出灵活层间混合注意力骨干，精细控制线性与softmax注意力集成。
- 在ImageNet-1K和密集预测任务中超越纯线性及其他混合模型，实现精度与成本权衡。

## 摘要（原文）

> Standard softmax self-attention excels in vision tasks but incurs quadratic complexity O(N^2), limiting high-resolution deployment. Linear attention reduces the cost to O(N), yet its compressed state representations can impair modeling capacity and accuracy. We present an analytical study that contrasts linear and softmax attention for visual representation learning from a layer-stacking perspective. We further conduct systematic experiments on layer-wise hybridization patterns of linear and softmax attention. Our results show that, compared with rigid intra-block hybrid designs, fine-grained layer-wise hybridization can match or surpass performance while requiring fewer softmax layers. Building on these findings, we propose SoLA-Vision (Softmax-Linear Attention Vision), a flexible layer-wise hybrid attention backbone that enables fine-grained control over how linear and softmax attention are integrated. By strategically inserting a small number of global softmax layers, SoLA-Vision achieves a strong trade-off between accuracy and computational cost. On ImageNet-1K, SoLA-Vision outperforms purely linear and other hybrid attention models. On dense prediction tasks, it consistently surpasses strong baselines by a considerable margin. Code will be released.

