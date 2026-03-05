---
layout: default
title: Mask-Guided Attention Regulation for Anatomically Consistent Counterfactual CXR Synthesis
---

# Mask-Guided Attention Regulation for Anatomically Consistent Counterfactual CXR Synthesis
**arXiv**：[2603.04130v1](https://arxiv.org/abs/2603.04130) · [PDF](https://arxiv.org/pdf/2603.04130.pdf)  
**作者**：Zichun Zhang, Weizhi Nie, Honglin Guo, Yuting Su  

**一句话要点**：提出基于掩码引导注意力调控的推理框架，以解决胸部X光反事实合成中的结构漂移和病理表达不稳定问题。

**关键词**：反事实合成, 注意力调控, 胸部X光编辑, 扩散模型, 解剖一致性, 病理定位

## 3 点简述
- 核心问题：扩散编辑方法在胸部X光反事实合成中易出现结构漂移和病理表达不稳定，影响解剖一致性和编辑精度。
- 方法要点：通过器官掩码调控自注意力和解剖标记交叉注意力，并利用病理引导模块增强早期去噪中的病理标记注意力，实现可控病变定位。
- 实验或效果：在胸部X光数据集上评估，相比标准扩散编辑，提高了解剖一致性和病理编辑的精确可控性，支持下游任务的数据增强。

## 摘要（原文）

> Counterfactual generation for chest X-rays (CXR) aims to simulate plausible pathological changes while preserving patient-specific anatomy. However, diffusion-based editing methods often suffer from structural drift, where stable anatomical semantics propagate globally through attention and distort non-target regions, and unstable pathology expression, since subtle and localized lesions induce weak and noisy conditioning signals. We present an inference-time attention regulation framework for reliable counterfactual CXR synthesis. An anatomy-aware attention regularization module gates self-attention and anatomy-token cross-attention with organ masks, confining structural interactions to anatomical ROIs and reducing unintended distortions. A pathology-guided module enhances pathology-token cross-attention within target lung regions during early denoising and performs lightweight latent corrections driven by an attention-concentration energy, enabling controllable lesion localization and extent. Extensive evaluations on CXR datasets show improved anatomical consistency and more precise, controllable pathological edits compared with standard diffusion editing, supporting localized counterfactual analysis and data augmentation for downstream tasks.

