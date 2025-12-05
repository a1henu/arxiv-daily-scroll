---
layout: default
title: MAFNet:Multi-frequency Adaptive Fusion Network for Real-time Stereo Matching
---

# MAFNet:Multi-frequency Adaptive Fusion Network for Real-time Stereo Matching
**arXiv**：[2512.04358v1](https://arxiv.org/abs/2512.04358) · [PDF](https://arxiv.org/pdf/2512.04358.pdf)  
**作者**：Ao Xu, Rujin Zhao, Xiong Xu, Boceng Huang, Yujia Jia, Hongfeng Long, Fuxuan Chen, Zilong Cao, Fangyuan Chen  

**一句话要点**：提出MAFNet以在资源受限设备上实现实时立体匹配，通过多频自适应融合提升精度与效率。

**关键词**：立体匹配, 实时计算, 频域滤波, 注意力机制, 成本体积, 移动设备

## 3 点简述
- 现有立体匹配网络在计算开销或非局部上下文建模上存在不足，限制实时部署。
- MAFNet设计自适应频域滤波注意力模块，分解成本体积为高低频部分进行特征聚合。
- 实验显示MAFNet在Scene Flow和KITTI 2015数据集上优于现有实时方法，平衡精度与速度。

## 摘要（原文）

> Existing stereo matching networks typically rely on either cost-volume construction based on 3D convolutions or deformation methods based on iterative optimization. The former incurs significant computational overhead during cost aggregation, whereas the latter often lacks the ability to model non-local contextual information. These methods exhibit poor compatibility on resource-constrained mobile devices, limiting their deployment in real-time applications. To address this, we propose a Multi-frequency Adaptive Fusion Network (MAFNet), which can produce high-quality disparity maps using only efficient 2D convolutions. Specifically, we design an adaptive frequency-domain filtering attention module that decomposes the full cost volume into high-frequency and low-frequency volumes, performing frequency-aware feature aggregation separately. Subsequently, we introduce a Linformer-based low-rank attention mechanism to adaptively fuse high- and low-frequency information, yielding more robust disparity estimation. Extensive experiments demonstrate that the proposed MAFNet significantly outperforms existing real-time methods on public datasets such as Scene Flow and KITTI 2015, showing a favorable balance between accuracy and real-time performance.

