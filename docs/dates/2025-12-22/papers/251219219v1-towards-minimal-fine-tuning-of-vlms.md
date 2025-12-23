---
layout: default
title: Towards Minimal Fine-Tuning of VLMs
---

# Towards Minimal Fine-Tuning of VLMs
**arXiv**：[2512.19219v1](https://arxiv.org/abs/2512.19219) · [PDF](https://arxiv.org/pdf/2512.19219.pdf)  
**作者**：Tiange Luo, Lajanugen Logeswaran, Jaekyeom Kim, Justin Johnson, Honglak Lee  

**一句话要点**：提出Image-LoRA以轻量化微调视觉语言模型，提升参数效率并保持性能。

**关键词**：视觉语言模型, 参数高效微调, 低秩适配, 注意力机制, 轻量化训练

## 3 点简述
- 核心问题：标准LoRA在微调视觉语言模型时计算开销大，可能影响文本推理能力。
- 方法要点：仅对视觉令牌跨度的注意力层值路径应用低秩适配，并选择部分注意力头进行优化。
- 实验或效果：在多种基准测试中匹配或接近标准LoRA准确度，参数和计算量更低，且保持文本推理性能。

## 摘要（原文）

> We introduce Image-LoRA, a lightweight parameter efficient fine-tuning (PEFT) recipe for transformer-based vision-language models (VLMs). Image-LoRA applies low-rank adaptation only to the value path of attention layers within the visual-token span, reducing adapter-only training FLOPs roughly in proportion to the visual-token fraction. We further adapt only a subset of attention heads, selected using head influence scores estimated with a rank-1 Image-LoRA, and stabilize per-layer updates via selection-size normalization. Across screen-centric grounding and referring benchmarks spanning text-heavy to image-heavy regimes, Image-LoRA matches or closely approaches standard LoRA accuracy while using fewer trainable parameters and lower adapter-only training FLOPs. The method also preserves the pure-text reasoning performance of VLMs before and after fine-tuning, as further shown on GSM8K.

