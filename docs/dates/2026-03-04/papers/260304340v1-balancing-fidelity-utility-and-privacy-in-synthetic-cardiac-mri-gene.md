---
layout: default
title: Balancing Fidelity, Utility, and Privacy in Synthetic Cardiac MRI Generation: A Comparative Study
---

# Balancing Fidelity, Utility, and Privacy in Synthetic Cardiac MRI Generation: A Comparative Study
**arXiv**：[2603.04340v1](https://arxiv.org/abs/2603.04340) · [PDF](https://arxiv.org/pdf/2603.04340.pdf)  
**作者**：Madhura Edirisooriya, Dasuni Kawya, Ishan Kumarasinghe, Isuri Devindi, Mary M. Maleckar, Roshan Ragel, Isuru Nawinne, Vajira Thambawita  

**一句话要点**：比较DDPM、LDM和FM在合成心脏MRI生成中平衡保真度、实用性和隐私性的表现

**关键词**：心脏MRI合成, 生成模型比较, 隐私保护, 数据增强, 医学影像

## 3 点简述
- 核心问题：心脏MRI数据稀缺和隐私限制阻碍深度学习应用
- 方法要点：采用基于解剖掩码的两阶段管道，评估三种生成模型
- 实验或效果：DDPM在有限数据下平衡最佳，FM隐私性突出但性能稍低

## 摘要（原文）

> Deep learning in cardiac MRI (CMR) is fundamentally constrained by both data scarcity and privacy regulations. This study systematically benchmarks three generative architectures: Denoising Diffusion Probabilistic Models (DDPM), Latent Diffusion Models (LDM), and Flow Matching (FM) for synthetic CMR generation. Utilizing a two-stage pipeline where anatomical masks condition image synthesis, we evaluate generated data across three critical axes: fidelity, utility, and privacy. Our results show that diffusion-based models, particularly DDPM, provide the most effective balance between downstream segmentation utility, image fidelity, and privacy preservation under limited-data conditions, while FM demonstrates promising privacy characteristics with slightly lower task-level performance. These findings quantify the trade-offs between cross-domain generalization and patient confidentiality, establishing a framework for safe and effective synthetic data augmentation in medical imaging.

