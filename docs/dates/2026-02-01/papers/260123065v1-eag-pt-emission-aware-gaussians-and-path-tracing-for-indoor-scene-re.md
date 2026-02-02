---
layout: default
title: EAG-PT: Emission-Aware Gaussians and Path Tracing for Indoor Scene Reconstruction and Editing
---

# EAG-PT: Emission-Aware Gaussians and Path Tracing for Indoor Scene Reconstruction and Editing
**arXiv**：[2601.23065v1](https://arxiv.org/abs/2601.23065) · [PDF](https://arxiv.org/pdf/2601.23065.pdf)  
**作者**：Xijie Yang, Mulin Yu, Changjian Jiang, Kerui Ren, Tao Lu, Jiangmiao Pang, Dahua Lin, Bo Dai, Linning Xu  

**一句话要点**：提出EAG-PT方法，基于2D高斯表示实现室内场景的物理光传输重建与编辑

**关键词**：室内场景重建, 物理光传输, 2D高斯表示, 逆渲染, 路径追踪, 场景编辑

## 3 点简述
- 核心问题：现有方法如NeRF和3DGS在场景编辑时因光照烘焙和缺乏显式光传输而失效，而基于网格的逆渲染对几何精度要求高。
- 方法要点：使用2D高斯作为统一场景表示和光传输友好的几何代理，分离发射与非发射组件，并采用单次反弹优化与多反弹路径追踪解耦重建与渲染。
- 实验效果：在合成和真实室内场景中，EAG-PT在编辑后产生更自然、物理一致的渲染，同时保留几何细节并避免网格伪影。

## 摘要（原文）

> Recent reconstruction methods based on radiance field such as NeRF and 3DGS reproduce indoor scenes with high visual fidelity, but break down under scene editing due to baked illumination and the lack of explicit light transport. In contrast, physically based inverse rendering relies on mesh representations and path tracing, which enforce correct light transport but place strong requirements on geometric fidelity, becoming a practical bottleneck for real indoor scenes. In this work, we propose Emission-Aware Gaussians and Path Tracing (EAG-PT), aiming for physically based light transport with a unified 2D Gaussian representation. Our design is based on three cores: (1) using 2D Gaussians as a unified scene representation and transport-friendly geometry proxy that avoids reconstructed mesh, (2) explicitly separating emissive and non-emissive components during reconstruction for further scene editing, and (3) decoupling reconstruction from final rendering by using efficient single-bounce optimization and high-quality multi-bounce path tracing after scene editing. Experiments on synthetic and real indoor scenes show that EAG-PT produces more natural and physically consistent renders after editing than radiant scene reconstructions, while preserving finer geometric detail and avoiding mesh-induced artifacts compared to mesh-based inverse path tracing. These results suggest promising directions for future use in interior design, XR content creation, and embodied AI.

