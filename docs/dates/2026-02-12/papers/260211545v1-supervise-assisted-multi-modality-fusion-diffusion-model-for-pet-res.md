---
layout: default
title: Supervise-assisted Multi-modality Fusion Diffusion Model for PET Restoration
---

# Supervise-assisted Multi-modality Fusion Diffusion Model for PET Restoration
**arXiv**：[2602.11545v1](https://arxiv.org/abs/2602.11545) · [PDF](https://arxiv.org/pdf/2602.11545.pdf)  
**作者**：Yingkai Zhang, Shuang Chen, Ye Tian, Yunyi Gao, Jianyong Jiang, Ying Fu  

**一句话要点**：提出监督辅助多模态融合扩散模型以解决PET图像恢复中的模态不一致和分布外数据挑战

**关键词**：PET图像恢复, 多模态融合, 扩散模型, 监督辅助学习, 分布外数据

## 3 点简述
- 核心问题：低剂量PET图像恢复时，多模态融合的结构纹理不一致和分布外数据不匹配问题。
- 方法要点：设计多模态特征融合模块和扩散模型，结合两阶段监督辅助学习策略。
- 实验或效果：实验表明MFdiff能有效恢复高质量标准剂量PET图像，优于现有方法。

## 摘要（原文）

> Positron emission tomography (PET) offers powerful functional imaging but involves radiation exposure. Efforts to reduce this exposure by lowering the radiotracer dose or scan time can degrade image quality. While using magnetic resonance (MR) images with clearer anatomical information to restore standard-dose PET (SPET) from low-dose PET (LPET) is a promising approach, it faces challenges with the inconsistencies in the structure and texture of multi-modality fusion, as well as the mismatch in out-of-distribution (OOD) data. In this paper, we propose a supervise-assisted multi-modality fusion diffusion model (MFdiff) for addressing these challenges for high-quality PET restoration. Firstly, to fully utilize auxiliary MR images without introducing extraneous details in the restored image, a multi-modality feature fusion module is designed to learn an optimized fusion feature. Secondly, using the fusion feature as an additional condition, high-quality SPET images are iteratively generated based on the diffusion model. Furthermore, we introduce a two-stage supervise-assisted learning strategy that harnesses both generalized priors from simulated in-distribution datasets and specific priors tailored to in-vivo OOD data. Experiments demonstrate that the proposed MFdiff effectively restores high-quality SPET images from multi-modality inputs and outperforms state-of-the-art methods both qualitatively and quantitatively.

