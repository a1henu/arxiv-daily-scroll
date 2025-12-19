---
layout: default
title: FrameDiffuser: G-Buffer-Conditioned Diffusion for Neural Forward Frame Rendering
---

# FrameDiffuser: G-Buffer-Conditioned Diffusion for Neural Forward Frame Rendering
**arXiv**：[2512.16670v1](https://arxiv.org/abs/2512.16670) · [PDF](https://arxiv.org/pdf/2512.16670.pdf)  
**作者**：Ole Beisswenger, Jan-Niklas Dihlmann, Hendrik P. A. Lensch  

**一句话要点**：提出FrameDiffuser以解决交互式应用中基于G-buffer的神经前向帧渲染的时序一致性和计算效率问题。

**关键词**：神经渲染, 扩散模型, 时序一致性, G-buffer条件, 自回归生成, 环境特定训练

## 3 点简述
- 核心问题：现有扩散模型在G-buffer条件图像合成中缺乏时序一致性或计算成本过高，不适合交互式应用。
- 方法要点：采用自回归框架，结合ControlNet和ControlLoRA进行结构和时序双重条件控制，实现稳定生成。
- 实验或效果：通过环境特定训练，在数百至数千帧中保持时序一致，提升光照、阴影和反射的逼真度。

## 摘要（原文）

> Neural rendering for interactive applications requires translating geometric and material properties (G-buffer) to photorealistic images with realistic lighting on a frame-by-frame basis. While recent diffusion-based approaches show promise for G-buffer-conditioned image synthesis, they face critical limitations: single-image models like RGBX generate frames independently without temporal consistency, while video models like DiffusionRenderer are too computationally expensive for most consumer gaming sets ups and require complete sequences upfront, making them unsuitable for interactive applications where future frames depend on user input. We introduce FrameDiffuser, an autoregressive neural rendering framework that generates temporally consistent, photorealistic frames by conditioning on G-buffer data and the models own previous output. After an initial frame, FrameDiffuser operates purely on incoming G-buffer data, comprising geometry, materials, and surface properties, while using its previously generated frame for temporal guidance, maintaining stable, temporal consistent generation over hundreds to thousands of frames. Our dual-conditioning architecture combines ControlNet for structural guidance with ControlLoRA for temporal coherence. A three-stage training strategy enables stable autoregressive generation. We specialize our model to individual environments, prioritizing consistency and inference speed over broad generalization, demonstrating that environment-specific training achieves superior photorealistic quality with accurate lighting, shadows, and reflections compared to generalized approaches.

