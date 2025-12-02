---
layout: default
title: Low-Rank Prehab: Preparing Neural Networks for SVD Compression
---

# Low-Rank Prehab: Preparing Neural Networks for SVD Compression
**arXiv**：[2512.01980v1](https://arxiv.org/abs/2512.01980) · [PDF](https://arxiv.org/pdf/2512.01980.pdf)  
**作者**：Haoran Qin, Shansita Sharma, Ali Abbasi, Chayne Thrash, Soheil Kolouri  

**一句话要点**：提出低秩预适应方法，在SVD压缩前优化神经网络权重结构以提升压缩效果。

**关键词**：神经网络压缩, 低秩近似, 奇异值分解, 预适应微调, Transformer架构

## 3 点简述
- 核心问题：SVD压缩神经网络后需微调恢复精度，但压缩时精度下降较大。
- 方法要点：引入预压缩微调阶段，鼓励权重矩阵低秩化，为SVD压缩做准备。
- 实验或效果：在LLMs和ViTs上验证，减少压缩后精度下降，优于现有SVD技术。

## 摘要（原文）

> Low-rank approximation methods such as singular value decomposition (SVD) and its variants (e.g., Fisher-weighted SVD, Activation SVD) have recently emerged as effective tools for neural network compression. In this setting, decomposition acts as a "surgical" intervention, followed by fine-tuning that serves as "rehab" to recover accuracy. Inspired by prehabilitation in surgery, we introduce a pre-compression fine-tuning stage, Low-Rank Prehab, that explicitly encourages low-rank structure in weight matrices while preserving task performance. By conditioning the model before SVD, Prehab steers weights toward spectrally compact regions of the parameter space, enabling smoother low-rank approximation and improved recovery. Experiments on large language models (LLMs) and other Transformer-based architectures, including Vision Transformers (ViTs), show that Prehab substantially reduces the immediate accuracy drop after compression and consistently improves post-finetuning performance. Across a wide range of compression ratios, our method outperforms state-of-the-art SVD-based techniques such as SVD-LLM, highlighting the importance of preparing models for compression rather than only improving the compression and recovery stages. Source code is available at https://github.com/niqretnuh/PREHAB-SVD

