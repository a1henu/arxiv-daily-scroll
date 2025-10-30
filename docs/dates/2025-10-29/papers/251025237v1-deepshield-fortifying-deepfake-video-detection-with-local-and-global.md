---
layout: default
title: DeepShield: Fortifying Deepfake Video Detection with Local and Global Forgery Analysis
---

# DeepShield: Fortifying Deepfake Video Detection with Local and Global Forgery Analysis
**arXiv**：[2510.25237v1](https://arxiv.org/abs/2510.25237) · [PDF](https://arxiv.org/pdf/2510.25237.pdf)  
**作者**：Yinqi Cai, Jichang Li, Zhaolun Li, Weikai Chen, Rushi Lan, Xi Xie, Xiaonan Luo, Guanbin Li  

**一句话要点**：提出DeepShield框架，通过局部和全局伪造分析增强深度伪造视频检测的鲁棒性。

**关键词**：深度伪造检测, 局部全局分析, 跨域泛化, 视频伪造, CLIP-ViT增强

## 3 点简述
- 核心问题：现有检测器依赖特定伪造痕迹，在跨域场景中泛化能力差。
- 方法要点：结合局部补丁指导和全局伪造多样化，提升对未知伪造的适应性。
- 实验或效果：在跨数据集和跨操纵评估中优于现有方法，实现更高鲁棒性。

## 摘要（原文）

> Recent advances in deep generative models have made it easier to manipulate
> face videos, raising significant concerns about their potential misuse for
> fraud and misinformation. Existing detectors often perform well in in-domain
> scenarios but fail to generalize across diverse manipulation techniques due to
> their reliance on forgery-specific artifacts. In this work, we introduce
> DeepShield, a novel deepfake detection framework that balances local
> sensitivity and global generalization to improve robustness across unseen
> forgeries. DeepShield enhances the CLIP-ViT encoder through two key components:
> Local Patch Guidance (LPG) and Global Forgery Diversification (GFD). LPG
> applies spatiotemporal artifact modeling and patch-wise supervision to capture
> fine-grained inconsistencies often overlooked by global models. GFD introduces
> domain feature augmentation, leveraging domain-bridging and boundary-expanding
> feature generation to synthesize diverse forgeries, mitigating overfitting and
> enhancing cross-domain adaptability. Through the integration of novel local and
> global analysis for deepfake detection, DeepShield outperforms state-of-the-art
> methods in cross-dataset and cross-manipulation evaluations, achieving superior
> robustness against unseen deepfake attacks.

