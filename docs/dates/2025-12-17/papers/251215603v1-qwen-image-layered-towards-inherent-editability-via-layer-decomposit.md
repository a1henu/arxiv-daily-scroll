---
layout: default
title: Qwen-Image-Layered: Towards Inherent Editability via Layer Decomposition
---

# Qwen-Image-Layered: Towards Inherent Editability via Layer Decomposition
**arXiv**：[2512.15603v1](https://arxiv.org/abs/2512.15603) · [PDF](https://arxiv.org/pdf/2512.15603.pdf)  
**作者**：Shengming Yin, Zekai Zhang, Zecheng Tang, Kaiyuan Gao, Xiao Xu, Kun Yan, Jiahao Li, Yilei Chen, Yuxiang Chen, Heung-Yeung Shum, Lionel M. Ni, Jingren Zhou, Junyang Lin, Chenfei Wu  

**一句话要点**：提出Qwen-Image-Layered，通过分层分解实现图像固有可编辑性

**关键词**：图像分层分解, RGBA-VAE, 可变层数分解, 一致图像编辑, 扩散模型, PSD数据提取

## 3 点简述
- 核心问题：现有视觉生成模型在图像编辑时因光栅图像纠缠导致一致性差。
- 方法要点：引入RGBA-VAE、VLD-MMDiT架构和多阶段训练策略，支持可变层数分解。
- 实验或效果：在分解质量上显著超越现有方法，建立一致图像编辑新范式。

## 摘要（原文）

> Recent visual generative models often struggle with consistency during image editing due to the entangled nature of raster images, where all visual content is fused into a single canvas. In contrast, professional design tools employ layered representations, allowing isolated edits while preserving consistency. Motivated by this, we propose \textbf{Qwen-Image-Layered}, an end-to-end diffusion model that decomposes a single RGB image into multiple semantically disentangled RGBA layers, enabling \textbf{inherent editability}, where each RGBA layer can be independently manipulated without affecting other content. To support variable-length decomposition, we introduce three key components: (1) an RGBA-VAE to unify the latent representations of RGB and RGBA images; (2) a VLD-MMDiT (Variable Layers Decomposition MMDiT) architecture capable of decomposing a variable number of image layers; and (3) a Multi-stage Training strategy to adapt a pretrained image generation model into a multilayer image decomposer. Furthermore, to address the scarcity of high-quality multilayer training images, we build a pipeline to extract and annotate multilayer images from Photoshop documents (PSD). Experiments demonstrate that our method significantly surpasses existing approaches in decomposition quality and establishes a new paradigm for consistent image editing. Our code and models are released on \href{https://github.com/QwenLM/Qwen-Image-Layered}{https://github.com/QwenLM/Qwen-Image-Layered}

