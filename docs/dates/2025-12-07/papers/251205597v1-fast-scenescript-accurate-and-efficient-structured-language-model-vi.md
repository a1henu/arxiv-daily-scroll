---
layout: default
title: Fast SceneScript: Accurate and Efficient Structured Language Model via Multi-Token Prediction
---

# Fast SceneScript: Accurate and Efficient Structured Language Model via Multi-Token Prediction
**arXiv**：[2512.05597v1](https://arxiv.org/abs/2512.05597) · [PDF](https://arxiv.org/pdf/2512.05597.pdf)  
**作者**：Ruihong Yin, Xuepeng Shi, Oleksandr Bailo, Marco Manfredi, Theo Gevers  

**一句话要点**：提出Fast SceneScript，通过多令牌预测加速3D场景布局估计，保持准确性。

**关键词**：3D场景布局估计, 结构化语言模型, 多令牌预测, 自推测解码, 置信度引导解码, 参数高效机制

## 3 点简述
- 问题：基于语言模型的感知通用方法在3D场景布局估计中依赖自回归预测，导致推理速度慢。
- 方法：采用多令牌预测减少自回归迭代，结合自推测解码和置信度引导解码过滤不可靠令牌，设计参数高效机制。
- 效果：在ASE和Structured3D基准上，每步生成最多9个令牌，不损失准确性，参数增加约7.5%。

## 摘要（原文）

> Recent perception-generalist approaches based on language models have achieved state-of-the-art results across diverse tasks, including 3D scene layout estimation, via unified architecture and interface. However, these approaches rely on autoregressive next-token prediction, which is inherently slow. In this work, we introduce Fast SceneScript, a novel structured language model for accurate and efficient 3D scene layout estimation. Our method employs multi-token prediction (MTP) to reduce the number of autoregressive iterations and significantly accelerate inference. While MTP improves speed, unreliable token predictions can significantly reduce accuracy. To filter out unreliable tokens, we adapt self-speculative decoding (SSD) for structured language models and introduce confidence-guided decoding (CGD) with an improved scoring mechanism for token reliability. Furthermore, we design a parameter-efficient mechanism that reduces the parameter overhead of MTP. Extensive experiments on the ASE and Structured3D benchmarks demonstrate that Fast SceneScript can generate up to 9 tokens per decoder inference step without compromising accuracy, while adding only $\sim7.5\%$ additional parameters.

