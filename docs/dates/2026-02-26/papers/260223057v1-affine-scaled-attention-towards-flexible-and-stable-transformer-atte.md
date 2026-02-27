---
layout: default
title: Affine-Scaled Attention: Towards Flexible and Stable Transformer Attention
---

# Affine-Scaled Attention: Towards Flexible and Stable Transformer Attention
**arXiv**：[2602.23057v1](https://arxiv.org/abs/2602.23057) · [PDF](https://arxiv.org/pdf/2602.23057.pdf)  
**作者**：Jeongin Bae, Baeseong Park, Gunho Park, Minsub Kim, Joonhyung Lee, Junhee Yoo, Sunghyeon Woo, Jiwon Ryu, Se Jung Kwon, Dongsoo Lee  

**一句话要点**：提出Affine-Scaled Attention以解决Transformer注意力归一化限制导致的灵活性与稳定性问题。

**关键词**：Transformer注意力, 归一化约束, 训练稳定性, 语言模型预训练, 注意力重加权

## 3 点简述
- 核心问题：标准softmax注意力强制单位归一化，可能限制注意力幅度控制并导致训练中注意力模式过度集中或不稳定。
- 方法要点：引入输入依赖的缩放和偏置项，放松归一化约束，允许调整注意力的相对分布和尺度。
- 实验或效果：在大规模语言模型预训练中，相比标准注意力和注意力汇基线，提升训练稳定性、优化行为和下游任务性能。

## 摘要（原文）

> Transformer attention is typically implemented using softmax normalization, which enforces attention weights with unit sum normalization. While effective in many settings, this constraint can limit flexibility in controlling attention magnitudes and may contribute to overly concentrated or unstable attention patterns during training. Prior work has explored modifications such as attention sinks or gating mechanisms, but these approaches provide only limited or indirect control over attention reweighting. We propose Affine-Scaled Attention, a simple extension to standard attention that introduces input-dependent scaling and a corresponding bias term applied to softmax-normalized attention weights. This design relaxes the strict normalization constraint while maintaining aggregation of value representations, allowing the model to adjust both the relative distribution and the scale of attention in a controlled manner.
>   We empirically evaluate Affine-Scaled Attention in large-scale language model pretraining across multiple model sizes. Experimental results show consistent improvements in training stability, optimization behavior, and downstream task performance compared to standard softmax attention and attention sink baselines. These findings suggest that modest reweighting of attention outputs provides a practical and effective way to improve attention behavior in Transformer models.

