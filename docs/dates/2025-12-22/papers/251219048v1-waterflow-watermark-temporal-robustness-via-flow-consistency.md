---
layout: default
title: WaTeRFlow: Watermark Temporal Robustness via Flow Consistency
---

# WaTeRFlow: Watermark Temporal Robustness via Flow Consistency
**arXiv**：[2512.19048v1](https://arxiv.org/abs/2512.19048) · [PDF](https://arxiv.org/pdf/2512.19048.pdf)  
**作者**：Utae Jeong, Sumin In, Hyunju Ryu, Jaewan Choi, Feng Yang, Jongheon Jeong, Seungryong Kim, Sangpil Kim  

**一句话要点**：提出WaTeRFlow框架以增强图像水印在图像转视频中的时序鲁棒性

**关键词**：图像水印, 时序鲁棒性, 图像转视频, 流一致性, 深度学习水印

## 3 点简述
- 核心问题：图像水印在图像转视频后检测性能下降，现有方法对时序失真鲁棒性不足
- 方法要点：结合流引导合成引擎、时序一致性损失和语义保持损失，提升跨模态水印恢复
- 实验或效果：在多种图像转视频模型中实现高精度水印恢复，对失真具有强韧性

## 摘要（原文）

> Image watermarking supports authenticity and provenance, yet many schemes are still easy to bypass with various distortions and powerful generative edits. Deep learning-based watermarking has improved robustness to diffusion-based image editing, but a gap remains when a watermarked image is converted to video by image-to-video (I2V), in which per-frame watermark detection weakens. I2V has quickly advanced from short, jittery clips to multi-second, temporally coherent scenes, and it now serves not only content creation but also world-modeling and simulation workflows, making cross-modal watermark recovery crucial. We present WaTeRFlow, a framework tailored for robustness under I2V. It consists of (i) FUSE (Flow-guided Unified Synthesis Engine), which exposes the encoder-decoder to realistic distortions via instruction-driven edits and a fast video diffusion proxy during training, (ii) optical-flow warping with a Temporal Consistency Loss (TCL) that stabilizes per-frame predictions, and (iii) a semantic preservation loss that maintains the conditioning signal. Experiments across representative I2V models show accurate watermark recovery from frames, with higher first-frame and per-frame bit accuracy and resilience when various distortions are applied before or after video generation.

