---
layout: default
title: Beyond Artifacts: Real-Centric Envelope Modeling for Reliable AI-Generated Image Detection
---

# Beyond Artifacts: Real-Centric Envelope Modeling for Reliable AI-Generated Image Detection
**arXiv**：[2512.20937v1](https://arxiv.org/abs/2512.20937) · [PDF](https://arxiv.org/pdf/2512.20937.pdf)  
**作者**：Ruiqi Liu, Yi Han, Zhengbo Zhang, Liwei Yao, Zhiyuan Yan, Jialiang Shen, ZhiJin Chen, Boyi Sun, Lubin Weng, Jing Dong, Yan Wang, Shu Wu  

**一句话要点**：提出真实中心包络建模以解决真实条件下AI生成图像检测的泛化问题

**关键词**：AI生成图像检测, 真实世界退化, 包络建模, 泛化能力, 基准构建

## 3 点简述
- 现有检测器易过拟合生成器特定伪影，对真实世界退化敏感，导致泛化能力不足
- REM通过自重建特征扰动生成近真实样本，用包络估计器学习真实图像流形边界
- 在RealChain基准上平均提升7.5%，在严重退化条件下保持优异泛化性能

## 摘要（原文）

> The rapid progress of generative models has intensified the need for reliable and robust detection under real-world conditions. However, existing detectors often overfit to generator-specific artifacts and remain highly sensitive to real-world degradations. As generative architectures evolve and images undergo multi-round cross-platform sharing and post-processing (chain degradations), these artifact cues become obsolete and harder to detect. To address this, we propose Real-centric Envelope Modeling (REM), a new paradigm that shifts detection from learning generator artifacts to modeling the robust distribution of real images. REM introduces feature-level perturbations in self-reconstruction to generate near-real samples, and employs an envelope estimator with cross-domain consistency to learn a boundary enclosing the real image manifold. We further build RealChain, a comprehensive benchmark covering both open-source and commercial generators with simulated real-world degradation. Across eight benchmark evaluations, REM achieves an average improvement of 7.5% over state-of-the-art methods, and notably maintains exceptional generalization on the severely degraded RealChain benchmark, establishing a solid foundation for synthetic image detection under real-world conditions. The code and the RealChain benchmark will be made publicly available upon acceptance of the paper.

