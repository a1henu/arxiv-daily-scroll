---
layout: default
title: Lighting in Motion: Spatiotemporal HDR Lighting Estimation
---

# Lighting in Motion: Spatiotemporal HDR Lighting Estimation
**arXiv**：[2512.13597v1](https://arxiv.org/abs/2512.13597) · [PDF](https://arxiv.org/pdf/2512.13597.pdf)  
**作者**：Christophe Bolduc, Julien Philip, Li Ma, Mingming He, Paul Debevec, Jean-François Lalonde  

**一句话要点**：提出LiMo扩散模型，用于时空高动态范围光照估计，提升细节与照度准确性。

**关键词**：时空光照估计, 扩散模型, 高动态范围成像, 几何条件, 可微分渲染

## 3 点简述
- 核心问题：时空光照估计需兼顾高频细节与照度准确性，现有方法空间控制不足。
- 方法要点：基于扩散先验，生成多曝光球体，引入新几何条件增强空间控制。
- 实验或效果：在定制数据集上评估，LiMo在空间控制与预测精度上达到先进水平。

## 摘要（原文）

> We present Lighting in Motion (LiMo), a diffusion-based approach to spatiotemporal lighting estimation. LiMo targets both realistic high-frequency detail prediction and accurate illuminance estimation. To account for both, we propose generating a set of mirrored and diffuse spheres at different exposures, based on their 3D positions in the input. Making use of diffusion priors, we fine-tune powerful existing diffusion models on a large-scale customized dataset of indoor and outdoor scenes, paired with spatiotemporal light probes. For accurate spatial conditioning, we demonstrate that depth alone is insufficient and we introduce a new geometric condition to provide the relative position of the scene to the target 3D position. Finally, we combine diffuse and mirror predictions at different exposures into a single HDRI map leveraging differentiable rendering. We thoroughly evaluate our method and design choices to establish LiMo as state-of-the-art for both spatial control and prediction accuracy.

