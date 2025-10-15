---
layout: default
title: An Adaptive Edge-Guided Dual-Network Framework for Fast QR Code Motion Deblurring
---

# An Adaptive Edge-Guided Dual-Network Framework for Fast QR Code Motion Deblurring
**arXiv**：[2510.12098v1](https://arxiv.org/abs/2510.12098) · [PDF](https://arxiv.org/pdf/2510.12098.pdf)  
**作者**：Jianping Li, Dongyang Guo, Wenjie Li, Wei Zhao  

**一句话要点**：提出自适应双网络框架，结合边缘引导Transformer和轻量网络，优化移动设备上QR码运动去模糊。

**关键词**：QR码去模糊, 边缘引导注意力, 自适应网络, Transformer架构, 移动设备优化

## 3 点简述
- 核心问题：现有深度学习方法未充分利用QR码结构化边缘先验，影响解码成功率。
- 方法要点：设计边缘引导注意力块和自适应双网络，根据模糊程度动态选择模型。
- 实验或效果：在严重模糊QR码上提升解码率，速度快，适合移动设备部署。

## 摘要（原文）

> Unlike general image deblurring that prioritizes perceptual quality, QR code
> deblurring focuses on ensuring successful decoding. QR codes are characterized
> by highly structured patterns with sharp edges, a robust prior for restoration.
> Yet existing deep learning methods rarely exploit these priors explicitly. To
> address this gap, we propose the Edge-Guided Attention Block (EGAB), which
> embeds explicit edge priors into a Transformer architecture. Based on EGAB, we
> develop Edge-Guided Restormer (EG-Restormer), an effective network that
> significantly boosts the decoding rate of severely blurred QR codes. For mildly
> blurred inputs, we design the Lightweight and Efficient Network (LENet) for
> fast deblurring. We further integrate these two networks into an Adaptive
> Dual-network (ADNet), which dynamically selects the suitable network based on
> input blur severity, making it ideal for resource-constrained mobile devices.
> Extensive experiments show that our EG-Restormer and ADNet achieve
> state-of-the-art performance with a competitive speed. Project page:
> https://github.com/leejianping/ADNet

