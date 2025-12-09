---
layout: default
title: WorldReel: 4D Video Generation with Consistent Geometry and Motion Modeling
---

# WorldReel: 4D Video Generation with Consistent Geometry and Motion Modeling
**arXiv**：[2512.07821v1](https://arxiv.org/abs/2512.07821) · [PDF](https://arxiv.org/pdf/2512.07821.pdf)  
**作者**：Shaoheng Fang, Hanwen Jiang, Yunpeng Bai, Niloy J. Mitra, Qixing Huang  

**一句话要点**：提出WorldReel以解决视频生成中3D不一致问题，通过4D场景表示实现时空一致性。

**关键词**：4D视频生成, 时空一致性, 几何建模, 运动建模, 合成与真实数据融合, 动态场景处理

## 3 点简述
- 现有视频生成器在3D上存在不一致性，WorldReel联合生成RGB帧和4D场景表示（如点云、相机轨迹）。
- 方法结合合成数据提供精确4D监督和真实视频增强视觉多样性，确保几何保真度和泛化能力。
- 实验显示WorldReel在动态场景和移动相机下提升几何一致性、运动连贯性，减少视时伪影，优于现有方法。

## 摘要（原文）

> Recent video generators achieve striking photorealism, yet remain fundamentally inconsistent in 3D. We present WorldReel, a 4D video generator that is natively spatio-temporally consistent. WorldReel jointly produces RGB frames together with 4D scene representations, including pointmaps, camera trajectory, and dense flow mapping, enabling coherent geometry and appearance modeling over time. Our explicit 4D representation enforces a single underlying scene that persists across viewpoints and dynamic content, yielding videos that remain consistent even under large non-rigid motion and significant camera movement. We train WorldReel by carefully combining synthetic and real data: synthetic data providing precise 4D supervision (geometry, motion, and camera), while real videos contribute visual diversity and realism. This blend allows WorldReel to generalize to in-the-wild footage while preserving strong geometric fidelity. Extensive experiments demonstrate that WorldReel sets a new state-of-the-art for consistent video generation with dynamic scenes and moving cameras, improving metrics of geometric consistency, motion coherence, and reducing view-time artifacts over competing methods. We believe that WorldReel brings video generation closer to 4D-consistent world modeling, where agents can render, interact, and reason about scenes through a single and stable spatiotemporal representation.

