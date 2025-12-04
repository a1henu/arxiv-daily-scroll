---
layout: default
title: CoDA: From Text-to-Image Diffusion Models to Training-Free Dataset Distillation
---

# CoDA: From Text-to-Image Diffusion Models to Training-Free Dataset Distillation
**arXiv**：[2512.03844v1](https://arxiv.org/abs/2512.03844) · [PDF](https://arxiv.org/pdf/2512.03844.pdf)  
**作者**：Letian Zhou, Songhua Liu, Xinchao Wang  

**一句话要点**：提出CoDA框架，利用现成文本到图像模型实现免训练数据集蒸馏

**关键词**：数据集蒸馏, 文本到图像模型, 核心分布对齐, 免训练蒸馏, 生成模型, 图像分类

## 3 点简述
- 现有数据集蒸馏方法依赖目标数据集预训练扩散模型，成本高且违背蒸馏初衷
- CoDA通过识别目标数据集核心分布并引导生成对齐，弥合通用生成先验与目标语义差距
- 实验显示CoDA在ImageNet-1K等基准上性能媲美或超越依赖目标特定训练的方法

## 摘要（原文）

> Prevailing Dataset Distillation (DD) methods leveraging generative models confront two fundamental limitations. First, despite pioneering the use of diffusion models in DD and delivering impressive performance, the vast majority of approaches paradoxically require a diffusion model pre-trained on the full target dataset, undermining the very purpose of DD and incurring prohibitive training costs. Second, although some methods turn to general text-to-image models without relying on such target-specific training, they suffer from a significant distributional mismatch, as the web-scale priors encapsulated in these foundation models fail to faithfully capture the target-specific semantics, leading to suboptimal performance. To tackle these challenges, we propose Core Distribution Alignment (CoDA), a framework that enables effective DD using only an off-the-shelf text-to-image model. Our key idea is to first identify the "intrinsic core distribution" of the target dataset using a robust density-based discovery mechanism. We then steer the generative process to align the generated samples with this core distribution. By doing so, CoDA effectively bridges the gap between general-purpose generative priors and target semantics, yielding highly representative distilled datasets. Extensive experiments suggest that, without relying on a generative model specifically trained on the target dataset, CoDA achieves performance on par with or even superior to previous methods with such reliance across all benchmarks, including ImageNet-1K and its subsets. Notably, it establishes a new state-of-the-art accuracy of 60.4% at the 50-images-per-class (IPC) setup on ImageNet-1K. Our code is available on the project webpage: https://github.com/zzzlt422/CoDA

