---
layout: default
title: GEN3D: Generating Domain-Free 3D Scenes from a Single Image
---

# GEN3D: Generating Domain-Free 3D Scenes from a Single Image
**arXiv**：[2511.14291v1](https://arxiv.org/abs/2511.14291) · [PDF](https://arxiv.org/pdf/2511.14291.pdf)  
**作者**：Yuxin Zhang, Ziyu Lu, Hongbo Duan, Keyu Fan, Pengting Luo, Peiyu Zhuang, Mengyu Yang, Houde Liu  

**一句话要点**：提出Gen3D方法，从单图像生成通用3D场景以解决多视图依赖问题。

**关键词**：3D场景生成, 单图像重建, 高斯溅射, 世界模型, 神经3D重建

## 3 点简述
- 核心问题：神经3D重建依赖密集多视图，限制广泛应用。
- 方法要点：从RGBD图像创建点云，扩展世界模型，优化高斯溅射表示。
- 实验或效果：多数据集验证，生成高保真、一致新视图，泛化能力强。

## 摘要（原文）

> Despite recent advancements in neural 3D reconstruction, the dependence on dense multi-view captures restricts their broader applicability. Additionally, 3D scene generation is vital for advancing embodied AI and world models, which depend on diverse, high-quality scenes for learning and evaluation. In this work, we propose Gen3d, a novel method for generation of high-quality, wide-scope, and generic 3D scenes from a single image. After the initial point cloud is created by lifting the RGBD image, Gen3d maintains and expands its world model. The 3D scene is finalized through optimizing a Gaussian splatting representation. Extensive experiments on diverse datasets demonstrate the strong generalization capability and superior performance of our method in generating a world model and Synthesizing high-fidelity and consistent novel views.

