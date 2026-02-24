---
layout: default
title: Flow3r: Factored Flow Prediction for Scalable Visual Geometry Learning
---

# Flow3r: Factored Flow Prediction for Scalable Visual Geometry Learning
**arXiv**：[2602.20157v1](https://arxiv.org/abs/2602.20157) · [PDF](https://arxiv.org/pdf/2602.20157.pdf)  
**作者**：Zhongxiao Cong, Qitao Zhao, Minsik Jeon, Shubham Tulsiani  

**一句话要点**：提出Flow3r框架，通过分解流预测实现无监督单目视频的视觉几何学习

**关键词**：视觉几何学习, 无监督学习, 流预测, 单目视频, 动态场景, 分解预测

## 3 点简述
- 当前3D/4D重建系统依赖密集几何和姿态监督，数据获取成本高且稀缺
- Flow3r使用分解流预测，从几何潜变量和姿态潜变量分别预测图像间流，指导几何和相机运动学习
- 在无标签视频上训练，Flow3r在静态和动态场景基准上取得先进结果，尤其在动态视频中提升显著

## 摘要（原文）

> Current feed-forward 3D/4D reconstruction systems rely on dense geometry and pose supervision -- expensive to obtain at scale and particularly scarce for dynamic real-world scenes. We present Flow3r, a framework that augments visual geometry learning with dense 2D correspondences (`flow') as supervision, enabling scalable training from unlabeled monocular videos. Our key insight is that the flow prediction module should be factored: predicting flow between two images using geometry latents from one and pose latents from the other. This factorization directly guides the learning of both scene geometry and camera motion, and naturally extends to dynamic scenes. In controlled experiments, we show that factored flow prediction outperforms alternative designs and that performance scales consistently with unlabeled data. Integrating factored flow into existing visual geometry architectures and training with ${\sim}800$K unlabeled videos, Flow3r achieves state-of-the-art results across eight benchmarks spanning static and dynamic scenes, with its largest gains on in-the-wild dynamic videos where labeled data is most scarce.

