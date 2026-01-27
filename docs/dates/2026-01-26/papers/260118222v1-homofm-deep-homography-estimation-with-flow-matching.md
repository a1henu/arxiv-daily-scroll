---
layout: default
title: HomoFM: Deep Homography Estimation with Flow Matching
---

# HomoFM: Deep Homography Estimation with Flow Matching
**arXiv**：[2601.18222v1](https://arxiv.org/abs/2601.18222) · [PDF](https://arxiv.org/pdf/2601.18222.pdf)  
**作者**：Mengfan He, Liangzheng Sun, Chunyu Li, Ziyang Meng  

**一句话要点**：提出HomoFM框架，首次将流匹配技术引入单应性估计，以提升精度与鲁棒性。

**关键词**：单应性估计, 流匹配, 域适应, 速度场学习, 梯度反转层

## 3 点简述
- 现有深度单应性估计方法难以处理复杂几何变换或跨域泛化问题。
- 将单应性估计建模为速度场学习，通过条件流轨迹恢复高精度变换。
- 集成梯度反转层以学习域不变特征，实验显示在标准基准上优于现有方法。

## 摘要（原文）

> Deep homography estimation has broad applications in computer vision and robotics. Remarkable progresses have been achieved while the existing methods typically treat it as a direct regression or iterative refinement problem and often struggling to capture complex geometric transformations or generalize across different domains. In this work, we propose HomoFM, a new framework that introduces the flow matching technique from generative modeling into the homography estimation task for the first time. Unlike the existing methods, we formulate homography estimation problem as a velocity field learning problem. By modeling a continuous and point-wise velocity field that transforms noisy distributions into registered coordinates, the proposed network recovers high-precision transformations through a conditional flow trajectory. Furthermore, to address the challenge of domain shifts issue, e.g., the cases of multimodal matching or varying illumination scenarios, we integrate a gradient reversal layer (GRL) into the feature extraction backbone. This domain adaptation strategy explicitly constrains the encoder to learn domain-invariant representations, significantly enhancing the network's robustness. Extensive experiments demonstrate the effectiveness of the proposed method, showing that HomoFM outperforms state-of-the-art methods in both estimation accuracy and robustness on standard benchmarks. Code and data resource are available at https://github.com/hmf21/HomoFM.

