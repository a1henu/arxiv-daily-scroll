---
layout: default
title: Physics Informed Generative AI Enabling Labour Free Segmentation For Microscopy Analysis
---

# Physics Informed Generative AI Enabling Labour Free Segmentation For Microscopy Analysis
**arXiv**：[2602.01710v1](https://arxiv.org/abs/2602.01710) · [PDF](https://arxiv.org/pdf/2602.01710.pdf)  
**作者**：Salma Zahran, Zhou Ao, Zhengyang Zhang, Chen Chi, Chenchen Yuan, Yanming Wang  

**一句话要点**：提出基于物理模拟与生成对抗网络的免标注分割框架，以解决显微镜图像语义分割的数据稀缺问题。

**关键词**：显微镜图像分割, 物理模拟, 生成对抗网络, 域适应, 语义分割, 材料表征

## 3 点简述
- 核心问题：显微镜图像语义分割依赖专家标注，成本高且数据稀缺，模拟数据因域差距难以泛化。
- 方法要点：利用相场模拟生成完美标注的微结构形态，通过CycleGAN将模拟图像转换为高保真实SEM图像。
- 实验或效果：仅用合成数据训练的U-Net在未见实验图像上实现高精度分割，边界F1分数0.90，IOU 0.88。

## 摘要（原文）

> Semantic segmentation of microscopy images is a critical task for high-throughput materials characterisation, yet its automation is severely constrained by the prohibitive cost, subjectivity, and scarcity of expert-annotated data. While physics-based simulations offer a scalable alternative to manual labelling, models trained on such data historically fail to generalise due to a significant domain gap, lacking the complex textures, noise patterns, and imaging artefacts inherent to experimental data. This paper introduces a novel framework for labour-free segmentation that successfully bridges this simulation-to-reality gap. Our pipeline leverages phase-field simulations to generate an abundant source of microstructural morphologies with perfect, intrinsically-derived ground-truth masks. We then employ a Cycle-Consistent Generative Adversarial Network (CycleGAN) for unpaired image-to-image translation, transforming the clean simulations into a large-scale dataset of high-fidelity, realistic SEM images. A U-Net model, trained exclusively on this synthetic data, demonstrated remarkable generalisation when deployed on unseen experimental images, achieving a mean Boundary F1-Score of 0.90 and an Intersection over Union (IOU) of 0.88. Comprehensive validation using t-SNE feature-space projection and Shannon entropy analysis confirms that our synthetic images are statistically and featurally indistinguishable from the real data manifold. By completely decoupling model training from manual annotation, our generative framework transforms a data-scarce problem into one of data abundance, providing a robust and fully automated solution to accelerate materials discovery and analysis.

