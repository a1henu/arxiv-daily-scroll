---
layout: default
title: ViSA: 3D-Aware Video Shading for Real-Time Upper-Body Avatar Creation
---

# ViSA: 3D-Aware Video Shading for Real-Time Upper-Body Avatar Creation
**arXiv**：[2512.07720v1](https://arxiv.org/abs/2512.07720) · [PDF](https://arxiv.org/pdf/2512.07720.pdf)  
**作者**：Fan Yang, Heyuan Li, Peihao Li, Weihao Yuan, Lingteng Qiu, Chaoyue Song, Cheng Chen, Yisheng He, Shifeng Zhang, Xiaoguang Han, Steven Hoi, Guosheng Lin  

**一句话要点**：提出ViSA框架，结合3D重建与视频生成，实现实时高保真上身虚拟人创建。

**关键词**：3D虚拟人生成, 视频扩散模型, 实时渲染, 上身虚拟人, 结构先验

## 3 点简述
- 核心问题：单图像生成上身3D虚拟人存在纹理模糊、运动僵硬或结构不稳定问题。
- 方法要点：使用3D重建模型提供结构先验，引导实时自回归视频扩散模型渲染细节与动态。
- 实验或效果：显著减少伪影，提升视觉质量，适用于游戏和虚拟现实等实时应用。

## 摘要（原文）

> Generating high-fidelity upper-body 3D avatars from one-shot input image remains a significant challenge. Current 3D avatar generation methods, which rely on large reconstruction models, are fast and capable of producing stable body structures, but they often suffer from artifacts such as blurry textures and stiff, unnatural motion. In contrast, generative video models show promising performance by synthesizing photorealistic and dynamic results, but they frequently struggle with unstable behavior, including body structural errors and identity drift. To address these limitations, we propose a novel approach that combines the strengths of both paradigms. Our framework employs a 3D reconstruction model to provide robust structural and appearance priors, which in turn guides a real-time autoregressive video diffusion model for rendering. This process enables the model to synthesize high-frequency, photorealistic details and fluid dynamics in real time, effectively reducing texture blur and motion stiffness while preventing the structural inconsistencies common in video generation methods. By uniting the geometric stability of 3D reconstruction with the generative capabilities of video models, our method produces high-fidelity digital avatars with realistic appearance and dynamic, temporally coherent motion. Experiments demonstrate that our approach significantly reduces artifacts and achieves substantial improvements in visual quality over leading methods, providing a robust and efficient solution for real-time applications such as gaming and virtual reality. Project page: https://lhyfst.github.io/visa

