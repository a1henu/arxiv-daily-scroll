---
layout: default
title: UFO-DETR: Frequency-Guided End-to-End Detector for UAV Tiny Objects
---

# UFO-DETR: Frequency-Guided End-to-End Detector for UAV Tiny Objects
**arXiv**：[2602.22712v1](https://arxiv.org/abs/2602.22712) · [PDF](https://arxiv.org/pdf/2602.22712.pdf)  
**作者**：Yuankai Chen, Kai Lin, Qihong Wu, Xinxuan Yang, Jiashuo Lai, Ruoen Chen, Haonan Shi, Minfan He, Meihua Wang  

**一句话要点**：提出UFO-DETR以解决无人机图像中小目标检测的挑战

**关键词**：无人机图像检测, 小目标检测, 端到端检测器, 频率特征增强, 多尺度建模

## 3 点简述
- 核心问题：无人机图像中小目标检测面临尺度变化、密集分布和计算效率平衡难题
- 方法要点：集成LSKNet骨干、DAttention和AIFI模块，并引入DynFreq-C3进行跨空间频率特征增强
- 实验或效果：相比RT-DETR-L，在检测性能和计算效率上均有显著优势

## 摘要（原文）

> Small target detection in UAV imagery faces significant challenges such as scale variations, dense distribution, and the dominance of small targets. Existing algorithms rely on manually designed components, and general-purpose detectors are not optimized for UAV images, making it difficult to balance accuracy and complexity. To address these challenges, this paper proposes an end-to-end object detection framework, UFO-DETR, which integrates an LSKNet-based backbone network to optimize the receptive field and reduce the number of parameters. By combining the DAttention and AIFI modules, the model flexibly models multi-scale spatial relationships, improving multi-scale target detection performance. Additionally, the DynFreq-C3 module is proposed to enhance small target detection capability through cross-space frequency feature enhancement. Experimental results show that, compared to RT-DETR-L, the proposed method offers significant advantages in both detection performance and computational efficiency, providing an efficient solution for UAV edge computing.

