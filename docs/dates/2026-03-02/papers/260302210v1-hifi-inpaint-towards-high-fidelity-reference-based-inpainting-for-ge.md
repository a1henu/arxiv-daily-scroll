---
layout: default
title: HiFi-Inpaint: Towards High-Fidelity Reference-Based Inpainting for Generating Detail-Preserving Human-Product Images
---

# HiFi-Inpaint: Towards High-Fidelity Reference-Based Inpainting for Generating Detail-Preserving Human-Product Images
**arXiv**：[2603.02210v1](https://arxiv.org/abs/2603.02210) · [PDF](https://arxiv.org/pdf/2603.02210.pdf)  
**作者**：Yichen Liu, Donghao Zhou, Jie Wang, Xin Gao, Guisheng Liu, Jiatong Li, Quanwei Zhang, Qiang Lyu, Lanqing Guo, Shilei Wen, Weiqiang Wang, Pheng-Ann Heng  

**一句话要点**：提出HiFi-Inpaint框架，通过共享增强注意力和细节感知损失，解决人-产品图像生成中产品细节保真度不足的问题。

**关键词**：参考修复, 图像生成, 细节保留, 注意力机制, 损失函数, 人-产品图像

## 3 点简述
- 核心问题：现有基于参考的修复方法在训练数据、产品细节保留和精确监督方面存在局限。
- 方法要点：引入共享增强注意力优化细粒度产品特征，使用细节感知损失进行像素级监督。
- 实验或效果：构建HP-Image-40K数据集，实验显示HiFi-Inpaint在细节保留上达到先进水平。

## 摘要（原文）

> Human-product images, which showcase the integration of humans and products, play a vital role in advertising, e-commerce, and digital marketing. The essential challenge of generating such images lies in ensuring the high-fidelity preservation of product details. Among existing paradigms, reference-based inpainting offers a targeted solution by leveraging product reference images to guide the inpainting process. However, limitations remain in three key aspects: the lack of diverse large-scale training data, the struggle of current models to focus on product detail preservation, and the inability of coarse supervision for achieving precise guidance. To address these issues, we propose HiFi-Inpaint, a novel high-fidelity reference-based inpainting framework tailored for generating human-product images. HiFi-Inpaint introduces Shared Enhancement Attention (SEA) to refine fine-grained product features and Detail-Aware Loss (DAL) to enforce precise pixel-level supervision using high-frequency maps. Additionally, we construct a new dataset, HP-Image-40K, with samples curated from self-synthesis data and processed with automatic filtering. Experimental results show that HiFi-Inpaint achieves state-of-the-art performance, delivering detail-preserving human-product images.

