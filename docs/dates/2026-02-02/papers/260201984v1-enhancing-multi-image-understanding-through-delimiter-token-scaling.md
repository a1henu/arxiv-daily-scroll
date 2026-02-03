---
layout: default
title: Enhancing Multi-Image Understanding through Delimiter Token Scaling
---

# Enhancing Multi-Image Understanding through Delimiter Token Scaling
**arXiv**：[2602.01984v1](https://arxiv.org/abs/2602.01984) · [PDF](https://arxiv.org/pdf/2602.01984.pdf)  
**作者**：Minyoung Lee, Yeji Park, Dongjun Hwang, Yejin Kim, Seong Joon Oh, Junsuk Choe  

**一句话要点**：提出分隔符令牌缩放方法以增强多图像理解中的跨图像信息泄漏问题

**关键词**：多图像理解, 分隔符令牌, 跨图像信息泄漏, 视觉语言模型, 隐藏状态缩放

## 3 点简述
- 核心问题：大型视觉语言模型在多图像输入时性能下降，主要由于跨图像信息泄漏。
- 方法要点：通过缩放分隔符令牌的隐藏状态，强化图像内交互并限制跨图像交互。
- 实验或效果：在Mantis等多图像基准上性能提升，无需额外训练或推理成本。

## 摘要（原文）

> Large Vision-Language Models (LVLMs) achieve strong performance on single-image tasks, but their performance declines when multiple images are provided as input. One major reason is the cross-image information leakage, where the model struggles to distinguish information across different images. Existing LVLMs already employ delimiter tokens to mark the start and end of each image, yet our analysis reveals that these tokens fail to effectively block cross-image information leakage. To enhance their effectiveness, we propose a method that scales the hidden states of delimiter tokens. This enhances the model's ability to preserve image-specific information by reinforcing intra-image interaction and limiting undesired cross-image interactions. Consequently, the model is better able to distinguish between images and reason over them more accurately. Experiments show performance gains on multi-image benchmarks such as Mantis, MuirBench, MIRB, and QBench2. We further evaluate our method on text-only tasks that require clear distinction. The method improves performance on multi-document and multi-table understanding benchmarks, including TQABench, MultiNews, and WCEP-10. Notably, our method requires no additional training or inference cost.

