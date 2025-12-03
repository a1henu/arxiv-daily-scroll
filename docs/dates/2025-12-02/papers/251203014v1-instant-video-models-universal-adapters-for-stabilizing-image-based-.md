---
layout: default
title: Instant Video Models: Universal Adapters for Stabilizing Image-Based Networks
---

# Instant Video Models: Universal Adapters for Stabilizing Image-Based Networks
**arXiv**：[2512.03014v1](https://arxiv.org/abs/2512.03014) · [PDF](https://arxiv.org/pdf/2512.03014.pdf)  
**作者**：Matthew Dutson, Nathan Labiosa, Yin Li, Mohit Gupta  

**一句话要点**：提出通用稳定性适配器以解决图像网络在视频处理中的时序不一致问题

**关键词**：视频稳定性, 通用适配器, 时序一致性, 图像噪声鲁棒性, 冻结网络训练, 精度-稳定性-鲁棒性损失

## 3 点简述
- 核心问题：帧基网络在视频序列中输出时序不一致，如闪烁，输入含时变噪声时加剧
- 方法要点：设计可插入任意架构的稳定性适配器，基于冻结基网络进行高效训练，提出精度-稳定性-鲁棒性损失统一框架
- 实验或效果：在去噪、图像增强、深度估计和语义分割任务中验证，提升时序稳定性和抗图像噪声鲁棒性，保持或改进预测质量

## 摘要（原文）

> When applied sequentially to video, frame-based networks often exhibit temporal inconsistency - for example, outputs that flicker between frames. This problem is amplified when the network inputs contain time-varying corruptions. In this work, we introduce a general approach for adapting frame-based models for stable and robust inference on video. We describe a class of stability adapters that can be inserted into virtually any architecture and a resource-efficient training process that can be performed with a frozen base network. We introduce a unified conceptual framework for describing temporal stability and corruption robustness, centered on a proposed accuracy-stability-robustness loss. By analyzing the theoretical properties of this loss, we identify the conditions where it produces well-behaved stabilizer training. Our experiments validate our approach on several vision tasks including denoising (NAFNet), image enhancement (HDRNet), monocular depth (Depth Anything v2), and semantic segmentation (DeepLabv3+). Our method improves temporal stability and robustness against a range of image corruptions (including compression artifacts, noise, and adverse weather), while preserving or improving the quality of predictions.

