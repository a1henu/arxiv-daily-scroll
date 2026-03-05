---
layout: default
title: Dual Diffusion Models for Multi-modal Guided 3D Avatar Generation
---

# Dual Diffusion Models for Multi-modal Guided 3D Avatar Generation
**arXiv**：[2603.04307v1](https://arxiv.org/abs/2603.04307) · [PDF](https://arxiv.org/pdf/2603.04307.pdf)  
**作者**：Hong Li, Yutang Feng, Minqi Meng, Yichen Yang, Xuhui Liu, Baochang Zhang  

**一句话要点**：提出PromptAvatar框架，通过双扩散模型从多模态提示快速生成高保真3D虚拟形象

**关键词**：3D虚拟形象生成, 多模态引导, 扩散模型, 纹理扩散, 几何扩散, 快速推理

## 3 点简述
- 现有方法在细粒度语义控制和推理速度上存在不足，且高质量3D面部数据稀缺
- 构建大规模多模态数据集，并集成纹理和几何扩散模型，实现从文本/图像到3D的直接映射
- 实验表明，该方法在10秒内生成无阴影高保真3D虚拟形象，质量和效率优于现有技术

## 摘要（原文）

> Generating high-fidelity 3D avatars from text or image prompts is highly sought after in virtual reality and human-computer interaction. However, existing text-driven methods often rely on iterative Score Distillation Sampling (SDS) or CLIP optimization, which struggle with fine-grained semantic control and suffer from excessively slow inference. Meanwhile, image-driven approaches are severely bottlenecked by the scarcity and high acquisition cost of high-quality 3D facial scans, limiting model generalization. To address these challenges, we first construct a novel, large-scale dataset comprising over 100,000 pairs across four modalities: fine-grained textual descriptions, in-the-wild face images, high-quality light-normalized texture UV maps, and 3D geometric shapes. Leveraging this comprehensive dataset, we propose PromptAvatar, a framework featuring dual diffusion models. Specifically, it integrates a Texture Diffusion Model (TDM) that supports flexible multi-condition guidance from text and/or image prompts, alongside a Geometry Diffusion Model (GDM) guided by text prompts. By learning the direct mapping from multi-modal prompts to 3D representations, PromptAvatar eliminates the need for time-consuming iterative optimization, successfully generating high-fidelity, shading-free 3D avatars in under 10 seconds. Extensive quantitative and qualitative experiments demonstrate that our method significantly outperforms existing state-of-the-art approaches in generation quality, fine-grained detail alignment, and computational efficiency.

