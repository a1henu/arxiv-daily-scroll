---
layout: default
title: Fourier-Attentive Representation Learning: A Fourier-Guided Framework for Few-Shot Generalization in Vision-Language Models
---

# Fourier-Attentive Representation Learning: A Fourier-Guided Framework for Few-Shot Generalization in Vision-Language Models
**arXiv**：[2512.04395v1](https://arxiv.org/abs/2512.04395) · [PDF](https://arxiv.org/pdf/2512.04395.pdf)  
**作者**：Hieu Dinh Trung Pham, Huy Minh Nhat Nguyen, Cuong Tuan Nguyen  

**一句话要点**：提出FARL框架，通过傅里叶分析解耦视觉表示以增强视觉语言模型的小样本泛化能力

**关键词**：视觉语言模型, 小样本学习, 傅里叶分析, 表示解耦, 交叉注意力, 泛化增强

## 3 点简述
- 核心问题：现有视觉语言模型在表示学习中隐式纠缠图像的结构与风格特征，限制小样本泛化。
- 方法要点：采用傅里叶分析，通过双交叉注意力机制分别从相位谱和幅度谱提取结构与风格特征，并注入编码器。
- 实验或效果：在15个数据集上验证了方法的有效性，提升了视觉语言对齐的鲁棒性。

## 摘要（原文）

> Large-scale pre-trained Vision-Language Models (VLMs) have demonstrated strong few-shot learning capabilities. However, these methods typically learn holistic representations where an image's domain-invariant structure is implicitly entangled with its domain-specific style. This presents an opportunity to further enhance generalization by disentangling these visual cues. In this paper, we propose Fourier-Attentive Representation Learning (FARL), a novel framework that addresses this by explicitly disentangling visual representations using Fourier analysis. The core of our method is a dual cross-attention mechanism, where learnable representation tokens separately query an image's structural features (from the phase spectrum) and stylistic features (from the amplitude spectrum). This process yields enriched, disentangled tokens that are then injected deep into the VLM encoders to guide adaptation. Our design, which includes an asymmetric injection strategy, forces the model to learn a more robust vision-language alignment. Extensive experiments on 15 datasets demonstrate the effectiveness of our approach.

