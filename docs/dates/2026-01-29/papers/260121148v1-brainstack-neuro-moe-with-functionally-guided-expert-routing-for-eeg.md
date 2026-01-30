---
layout: default
title: BrainStack: Neuro-MoE with Functionally Guided Expert Routing for EEG-Based Language Decoding
---

# BrainStack: Neuro-MoE with Functionally Guided Expert Routing for EEG-Based Language Decoding
**arXiv**：[2601.21148v1](https://arxiv.org/abs/2601.21148) · [PDF](https://arxiv.org/pdf/2601.21148.pdf)  
**作者**：Ziyi Zhao, Jinzhao Zhou, Xiaowei Jiang, Beining Cao, Wenhao Ma, Yang Shen, Ren Li, Yu-Kai Wang, Chin-teng Lin  

**一句话要点**：提出BrainStack框架，通过功能引导的神经专家混合模型解决基于EEG的语言解码挑战。

**关键词**：脑电语言解码, 神经专家混合, 功能引导路由, 跨区域蒸馏, 大规模数据集

## 3 点简述
- 核心问题：EEG信号分布非线性，解码语言信息困难。
- 方法要点：结合解剖分区专家和全局Transformer，自适应路由融合。
- 实验或效果：在大型数据集上超越现有模型，提升准确性和泛化能力。

## 摘要（原文）

> Decoding linguistic information from electroencephalography (EEG) remains challenging due to the brain's distributed and nonlinear organization. We present BrainStack, a functionally guided neuro-mixture-of-experts (Neuro-MoE) framework that models the brain's modular functional architecture through anatomically partitioned expert networks. Each functional region is represented by a specialized expert that learns localized neural dynamics, while a transformer-based global expert captures cross-regional dependencies. A learnable routing gate adaptively aggregates these heterogeneous experts, enabling context-dependent expert coordination and selective fusion. To promote coherent representation across the hierarchy, we introduce cross-regional distillation, where the global expert provides top-down regularization to the regional experts. We further release SilentSpeech-EEG (SS-EEG), a large-scale benchmark comprising over 120 hours of EEG recordings from 12 subjects performing 24 silent words, the largest dataset of its kind. Experiments demonstrate that BrainStack consistently outperforms state-of-the-art models, achieving superior accuracy and generalization across subjects. Our results establish BrainStack as a functionally modular, neuro-inspired MoE paradigm that unifies neuroscientific priors with adaptive expert routing, paving the way for scalable and interpretable brain-language decoding.

