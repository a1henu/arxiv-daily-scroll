---
layout: default
title: DCText: Scheduled Attention Masking for Visual Text Generation via Divide-and-Conquer Strategy
---

# DCText: Scheduled Attention Masking for Visual Text Generation via Divide-and-Conquer Strategy
**arXiv**：[2512.01302v1](https://arxiv.org/abs/2512.01302) · [PDF](https://arxiv.org/pdf/2512.01302.pdf)  
**作者**：Jaewoo Song, Jooyoung Choi, Kanghyun Baek, Sangyub Lee, Daemin Park, Sungroh Yoon  

**一句话要点**：提出DCText方法，通过分治策略解决文本到图像模型中长文本或多文本渲染的注意力稀释问题。

**关键词**：视觉文本生成, 分治策略, 注意力掩码, 多模态扩散变换器, 文本渲染, 图像连贯性

## 3 点简述
- 核心问题：现有文本到图像模型在渲染长文本或多文本时，因全局注意力稀释导致文本准确性下降。
- 方法要点：采用分治策略，将目标文本分解并分配到指定区域，通过顺序应用文本聚焦和上下文扩展注意力掩码来保持图像连贯性。
- 实验或效果：在单句和多句基准测试中，DCText实现了最佳文本准确性，不损害图像质量，且生成延迟最低。

## 摘要（原文）

> Despite recent text-to-image models achieving highfidelity text rendering, they still struggle with long or multiple texts due to diluted global attention. We propose DCText, a training-free visual text generation method that adopts a divide-and-conquer strategy, leveraging the reliable short-text generation of Multi-Modal Diffusion Transformers. Our method first decomposes a prompt by extracting and dividing the target text, then assigns each to a designated region. To accurately render each segment within their regions while preserving overall image coherence, we introduce two attention masks - Text-Focus and Context-Expansion - applied sequentially during denoising. Additionally, Localized Noise Initialization further improves text accuracy and region alignment without increasing computational cost. Extensive experiments on single- and multisentence benchmarks show that DCText achieves the best text accuracy without compromising image quality while also delivering the lowest generation latency.

