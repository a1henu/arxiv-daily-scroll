---
layout: default
title: CAViT -- Channel-Aware Vision Transformer for Dynamic Feature Fusion
---

# CAViT -- Channel-Aware Vision Transformer for Dynamic Feature Fusion
**arXiv**：[2602.05598v1](https://arxiv.org/abs/2602.05598) · [PDF](https://arxiv.org/pdf/2602.05598.pdf)  
**作者**：Aon Safdar, Mohamed Saadeldin  

**一句话要点**：提出CAViT以解决ViT中通道混合静态问题，通过双注意力机制实现动态特征融合。

**关键词**：视觉Transformer, 动态特征融合, 通道注意力, 双注意力架构, 计算机视觉

## 3 点简述
- 核心问题：ViT的通道混合依赖静态MLP，缺乏对输入内容的适应性。
- 方法要点：在Transformer块中结合空间和通道自注意力，实现动态特征重校准。
- 实验或效果：在五个基准数据集上准确率提升达3.6%，参数和计算量减少超30%。

## 摘要（原文）

> Vision Transformers (ViTs) have demonstrated strong performance across a range of computer vision tasks by modeling long-range spatial interactions via self-attention. However, channel-wise mixing in ViTs remains static, relying on fixed multilayer perceptrons (MLPs) that lack adaptability to input content. We introduce 'CAViT', a dual-attention architecture that replaces the static MLP with a dynamic, attention-based mechanism for feature interaction. Each Transformer block in CAViT performs spatial self-attention followed by channel-wise self-attention, allowing the model to dynamically recalibrate feature representations based on global image context. This unified and content-aware token mixing strategy enhances representational expressiveness without increasing depth or complexity. We validate CAViT across five benchmark datasets spanning both natural and medical domains, where it outperforms the standard ViT baseline by up to +3.6% in accuracy, while reducing parameter count and FLOPs by over 30%. Qualitative attention maps reveal sharper and semantically meaningful activation patterns, validating the effectiveness of our attention-driven token mixing.

