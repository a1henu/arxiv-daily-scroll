---
layout: default
title: Unsupervised Anomaly Detection in Brain MRI via Disentangled Anatomy Learning
---

# Unsupervised Anomaly Detection in Brain MRI via Disentangled Anatomy Learning
**arXiv**：[2512.21924v1](https://arxiv.org/abs/2512.21924) · [PDF](https://arxiv.org/pdf/2512.21924.pdf)  
**作者**：Tao Yang, Xiuying Wang, Hao Liu, Guanzhong Gong, Lian-Ming Wu, Yu-Ping Wang, Lisheng Wang  

**一句话要点**：提出解耦解剖学习与边缘恢复模块，以提升脑MRI无监督异常检测的泛化性与性能。

**关键词**：无监督异常检测, 脑MRI分析, 解耦表示学习, 伪健康图像重建, 多中心数据, 解剖先验

## 3 点简述
- 核心问题：现有无监督方法在脑MRI异常检测中泛化性差且性能受限，因依赖特定成像信息及异常残差传播。
- 方法要点：通过解耦表示模块分离成像与解剖信息，结合边缘到图像恢复模块重建高质量伪健康图像。
- 实验或效果：在九个公共数据集上评估，优于17种先进方法，AP和DSC分别提升18.32%和13.64%。

## 摘要（原文）

> Detection of various lesions in brain MRI is clinically critical, but challenging due to the diversity of lesions and variability in imaging conditions. Current unsupervised learning methods detect anomalies mainly through reconstructing abnormal images into pseudo-healthy images (PHIs) by normal samples learning and then analyzing differences between images. However, these unsupervised models face two significant limitations: restricted generalizability to multi-modality and multi-center MRIs due to their reliance on the specific imaging information in normal training data, and constrained performance due to abnormal residuals propagated from input images to reconstructed PHIs. To address these limitations, two novel modules are proposed, forming a new PHI reconstruction framework. Firstly, the disentangled representation module is proposed to improve generalizability by decoupling brain MRI into imaging information and essential imaging-invariant anatomical images, ensuring that the reconstruction focuses on the anatomy. Specifically, brain anatomical priors and a differentiable one-hot encoding operator are introduced to constrain the disentanglement results and enhance the disentanglement stability. Secondly, the edge-to-image restoration module is designed to reconstruct high-quality PHIs by restoring the anatomical representation from the high-frequency edge information of anatomical images, and then recoupling the disentangled imaging information. This module not only suppresses abnormal residuals in PHI by reducing abnormal pixels input through edge-only input, but also effectively reconstructs normal regions using the preserved structural details in the edges. Evaluated on nine public datasets (4,443 patients' MRIs from multiple centers), our method outperforms 17 SOTA methods, achieving absolute improvements of +18.32% in AP and +13.64% in DSC.

