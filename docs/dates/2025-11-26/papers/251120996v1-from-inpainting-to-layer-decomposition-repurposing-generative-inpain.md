---
layout: default
title: From Inpainting to Layer Decomposition: Repurposing Generative Inpainting Models for Image Layer Decomposition
---

# From Inpainting to Layer Decomposition: Repurposing Generative Inpainting Models for Image Layer Decomposition
**arXiv**：[2511.20996v1](https://arxiv.org/abs/2511.20996) · [PDF](https://arxiv.org/pdf/2511.20996.pdf)  
**作者**：Jingxi Chen, Yixiao Zhang, Xiaoye Qian, Zongxia Li, Cornelia Fermuller, Caren Chen, Yiannis Aloimonos  

**一句话要点**：提出基于扩散修复模型的图像层分解方法，用于独立编辑图像元素。

**关键词**：图像层分解, 扩散模型, 修复任务, 多模态融合, 合成数据集, 图像编辑

## 3 点简述
- 核心问题：单图像层分解因方法和数据有限而具挑战性。
- 方法要点：轻量微调扩散修复模型，引入多模态上下文融合模块。
- 实验或效果：在合成数据集上训练，实现优越的对象移除和遮挡恢复性能。

## 摘要（原文）

> Images can be viewed as layered compositions, foreground objects over background, with potential occlusions. This layered representation enables independent editing of elements, offering greater flexibility for content creation. Despite the progress in large generative models, decomposing a single image into layers remains challenging due to limited methods and data. We observe a strong connection between layer decomposition and in/outpainting tasks, and propose adapting a diffusion-based inpainting model for layer decomposition using lightweight finetuning. To further preserve detail in the latent space, we introduce a novel multi-modal context fusion module with linear attention complexity. Our model is trained purely on a synthetic dataset constructed from open-source assets and achieves superior performance in object removal and occlusion recovery, unlocking new possibilities in downstream editing and creative applications.

