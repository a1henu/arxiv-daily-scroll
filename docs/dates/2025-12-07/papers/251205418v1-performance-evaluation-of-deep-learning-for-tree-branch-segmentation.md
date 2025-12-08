---
layout: default
title: Performance Evaluation of Deep Learning for Tree Branch Segmentation in Autonomous Forestry Systems
---

# Performance Evaluation of Deep Learning for Tree Branch Segmentation in Autonomous Forestry Systems
**arXiv**：[2512.05418v1](https://arxiv.org/abs/2512.05418) · [PDF](https://arxiv.org/pdf/2512.05418.pdf)  
**作者**：Yida Lin, Bing Xue, Mengjie Zhang, Sam Schofield, Richard Green  

**一句话要点**：评估深度学习在自主林业系统中树分支分割的性能，建立多分辨率精度-效率权衡基准。

**关键词**：树分支分割, 深度学习评估, 多分辨率基准, 自主林业系统, 精度-效率权衡

## 3 点简述
- 核心问题：无人机自主林业操作需快速精确的树分支分割，以应对不同像素分辨率和操作条件。
- 方法要点：使用Urban Street Tree Dataset，在三种分辨率下评估多种深度学习模型，包括标准指标和专门指标如TS-IoU和CPR。
- 实验或效果：U-Net+MiT-B4在256x256表现强，MiT-B4在512x512领先，U-Net+MiT-B3在1024x1024验证性能最佳，PSPNet效率最高但精度降低。

## 摘要（原文）

> UAV-based autonomous forestry operations require rapid and precise tree branch segmentation for safe navigation and automated pruning across varying pixel resolutions and operational conditions. We evaluate different deep learning methods at three resolutions (256x256, 512x512, 1024x1024) using the Urban Street Tree Dataset, employing standard metrics (IoU, Dice) and specialized measures including Thin Structure IoU (TS-IoU) and Connectivity Preservation Rate (CPR). Among 22 configurations tested, U-Net with MiT-B4 backbone achieves strong performance at 256x256. At 512x512, MiT-B4 leads in IoU, Dice, TS-IoU, and Boundary-F1. At 1024x1024, U-Net+MiT-B3 shows the best validation performance for IoU/Dice and precision, while U-Net++ excels in boundary quality. PSPNet provides the most efficient option (2.36/9.43/37.74 GFLOPs) with 25.7/19.6/11.8 percentage point IoU reductions compared to top performers at respective resolutions. These results establish multi-resolution benchmarks for accuracy-efficiency trade-offs in embedded forestry systems. Implementation is available at https://github.com/BennyLinntu/PerformanceTreeBranchSegmentation.

