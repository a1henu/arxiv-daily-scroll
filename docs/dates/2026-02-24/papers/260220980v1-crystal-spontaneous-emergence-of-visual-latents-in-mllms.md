---
layout: default
title: CrystaL: Spontaneous Emergence of Visual Latents in MLLMs
---

# CrystaL: Spontaneous Emergence of Visual Latents in MLLMs
**arXiv**：[2602.20980v1](https://arxiv.org/abs/2602.20980) · [PDF](https://arxiv.org/pdf/2602.20980.pdf)  
**作者**：Yang Zhang, Danyang Li, Yuxuan Li, Xin Zhang, Tianyu Xie, Mingming Cheng, Xiang Li  

**一句话要点**：提出CrystaL框架以解决多模态大模型中视觉信息在隐式推理中的保留问题

**关键词**：多模态大语言模型, 隐式推理, 视觉语义对齐, 注意力模式, 细粒度视觉理解, 单阶段框架

## 3 点简述
- 现有隐式推理方法依赖启发式监督，难以在中间隐状态中保留关键视觉信息
- CrystaL通过双路径处理完整与损坏图像，对齐注意力模式和预测分布，无需额外标注
- 在感知密集型基准测试中，CrystaL显著提升细粒度视觉理解，同时保持推理鲁棒性

## 摘要（原文）

> Multimodal Large Language Models (MLLMs) have achieved remarkable performance by integrating powerful language backbones with large-scale visual encoders. Among these, latent Chain-of-Thought (CoT) methods enable implicit reasoning in continuous hidden states, facilitating seamless vision-language integration and faster inference. However, existing heuristically predefined supervision signals in latent CoT provide limited guidance for preserving critical visual information in intermediate latent states. To address this limitation, we propose CrystaL (Crystallized Latent Reasoning), a single-stage framework with two paths to process intact and corrupted images, respectively. By explicitly aligning the attention patterns and prediction distributions across the two paths, CrystaL crystallizes latent representations into task-relevant visual semantics, without relying on auxiliary annotations or external modules. Extensive experiments on perception-intensive benchmarks demonstrate that CrystaL consistently outperforms state-of-the-art baselines, achieving substantial gains in fine-grained visual understanding while maintaining robust reasoning capabilities.

