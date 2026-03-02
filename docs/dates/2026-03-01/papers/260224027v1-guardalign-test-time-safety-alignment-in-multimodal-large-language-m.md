---
layout: default
title: GuardAlign: Test-time Safety Alignment in Multimodal Large Language Models
---

# GuardAlign: Test-time Safety Alignment in Multimodal Large Language Models
**arXiv**：[2602.24027v1](https://arxiv.org/abs/2602.24027) · [PDF](https://arxiv.org/pdf/2602.24027.pdf)  
**作者**：Xingyu Zhu, Beier Zhu, Junfeng Fang, Shuo Wang, Yin Zhang, Xiang Wang, Xiangnan He  

**一句话要点**：提出GuardAlign框架以解决多模态大语言模型在测试时的安全对齐问题

**关键词**：多模态大语言模型, 安全对齐, 最优传输, 注意力校准, 测试时防御, 视觉语言推理

## 3 点简述
- 核心问题：现有输入侧防御在复杂场景下检测不准确且解码时安全信号不稳定
- 方法要点：结合最优传输增强安全检测和跨模态注意力校准，无需训练
- 实验或效果：在SPA-VL上降低不安全响应率高达39%，同时提升VQAv2性能

## 摘要（原文）

> Large vision-language models (LVLMs) have achieved remarkable progress in vision-language reasoning tasks, yet ensuring their safety remains a critical challenge. Recent input-side defenses detect unsafe images with CLIP and prepend safety prefixes to prompts, but they still suffer from inaccurate detection in complex scenes and unstable safety signals during decoding. To address these issues, we propose GuardAlign, a training-free defense framework that integrates two strategies. First, OT-enhanced safety detection leverages optimal transport to measure distribution distances between image patches and unsafe semantics, enabling accurate identification of malicious regions without additional computational cost. Second, cross-modal attentive calibration strengthens the influence of safety prefixes by adaptively reallocating attention across layers, ensuring that safety signals remain consistently activated throughout generation. Extensive evaluations on six representative MLLMs demonstrate that GuardAlign reduces unsafe response rates by up to 39% on SPA-VL, while preserving utility, achieving an improvement on VQAv2 from 78.51% to 79.21%.

