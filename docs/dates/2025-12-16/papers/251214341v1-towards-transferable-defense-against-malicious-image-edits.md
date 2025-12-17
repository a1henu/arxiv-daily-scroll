---
layout: default
title: Towards Transferable Defense Against Malicious Image Edits
---

# Towards Transferable Defense Against Malicious Image Edits
**arXiv**：[2512.14341v1](https://arxiv.org/abs/2512.14341) · [PDF](https://arxiv.org/pdf/2512.14341.pdf)  
**作者**：Jie Zhang, Shuai Dong, Shiguang Shan, Xilin Chen  

**一句话要点**：提出TDAE框架以增强图像对恶意编辑的跨模型免疫能力

**关键词**：恶意图像编辑防御, 跨模型迁移性, 梯度正则化, 对抗优化, 图像-文本协同, 扩散模型安全

## 3 点简述
- 现有防御方法在跨模型评估中迁移性有限，难以应对未知编辑模型
- TDAE结合视觉FlatGrad防御和文本Dynamic Prompt防御，通过图像-文本协同优化提升免疫鲁棒性
- 实验显示TDAE在模型内和跨模型评估中均达到最优性能，有效缓解恶意编辑

## 摘要（原文）

> Recent approaches employing imperceptible perturbations in input images have demonstrated promising potential to counter malicious manipulations in diffusion-based image editing systems. However, existing methods suffer from limited transferability in cross-model evaluations. To address this, we propose Transferable Defense Against Malicious Image Edits (TDAE), a novel bimodal framework that enhances image immunity against malicious edits through coordinated image-text optimization. Specifically, at the visual defense level, we introduce FlatGrad Defense Mechanism (FDM), which incorporates gradient regularization into the adversarial objective. By explicitly steering the perturbations toward flat minima, FDM amplifies immune robustness against unseen editing models. For textual enhancement protection, we propose an adversarial optimization paradigm named Dynamic Prompt Defense (DPD), which periodically refines text embeddings to align the editing outcomes of immunized images with those of the original images, then updates the images under optimized embeddings. Through iterative adversarial updates to diverse embeddings, DPD enforces the generation of immunized images that seek a broader set of immunity-enhancing features, thereby achieving cross-model transferability. Extensive experimental results demonstrate that our TDAE achieves state-of-the-art performance in mitigating malicious edits under both intra- and cross-model evaluations.

