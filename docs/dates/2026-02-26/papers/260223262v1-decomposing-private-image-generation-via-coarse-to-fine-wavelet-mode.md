---
layout: default
title: Decomposing Private Image Generation via Coarse-to-Fine Wavelet Modeling
---

# Decomposing Private Image Generation via Coarse-to-Fine Wavelet Modeling
**arXiv**：[2602.23262v1](https://arxiv.org/abs/2602.23262) · [PDF](https://arxiv.org/pdf/2602.23262.pdf)  
**作者**：Jasmine Bayrooti, Weiwei Kong, Natalia Ponomareva, Carlos Esteves, Ameesh Makadia, Amanda Prorok  

**一句话要点**：提出基于小波建模的谱差分隐私框架，以提升私有图像生成的质量与隐私权衡。

**关键词**：差分隐私, 图像生成, 小波变换, 谱分析, 隐私保护, 超分辨率

## 3 点简述
- 核心问题：差分隐私微调导致图像质量下降，尤其在高频纹理，因噪声添加不区分。
- 方法要点：假设隐私敏感部分为小波空间低频成分，分两阶段：DP微调低频系数，公开模型上采样高频细节。
- 实验或效果：在MS-COCO和MM-CelebA-HQ数据集上，相比其他DP框架，图像质量和风格捕获有改进。

## 摘要（原文）

> Generative models trained on sensitive image datasets risk memorizing and reproducing individual training examples, making strong privacy guarantees essential. While differential privacy (DP) provides a principled framework for such guarantees, standard DP finetuning (e.g., with DP-SGD) often results in severe degradation of image quality, particularly in high-frequency textures, due to the indiscriminate addition of noise across all model parameters. In this work, we propose a spectral DP framework based on the hypothesis that the most privacy-sensitive portions of an image are often low-frequency components in the wavelet space (e.g., facial features and object shapes) while high-frequency components are largely generic and public. Based on this hypothesis, we propose the following two-stage framework for DP image generation with coarse image intermediaries: (1) DP finetune an autoregressive spectral image tokenizer model on the low-resolution wavelet coefficients of the sensitive images, and (2) perform high-resolution upsampling using a publicly pretrained super-resolution model. By restricting the privacy budget to the global structures of the image in the first stage, and leveraging the post-processing property of DP for detail refinement, we achieve promising trade-offs between privacy and utility. Experiments on the MS-COCO and MM-CelebA-HQ datasets show that our method generates images with improved quality and style capture relative to other leading DP image frameworks.

