---
layout: default
title: DGGT: Feedforward 4D Reconstruction of Dynamic Driving Scenes using Unposed Images
---

# DGGT: Feedforward 4D Reconstruction of Dynamic Driving Scenes using Unposed Images
**arXiv**：[2512.03004v1](https://arxiv.org/abs/2512.03004) · [PDF](https://arxiv.org/pdf/2512.03004.pdf)  
**作者**：Xiaoxue Chen, Ziyi Xiong, Yuantao Chen, Gen Li, Nan Wang, Hongcheng Luo, Long Chen, Haiyang Sun, Bing Wang, Guang Chen, Hangjun Ye, Hongyang Li, Ya-Qin Zhang, Hao Zhao  

**一句话要点**：提出DGGT框架，从无位姿图像实现前馈式动态驾驶场景4D重建。

**关键词**：动态场景重建, 无位姿重建, 4D重建, 驾驶场景, 前馈模型, 高斯图预测

## 3 点简述
- 核心问题：现有动态驾驶场景重建方法依赖位姿输入或逐场景优化，导致速度慢、灵活性差。
- 方法要点：联合预测3D高斯图和相机参数，通过动态头和寿命头解耦动态并保持时序一致性。
- 实验或效果：在多个大规模驾驶数据集上实现SOTA性能和速度，支持零样本跨数据集迁移。

## 摘要（原文）

> Autonomous driving needs fast, scalable 4D reconstruction and re-simulation for training and evaluation, yet most methods for dynamic driving scenes still rely on per-scene optimization, known camera calibration, or short frame windows, making them slow and impractical. We revisit this problem from a feedforward perspective and introduce \textbf{Driving Gaussian Grounded Transformer (DGGT)}, a unified framework for pose-free dynamic scene reconstruction. We note that the existing formulations, treating camera pose as a required input, limit flexibility and scalability. Instead, we reformulate pose as an output of the model, enabling reconstruction directly from sparse, unposed images and supporting an arbitrary number of views for long sequences. Our approach jointly predicts per-frame 3D Gaussian maps and camera parameters, disentangles dynamics with a lightweight dynamic head, and preserves temporal consistency with a lifespan head that modulates visibility over time. A diffusion-based rendering refinement further reduces motion/interpolation artifacts and improves novel-view quality under sparse inputs. The result is a single-pass, pose-free algorithm that achieves state-of-the-art performance and speed. Trained and evaluated on large-scale driving benchmarks (Waymo, nuScenes, Argoverse2), our method outperforms prior work both when trained on each dataset and in zero-shot transfer across datasets, and it scales well as the number of input frames increases.

