---
layout: default
title: AdaIAT: Adaptively Increasing Attention to Generated Text to Alleviate Hallucinations in LVLM
---

# AdaIAT: Adaptively Increasing Attention to Generated Text to Alleviate Hallucinations in LVLM
**arXiv**：[2603.04908v1](https://arxiv.org/abs/2603.04908) · [PDF](https://arxiv.org/pdf/2603.04908.pdf)  
**作者**：Li'an Zhong, Ziqiang He, Jibin Zheng, Jin Li, Z. Jane Wang, Xiangui Kang  

**一句话要点**：提出AdaIAT方法，通过自适应增强对生成文本的注意力来缓解大型视觉语言模型的幻觉问题。

**关键词**：大型视觉语言模型, 幻觉缓解, 注意力机制, 自适应增强, 文本生成, 视觉语言对齐

## 3 点简述
- 核心问题：大型视觉语言模型在推理时易产生幻觉，即生成与图像不符的描述，阻碍其应用发展。
- 方法要点：基于注意力模式分析，提出自适应增强对生成文本的注意力，通过层间阈值控制干预时机和幅度，避免重复描述并保持语言连贯性。
- 实验或效果：在LLaVA-1.5等模型上，AdaIAT显著降低幻觉率（如CS和CI分别减少35.8%和37.1%），同时保持语言性能和预测能力，实现良好权衡。

## 摘要（原文）

> Hallucination has been a significant impediment to the development and application of current Large Vision-Language Models (LVLMs). To mitigate hallucinations, one intuitive and effective way is to directly increase attention weights to image tokens during inference. Although this effectively reduces the hallucination rate, it often induces repetitive descriptions. To address this, we first conduct an analysis of attention patterns and reveal that real object tokens tend to assign higher attention to the generated text than hallucinated ones. This inspires us to leverage the generated text, which contains instruction-related visual information and contextual knowledge, to alleviate hallucinations while maintaining linguistic coherence. We therefore propose Attention to Generated Text (IAT) and demonstrate that it significantly reduces the hallucination rate while avoiding repetitive descriptions. To prevent naive amplification from impairing the inherent prediction capabilities of LVLMs, we further explore Adaptive IAT (AdaIAT) that employs a layer-wise threshold to control intervention time and fine-grained amplification magnitude tailored to the characteristics of each attention head. Both analysis and experiments demonstrate the effectiveness of AdaIAT. Results of several LVLMs show that AdaIAT effectively alleviates hallucination (reducing hallucination rates $C_S$ and $C_I$ on LLaVA-1.5 by 35.8% and 37.1%, respectively) while preserving linguistic performance and prediction capability, achieving an attractive trade-off.

