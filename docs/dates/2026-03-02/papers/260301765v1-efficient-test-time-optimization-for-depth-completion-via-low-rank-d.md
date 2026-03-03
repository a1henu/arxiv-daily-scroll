---
layout: default
title: Efficient Test-Time Optimization for Depth Completion via Low-Rank Decoder Adaptation
---

# Efficient Test-Time Optimization for Depth Completion via Low-Rank Decoder Adaptation
**arXiv**：[2603.01765v1](https://arxiv.org/abs/2603.01765) · [PDF](https://arxiv.org/pdf/2603.01765.pdf)  
**作者**：Minseok Seo, Wonjun Lee, Jaehyuk Jang, Changick Kim  

**一句话要点**：提出低秩解码器适应方法以高效实现零样本深度补全的测试时优化

**关键词**：深度补全, 测试时优化, 零样本学习, 低秩适应, 解码器适应, 稀疏监督

## 3 点简述
- 核心问题：现有零样本深度补全方法依赖计算昂贵的扩散优化或重复前向-反向传播，导致推理缓慢
- 方法要点：仅适应低维解码器子空间，利用稀疏深度监督进行轻量级测试时优化
- 实验或效果：在五个室内外数据集上实现最先进性能，在精度与效率间建立新帕累托前沿

## 摘要（原文）

> Zero-shot depth completion has gained attention for its ability to generalize across environments without sensor-specific datasets or retraining. However, most existing approaches rely on diffusion-based test-time optimization, which is computationally expensive due to iterative denoising. Recent visual-prompt-based methods reduce training cost but still require repeated forward--backward passes through the full frozen network to optimize input-level prompts, resulting in slow inference. In this work, we show that adapting only the decoder is sufficient for effective test-time optimization, as depth foundation models concentrate depth-relevant information within a low-dimensional decoder subspace. Based on this insight, we propose a lightweight test-time adaptation method that updates only this low-dimensional subspace using sparse depth supervision. Our approach achieves state-of-the-art performance, establishing a new Pareto frontier between accuracy and efficiency for test-time adaptation. Extensive experiments on five indoor and outdoor datasets demonstrate consistent improvements over prior methods, highlighting the practicality of fast zero-shot depth completion.

