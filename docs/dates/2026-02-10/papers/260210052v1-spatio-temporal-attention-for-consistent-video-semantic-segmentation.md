---
layout: default
title: Spatio-Temporal Attention for Consistent Video Semantic Segmentation in Automated Driving
---

# Spatio-Temporal Attention for Consistent Video Semantic Segmentation in Automated Driving
**arXiv**：[2602.10052v1](https://arxiv.org/abs/2602.10052) · [PDF](https://arxiv.org/pdf/2602.10052.pdf)  
**作者**：Serin Varghese, Kevin Ross, Fabian Hueger, Kira Maag  

**一句话要点**：提出时空注意力机制以提升自动驾驶视频语义分割的准确性和稳定性

**关键词**：视频语义分割, 时空注意力, 自动驾驶, Transformer架构, 时间一致性

## 3 点简述
- 现有模型独立处理视频帧，未利用时间一致性，影响动态场景性能
- 扩展Transformer注意力块，引入多帧上下文，实现高效时空特征表示
- 在Cityscapes和BDD100k数据集上，时间一致性指标提升9.20个百分点，mIoU最高提升1.76个百分点

## 摘要（原文）

> Deep neural networks, especially transformer-based architectures, have achieved remarkable success in semantic segmentation for environmental perception. However, existing models process video frames independently, thus failing to leverage temporal consistency, which could significantly improve both accuracy and stability in dynamic scenes. In this work, we propose a Spatio-Temporal Attention (STA) mechanism that extends transformer attention blocks to incorporate multi-frame context, enabling robust temporal feature representations for video semantic segmentation. Our approach modifies standard self-attention to process spatio-temporal feature sequences while maintaining computational efficiency and requiring minimal changes to existing architectures. STA demonstrates broad applicability across diverse transformer architectures and remains effective across both lightweight and larger-scale models. A comprehensive evaluation on the Cityscapes and BDD100k datasets shows substantial improvements of 9.20 percentage points in temporal consistency metrics and up to 1.76 percentage points in mean intersection over union compared to single-frame baselines. These results demonstrate STA as an effective architectural enhancement for video-based semantic segmentation applications.

