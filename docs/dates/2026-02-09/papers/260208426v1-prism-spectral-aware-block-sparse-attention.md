---
layout: default
title: Prism: Spectral-Aware Block-Sparse Attention
---

# Prism: Spectral-Aware Block-Sparse Attention
**arXiv**：[2602.08426v1](https://arxiv.org/abs/2602.08426) · [PDF](https://arxiv.org/pdf/2602.08426.pdf)  
**作者**：Xinghao Wang, Pengyu Wang, Xiaoran Liu, Fangxu Liu, Jason Chu, Kai Song, Xipeng Qiu  

**一句话要点**：提出Prism方法以解决块稀疏注意力中块重要性估计不准确的问题，提升长上下文LLM预填充效率。

**关键词**：块稀疏注意力, 长上下文处理, 位置编码, 频谱分析, 训练自由方法, LLM加速

## 3 点简述
- 核心问题：现有块稀疏注意力方法使用平均池化作为块重要性估计代理，但受RoPE影响导致局部位置信息丢失，造成估计不准确。
- 方法要点：Prism通过频谱感知分解块选择为高频和低频分支，应用基于能量的温度校准恢复衰减的位置信号，实现纯块级操作。
- 实验或效果：评估显示Prism在保持与全注意力精度相当的同时，实现最高5.1倍加速。

## 摘要（原文）

> Block-sparse attention is promising for accelerating long-context LLM pre-filling, yet identifying relevant blocks efficiently remains a bottleneck. Existing methods typically employ coarse-grained attention as a proxy for block importance estimation, but often resort to expensive token-level searching or scoring, resulting in significant selection overhead. In this work, we trace the inaccuracy of standard coarse-grained attention via mean pooling to a theoretical root cause: the interaction between mean pooling and Rotary Positional Embeddings (RoPE). We prove that mean pooling acts as a low-pass filter that induces destructive interference in high-frequency dimensions, effectively creating a "blind spot" for local positional information (e.g., slash patterns). To address this, we introduce Prism, a training-free spectral-aware approach that decomposes block selection into high-frequency and low-frequency branches. By applying energy-based temperature calibration, Prism restores the attenuated positional signals directly from pooled representations, enabling block importance estimation using purely block-level operations, thereby improving efficiency. Extensive evaluations confirm that Prism maintains accuracy parity with full attention while delivering up to $\mathbf{5.1\times}$ speedup.

