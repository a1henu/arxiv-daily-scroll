---
layout: default
title: TumorFlow: Physics-Guided Longitudinal MRI Synthesis of Glioblastoma Growth
---

# TumorFlow: Physics-Guided Longitudinal MRI Synthesis of Glioblastoma Growth
**arXiv**：[2603.04058v1](https://arxiv.org/abs/2603.04058) · [PDF](https://arxiv.org/pdf/2603.04058.pdf)  
**作者**：Valentin Biller, Niklas Bubeck, Lucas Zimmer, Ayhan Can Erdur, Sandeep Nagar, Anke Meyer-Baese, Daniel Rückert, Benedikt Wiestler, Jonas Weidner  

**一句话要点**：提出基于生物物理引导的生成框架，用于合成胶质母细胞瘤生长的纵向MRI序列

**关键词**：胶质母细胞瘤生长模拟, 生物物理引导生成, 纵向MRI合成, 肿瘤浸润估计, 可控数据生成

## 3 点简述
- 胶质母细胞瘤生长模式多样且部分不可见，难以评估真实肿瘤范围
- 结合生成模型与生物物理生长模型，合成可控且生物真实的3D MRI
- 在纵向病例上生成时间一致序列，Dice重叠达75%，PSNR保持25

## 摘要（原文）

> Glioblastoma exhibits diverse, infiltrative, and patient-specific growth patterns that are only partially visible on routine MRI, making it difficult to reliably assess true tumor extent and personalize treatment planning and follow-up. We present a biophysically-conditioned generative framework that synthesizes biologically realistic 3D brain MRI volumes from estimated, spatially continuous tumor-concentration fields. Our approach combines a generative model with tumor-infiltration maps that can be propagated through time using a biophysical growth model, enabling fine-grained control over tumor shape and growth while preserving patient anatomy. This enables us to synthesize consistent tumor growth trajectories directly in the space of real patients, providing interpretable, controllable estimation of tumor infiltration and progression beyond what is explicitly observed in imaging. We evaluate the framework on longitudinal glioblastoma cases and demonstrate that it can generate temporally coherent sequences with realistic changes in tumor appearance and surrounding tissue response. These results suggest that integrating mechanistic tumor growth priors with modern generative modeling can provide a practical tool for patient-specific progression visualization and for generating controlled synthetic data to support downstream neuro-oncology workflows. In longitudinal extrapolation, we achieve a consistent 75% Dice overlap with the biophysical model while maintaining a constant PSNR of 25 in the surrounding tissue. Our code is available at: https://github.com/valentin-biller/lgm.git

