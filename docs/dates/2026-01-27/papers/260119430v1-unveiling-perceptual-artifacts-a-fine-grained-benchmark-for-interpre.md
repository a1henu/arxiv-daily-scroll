---
layout: default
title: Unveiling Perceptual Artifacts: A Fine-Grained Benchmark for Interpretable AI-Generated Image Detection
---

# Unveiling Perceptual Artifacts: A Fine-Grained Benchmark for Interpretable AI-Generated Image Detection
**arXiv**：[2601.19430v1](https://arxiv.org/abs/2601.19430) · [PDF](https://arxiv.org/pdf/2601.19430.pdf)  
**作者**：Yao Xiao, Weiyan Chen, Jiahao Chen, Zijie Cao, Weijian Deng, Binbin Yang, Ziyi Dong, Xiangyang Ji, Wei Ke, Pengxu Wei, Liang Lin  

**一句话要点**：提出X-AIGD基准以解决AI生成图像检测中缺乏细粒度可解释性评估的问题

**关键词**：AI生成图像检测, 可解释性基准, 感知伪影标注, 细粒度评估, 模型注意力对齐

## 3 点简述
- 现有AI生成图像检测方法依赖二分类，缺乏可解释证据，源于基准覆盖不足
- 引入X-AIGD基准，提供像素级分类标注，涵盖低层失真、高层语义和认知级反事实
- 实验发现现有检测器对感知伪影依赖低，对齐注意力可提升可解释性和泛化性

## 摘要（原文）

> Current AI-Generated Image (AIGI) detection approaches predominantly rely on binary classification to distinguish real from synthetic images, often lacking interpretable or convincing evidence to substantiate their decisions. This limitation stems from existing AIGI detection benchmarks, which, despite featuring a broad collection of synthetic images, remain restricted in their coverage of artifact diversity and lack detailed, localized annotations. To bridge this gap, we introduce a fine-grained benchmark towards eXplainable AI-Generated image Detection, named X-AIGD, which provides pixel-level, categorized annotations of perceptual artifacts, spanning low-level distortions, high-level semantics, and cognitive-level counterfactuals. These comprehensive annotations facilitate fine-grained interpretability evaluation and deeper insight into model decision-making processes. Our extensive investigation using X-AIGD provides several key insights: (1) Existing AIGI detectors demonstrate negligible reliance on perceptual artifacts, even at the most basic distortion level. (2) While AIGI detectors can be trained to identify specific artifacts, they still substantially base their judgment on uninterpretable features. (3) Explicitly aligning model attention with artifact regions can increase the interpretability and generalization of detectors. The data and code are available at: https://github.com/Coxy7/X-AIGD.

