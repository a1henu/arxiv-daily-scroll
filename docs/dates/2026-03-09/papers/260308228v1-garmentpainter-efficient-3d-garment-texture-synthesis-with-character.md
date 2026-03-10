---
layout: default
title: GarmentPainter: Efficient 3D Garment Texture Synthesis with Character-Guided Diffusion Model
---

# GarmentPainter: Efficient 3D Garment Texture Synthesis with Character-Guided Diffusion Model
**arXiv**：[2603.08228v1](https://arxiv.org/abs/2603.08228) · [PDF](https://arxiv.org/pdf/2603.08228.pdf)  
**作者**：Jinbo Wu, Xiaobo Gao, Xing Liu, Chen Zhao, Jialun Liu  

**一句话要点**：提出GarmentPainter框架，利用UV位置图和角色参考高效合成3D一致服装纹理

**关键词**：3D服装纹理合成, UV空间扩散模型, 角色引导生成, 纹理一致性, 高效计算

## 3 点简述
- 核心问题：现有方法在3D一致性、计算效率或灵活性上不足，难以生成高质量服装纹理
- 方法要点：使用UV位置图作为3D结构引导，结合角色参考图像通过扩散模型在UV空间合成纹理
- 实验或效果：在视觉保真度、3D一致性和计算效率上优于现有方法，实现高效可控的纹理生成

## 摘要（原文）

> Generating high-fidelity, 3D-consistent garment textures remains a challenging problem due to the inherent complexities of garment structures and the stringent requirement for detailed, globally consistent texture synthesis. Existing approaches either rely on 2D-based diffusion models, which inherently struggle with 3D consistency, require expensive multi-step optimization or depend on strict spatial alignment between 2D reference images and 3D meshes, which limits their flexibility and scalability. In this work, we introduce GarmentPainter, a simple yet efficient framework for synthesizing high-quality, 3D-aware garment textures in UV space. Our method leverages a UV position map as the 3D structural guidance, ensuring texture consistency across the garment surface during texture generation. To enhance control and adaptability, we introduce a type selection module, enabling fine-grained texture generation for specific garment components based on a character reference image, without requiring alignment between the reference image and the 3D mesh. GarmentPainter efficiently integrates all guidance signals into the input of a diffusion model in a spatially aligned manner, without modifying the underlying UNet architecture. Extensive experiments demonstrate that GarmentPainter achieves state-of-the-art performance in terms of visual fidelity, 3D consistency, and computational efficiency, outperforming existing methods in both qualitative and quantitative evaluations.

