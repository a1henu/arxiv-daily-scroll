---
layout: default
title: CRISP: Contact-Guided Real2Sim from Monocular Video with Planar Scene Primitives
---

# CRISP: Contact-Guided Real2Sim from Monocular Video with Planar Scene Primitives
**arXiv**：[2512.14696v1](https://arxiv.org/abs/2512.14696) · [PDF](https://arxiv.org/pdf/2512.14696.pdf)  
**作者**：Zihan Wang, Jiashun Wang, Jeff Tan, Yiwen Zhao, Jessica Hodgins, Shubham Tulsiani, Deva Ramanan  

**一句话要点**：提出CRISP方法，从单目视频恢复可模拟人体运动与场景几何，提升物理交互的鲁棒性。

**关键词**：单目视频重建, 人-场景交互, 平面基元拟合, 强化学习模拟, 物理验证运动, 真实到模拟

## 3 点简述
- 核心问题：现有方法依赖数据先验或无物理优化，导致几何噪声和运动跟踪失败。
- 方法要点：通过深度、法线和光流聚类拟合平面基元，结合人-场景接触建模恢复遮挡几何。
- 实验效果：在基准测试中降低跟踪失败率至6.9%，提升模拟吞吐量43%，验证于真实和生成视频。

## 摘要（原文）

> We introduce CRISP, a method that recovers simulatable human motion and scene geometry from monocular video. Prior work on joint human-scene reconstruction relies on data-driven priors and joint optimization with no physics in the loop, or recovers noisy geometry with artifacts that cause motion tracking policies with scene interactions to fail. In contrast, our key insight is to recover convex, clean, and simulation-ready geometry by fitting planar primitives to a point cloud reconstruction of the scene, via a simple clustering pipeline over depth, normals, and flow. To reconstruct scene geometry that might be occluded during interactions, we make use of human-scene contact modeling (e.g., we use human posture to reconstruct the occluded seat of a chair). Finally, we ensure that human and scene reconstructions are physically-plausible by using them to drive a humanoid controller via reinforcement learning. Our approach reduces motion tracking failure rates from 55.2\% to 6.9\% on human-centric video benchmarks (EMDB, PROX), while delivering a 43\% faster RL simulation throughput. We further validate it on in-the-wild videos including casually-captured videos, Internet videos, and even Sora-generated videos. This demonstrates CRISP's ability to generate physically-valid human motion and interaction environments at scale, greatly advancing real-to-sim applications for robotics and AR/VR.

