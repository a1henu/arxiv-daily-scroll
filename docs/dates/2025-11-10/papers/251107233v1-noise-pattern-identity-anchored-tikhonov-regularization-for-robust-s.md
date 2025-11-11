---
layout: default
title: Noise & pattern: identity-anchored Tikhonov regularization for robust structural anomaly detection
---

# Noise & pattern: identity-anchored Tikhonov regularization for robust structural anomaly detection
**arXiv**：[2511.07233v1](https://arxiv.org/abs/2511.07233) · [PDF](https://arxiv.org/pdf/2511.07233.pdf)  
**作者**：Alexander Bauer, Klaus-Robert Müller  

**一句话要点**：提出身份锚定Tikhonov正则化方法，用于工业视觉中的结构异常检测。

**关键词**：结构异常检测, 自监督学习, Tikhonov正则化, 工业视觉, 自编码器, 图像修复

## 3 点简述
- 核心问题：工业检测中难以收集所有异常样本，需检测细微结构缺陷。
- 方法要点：使用自监督自编码器，注入结构化扰动并添加高斯噪声作为正则化。
- 实验或效果：在MVTec AD基准上实现SOTA结果，AUROC达99.9/99.4。

## 摘要（原文）

> Anomaly detection plays a pivotal role in automated industrial inspection,
> aiming to identify subtle or rare defects in otherwise uniform visual patterns.
> As collecting representative examples of all possible anomalies is infeasible,
> we tackle structural anomaly detection using a self-supervised autoencoder that
> learns to repair corrupted inputs. To this end, we introduce a corruption model
> that injects artificial disruptions into training images to mimic structural
> defects. While reminiscent of denoising autoencoders, our approach differs in
> two key aspects. First, instead of unstructured i.i.d.\ noise, we apply
> structured, spatially coherent perturbations that make the task a hybrid of
> segmentation and inpainting. Second, and counterintuitively, we add and
> preserve Gaussian noise on top of the occlusions, which acts as a Tikhonov
> regularizer anchoring the Jacobian of the reconstruction function toward
> identity. This identity-anchored regularization stabilizes reconstruction and
> further improves both detection and segmentation accuracy. On the MVTec AD
> benchmark, our method achieves state-of-the-art results (I/P-AUROC: 99.9/99.4),
> supporting our theoretical framework and demonstrating its practical relevance
> for automatic inspection.

