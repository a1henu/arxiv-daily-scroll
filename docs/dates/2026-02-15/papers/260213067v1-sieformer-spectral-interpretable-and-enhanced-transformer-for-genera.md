---
layout: default
title: SIEFormer: Spectral-Interpretable and -Enhanced Transformer for Generalized Category Discovery
---

# SIEFormer: Spectral-Interpretable and -Enhanced Transformer for Generalized Category Discovery
**arXiv**：[2602.13067v1](https://arxiv.org/abs/2602.13067) · [PDF](https://arxiv.org/pdf/2602.13067.pdf)  
**作者**：Chunming Li, Shidong Wang, Tong Xin, Haofeng Zhang  

**一句话要点**：提出SIEFormer，通过谱分析增强Transformer以解决广义类别发现任务

**关键词**：广义类别发现, 谱分析, Transformer, 图拉普拉斯, 傅里叶变换, 图像识别

## 3 点简述
- 核心问题：广义类别发现任务中，传统ViT注意力机制在特征适应性和可解释性方面存在局限
- 方法要点：设计双分支结构，结合隐式谱视角的图拉普拉斯建模和显式谱视角的傅里叶变换滤波
- 实验或效果：在多个图像识别数据集上实现最先进性能，并通过消融研究和可视化验证方法优势

## 摘要（原文）

> This paper presents a novel approach, Spectral-Interpretable and -Enhanced Transformer (SIEFormer), which leverages spectral analysis to reinterpret the attention mechanism within Vision Transformer (ViT) and enhance feature adaptability, with particular emphasis on challenging Generalized Category Discovery (GCD) tasks. The proposed SIEFormer is composed of two main branches, each corresponding to an implicit and explicit spectral perspective of the ViT, enabling joint optimization. The implicit branch realizes the use of different types of graph Laplacians to model the local structure correlations of tokens, along with a novel Band-adaptive Filter (BaF) layer that can flexibly perform both band-pass and band-reject filtering. The explicit branch, on the other hand, introduces a Maneuverable Filtering Layer (MFL) that learns global dependencies among tokens by applying the Fourier transform to the input ``value" features, modulating the transformed signal with a set of learnable parameters in the frequency domain, and then performing an inverse Fourier transform to obtain the enhanced features. Extensive experiments reveal state-of-the-art performance on multiple image recognition datasets, reaffirming the superiority of our approach through ablation studies and visualizations.

