---
layout: default
title: Bridging Fidelity-Reality with Controllable One-Step Diffusion for Image Super-Resolution
---

# Bridging Fidelity-Reality with Controllable One-Step Diffusion for Image Super-Resolution
**arXiv**：[2512.14061v1](https://arxiv.org/abs/2512.14061) · [PDF](https://arxiv.org/pdf/2512.14061.pdf)  
**作者**：Hao Chen, Junyang Chen, Jinshan Pan, Jiangxin Dong  

**一句话要点**：提出可控一步扩散网络CODSR以解决图像超分辨率中的保真度与感知质量平衡问题

**关键词**：图像超分辨率, 一步扩散模型, 可控生成, 保真度增强, 文本引导

## 3 点简述
- 核心问题：现有一步扩散方法存在保真度不足、生成先验激活不充分及文本提示与语义区域不对齐
- 方法要点：引入低质量引导特征调制模块、区域自适应生成先验激活方法和文本匹配引导策略
- 实验或效果：在高效一步推理下，CODSR实现优越感知质量和竞争性保真度

## 摘要（原文）

> Recent diffusion-based one-step methods have shown remarkable progress in the field of image super-resolution, yet they remain constrained by three critical limitations: (1) inferior fidelity performance caused by the information loss from compression encoding of low-quality (LQ) inputs; (2) insufficient region-discriminative activation of generative priors; (3) misalignment between text prompts and their corresponding semantic regions. To address these limitations, we propose CODSR, a controllable one-step diffusion network for image super-resolution. First, we propose an LQ-guided feature modulation module that leverages original uncompressed information from LQ inputs to provide high-fidelity conditioning for the diffusion process. We then develop a region-adaptive generative prior activation method to effectively enhance perceptual richness without sacrificing local structural fidelity. Finally, we employ a text-matching guidance strategy to fully harness the conditioning potential of text prompts. Extensive experiments demonstrate that CODSR achieves superior perceptual quality and competitive fidelity compared with state-of-the-art methods with efficient one-step inference.

