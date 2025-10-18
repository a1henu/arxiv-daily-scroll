---
layout: default
title: 3D Scene Prompting for Scene-Consistent Camera-Controllable Video Generation
---

# 3D Scene Prompting for Scene-Consistent Camera-Controllable Video Generation
**arXiv**：[2510.14945v1](https://arxiv.org/abs/2510.14945) · [PDF](https://arxiv.org/pdf/2510.14945.pdf)  
**作者**：JoungBin Lee, Jaewoo Jung, Jisang Han, Takuya Narihira, Kazumi Fukuda, Junyoung Seo, Sunghwan Hong, Yuki Mitsufuji, Seungryong Kim  

**一句话要点**：提出3DScenePrompt框架，通过3D场景记忆实现场景一致和相机可控的视频生成。

**关键词**：视频生成, 3D场景建模, 相机控制, 场景一致性, 动态SLAM, 空间提示

## 3 点简述
- 核心问题：长视频生成中场景一致性和相机控制难以兼顾，动态元素干扰静态几何。
- 方法要点：使用动态SLAM和动态掩码分离静态几何，构建3D场景记忆作为空间提示。
- 实验或效果：在场景一致性、相机可控性和生成质量上显著优于现有方法。

## 摘要（原文）

> We present 3DScenePrompt, a framework that generates the next video chunk
> from arbitrary-length input while enabling precise camera control and
> preserving scene consistency. Unlike methods conditioned on a single image or a
> short clip, we employ dual spatio-temporal conditioning that reformulates
> context-view referencing across the input video. Our approach conditions on
> both temporally adjacent frames for motion continuity and spatially adjacent
> content for scene consistency. However, when generating beyond temporal
> boundaries, directly using spatially adjacent frames would incorrectly preserve
> dynamic elements from the past. We address this by introducing a 3D scene
> memory that represents exclusively the static geometry extracted from the
> entire input video. To construct this memory, we leverage dynamic SLAM with our
> newly introduced dynamic masking strategy that explicitly separates static
> scene geometry from moving elements. The static scene representation can then
> be projected to any target viewpoint, providing geometrically consistent warped
> views that serve as strong 3D spatial prompts while allowing dynamic regions to
> evolve naturally from temporal context. This enables our model to maintain
> long-range spatial coherence and precise camera control without sacrificing
> computational efficiency or motion realism. Extensive experiments demonstrate
> that our framework significantly outperforms existing methods in scene
> consistency, camera controllability, and generation quality. Project page :
> https://cvlab-kaist.github.io/3DScenePrompt/

