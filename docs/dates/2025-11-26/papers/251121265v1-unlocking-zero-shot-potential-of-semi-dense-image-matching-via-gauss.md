---
layout: default
title: Unlocking Zero-shot Potential of Semi-dense Image Matching via Gaussian Splatting
---

# Unlocking Zero-shot Potential of Semi-dense Image Matching via Gaussian Splatting
**arXiv**：[2511.21265v1](https://arxiv.org/abs/2511.21265) · [PDF](https://arxiv.org/pdf/2511.21265.pdf)  
**作者**：Juncheng Chen, Chao Xu, Yanjun Cao  

**一句话要点**：提出MatchGS框架，通过几何校正与表示对齐实现零样本半稠密图像匹配

**关键词**：图像匹配, 3D高斯溅射, 零样本学习, 几何校正, 表示对齐, 半稠密匹配

## 3 点简述
- 核心问题：基于学习的图像匹配依赖高质量训练数据，但3D高斯溅射存在几何不准确问题
- 方法要点：结合几何精炼数据生成与2D-3D表示对齐，提升匹配鲁棒性
- 实验或效果：在公共基准上零样本性能提升达17.7%，极向误差降低40倍

## 摘要（原文）

> Learning-based image matching critically depends on large-scale, diverse, and geometrically accurate training data. 3D Gaussian Splatting (3DGS) enables photorealistic novel-view synthesis and thus is attractive for data generation. However, its geometric inaccuracies and biased depth rendering currently prevent robust correspondence labeling. To address this, we introduce MatchGS, the first framework designed to systematically correct and leverage 3DGS for robust, zero-shot image matching. Our approach is twofold: (1) a geometrically-faithful data generation pipeline that refines 3DGS geometry to produce highly precise correspondence labels, enabling the synthesis of a vast and diverse range of viewpoints without compromising rendering fidelity; and (2) a 2D-3D representation alignment strategy that infuses 3DGS' explicit 3D knowledge into the 2D matcher, guiding 2D semi-dense matchers to learn viewpoint-invariant 3D representations. Our generated ground-truth correspondences reduce the epipolar error by up to 40 times compared to existing datasets, enable supervision under extreme viewpoint changes, and provide self-supervisory signals through Gaussian attributes. Consequently, state-of-the-art matchers trained solely on our data achieve significant zero-shot performance gains on public benchmarks, with improvements of up to 17.7%. Our work demonstrates that with proper geometric refinement, 3DGS can serve as a scalable, high-fidelity, and structurally-rich data source, paving the way for a new generation of robust zero-shot image matchers.

