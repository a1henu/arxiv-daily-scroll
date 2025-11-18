---
layout: default
title: CoordAR: One-Reference 6D Pose Estimation of Novel Objects via Autoregressive Coordinate Map Generation
---

# CoordAR: One-Reference 6D Pose Estimation of Novel Objects via Autoregressive Coordinate Map Generation
**arXiv**：[2511.12919v1](https://arxiv.org/abs/2511.12919) · [PDF](https://arxiv.org/pdf/2511.12919.pdf)  
**作者**：Dexin Zuo, Ang Li, Wei Wang, Wenxian Yu, Danping Zou  

**一句话要点**：提出CoordAR自回归框架以解决单参考视图下新物体6D姿态估计问题

**关键词**：6D姿态估计, 自回归模型, 单参考视图, 3D-3D对应, 概率预测, Transformer解码器

## 3 点简述
- 核心问题：新物体6D姿态估计依赖3D模型，现有方法在对称和遮挡场景下全局一致性不足
- 方法要点：将3D-3D对应关系离散化为token，采用自回归和概率预测提升准确性
- 实验效果：在多个基准测试中显著优于现有方法，对对称和遮挡具有强鲁棒性

## 摘要（原文）

> Object 6D pose estimation, a crucial task for robotics and augmented reality applications, becomes particularly challenging when dealing with novel objects whose 3D models are not readily available. To reduce dependency on 3D models, recent studies have explored one-reference-based pose estimation, which requires only a single reference view instead of a complete 3D model. However, existing methods that rely on real-valued coordinate regression suffer from limited global consistency due to the local nature of convolutional architectures and face challenges in symmetric or occluded scenarios owing to a lack of uncertainty modeling. We present CoordAR, a novel autoregressive framework for one-reference 6D pose estimation of unseen objects. CoordAR formulates 3D-3D correspondences between the reference and query views as a map of discrete tokens, which is obtained in an autoregressive and probabilistic manner. To enable accurate correspondence regression, CoordAR introduces 1) a novel coordinate map tokenization that enables probabilistic prediction over discretized 3D space; 2) a modality-decoupled encoding strategy that separately encodes RGB appearance and coordinate cues; and 3) an autoregressive transformer decoder conditioned on both position-aligned query features and the partially generated token sequence. With these novel mechanisms, CoordAR significantly outperforms existing methods on multiple benchmarks and demonstrates strong robustness to symmetry, occlusion, and other challenges in real-world tests.

