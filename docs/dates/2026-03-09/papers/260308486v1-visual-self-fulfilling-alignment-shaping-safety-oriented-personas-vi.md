---
layout: default
title: Visual Self-Fulfilling Alignment: Shaping Safety-Oriented Personas via Threat-Related Images
---

# Visual Self-Fulfilling Alignment: Shaping Safety-Oriented Personas via Threat-Related Images
**arXiv**：[2603.08486v1](https://arxiv.org/abs/2603.08486) · [PDF](https://arxiv.org/pdf/2603.08486.pdf)  
**作者**：Qishun Yang, Shu Yang, Lijie Hu, Di Wang  

**一句话要点**：提出视觉自实现对齐方法，通过威胁相关图像微调视觉语言模型以解决安全对齐问题。

**关键词**：视觉语言模型, 安全对齐, 自实现机制, 威胁相关图像, 无标签微调

## 3 点简述
- 多模态大语言模型面临视觉输入导致有害输出的安全对齐问题。
- VSFA在无安全标签下，基于威胁相关图像构建中性VQA任务进行微调。
- 实验表明VSFA降低攻击成功率，提升响应质量，并缓解过度拒绝。

## 摘要（原文）

> Multimodal large language models (MLLMs) face safety misalignment, where visual inputs enable harmful outputs. To address this, existing methods require explicit safety labels or contrastive data; yet, threat-related concepts are concrete and visually depictable, while safety concepts, like helpfulness, are abstract and lack visual referents. Inspired by the Self-Fulfilling mechanism underlying emergent misalignment, we propose Visual Self-Fulfilling Alignment (VSFA). VSFA fine-tunes vision-language models (VLMs) on neutral VQA tasks constructed around threat-related images, without any safety labels. Through repeated exposure to threat-related visual content, models internalize the implicit semantics of vigilance and caution, shaping safety-oriented personas. Experiments across multiple VLMs and safety benchmarks demonstrate that VSFA reduces the attack success rate, improves response quality, and mitigates over-refusal while preserving general capabilities. Our work extends the self-fulfilling mechanism from text to visual modalities, offering a label-free approach to VLMs alignment.

