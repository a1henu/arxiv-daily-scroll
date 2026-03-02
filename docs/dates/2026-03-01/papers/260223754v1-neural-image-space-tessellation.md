---
layout: default
title: Neural Image Space Tessellation
---

# Neural Image Space Tessellation
**arXiv**：[2602.23754v1](https://arxiv.org/abs/2602.23754) · [PDF](https://arxiv.org/pdf/2602.23754.pdf)  
**作者**：Youyang Du, Junqiu Zhu, Zheng Zeng, Lu Wang, Lingqi Yan  

**一句话要点**：提出神经图像空间细分（NIST），作为轻量级后处理实现细分几何视觉效果，适用于大规模实时渲染。

**关键词**：神经细分, 屏幕空间后处理, 实时渲染, 图像空间变形, 纹理一致性

## 3 点简述
- 核心问题：传统细分依赖几何预处理，增加计算开销，难以适应大规模实时渲染场景。
- 方法要点：利用几何法线与着色法线差异作为线索，通过卷积操作在图像空间多尺度变形轮廓，结合隐式扭曲保持纹理一致性。
- 实验或效果：实验显示NIST产生平滑轮廓，视觉质量可比几何细分，每帧成本恒定且与几何复杂度解耦。

## 摘要（原文）

> We present Neural Image-Space Tessellation (NIST), a lightweight screen-space post-processing approach that produces the visual effect of tessellated geometry while rendering only the original low-polygon meshes. Inspired by our observation from Phong tessellation, NIST leverages the discrepancy between geometric normals and shading normals as a minimal, view-dependent cue for silhouette refinement. At its core, NIST performs multi-scale neural tessellation by progressively deforming image-space contours with convolutional operators, while jointly reassigning appearance information through an implicit warping mechanism to preserve texture coherence and visual fidelity. Experiments demonstrate that our approach produces smooth, visually coherent silhouettes comparable to geometric tessellation, while incurring a constant per-frame cost and fully decoupled from geometric complexity, making it well-suited for large-scale real-time rendering scenarios. To the best of our knowledge, our NIST is the first work to reformulate tessellation as a post-processing operation, shifting it from a pre-rendering geometry pipeline to a screen space neural post-processing stage.

