---
layout: default
title: VLIC: Vision-Language Models As Perceptual Judges for Human-Aligned Image Compression
---

# VLIC: Vision-Language Models As Perceptual Judges for Human-Aligned Image Compression
**arXiv**：[2512.15701v1](https://arxiv.org/abs/2512.15701) · [PDF](https://arxiv.org/pdf/2512.15701.pdf)  
**作者**：Kyle Sargent, Ruiqi Gao, Philipp Henzler, Charles Herrmann, Aleksander Holynski, Li Fei-Fei, Jiajun Wu, Jason Zhang  

**一句话要点**：提出VLIC，利用视觉语言模型作为感知评判器，优化人类对齐的图像压缩系统。

**关键词**：图像压缩, 视觉语言模型, 人类感知对齐, 扩散模型, 后训练, 二元选择判断

## 3 点简述
- 核心问题：传统图像压缩评估如MSE与人类感知不一致，需更优对齐方法。
- 方法要点：利用视觉语言模型零-shot复制人类二元选择判断，结合扩散模型后训练优化压缩。
- 实验或效果：在人类对齐压缩任务中，VLIC在感知指标和用户研究中表现竞争性或领先。

## 摘要（原文）

> Evaluations of image compression performance which include human preferences have generally found that naive distortion functions such as MSE are insufficiently aligned to human perception. In order to align compression models to human perception, prior work has employed differentiable perceptual losses consisting of neural networks calibrated on large-scale datasets of human psycho-visual judgments. We show that, surprisingly, state-of-the-art vision-language models (VLMs) can replicate binary human two-alternative forced choice (2AFC) judgments zero-shot when asked to reason about the differences between pairs of images. Motivated to exploit the powerful zero-shot visual reasoning capabilities of VLMs, we propose Vision-Language Models for Image Compression (VLIC), a diffusion-based image compression system designed to be post-trained with binary VLM judgments. VLIC leverages existing techniques for diffusion model post-training with preferences, rather than distilling the VLM judgments into a separate perceptual loss network. We show that calibrating this system on VLM judgments produces competitive or state-of-the-art performance on human-aligned visual compression depending on the dataset, according to perceptual metrics and large-scale user studies. We additionally conduct an extensive analysis of the VLM-based reward design and training procedure and share important insights. More visuals are available at https://kylesargent.github.io/vlic

