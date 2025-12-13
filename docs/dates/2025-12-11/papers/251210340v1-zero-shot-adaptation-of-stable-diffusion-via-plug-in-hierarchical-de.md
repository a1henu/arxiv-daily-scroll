---
layout: default
title: Zero-shot Adaptation of Stable Diffusion via Plug-in Hierarchical Degradation Representation for Real-World Super-Resolution
---

# Zero-shot Adaptation of Stable Diffusion via Plug-in Hierarchical Degradation Representation for Real-World Super-Resolution
**arXiv**：[2512.10340v1](https://arxiv.org/abs/2512.10340) · [PDF](https://arxiv.org/pdf/2512.10340.pdf)  
**作者**：Yi-Cheng Liao, Shyang-En Weng, Yu-Syuan Xu, Chi-Wei Hsiao, Wei-Chen Chiu, Ching-Chun Huang  

**一句话要点**：提出HD-CLIP插件模块，通过层次化退化表示实现稳定扩散的零样本适应，以解决真实世界超分辨率问题。

**关键词**：真实世界超分辨率, 稳定扩散, 零样本适应, 层次化退化表示, 即插即用模块, 分类器自由投影引导

## 3 点简述
- 核心问题：真实世界超分辨率中未知复杂退化导致现有方法泛化能力受限，CLIP文本编码器无法捕捉数值退化程度。
- 方法要点：HD-CLIP将低质量图像分解为语义嵌入和有序退化嵌入，支持未见退化级别的插值，并通过CFPG集成到扩散模型中。
- 实验或效果：作为即插即用模块，无需训练即可提升多种框架的细节保真度和感知真实感，在多样数据集上验证有效。

## 摘要（原文）

> Real-World Image Super-Resolution (Real-ISR) aims to recover high-quality images from low-quality inputs degraded by unknown and complex real-world factors. Real-world scenarios involve diverse and coupled degradations, making it necessary to provide diffusion models with richer and more informative guidance. However, existing methods often assume known degradation severity and rely on CLIP text encoders that cannot capture numerical severity, limiting their generalization ability. To address this, we propose \textbf{HD-CLIP} (\textbf{H}ierarchical \textbf{D}egradation CLIP), which decomposes a low-quality image into a semantic embedding and an ordinal degradation embedding that captures ordered relationships and allows interpolation across unseen levels. Furthermore, we integrated it into diffusion models via classifier-free guidance (CFG) and proposed classifier-free projection guidance (CFPG). HD-CLIP leverages semantic cues to guide generative restoration while using degradation cues to suppress undesired hallucinations and artifacts. As a \textbf{plug-and-play module}, HD-CLIP can be seamlessly integrated into various super-resolution frameworks without training, significantly improving detail fidelity and perceptual realism across diverse real-world datasets.

