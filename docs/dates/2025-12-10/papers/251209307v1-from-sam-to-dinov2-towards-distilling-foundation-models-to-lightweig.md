---
layout: default
title: From SAM to DINOv2: Towards Distilling Foundation Models to Lightweight Baselines for Generalized Polyp Segmentation
---

# From SAM to DINOv2: Towards Distilling Foundation Models to Lightweight Baselines for Generalized Polyp Segmentation
**arXiv**：[2512.09307v1](https://arxiv.org/abs/2512.09307) · [PDF](https://arxiv.org/pdf/2512.09307.pdf)  
**作者**：Shivanshu Agnihotri, Snehashis Majhi, Deepak Ranjan Nayak, Debesh Jha  

**一句话要点**：提出Polyp-DiFoM蒸馏框架，将基础模型知识注入轻量基线以提升息肉分割性能。

**关键词**：息肉分割, 知识蒸馏, 轻量模型, 基础模型, 医学图像分析, 频域编码

## 3 点简述
- 核心问题：轻量基线模型在息肉分割中因尺寸、形状和颜色变化及伪装特性而性能受限。
- 方法要点：通过蒸馏框架将SAM、DINOv2等基础模型的语义先验注入U-Net等架构，并采用频域编码增强蒸馏效果。
- 实验或效果：在五个基准数据集上显著超越基线及SOTA模型，计算开销减少近9倍。

## 摘要（原文）

> Accurate polyp segmentation during colonoscopy is critical for the early detection of colorectal cancer and still remains challenging due to significant size, shape, and color variations, and the camouflaged nature of polyps. While lightweight baseline models such as U-Net, U-Net++, and PraNet offer advantages in terms of easy deployment and low computational cost, they struggle to deal with the above issues, leading to limited segmentation performance. In contrast, large-scale vision foundation models such as SAM, DINOv2, OneFormer, and Mask2Former have exhibited impressive generalization performance across natural image domains. However, their direct transfer to medical imaging tasks (e.g., colonoscopic polyp segmentation) is not straightforward, primarily due to the scarcity of large-scale datasets and lack of domain-specific knowledge. To bridge this gap, we propose a novel distillation framework, Polyp-DiFoM, that transfers the rich representations of foundation models into lightweight segmentation baselines, allowing efficient and accurate deployment in clinical settings. In particular, we infuse semantic priors from the foundation models into canonical architectures such as U-Net and U-Net++ and further perform frequency domain encoding for enhanced distillation, corroborating their generalization capability. Extensive experiments are performed across five benchmark datasets, such as Kvasir-SEG, CVC-ClinicDB, ETIS, ColonDB, and CVC-300. Notably, Polyp-DiFoM consistently outperforms respective baseline models significantly, as well as the state-of-the-art model, with nearly 9 times reduced computation overhead. The code is available at https://github.com/lostinrepo/PolypDiFoM.

