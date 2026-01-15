---
layout: default
title: Knowledge-Embedded and Hypernetwork-Guided Few-Shot Substation Meter Defect Image Generation Method
---

# Knowledge-Embedded and Hypernetwork-Guided Few-Shot Substation Meter Defect Image Generation Method
**arXiv**：[2601.09238v1](https://arxiv.org/abs/2601.09238) · [PDF](https://arxiv.org/pdf/2601.09238.pdf)  
**作者**：Jackie Alex, Justin Petter  

**一句话要点**：提出知识嵌入与超网络引导的少样本变电站仪表缺陷图像生成方法，以解决缺陷样本稀缺问题。

**关键词**：少样本生成, 知识嵌入, 超网络引导, 缺陷图像合成, 工业检测, Stable Diffusion

## 3 点简述
- 核心问题：变电站仪表缺陷检测因标注样本稀缺而受限，需从有限数据生成真实可控的缺陷图像。
- 方法要点：结合知识嵌入与超网络引导控制，在Stable Diffusion中集成几何裂纹建模，实现像素级可控生成。
- 实验或效果：在真实数据集上显著提升生成质量，降低FID 32.7%，并提高下游检测器mAP 15.3%。

## 摘要（原文）

> Substation meters play a critical role in monitoring and ensuring the stable operation of power grids, yet their detection of cracks and other physical defects is often hampered by a severe scarcity of annotated samples. To address this few-shot generation challenge, we propose a novel framework that integrates Knowledge Embedding and Hypernetwork-Guided Conditional Control into a Stable Diffusion pipeline, enabling realistic and controllable synthesis of defect images from limited data.
>   First, we bridge the substantial domain gap between natural-image pre-trained models and industrial equipment by fine-tuning a Stable Diffusion backbone using DreamBooth-style knowledge embedding. This process encodes the unique structural and textural priors of substation meters, ensuring generated images retain authentic meter characteristics.
>   Second, we introduce a geometric crack modeling module that parameterizes defect attributes--such as location, length, curvature, and branching pattern--to produce spatially constrained control maps. These maps provide precise, pixel-level guidance during generation.
>   Third, we design a lightweight hypernetwork that dynamically modulates the denoising process of the diffusion model in response to the control maps and high-level defect descriptors, achieving a flexible balance between generation fidelity and controllability.
>   Extensive experiments on a real-world substation meter dataset demonstrate that our method substantially outperforms existing augmentation and generation baselines. It reduces Frechet Inception Distance (FID) by 32.7%, increases diversity metrics, and--most importantly--boosts the mAP of a downstream defect detector by 15.3% when trained on augmented data. The framework offers a practical, high-quality data synthesis solution for industrial inspection systems where defect samples are rare.

