---
layout: default
title: Synthetic Crop-Weed Image Generation and its Impact on Model Generalization
---

# Synthetic Crop-Weed Image Generation and its Impact on Model Generalization
**arXiv**：[2511.02417v1](https://arxiv.org/abs/2511.02417) · [PDF](https://arxiv.org/pdf/2511.02417.pdf)  
**作者**：Garen Boyadjian, Cyrille Pierre, Johann Laconte, Riccardo Bertoglio  

**一句话要点**：提出基于Blender的合成作物-杂草图像生成流程，以提升农业除草机器人的语义分割模型泛化能力。

**关键词**：语义分割, 合成数据生成, 农业机器人, 域适应, Blender模拟

## 3 点简述
- 核心问题：真实农田图像标注成本高，合成数据与真实图像存在域差距。
- 方法要点：使用Blender程序化生成多样条件下的合成图像，包括植物生长、杂草密度等。
- 实验或效果：合成数据训练模型在跨域泛化中优于真实数据，sim-to-real差距为10%。

## 摘要（原文）

> Precise semantic segmentation of crops and weeds is necessary for
> agricultural weeding robots. However, training deep learning models requires
> large annotated datasets, which are costly to obtain in real fields. Synthetic
> data can reduce this burden, but the gap between simulated and real images
> remains a challenge. In this paper, we present a pipeline for procedural
> generation of synthetic crop-weed images using Blender, producing annotated
> datasets under diverse conditions of plant growth, weed density, lighting, and
> camera angle. We benchmark several state-of-the-art segmentation models on
> synthetic and real datasets and analyze their cross-domain generalization. Our
> results show that training on synthetic images leads to a sim-to-real gap of
> 10%, surpassing previous state-of-the-art methods. Moreover, synthetic data
> demonstrates good generalization properties, outperforming real datasets in
> cross-domain scenarios. These findings highlight the potential of synthetic
> agricultural datasets and support hybrid strategies for more efficient model
> training.

