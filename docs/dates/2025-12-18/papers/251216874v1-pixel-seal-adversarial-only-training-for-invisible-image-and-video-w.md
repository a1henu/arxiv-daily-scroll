---
layout: default
title: Pixel Seal: Adversarial-only training for invisible image and video watermarking
---

# Pixel Seal: Adversarial-only training for invisible image and video watermarking
**arXiv**：[2512.16874v1](https://arxiv.org/abs/2512.16874) · [PDF](https://arxiv.org/pdf/2512.16874.pdf)  
**作者**：Tomáš Souček, Pierre Fernandez, Hady Elsahar, Sylvestre-Alvise Rebuffi, Valeriu Lacatusu, Tuan Tran, Tom Sander, Alexandre Mourachko  

**一句话要点**：提出Pixel Seal，通过对抗性训练解决图像和视频不可见水印的鲁棒性与不可感知性平衡问题

**关键词**：不可见水印, 对抗性训练, 高分辨率适应, 视频水印, 鲁棒性优化, 不可感知性

## 3 点简述
- 核心问题：现有方法依赖代理感知损失导致可见水印，优化不稳定，高分辨率下性能下降
- 方法要点：采用对抗性训练消除像素级损失，三阶段训练解耦目标，高分辨率适应消除缩放伪影
- 实验或效果：在多种图像类型和变换下评估，鲁棒性和不可感知性优于现有技术，视频适应高效

## 摘要（原文）

> Invisible watermarking is essential for tracing the provenance of digital content. However, training state-of-the-art models remains notoriously difficult, with current approaches often struggling to balance robustness against true imperceptibility. This work introduces Pixel Seal, which sets a new state-of-the-art for image and video watermarking. We first identify three fundamental issues of existing methods: (i) the reliance on proxy perceptual losses such as MSE and LPIPS that fail to mimic human perception and result in visible watermark artifacts; (ii) the optimization instability caused by conflicting objectives, which necessitates exhaustive hyperparameter tuning; and (iii) reduced robustness and imperceptibility of watermarks when scaling models to high-resolution images and videos. To overcome these issues, we first propose an adversarial-only training paradigm that eliminates unreliable pixel-wise imperceptibility losses. Second, we introduce a three-stage training schedule that stabilizes convergence by decoupling robustness and imperceptibility. Third, we address the resolution gap via high-resolution adaptation, employing JND-based attenuation and training-time inference simulation to eliminate upscaling artifacts. We thoroughly evaluate the robustness and imperceptibility of Pixel Seal on different image types and across a wide range of transformations, and show clear improvements over the state-of-the-art. We finally demonstrate that the model efficiently adapts to video via temporal watermark pooling, positioning Pixel Seal as a practical and scalable solution for reliable provenance in real-world image and video settings.

