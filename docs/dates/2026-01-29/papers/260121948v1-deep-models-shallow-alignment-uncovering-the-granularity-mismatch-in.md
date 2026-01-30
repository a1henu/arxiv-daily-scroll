---
layout: default
title: Deep Models, Shallow Alignment: Uncovering the Granularity Mismatch in Neural Decoding
---

# Deep Models, Shallow Alignment: Uncovering the Granularity Mismatch in Neural Decoding
**arXiv**：[2601.21948v1](https://arxiv.org/abs/2601.21948) · [PDF](https://arxiv.org/pdf/2601.21948.pdf)  
**作者**：Yang Du, Siyuan Dai, Yonghao Song, Paul M. Thompson, Haoteng Tang, Liang Zhan  

**一句话要点**：提出浅层对齐方法以解决神经解码中的粒度不匹配问题

**关键词**：神经视觉解码, 粒度不匹配, 浅层对齐, 对比学习, 视觉编码器, 缩放定律

## 3 点简述
- 核心问题：深度视觉模型与神经信号在粒度上不匹配，前者抑制纹理细节，后者混合低层与高层信息。
- 方法要点：通过对比学习将神经信号与视觉编码器的中间表示对齐，平衡纹理细节与语义特征。
- 实验或效果：在多个基准上显著优于标准最终层对齐，性能提升22%至58%，并解锁了缩放定律。

## 摘要（原文）

> Neural visual decoding is a central problem in brain computer interface research, aiming to reconstruct human visual perception and to elucidate the structure of neural representations. However, existing approaches overlook a fundamental granularity mismatch between human and machine vision, where deep vision models emphasize semantic invariance by suppressing local texture information, whereas neural signals preserve an intricate mixture of low-level visual attributes and high-level semantic content. To address this mismatch, we propose Shallow Alignment, a novel contrastive learning strategy that aligns neural signals with intermediate representations of visual encoders rather than their final outputs, thereby striking a better balance between low-level texture details and high-level semantic features. Extensive experiments across multiple benchmarks demonstrate that Shallow Alignment significantly outperforms standard final-layer alignment, with performance gains ranging from 22% to 58% across diverse vision backbones. Notably, our approach effectively unlocks the scaling law in neural visual decoding, enabling decoding performance to scale predictably with the capacity of pre-trained vision backbones. We further conduct systematic empirical analyses to shed light on the mechanisms underlying the observed performance gains.

