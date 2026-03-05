---
layout: default
title: MPFlow: Multi-modal Posterior-Guided Flow Matching for Zero-Shot MRI Reconstruction
---

# MPFlow: Multi-modal Posterior-Guided Flow Matching for Zero-Shot MRI Reconstruction
**arXiv**：[2603.03710v1](https://arxiv.org/abs/2603.03710) · [PDF](https://arxiv.org/pdf/2603.03710.pdf)  
**作者**：Seunghoi Kim, Chen Jin, Henry F. J. Tregidgo, Matteo Figini, Daniel C. Alexander  

**一句话要点**：提出MPFlow，一种基于多模态后验引导流匹配的零样本MRI重建框架，以利用辅助模态提升解剖保真度。

**关键词**：零样本MRI重建, 多模态引导, 流匹配, 自监督预训练, 解剖保真度, 幻觉抑制

## 3 点简述
- 核心问题：零样本MRI重建中，单模态无条件先验在严重病态下易产生幻觉，现有方法缺乏利用临床中常规可用的辅助模态信息。
- 方法要点：通过自监督预训练策略PAMRI学习跨模态共享表示，在推理时结合数据一致性和跨模态特征对齐，无需重新训练生成先验。
- 实验或效果：在HCP和BraTS数据集上，MPFlow仅用20%采样步骤匹配扩散基线图像质量，并将肿瘤幻觉减少超过15%（分割Dice分数）。

## 摘要（原文）

> Zero-shot MRI reconstruction relies on generative priors, but single-modality unconditional priors produce hallucinations under severe ill-posedness. In many clinical workflows, complementary MRI acquisitions (e.g. high-quality structural scans) are routinely available, yet existing reconstruction methods lack mechanisms to leverage this additional information. We propose MPFlow, a zero-shot multi-modal reconstruction framework built on rectified flow that incorporates auxiliary MRI modalities at inference time without retraining the generative prior to improve anatomical fidelity. Cross-modal guidance is enabled by our proposed self-supervised pretraining strategy, Patch-level Multi-modal MR Image Pretraining (PAMRI), which learns shared representations across modalities. Sampling is jointly guided by data consistency and cross-modal feature alignment using pre-trained PAMRI, systematically suppressing intrinsic and extrinsic hallucinations. Extensive experiments on HCP and BraTS show that MPFlow matches diffusion baselines on image quality using only 20% of sampling steps while reducing tumor hallucinations by more than 15% (segmentation dice score). This demonstrates that cross-modal guidance enables more reliable and efficient zero-shot MRI reconstruction.

