---
layout: default
title: Efficient Encoder-Free Fourier-based 3D Large Multimodal Model
---

# Efficient Encoder-Free Fourier-based 3D Large Multimodal Model
**arXiv**：[2602.23153v1](https://arxiv.org/abs/2602.23153) · [PDF](https://arxiv.org/pdf/2602.23153.pdf)  
**作者**：Guofeng Mei, Wei Lin, Luigi Riz, Yujiao Wu, Yiming Wang, Fabio Poiesi  

**一句话要点**：提出Fase3D，首个高效无编码器的傅里叶基3D大模型，以解决无序点云处理难题。

**关键词**：3D大模型, 点云处理, 傅里叶变换, 无编码器架构, 高效计算

## 3 点简述
- 核心问题：3D大模型依赖重编码器处理无序点云，效率低且扩展难。
- 方法要点：结合点云序列化和快速傅里叶变换，实现高效全局建模和令牌合并。
- 实验或效果：性能媲美编码器模型，计算和参数效率显著提升。

## 摘要（原文）

> Large Multimodal Models (LMMs) that process 3D data typically rely on heavy, pre-trained visual encoders to extract geometric features. While recent 2D LMMs have begun to eliminate such encoders for efficiency and scalability, extending this paradigm to 3D remains challenging due to the unordered and large-scale nature of point clouds. This leaves a critical unanswered question: How can we design an LMM that tokenizes unordered 3D data effectively and efficiently without a cumbersome encoder? We propose Fase3D, the first efficient encoder-free Fourier-based 3D scene LMM. Fase3D tackles the challenges of scalability and permutation invariance with a novel tokenizer that combines point cloud serialization and the Fast Fourier Transform (FFT) to approximate self-attention. This design enables an effective and computationally minimal architecture, built upon three key innovations: First, we represent large scenes compactly via structured superpoints. Second, our space-filling curve serialization followed by an FFT enables efficient global context modeling and graph-based token merging. Lastly, our Fourier-augmented LoRA adapters inject global frequency-aware interactions into the LLMs at a negligible cost. Fase3D achieves performance comparable to encoder-based 3D LMMs while being significantly more efficient in computation and parameters. Project website: https://tev-fbk.github.io/Fase3D.

