---
layout: default
title: QuEPT: Quantized Elastic Precision Transformers with One-Shot Calibration for Multi-Bit Switching
---

# QuEPT: Quantized Elastic Precision Transformers with One-Shot Calibration for Multi-Bit Switching
**arXiv**：[2602.12609v1](https://arxiv.org/abs/2602.12609) · [PDF](https://arxiv.org/pdf/2602.12609.pdf)  
**作者**：Ke Xu, Yixin Wang, Zhongcheng Li, Hao Cui, Jinshui Hu, Xingyi Zhang  

**一句话要点**：提出QuEPT，通过单次校准实现多比特切换，以解决Transformer弹性量化中的存储与优化成本问题。

**关键词**：弹性量化, 后训练量化, 多比特切换, Transformer优化, 低秩适配器, 单次校准

## 3 点简述
- 核心问题：Transformer架构弹性量化研究有限，存储和优化成本高，难以适应多比特部署场景。
- 方法要点：采用块级多比特误差重构与单次校准，结合MB-ToMe和MB-CLoRA增强精度与鲁棒性，支持实时切换量化模式。
- 实验或效果：在广泛实验中，QuEPT达到或超越现有后训练量化方法的性能，代码已开源。

## 摘要（原文）

> Elastic precision quantization enables multi-bit deployment via a single optimization pass, fitting diverse quantization scenarios.Yet, the high storage and optimization costs associated with the Transformer architecture, research on elastic quantization remains limited, particularly for large language models.This paper proposes QuEPT, an efficient post-training scheme that reconstructs block-wise multi-bit errors with one-shot calibration on a small data slice. It can dynamically adapt to various predefined bit-widths by cascading different low-rank adapters, and supports real-time switching between uniform quantization and mixed precision quantization without repeated optimization. To enhance accuracy and robustness, we introduce Multi-Bit Token Merging (MB-ToMe) to dynamically fuse token features across different bit-widths, improving robustness during bit-width switching. Additionally, we propose Multi-Bit Cascaded Low-Rank adapters (MB-CLoRA) to strengthen correlations between bit-width groups, further improve the overall performance of QuEPT. Extensive experiments demonstrate that QuEPT achieves comparable or better performance to existing state-of-the-art post-training quantization methods.Our code is available at https://github.com/xuke225/QuEPT

