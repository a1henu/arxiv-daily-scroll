---
layout: default
title: Reciprocal Latent Fields for Precomputed Sound Propagation
---

# Reciprocal Latent Fields for Precomputed Sound Propagation
**arXiv**：[2602.06937v1](https://arxiv.org/abs/2602.06937) · [PDF](https://arxiv.org/pdf/2602.06937.pdf)  
**作者**：Hugo Seuté, Pranai Vasudev, Etienne Richan, Louis-Xavier Buffoni  

**一句话要点**：提出互易潜在场以高效编码预计算声传播参数，降低内存占用。

**关键词**：声传播模拟, 波编码, 潜在场编码, 内存优化, 互易性, 主观评估

## 3 点简述
- 核心问题：波编码方法在大型场景中预计算声传播参数时内存占用过大。
- 方法要点：使用可训练潜在嵌入的体素网格和对称解码器，确保声学互易性。
- 实验或效果：RLF在保持质量的同时，内存占用减少数个数量级，主观测试显示与真实模拟感知无差异。

## 摘要（原文）

> Realistic sound propagation is essential for immersion in a virtual scene, yet physically accurate wave-based simulations remain computationally prohibitive for real-time applications. Wave coding methods address this limitation by precomputing and compressing impulse responses of a given scene into a set of scalar acoustic parameters, which can reach unmanageable sizes in large environments with many source-receiver pairs. We introduce Reciprocal Latent Fields (RLF), a memory-efficient framework for encoding and predicting these acoustic parameters. The RLF framework employs a volumetric grid of trainable latent embeddings decoded with a symmetric function, ensuring acoustic reciprocity. We study a variety of decoders and show that leveraging Riemannian metric learning leads to a better reproduction of acoustic phenomena in complex scenes. Experimental validation demonstrates that RLF maintains replication quality while reducing the memory footprint by several orders of magnitude. Furthermore, a MUSHRA-like subjective listening test indicates that sound rendered via RLF is perceptually indistinguishable from ground-truth simulations.

