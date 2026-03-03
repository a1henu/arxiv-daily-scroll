---
layout: default
title: Benchmarking Semantic Segmentation Models via Appearance and Geometry Attribute Editing
---

# Benchmarking Semantic Segmentation Models via Appearance and Geometry Attribute Editing
**arXiv**：[2603.01535v1](https://arxiv.org/abs/2603.01535) · [PDF](https://arxiv.org/pdf/2603.01535.pdf)  
**作者**：Zijin Yin, Bing Li, Kongming Liang, Hao Sun, Zhongjiang He, Zhanyu Ma, Jun Guo  

**一句话要点**：提出Gen4Seg自动数据生成管道，通过编辑外观与几何属性来压力测试语义分割模型。

**关键词**：语义分割评估, 扩散模型编辑, 属性变化生成, 鲁棒性测试, 自动数据生成

## 3 点简述
- 核心问题：语义分割模型在复杂场景中的鲁棒性评估不足，现有方法多关注全局天气和风格变化。
- 方法要点：利用扩散模型精确编辑真实图像的对象和图像级外观与几何属性，重用现有分割标签以降低成本。
- 实验或效果：构建Pascal-EA和COCO-EA基准，测试多种模型，发现开放词汇模型在几何变化下鲁棒性未更优，数据增强技术对提升外观鲁棒性有限。

## 摘要（原文）

> Semantic segmentation takes pivotal roles in various applications such as autonomous driving and medical image analysis. When deploying segmentation models in practice, it is critical to test their behaviors in varied and complex scenes in advance. In this paper, we construct an automatic data generation pipeline Gen4Seg to stress-test semantic segmentation models by generating various challenging samples with different attribute changes. Beyond previous evaluation paradigms focusing solely on global weather and style transfer, we investigate variations in both appearance and geometry attributes at the object and image level. These include object color, material, size, position, as well as image-level variations such as weather and style. To achieve this, we propose to edit visual attributes of existing real images with precise control of structural information, empowered by diffusion models. In this way, the existing segmentation labels can be reused for the edited images, which greatly reduces the labor costs. Using our pipeline, we construct two new benchmarks, Pascal-EA and COCO-EA. We benchmark a wide variety of semantic segmentation models, spanning from closed-set models to open-vocabulary large models. We have several key findings: 1) advanced open-vocabulary models do not exhibit greater robustness compared to closed-set methods under geometric variations; 2) data augmentation techniques, such as CutOut and CutMix, are limited in enhancing robustness against appearance variations; 3) our pipeline can also be employed as a data augmentation tool and improve both in-distribution and out-of-distribution performances. Our work suggests the potential of generative models as effective tools for automatically analyzing segmentation models, and we hope our findings will assist practitioners and researchers in developing more robust and reliable segmentation models.

