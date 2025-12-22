---
layout: default
title: Self-Supervised Weighted Image Guided Quantitative MRI Super-Resolution
---

# Self-Supervised Weighted Image Guided Quantitative MRI Super-Resolution
**arXiv**：[2512.17612v1](https://arxiv.org/abs/2512.17612) · [PDF](https://arxiv.org/pdf/2512.17612.pdf)  
**作者**：Alireza Samadifardheris, Dirk H. J. Poot, Florian Wiesinger, Stefan Klein, Juan A. Hernandez-Tamames  

**一句话要点**：提出自监督加权图像引导的定量MRI超分辨率框架，以解决高分辨率定量MRI获取耗时长的临床问题。

**关键词**：定量MRI超分辨率, 自监督学习, 加权图像引导, 物理模型, 贝叶斯推理, 临床工作流

## 3 点简述
- 核心问题：高分辨率定量MRI获取耗时，限制临床应用，需无高分辨率真值训练方法。
- 方法要点：基于贝叶斯最大后验推理，利用加权MRI引导和物理模型，实现自监督超分辨率学习。
- 实验或效果：在合成和体内数据验证，模型能快速生成高质量定量图，提升扫描效率。

## 摘要（原文）

> High-resolution (HR) quantitative MRI (qMRI) relaxometry provides objective tissue characterization but remains clinically underutilized due to lengthy acquisition times. We propose a physics-informed, self-supervised framework for qMRI super-resolution that uses routinely acquired HR weighted MRI (wMRI) scans as guidance, thus, removing the necessity for HR qMRI ground truth during training. We formulate super-resolution as Bayesian maximum a posteriori inference, minimizing two discrepancies: (1) between HR images synthesized from super-resolved qMRI maps and acquired wMRI guides via forward signal models, and (2) between acquired LR qMRI and downsampled predictions. This physics-informed objective allows the models to learn from clinical wMRI without HR qMRI supervision. To validate the concept, we generate training data by synthesizing wMRI guides from HR qMRI using signal equations, then degrading qMRI resolution via k-space truncation. A deep neural network learns the super-resolution mapping. Ablation experiments demonstrate that T1-weighted images primarily enhance T1 maps, T2-weighted images improve T2 maps, and combined guidance optimally enhances all parameters simultaneously. Validation on independently acquired in-vivo data from a different qMRI sequence confirms cross-qMRI sequence generalizability. Models trained on synthetic data can produce super-resolved maps from a 1-minute acquisition with quality comparable to a 5-minute reference scan, leveraging the scanner-independent nature of relaxometry parameters. By decoupling training from HR qMRI requirement, our framework enables fast qMRI acquisitions enhanced via routine clinical images, offering a practical pathway for integrating quantitative relaxometry into clinical workflows with acceptable additional scan time.

