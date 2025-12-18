---
layout: default
title: 3DProxyImg: Controllable 3D-Aware Animation Synthesis from Single Image via 2D-3D Aligned Proxy Embedding
---

# 3DProxyImg: Controllable 3D-Aware Animation Synthesis from Single Image via 2D-3D Aligned Proxy Embedding
**arXiv**：[2512.15126v1](https://arxiv.org/abs/2512.15126) · [PDF](https://arxiv.org/pdf/2512.15126.pdf)  
**作者**：Yupeng Zhu, Xiongzhen Zhang, Ye Chen, Bingbing Ni  

**一句话要点**：提出2D-3D对齐代理嵌入框架，以解决单图像3D动画生成中渲染质量与3D控制间的权衡问题。

**关键词**：单图像3D动画生成, 2D-3D对齐代理, 几何控制解耦, 轻量级框架, 交互式控制, 外观合成

## 3 点简述
- 核心问题：单图像3D动画生成面临渲染质量与3D控制间的根本权衡，传统方法成本高或可控性差。
- 方法要点：通过解耦几何控制与外观合成，使用粗糙3D估计作为结构载体，依赖图像空间生成先验实现高保真外观。
- 实验或效果：在低功耗平台上实现高效动画生成，在身份保持、几何纹理一致性和交互控制方面优于基于视频的方法。

## 摘要（原文）

> 3D animation is central to modern visual media, yet traditional production pipelines remain labor-intensive, expertise-demanding, and computationally expensive. Recent AIGC-based approaches partially automate asset creation and rigging, but they either inherit the heavy costs of full 3D pipelines or rely on video-synthesis paradigms that sacrifice 3D controllability and interactivity. We focus on single-image 3D animation generation and argue that progress is fundamentally constrained by a trade-off between rendering quality and 3D control.
>   To address this limitation, we propose a lightweight 3D animation framework that decouples geometric control from appearance synthesis. The core idea is a 2D-3D aligned proxy representation that uses a coarse 3D estimate as a structural carrier, while delegating high-fidelity appearance and view synthesis to learned image-space generative priors. This proxy formulation enables 3D-aware motion control and interaction comparable to classical pipelines, without requiring accurate geometry or expensive optimization, and naturally extends to coherent background animation. Extensive experiments demonstrate that our method achieves efficient animation generation on low-power platforms and outperforms video-based 3D animation generation in identity preservation, geometric and textural consistency, and the level of precise, interactive control it offers to users.

