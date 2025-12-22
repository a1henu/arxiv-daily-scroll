---
layout: default
title: LumiCtrl : Learning Illuminant Prompts for Lighting Control in Personalized Text-to-Image Models
---

# LumiCtrl : Learning Illuminant Prompts for Lighting Control in Personalized Text-to-Image Models
**arXiv**：[2512.17489v1](https://arxiv.org/abs/2512.17489) · [PDF](https://arxiv.org/pdf/2512.17489.pdf)  
**作者**：Muhammad Atif Butt, Kai Wang, Javier Vazquez-Corral, Joost Van De Weijer  

**一句话要点**：提出LumiCtrl方法，通过单张图像学习光照提示，以增强个性化文本到图像模型的光照控制能力。

**关键词**：光照控制, 文本到图像模型, 个性化学习, 提示学习, 图像生成, 视觉美学

## 3 点简述
- 核心问题：现有文本到图像模型缺乏对场景光照的精确控制，影响图像氛围和美学设计。
- 方法要点：基于物理的光照增强、边缘引导提示解耦和掩码重建损失，实现光照个性化学习。
- 实验或效果：在光照保真度、美学质量和场景一致性上优于基线，用户偏好研究证实其优势。

## 摘要（原文）

> Current text-to-image (T2I) models have demonstrated remarkable progress in creative image generation, yet they still lack precise control over scene illuminants, which is a crucial factor for content designers aiming to manipulate the mood, atmosphere, and visual aesthetics of generated images. In this paper, we present an illuminant personalization method named LumiCtrl that learns an illuminant prompt given a single image of an object. LumiCtrl consists of three basic components: given an image of the object, our method applies (a) physics-based illuminant augmentation along the Planckian locus to create fine-tuning variants under standard illuminants; (b) edge-guided prompt disentanglement using a frozen ControlNet to ensure prompts focus on illumination rather than structure; and (c) a masked reconstruction loss that focuses learning on the foreground object while allowing the background to adapt contextually, enabling what we call contextual light adaptation. We qualitatively and quantitatively compare LumiCtrl against other T2I customization methods. The results show that our method achieves significantly better illuminant fidelity, aesthetic quality, and scene coherence compared to existing personalization baselines. A human preference study further confirms strong user preference for LumiCtrl outputs. The code and data will be released upon publication.

