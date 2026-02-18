---
layout: default
title: RPT-SR: Regional Prior attention Transformer for infrared image Super-Resolution
---

# RPT-SR: Regional Prior attention Transformer for infrared image Super-Resolution
**arXiv**：[2602.15490v1](https://arxiv.org/abs/2602.15490) · [PDF](https://arxiv.org/pdf/2602.15490.pdf)  
**作者**：Youngwan Jin, Incheol Park, Yagiz Nalcakan, Hyeongjin Ju, Sanghyeop Yeo, Shiho Kim  

**一句话要点**：提出RPT-SR，利用区域先验注意力Transformer解决固定视角红外图像超分辨率中的冗余学习问题。

**关键词**：红外图像超分辨率, Transformer, 区域先验注意力, 双令牌框架, 固定视角场景

## 3 点简述
- 核心问题：通用超分辨率模型在固定视角红外场景中忽略空间先验，导致性能不佳。
- 方法要点：引入双令牌框架，融合可学习区域先验令牌与局部令牌，动态调制重建过程。
- 实验或效果：在长波和短波红外数据集上验证，实现新的最先进性能。

## 摘要（原文）

> General-purpose super-resolution models, particularly Vision Transformers, have achieved remarkable success but exhibit fundamental inefficiencies in common infrared imaging scenarios like surveillance and autonomous driving, which operate from fixed or nearly-static viewpoints. These models fail to exploit the strong, persistent spatial priors inherent in such scenes, leading to redundant learning and suboptimal performance. To address this, we propose the Regional Prior attention Transformer for infrared image Super-Resolution (RPT-SR), a novel architecture that explicitly encodes scene layout information into the attention mechanism. Our core contribution is a dual-token framework that fuses (1) learnable, regional prior tokens, which act as a persistent memory for the scene's global structure, with (2) local tokens that capture the frame-specific content of the current input. By utilizing these tokens into an attention, our model allows the priors to dynamically modulate the local reconstruction process. Extensive experiments validate our approach. While most prior works focus on a single infrared band, we demonstrate the broad applicability and versatility of RPT-SR by establishing new state-of-the-art performance across diverse datasets covering both Long-Wave (LWIR) and Short-Wave (SWIR) spectra

