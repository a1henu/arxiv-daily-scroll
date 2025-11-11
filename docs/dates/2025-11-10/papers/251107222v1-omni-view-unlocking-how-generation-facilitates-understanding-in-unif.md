---
layout: default
title: Omni-View: Unlocking How Generation Facilitates Understanding in Unified 3D Model based on Multiview images
---

# Omni-View: Unlocking How Generation Facilitates Understanding in Unified 3D Model based on Multiview images
**arXiv**：[2511.07222v1](https://arxiv.org/abs/2511.07222) · [PDF](https://arxiv.org/pdf/2511.07222.pdf)  
**作者**：JiaKui Hu, Shanshan Zhao, Qing-Guo Chen, Xuerui Qiu, Jialun Liu, Zhao Xu, Weihua Luo, Kaifu Zhang, Yanye Lu  

**一句话要点**：提出Omni-View统一模型，基于多视图图像实现3D场景理解与生成的协同交互。

**关键词**：3D场景理解, 新视图合成, 多视图图像, 生成促进理解, 统一模型, 几何估计

## 3 点简述
- 核心问题：探索生成如何促进理解，统一3D场景的多模态任务。
- 方法要点：结合理解模型、纹理模块和几何模块，联合建模理解、新视图合成和几何估计。
- 实验或效果：在VSI-Bench基准上达到55.4分，优于现有专用模型，并在生成任务中表现强劲。

## 摘要（原文）

> This paper presents Omni-View, which extends the unified multimodal
> understanding and generation to 3D scenes based on multiview images, exploring
> the principle that "generation facilitates understanding". Consisting of
> understanding model, texture module, and geometry module, Omni-View jointly
> models scene understanding, novel view synthesis, and geometry estimation,
> enabling synergistic interaction between 3D scene understanding and generation
> tasks. By design, it leverages the spatiotemporal modeling capabilities of its
> texture module responsible for appearance synthesis, alongside the explicit
> geometric constraints provided by its dedicated geometry module, thereby
> enriching the model's holistic understanding of 3D scenes. Trained with a
> two-stage strategy, Omni-View achieves a state-of-the-art score of 55.4 on the
> VSI-Bench benchmark, outperforming existing specialized 3D understanding
> models, while simultaneously delivering strong performance in both novel view
> synthesis and 3D scene generation.

