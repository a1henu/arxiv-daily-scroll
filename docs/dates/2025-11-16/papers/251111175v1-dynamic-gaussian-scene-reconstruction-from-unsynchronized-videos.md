---
layout: default
title: Dynamic Gaussian Scene Reconstruction from Unsynchronized Videos
---

# Dynamic Gaussian Scene Reconstruction from Unsynchronized Videos
**arXiv**：[2511.11175v1](https://arxiv.org/abs/2511.11175) · [PDF](https://arxiv.org/pdf/2511.11175.pdf)  
**作者**：Zhixin Xu, Hengyu Zhou, Yuan Liu, Wenhan Xue, Hao Pan, Wenping Wang, Bin Wang  

**一句话要点**：提出动态高斯场景重建方法以解决非同步多视角视频的时间对齐问题

**关键词**：动态场景重建, 4D高斯溅射, 时间对齐, 多视角视频, 非同步数据, 计算机视觉

## 3 点简述
- 核心问题：多视角视频因相机触发延迟导致时间不同步，降低重建质量。
- 方法要点：采用粗到精对齐模块估计并补偿相机时间偏移，实现子帧精度。
- 实验或效果：实验显示方法有效处理时间错位视频，显著提升基线方法性能。

## 摘要（原文）

> Multi-view video reconstruction plays a vital role in computer vision, enabling applications in film production, virtual reality, and motion analysis. While recent advances such as 4D Gaussian Splatting (4DGS) have demonstrated impressive capabilities in dynamic scene reconstruction, they typically rely on the assumption that input video streams are temporally synchronized. However, in real-world scenarios, this assumption often fails due to factors like camera trigger delays or independent recording setups, leading to temporal misalignment across views and reduced reconstruction quality. To address this challenge, a novel temporal alignment strategy is proposed for high-quality 4DGS reconstruction from unsynchronized multi-view videos. Our method features a coarse-to-fine alignment module that estimates and compensates for each camera's time shift. The method first determines a coarse, frame-level offset and then refines it to achieve sub-frame accuracy. This strategy can be integrated as a readily integrable module into existing 4DGS frameworks, enhancing their robustness when handling asynchronous data. Experiments show that our approach effectively processes temporally misaligned videos and significantly enhances baseline methods.

