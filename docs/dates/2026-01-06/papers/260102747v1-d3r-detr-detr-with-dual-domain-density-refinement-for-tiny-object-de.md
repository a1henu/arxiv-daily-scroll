---
layout: default
title: D$^3$R-DETR: DETR with Dual-Domain Density Refinement for Tiny Object Detection in Aerial Images
---

# D$^3$R-DETR: DETR with Dual-Domain Density Refinement for Tiny Object Detection in Aerial Images
**arXiv**：[2601.02747v1](https://arxiv.org/abs/2601.02747) · [PDF](https://arxiv.org/pdf/2601.02747.pdf)  
**作者**：Zixiao Wen, Zhen Yang, Xianjie Bao, Lei Zhang, Xiantai Xiang, Wenshuai Li, Yuhan Liu  

**一句话要点**：提出D$^3$R-DETR，通过双域密度细化解决航拍图像中小目标检测的收敛慢和匹配不准问题。

**关键词**：小目标检测, 航拍图像, DETR, 双域融合, 密度图, Transformer检测器

## 3 点简述
- 核心问题：航拍图像中小目标像素信息有限且密度变化大，导致Transformer检测器收敛慢和查询-对象匹配不准。
- 方法要点：融合空间和频域信息，细化低层特征图，预测更准确的对象密度图以精确定位小目标。
- 实验或效果：在AI-TOD-v2数据集上实验，D$^3$R-DETR优于现有最先进的小目标检测器。

## 摘要（原文）

> Detecting tiny objects plays a vital role in remote sensing intelligent interpretation, as these objects often carry critical information for downstream applications. However, due to the extremely limited pixel information and significant variations in object density, mainstream Transformer-based detectors often suffer from slow convergence and inaccurate query-object matching. To address these challenges, we propose D$^3$R-DETR, a novel DETR-based detector with Dual-Domain Density Refinement. By fusing spatial and frequency domain information, our method refines low-level feature maps and utilizes their rich details to predict more accurate object density map, thereby guiding the model to precisely localize tiny objects. Extensive experiments on the AI-TOD-v2 dataset demonstrate that D$^3$R-DETR outperforms existing state-of-the-art detectors for tiny object detection.

