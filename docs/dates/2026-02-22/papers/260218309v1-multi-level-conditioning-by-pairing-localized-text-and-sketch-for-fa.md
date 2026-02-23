---
layout: default
title: Multi-Level Conditioning by Pairing Localized Text and Sketch for Fashion Image Generation
---

# Multi-Level Conditioning by Pairing Localized Text and Sketch for Fashion Image Generation
**arXiv**：[2602.18309v1](https://arxiv.org/abs/2602.18309) · [PDF](https://arxiv.org/pdf/2602.18309.pdf)  
**作者**：Ziyue Liu, Davide Talon, Federico Girella, Zanxi Ruan, Mattia Mondo, Loris Bazzani, Yiming Wang, Marco Cristani  

**一句话要点**：提出LOTS框架，通过多级条件化结合局部文本与草图增强时尚图像生成

**关键词**：时尚图像生成, 多模态条件化, 扩散模型, 草图引导, 局部文本指导, 数据集构建

## 3 点简述
- 核心问题：如何有效结合文本和草图模态，在保持草图结构的同时利用文本的局部属性指导时尚图像生成
- 方法要点：采用多级条件化阶段独立编码局部特征，并通过扩散模型中的注意力引导整合局部与全局条件
- 实验或效果：在Sketchy数据集上验证，方法在全局结构遵循和局部语义指导方面优于现有技术，并公开数据集和代码

## 摘要（原文）

> Sketches offer designers a concise yet expressive medium for early-stage fashion ideation by specifying structure, silhouette, and spatial relationships, while textual descriptions complement sketches to convey material, color, and stylistic details. Effectively combining textual and visual modalities requires adherence to the sketch visual structure when leveraging the guidance of localized attributes from text. We present LOcalized Text and Sketch with multi-level guidance (LOTS), a framework that enhances fashion image generation by combining global sketch guidance with multiple localized sketch-text pairs. LOTS employs a Multi-level Conditioning Stage to independently encode local features within a shared latent space while maintaining global structural coordination. Then, the Diffusion Pair Guidance stage integrates both local and global conditioning via attention-based guidance within the diffusion model's multi-step denoising process. To validate our method, we develop Sketchy, the first fashion dataset where multiple text-sketch pairs are provided per image. Sketchy provides high-quality, clean sketches with a professional look and consistent structure. To assess robustness beyond this setting, we also include an "in the wild" split with non-expert sketches, featuring higher variability and imperfections. Experiments demonstrate that our method strengthens global structural adherence while leveraging richer localized semantic guidance, achieving improvement over state-of-the-art. The dataset, platform, and code are publicly available.

