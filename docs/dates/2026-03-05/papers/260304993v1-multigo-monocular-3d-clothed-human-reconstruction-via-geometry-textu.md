---
layout: default
title: MultiGO++: Monocular 3D Clothed Human Reconstruction via Geometry-Texture Collaboration
---

# MultiGO++: Monocular 3D Clothed Human Reconstruction via Geometry-Texture Collaboration
**arXiv**：[2603.04993v1](https://arxiv.org/abs/2603.04993) · [PDF](https://arxiv.org/pdf/2603.04993.pdf)  
**作者**：Nanjie Yao, Gangjian Zhang, Wenhao Shen, Jian Shu, Yu Feng, Hao Wang  

**一句话要点**：提出MultiGO++框架，通过几何-纹理协作实现单目图像3D穿衣人体重建

**关键词**：单目3D重建, 穿衣人体建模, 几何纹理协作, 多源纹理合成, 区域感知形状提取, 傅里叶几何编码

## 3 点简述
- 核心问题：现有方法受限于纹理数据不足、几何先验不准确和单模态监督偏差，导致重建效果不佳。
- 方法要点：采用多源纹理合成策略、区域感知形状提取模块和傅里叶几何编码器，结合双重建U-Net实现几何-纹理协作。
- 实验或效果：在多个基准测试和真实场景中优于现有方法，展示了高保真纹理3D人体网格的生成能力。

## 摘要（原文）

> Monocular 3D clothed human reconstruction aims to generate a complete and realistic textured 3D avatar from a single image. Existing methods are commonly trained under multi-view supervision with annotated geometric priors, and during inference, these priors are estimated by the pre-trained network from the monocular input. These methods are constrained by three key limitations: texturally by unavailability of training data, geometrically by inaccurate external priors, and systematically by biased single-modality supervision, all leading to suboptimal reconstruction. To address these issues, we propose a novel reconstruction framework, named MultiGO++, which achieves effective systematic geometry-texture collaboration. It consists of three core parts: (1) A multi-source texture synthesis strategy that constructs 15,000+ 3D textured human scans to improve the performance on texture quality estimation in challenge scenarios; (2) A region-aware shape extraction module that extracts and interacts features of each body region to obtain geometry information and a Fourier geometry encoder that mitigates the modality gap to achieve effective geometry learning; (3) A dual reconstruction U-Net that leverages geometry-texture collaborative features to refine and generate high-fidelity textured 3D human meshes. Extensive experiments on two benchmarks and many in-the-wild cases show the superiority of our method over state-of-the-art approaches.

