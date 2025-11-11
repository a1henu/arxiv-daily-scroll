---
layout: default
title: HENet++: Hybrid Encoding and Multi-task Learning for 3D Perception and End-to-end Autonomous Driving
---

# HENet++: Hybrid Encoding and Multi-task Learning for 3D Perception and End-to-end Autonomous Driving
**arXiv**：[2511.07106v1](https://arxiv.org/abs/2511.07106) · [PDF](https://arxiv.org/pdf/2511.07106.pdf)  
**作者**：Zhongyu Xia, Zhiwei Lin, Yongtao Wang, Ming-Hsuan Yang  

**一句话要点**：提出HENet++框架，通过混合编码和多任务学习解决自动驾驶3D感知与端到端推理问题

**关键词**：3D感知, 端到端自动驾驶, 混合编码, 多任务学习, 鸟瞰图分割, 占用预测

## 3 点简述
- 核心问题：计算资源限制下，大图像编码器和高分辨率输入难以兼容多任务3D感知
- 方法要点：使用大编码器处理短期帧、小编码器处理长期帧，并提取稠密与稀疏特征
- 实验或效果：在nuScenes基准上实现SOTA多任务感知和最低碰撞率

## 摘要（原文）

> Three-dimensional feature extraction is a critical component of autonomous
> driving systems, where perception tasks such as 3D object detection,
> bird's-eye-view (BEV) semantic segmentation, and occupancy prediction serve as
> important constraints on 3D features. While large image encoders,
> high-resolution images, and long-term temporal inputs can significantly enhance
> feature quality and deliver remarkable performance gains, these techniques are
> often incompatible in both training and inference due to computational resource
> constraints. Moreover, different tasks favor distinct feature representations,
> making it difficult for a single model to perform end-to-end inference across
> multiple tasks while maintaining accuracy comparable to that of single-task
> models. To alleviate these issues, we present the HENet and HENet++ framework
> for multi-task 3D perception and end-to-end autonomous driving. Specifically,
> we propose a hybrid image encoding network that uses a large image encoder for
> short-term frames and a small one for long-term frames. Furthermore, our
> framework simultaneously extracts both dense and sparse features, providing
> more suitable representations for different tasks, reducing cumulative errors,
> and delivering more comprehensive information to the planning module. The
> proposed architecture maintains compatibility with various existing 3D feature
> extraction methods and supports multimodal inputs. HENet++ achieves
> state-of-the-art end-to-end multi-task 3D perception results on the nuScenes
> benchmark, while also attaining the lowest collision rate on the nuScenes
> end-to-end autonomous driving benchmark.

