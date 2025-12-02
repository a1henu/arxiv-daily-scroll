---
layout: default
title: SAM3-UNet: Simplified Adaptation of Segment Anything Model 3
---

# SAM3-UNet: Simplified Adaptation of Segment Anything Model 3
**arXiv**：[2512.01789v1](https://arxiv.org/abs/2512.01789) · [PDF](https://arxiv.org/pdf/2512.01789.pdf)  
**作者**：Xinyu Xiong, Zihuang Wu, Lei Lu, Yufa Xia  

**一句话要点**：提出SAM3-UNet以低成本适配Segment Anything Model 3至下游任务

**关键词**：图像分割, 参数高效微调, 轻量解码器, 下游任务适配, SAM3

## 3 点简述
- 核心问题：如何高效适配SAM3至下游分割任务，降低计算成本。
- 方法要点：结合SAM3编码器、参数高效适配器和轻量U-Net解码器。
- 实验或效果：在镜面检测等任务中优于SAM2-UNet，训练内存低于6GB。

## 摘要（原文）

> In this paper, we introduce SAM3-UNet, a simplified variant of Segment Anything Model 3 (SAM3), designed to adapt SAM3 for downstream tasks at a low cost. Our SAM3-UNet consists of three components: a SAM3 image encoder, a simple adapter for parameter-efficient fine-tuning, and a lightweight U-Net-style decoder. Preliminary experiments on multiple tasks, such as mirror detection and salient object detection, demonstrate that the proposed SAM3-UNet outperforms the prior SAM2-UNet and other state-of-the-art methods, while requiring less than 6 GB of GPU memory during training with a batch size of 12. The code is publicly available at https://github.com/WZH0120/SAM3-UNet.

