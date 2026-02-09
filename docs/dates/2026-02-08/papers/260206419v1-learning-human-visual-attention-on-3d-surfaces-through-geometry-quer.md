---
layout: default
title: Learning Human Visual Attention on 3D Surfaces through Geometry-Queried Semantic Priors
---

# Learning Human Visual Attention on 3D Surfaces through Geometry-Queried Semantic Priors
**arXiv**：[2602.06419v1](https://arxiv.org/abs/2602.06419) · [PDF](https://arxiv.org/pdf/2602.06419.pdf)  
**作者**：Soham Pahari, Sandeep C. Kumain  

**一句话要点**：提出SemGeo-AttentionNet，通过几何查询语义先验解决3D表面人类视觉注意力建模问题。

**关键词**：3D视觉注意力, 几何语义融合, 双流架构, 扩散先验, 强化学习扫描路径

## 3 点简述
- 核心问题：现有3D显著性方法缺乏语义感知，无法解释人类注视语义重要但几何不显著区域。
- 方法要点：采用双流架构，通过非对称跨模态融合结合几何处理和扩散语义先验，实现几何特征查询语义内容。
- 实验或效果：在SAL3D、NUS3D和3DVA数据集上评估，显示显著改进，验证认知动机架构有效性。

## 摘要（原文）

> Human visual attention on three-dimensional objects emerges from the interplay between bottom-up geometric processing and top-down semantic recognition. Existing 3D saliency methods rely on hand-crafted geometric features or learning-based approaches that lack semantic awareness, failing to explain why humans fixate on semantically meaningful but geometrically unremarkable regions. We introduce SemGeo-AttentionNet, a dual-stream architecture that explicitly formalizes this dichotomy through asymmetric cross-modal fusion, leveraging diffusion-based semantic priors from geometry-conditioned multi-view rendering and point cloud transformers for geometric processing. Cross-attention ensures geometric features query semantic content, enabling bottom-up distinctiveness to guide top-down retrieval. We extend our framework to temporal scanpath generation through reinforcement learning, introducing the first formulation respecting 3D mesh topology with inhibition-of-return dynamics. Evaluation on SAL3D, NUS3D and 3DVA datasets demonstrates substantial improvements, validating how cognitively motivated architectures effectively model human visual attention on three-dimensional surfaces.

