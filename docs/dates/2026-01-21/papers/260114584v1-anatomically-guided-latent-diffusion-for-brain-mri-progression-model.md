---
layout: default
title: Anatomically Guided Latent Diffusion for Brain MRI Progression Modeling
---

# Anatomically Guided Latent Diffusion for Brain MRI Progression Modeling
**arXiv**：[2601.14584v1](https://arxiv.org/abs/2601.14584) · [PDF](https://arxiv.org/pdf/2601.14584.pdf)  
**作者**：Cheng Wan, Bahram Jafrasteh, Ehsan Adeli, Miaomiao Zhang, Qingyu Zhao  

**一句话要点**：提出解剖引导的潜在扩散模型以简化脑MRI进展建模并增强解剖一致性

**关键词**：脑MRI进展建模, 潜在扩散模型, 解剖引导, 端到端训练, 阿尔茨海默病

## 3 点简述
- 现有方法如BrLP架构复杂且解剖一致性有限，影响脑MRI进展建模准确性
- AG-LDM通过输入级融合基线解剖、噪声随访状态和临床协变量，实现端到端训练
- 在ADNI和OASIS-3数据集上，AG-LDM达到最优图像质量并减少15-20%体积误差

## 摘要（原文）

> Accurately modeling longitudinal brain MRI progression is crucial for understanding neurodegenerative diseases and predicting individualized structural changes. Existing state-of-the-art approaches, such as Brain Latent Progression (BrLP), often use multi-stage training pipelines with auxiliary conditioning modules but suffer from architectural complexity, suboptimal use of conditional clinical covariates, and limited guarantees of anatomical consistency. We propose Anatomically Guided Latent Diffusion Model (AG-LDM), a segmentation-guided framework that enforces anatomically consistent progression while substantially simplifying the training pipeline. AG-LDM conditions latent diffusion by directly fusing baseline anatomy, noisy follow-up states, and clinical covariates at the input level, a strategy that avoids auxiliary control networks by learning a unified, end-to-end model that represents both anatomy and progression. A lightweight 3D tissue segmentation model (WarpSeg) provides explicit anatomical supervision during both autoencoder fine-tuning and diffusion model training, ensuring consistent brain tissue boundaries and morphometric fidelity. Experiments on 31,713 ADNI longitudinal pairs and zero-shot evaluation on OASIS-3 demonstrate that AG-LDM matches or surpasses more complex diffusion models, achieving state-of-the-art image quality and 15-20\% reduction in volumetric errors in generated images. AG-LDM also exhibits markedly stronger utilization of temporal and clinical covariates (up to 31.5x higher sensitivity than BrLP) and generates biologically plausible counterfactual trajectories, accurately capturing hallmarks of Alzheimer's progression such as limbic atrophy and ventricular expansion. These results highlight AG-LDM as an efficient, anatomically grounded framework for reliable brain MRI progression modeling.

