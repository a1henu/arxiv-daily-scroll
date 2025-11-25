---
layout: default
title: STCDiT: Spatio-Temporally Consistent Diffusion Transformer for High-Quality Video Super-Resolution
---

# STCDiT: Spatio-Temporally Consistent Diffusion Transformer for High-Quality Video Super-Resolution
**arXiv**：[2511.18786v1](https://arxiv.org/abs/2511.18786) · [PDF](https://arxiv.org/pdf/2511.18786.pdf)  
**作者**：Junyang Chen, Jiangxin Dong, Long Sun, Yixin Yang, Jinshan Pan  

**一句话要点**：提出STCDiT框架以解决复杂相机运动下视频超分辨率的时空一致性问题

**关键词**：视频超分辨率, 扩散变换器, 时空一致性, 运动感知重建, 锚帧引导

## 3 点简述
- 核心问题：视频超分辨率中保持时间稳定性和结构保真度，尤其在复杂相机运动场景下
- 方法要点：采用运动感知VAE分段重建和锚帧引导，提升结构保真和生成稳定性
- 实验或效果：广泛实验显示在结构保真和时间一致性上优于现有先进方法

## 摘要（原文）

> We present STCDiT, a video super-resolution framework built upon a pre-trained video diffusion model, aiming to restore structurally faithful and temporally stable videos from degraded inputs, even under complex camera motions. The main challenges lie in maintaining temporal stability during reconstruction and preserving structural fidelity during generation. To address these challenges, we first develop a motion-aware VAE reconstruction method that performs segment-wise reconstruction, with each segment clip exhibiting uniform motion characteristic, thereby effectively handling videos with complex camera motions. Moreover, we observe that the first-frame latent extracted by the VAE encoder in each clip, termed the anchor-frame latent, remains unaffected by temporal compression and retains richer spatial structural information than subsequent frame latents. We further develop an anchor-frame guidance approach that leverages structural information from anchor frames to constrain the generation process and improve structural fidelity of video features. Coupling these two designs enables the video diffusion model to achieve high-quality video super-resolution. Extensive experiments show that STCDiT outperforms state-of-the-art methods in terms of structural fidelity and temporal consistency.

