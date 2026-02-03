---
layout: default
title: FreshMem: Brain-Inspired Frequency-Space Hybrid Memory for Streaming Video Understanding
---

# FreshMem: Brain-Inspired Frequency-Space Hybrid Memory for Streaming Video Understanding
**arXiv**：[2602.01683v1](https://arxiv.org/abs/2602.01683) · [PDF](https://arxiv.org/pdf/2602.01683.pdf)  
**作者**：Kangcong Li, Peng Ye, Lin Zhang, Chao Wang, Huafeng Qin, Tao Chen  

**一句话要点**：提出FreshMem频率-空间混合记忆网络，以解决流式视频理解中的细节丢失和上下文碎片化问题。

**关键词**：流式视频理解, 多模态大语言模型, 记忆网络, 频率空间混合, 免训练方法, 长视频理解

## 3 点简述
- 核心问题：现有方法缺乏灵活适应性，导致流式视频理解中不可逆的细节丢失和上下文碎片化。
- 方法要点：受大脑对数感知和记忆巩固启发，通过多尺度频率记忆和空间缩略图记忆协同，平衡短期保真与长期连贯。
- 实验或效果：在StreamingBench等基准上显著提升基线性能，作为免训练方案优于多个全微调方法。

## 摘要（原文）

> Transitioning Multimodal Large Language Models (MLLMs) from offline to online streaming video understanding is essential for continuous perception. However, existing methods lack flexible adaptivity, leading to irreversible detail loss and context fragmentation. To resolve this, we propose FreshMem, a Frequency-Space Hybrid Memory network inspired by the brain's logarithmic perception and memory consolidation. FreshMem reconciles short-term fidelity with long-term coherence through two synergistic modules: Multi-scale Frequency Memory (MFM), which projects overflowing frames into representative frequency coefficients, complemented by residual details to reconstruct a global historical "gist"; and Space Thumbnail Memory (STM), which discretizes the continuous stream into episodic clusters by employing an adaptive compression strategy to distill them into high-density space thumbnails. Extensive experiments show that FreshMem significantly boosts the Qwen2-VL baseline, yielding gains of 5.20%, 4.52%, and 2.34% on StreamingBench, OV-Bench, and OVO-Bench, respectively. As a training-free solution, FreshMem outperforms several fully fine-tuned methods, offering a highly efficient paradigm for long-horizon streaming video understanding.

