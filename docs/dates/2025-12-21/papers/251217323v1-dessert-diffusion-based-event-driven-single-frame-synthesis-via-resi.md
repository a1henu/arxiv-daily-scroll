---
layout: default
title: DESSERT: Diffusion-based Event-driven Single-frame Synthesis via Residual Training
---

# DESSERT: Diffusion-based Event-driven Single-frame Synthesis via Residual Training
**arXiv**：[2512.17323v1](https://arxiv.org/abs/2512.17323) · [PDF](https://arxiv.org/pdf/2512.17323.pdf)  
**作者**：Jiyun Kong, Jun-Hyuk Kim, Jong-Seok Lee  

**一句话要点**：提出DESSERT框架，通过残差训练和扩散模型解决事件相机视频帧预测中的空洞和模糊问题。

**关键词**：事件相机, 视频帧预测, 扩散模型, 残差训练, 时间一致性, 单帧合成

## 3 点简述
- 核心问题：事件相机视频帧预测中，基于光流的方法因像素位移不准确导致空洞和模糊。
- 方法要点：使用预训练Stable Diffusion模型，通过两阶段训练（ER-VAE对齐事件帧与残差，扩散模型去噪残差潜在表示）确保时间一致性。
- 实验或效果：在事件重建、视频帧预测等任务中优于现有方法，生成更清晰、时间一致的帧。

## 摘要（原文）

> Video frame prediction extrapolates future frames from previous frames, but suffers from prediction errors in dynamic scenes due to the lack of information about the next frame. Event cameras address this limitation by capturing per-pixel brightness changes asynchronously with high temporal resolution. Prior research on event-based video frame prediction has leveraged motion information from event data, often by predicting event-based optical flow and reconstructing frames via pixel warping. However, such approaches introduce holes and blurring when pixel displacement is inaccurate. To overcome this limitation, we propose DESSERT, a diffusion-based event-driven single-frame synthesis framework via residual training. Leveraging a pre-trained Stable Diffusion model, our method is trained on inter-frame residuals to ensure temporal consistency. The training pipeline consists of two stages: (1) an Event-to-Residual Alignment Variational Autoencoder (ER-VAE) that aligns the event frame between anchor and target frames with the corresponding residual, and (2) a diffusion model that denoises the residual latent conditioned on event data. Furthermore, we introduce Diverse-Length Temporal (DLT) augmentation, which improves robustness by training on frame segments of varying temporal lengths. Experimental results demonstrate that our method outperforms existing event-based reconstruction, image-based video frame prediction, event-based video frame prediction, and one-sided event-based video frame interpolation methods, producing sharper and more temporally consistent frame synthesis.

