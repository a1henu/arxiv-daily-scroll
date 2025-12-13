---
layout: default
title: Video Depth Propagation
---

# Video Depth Propagation
**arXiv**：[2512.10725v1](https://arxiv.org/abs/2512.10725) · [PDF](https://arxiv.org/pdf/2512.10725.pdf)  
**作者**：Luigi Piccinelli, Thiemo Wandel, Christos Sakaridis, Wim Abbeloos, Luc Van Gool  

**一句话要点**：提出VeloDepth以解决视频深度估计中的时间不一致和效率问题，适用于实时应用。

**关键词**：视频深度估计, 时间一致性, 特征传播, 实时应用, 零样本评估

## 3 点简述
- 核心问题：现有视频深度估计方法存在时间不一致或计算量大，限制实际应用。
- 方法要点：引入传播模块，基于光流扭曲和残差校正，有效利用时空先验进行深度特征传播。
- 实验或效果：在多个基准测试中实现零样本评估，展示领先的时间一致性和高效推理速度。

## 摘要（原文）

> Depth estimation in videos is essential for visual perception in real-world applications. However, existing methods either rely on simple frame-by-frame monocular models, leading to temporal inconsistencies and inaccuracies, or use computationally demanding temporal modeling, unsuitable for real-time applications. These limitations significantly restrict general applicability and performance in practical settings. To address this, we propose VeloDepth, an efficient and robust online video depth estimation pipeline that effectively leverages spatiotemporal priors from previous depth predictions and performs deep feature propagation. Our method introduces a novel Propagation Module that refines and propagates depth features and predictions using flow-based warping coupled with learned residual corrections. In addition, our design structurally enforces temporal consistency, resulting in stable depth predictions across consecutive frames with improved efficiency. Comprehensive zero-shot evaluation on multiple benchmarks demonstrates the state-of-the-art temporal consistency and competitive accuracy of VeloDepth, alongside its significantly faster inference compared to existing video-based depth estimators. VeloDepth thus provides a practical, efficient, and accurate solution for real-time depth estimation suitable for diverse perception tasks. Code and models are available at https://github.com/lpiccinelli-eth/velodepth

