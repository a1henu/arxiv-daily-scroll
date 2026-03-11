---
layout: default
title: QUSR: Quality-Aware and Uncertainty-Guided Image Super-Resolution Diffusion Model
---

# QUSR: Quality-Aware and Uncertainty-Guided Image Super-Resolution Diffusion Model
**arXiv**：[2603.09125v1](https://arxiv.org/abs/2603.09125) · [PDF](https://arxiv.org/pdf/2603.09125.pdf)  
**作者**：Junjie Yin, Jiaju Li, Hanfa Xing  

**一句话要点**：提出QUSR扩散模型，集成质量感知先验和不确定性引导噪声生成，以解决真实场景中未知非均匀退化导致的细节丢失或伪影问题。

**关键词**：图像超分辨率, 扩散模型, 不确定性引导, 质量感知先验, 真实场景处理

## 3 点简述
- 核心问题：真实场景图像超分辨率中，未知且空间非均匀的退化常导致细节丢失或视觉伪影。
- 方法要点：引入不确定性引导噪声生成模块，自适应调整噪声注入强度，以重建复杂细节并保留原始信息。
- 实验或效果：实验证实QUSR能在真实场景中生成高保真和高真实感的图像，代码已开源。

## 摘要（原文）

> Diffusion-based image super-resolution (ISR) has shown strong potential, but it still struggles in real-world scenarios where degradations are unknown and spatially non-uniform, often resulting in lost details or visual artifacts. To address this challenge, we propose a novel super-resolution diffusion model, QUSR, which integrates a Quality-Aware Prior (QAP) with an Uncertainty-Guided Noise Generation (UNG) module. The UNG module adaptively adjusts the noise injection intensity, applying stronger perturbations to high-uncertainty regions (e.g., edges and textures) to reconstruct complex details, while minimizing noise in low-uncertainty regions (e.g., flat areas) to preserve original information. Concurrently, the QAP leverages an advanced Multimodal Large Language Model (MLLM) to generate reliable quality descriptions, providing an effective and interpretable quality prior for the restoration process. Experimental results confirm that QUSR can produce high-fidelity and high-realism images in real-world scenarios. The source code is available at https://github.com/oTvTog/QUSR.

