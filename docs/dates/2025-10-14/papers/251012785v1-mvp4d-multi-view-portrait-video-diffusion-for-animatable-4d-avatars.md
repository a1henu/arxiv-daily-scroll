---
layout: default
title: MVP4D: Multi-View Portrait Video Diffusion for Animatable 4D Avatars
---

# MVP4D: Multi-View Portrait Video Diffusion for Animatable 4D Avatars
**arXiv**：[2510.12785v1](https://arxiv.org/abs/2510.12785) · [PDF](https://arxiv.org/pdf/2510.12785.pdf)  
**作者**：Felix Taubner, Ruihang Zhang, Mathieu Tuli, Sherwin Bahmani, David B. Lindell  

**一句话要点**：提出MVP4D模型，基于单参考图像生成可动画4D虚拟人，提升多视角真实感

**关键词**：4D虚拟人, 多视角视频生成, 视频扩散模型, 实时渲染, 单图像动画

## 3 点简述
- 核心问题：单图像生成虚拟人时，视角偏离导致质量下降，缺乏多视角约束
- 方法要点：基于预训练视频扩散模型，生成多视角视频并蒸馏为实时渲染4D虚拟人
- 实验或效果：相比先前方法，显著改进真实感、时间一致性和3D一致性

## 摘要（原文）

> Digital human avatars aim to simulate the dynamic appearance of humans in
> virtual environments, enabling immersive experiences across gaming, film,
> virtual reality, and more. However, the conventional process for creating and
> animating photorealistic human avatars is expensive and time-consuming,
> requiring large camera capture rigs and significant manual effort from
> professional 3D artists. With the advent of capable image and video generation
> models, recent methods enable automatic rendering of realistic animated avatars
> from a single casually captured reference image of a target subject. While
> these techniques significantly lower barriers to avatar creation and offer
> compelling realism, they lack constraints provided by multi-view information or
> an explicit 3D representation. So, image quality and realism degrade when
> rendered from viewpoints that deviate strongly from the reference image. Here,
> we build a video model that generates animatable multi-view videos of digital
> humans based on a single reference image and target expressions. Our model,
> MVP4D, is based on a state-of-the-art pre-trained video diffusion model and
> generates hundreds of frames simultaneously from viewpoints varying by up to
> 360 degrees around a target subject. We show how to distill the outputs of this
> model into a 4D avatar that can be rendered in real-time. Our approach
> significantly improves the realism, temporal consistency, and 3D consistency of
> generated avatars compared to previous methods.

