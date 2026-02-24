---
layout: default
title: InfScene-SR: Spatially Continuous Inference for Arbitrary-Size Image Super-Resolution
---

# InfScene-SR: Spatially Continuous Inference for Arbitrary-Size Image Super-Resolution
**arXiv**：[2602.19736v1](https://arxiv.org/abs/2602.19736) · [PDF](https://arxiv.org/pdf/2602.19736.pdf)  
**作者**：Shoukun Sun, Zhe Wang, Xiang Que, Jiyin Zhang, Xiaogang Ma  

**一句话要点**：提出InfScene-SR框架，通过引导融合机制实现任意尺寸图像的无缝超分辨率重建。

**关键词**：图像超分辨率, 扩散模型, 空间连续推理, 引导融合, 遥感图像处理

## 3 点简述
- 核心问题：基于扩散模型的超分辨率方法受限于固定尺寸训练，处理大图像时产生边界伪影。
- 方法要点：引入引导和方差校正融合机制，在迭代细化中实现空间连续生成，无需重新训练。
- 实验或效果：在遥感数据集上验证，消除边界伪影，提升感知质量，有益于下游语义分割任务。

## 摘要（原文）

> Image Super-Resolution (SR) aims to recover high-resolution (HR) details from low-resolution (LR) inputs, a task where Denoising Diffusion Probabilistic Models (DDPMs) have recently shown superior performance compared to Generative Adversarial Networks (GANs) based approaches. However, standard diffusion-based SR models, such as SR3, are typically trained on fixed-size patches and struggle to scale to arbitrary-sized images due to memory constraints. Applying these models via independent patch processing leads to visible seams and inconsistent textures across boundaries. In this paper, we propose InfScene-SR, a framework enabling spatially continuous super-resolution for large, arbitrary scenes. We adapt the iterative refinement process of diffusion models with a novel guided and variance-corrected fusion mechanism, allowing for the seamless generation of large-scale high-resolution imagery without retraining. We validate our approach on remote sensing datasets, demonstrating that InfScene-SR not only reconstructs fine details with high perceptual quality but also eliminates boundary artifacts, benefiting downstream tasks such as semantic segmentation.

