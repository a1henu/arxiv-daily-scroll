---
layout: default
title: Universal Pansharpening Foundation Model
---

# Universal Pansharpening Foundation Model
**arXiv**：[2603.03831v1](https://arxiv.org/abs/2603.03831) · [PDF](https://arxiv.org/pdf/2603.03831.pdf)  
**作者**：Hebaixu Wang, Jing Zhang, Haonan Guo, Di Wang, Jiayi Ma, Bo Du, Liangpei Zhang  

**一句话要点**：提出FoundPS通用全色锐化基础模型，以解决卫星依赖和场景依赖问题，实现跨传感器和场景的稳健融合。

**关键词**：全色锐化, 基础模型, Transformer, 潜在扩散, 跨传感器融合, 遥感图像处理

## 3 点简述
- 核心问题：现有全色锐化方法卫星和场景依赖性强，泛化能力差，限制实际应用。
- 方法要点：引入模态交错Transformer学习波段模态专业化，构建潜在扩散桥模型和无限维像素-潜在交互机制。
- 实验或效果：在PSBench基准上广泛实验，FoundPS优于现有方法，展示优越泛化和稳健性。

## 摘要（原文）

> Pansharpening generates the high-resolution multi-spectral (MS) image by integrating spatial details from a texture-rich panchromatic (PAN) image and spectral attributes from a low-resolution MS image. Existing methods are predominantly satellite-specific and scene-dependent, which severely limits their generalization across heterogeneous sensors and varied scenes, thereby reducing their real-world practicality. To address these challenges, we present FoundPS, a universal pansharpening foundation model for satellite-agnostic and scene-robust fusion. Specifically, we introduce a modality-interleaved transformer that learns band-wise modal specializations to form reversible spectral affine bases, mapping arbitrary-band MS into a unified latent space via tensor multiplication. Building upon this, we construct a latent diffusion bridge model to progressively evolve latent representations, and incorporate bridge posterior sampling to couple latent diffusion with pixel-space observations, enabling stable and controllable fusion. Furthermore, we devise infinite-dimensional pixel-to-latent interaction mechanisms to comprehensively capture the cross-domain dependencies between PAN observations and MS representations, thereby facilitating complementary information fusion. In addition, to support large-scale training and evaluation, we construct a comprehensive pansharpening benchmark, termed PSBench, consisting of worldwide MS and PAN image pairs from multiple satellites across diverse scenes. Extensive experiments demonstrate that FoundPS consistently outperforms state-of-the-art methods, exhibiting superior generalization and robustness across a wide range of pansharpening tasks.

