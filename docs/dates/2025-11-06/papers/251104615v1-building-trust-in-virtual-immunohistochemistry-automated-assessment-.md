---
layout: default
title: Building Trust in Virtual Immunohistochemistry: Automated Assessment of Image Quality
---

# Building Trust in Virtual Immunohistochemistry: Automated Assessment of Image Quality
**arXiv**：[2511.04615v1](https://arxiv.org/abs/2511.04615) · [PDF](https://arxiv.org/pdf/2511.04615.pdf)  
**作者**：Tushar Kataria, Shikha Dubey, Mary Bronner, Jolanta Jedrzkiewicz, Ben J. Brintz, Shireen Y. Elhabian, Beatrice S. Knudsen  

**一句话要点**：提出自动化框架评估虚拟免疫组化图像质量，以解决现有指标与染色准确性脱节问题。

**关键词**：虚拟免疫组化, 图像质量评估, 像素级准确性, 颜色反卷积, 全玻片图像, 深度学习模型

## 3 点简述
- 核心问题：现有图像保真度指标无法准确评估虚拟IHC染色准确性，与病理学家评估相关性差。
- 方法要点：通过颜色反卷积生成IHC阳性像素掩码，计算Dice等指标量化像素级染色准确性。
- 实验或效果：配对模型如PyramidPix2Pix表现最佳，全玻片图像评估揭示性能下降。

## 摘要（原文）

> Deep learning models can generate virtual immunohistochemistry (IHC) stains
> from hematoxylin and eosin (H&E) images, offering a scalable and low-cost
> alternative to laboratory IHC. However, reliable evaluation of image quality
> remains a challenge as current texture- and distribution-based metrics quantify
> image fidelity rather than the accuracy of IHC staining. Here, we introduce an
> automated and accuracy grounded framework to determine image quality across
> sixteen paired or unpaired image translation models. Using color deconvolution,
> we generate masks of pixels stained brown (i.e., IHC-positive) as predicted by
> each virtual IHC model. We use the segmented masks of real and virtual IHC to
> compute stain accuracy metrics (Dice, IoU, Hausdorff distance) that directly
> quantify correct pixel - level labeling without needing expert manual
> annotations. Our results demonstrate that conventional image fidelity metrics,
> including Frechet Inception Distance (FID), peak signal-to-noise ratio (PSNR),
> and structural similarity (SSIM), correlate poorly with stain accuracy and
> pathologist assessment. Paired models such as PyramidPix2Pix and AdaptiveNCE
> achieve the highest stain accuracy, whereas unpaired diffusion- and GAN-based
> models are less reliable in providing accurate IHC positive pixel labels.
> Moreover, whole-slide images (WSI) reveal performance declines that are
> invisible in patch-based evaluations, emphasizing the need for WSI-level
> benchmarks. Together, this framework defines a reproducible approach for
> assessing the quality of virtual IHC models, a critical step to accelerate
> translation towards routine use by pathologists.

