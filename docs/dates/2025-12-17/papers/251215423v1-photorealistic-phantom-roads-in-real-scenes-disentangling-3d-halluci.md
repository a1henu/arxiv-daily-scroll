---
layout: default
title: Photorealistic Phantom Roads in Real Scenes: Disentangling 3D Hallucinations from Physical Geometry
---

# Photorealistic Phantom Roads in Real Scenes: Disentangling 3D Hallucinations from Physical Geometry
**arXiv**：[2512.15423v1](https://arxiv.org/abs/2512.15423) · [PDF](https://arxiv.org/pdf/2512.15423.pdf)  
**作者**：Hoang Nguyen, Xiaohao Xu, Xiaonan Huang  

**一句话要点**：提出Grounded Self-Distillation框架，以解决单目深度估计中3D幻觉的安全风险。

**关键词**：单目深度估计, 3D幻觉, 基准评估, 蒸馏训练, 结构鲁棒性, 安全风险

## 3 点简述
- 核心问题：单目深度基础模型因语义先验而幻觉出虚假3D结构，称为3D Mirage。
- 方法要点：引入3D-Mirage基准和Laplacian评估框架，并设计Grounded Self-Distillation来强制幻觉区域平面化。
- 实验或效果：通过参数高效策略减少幻觉，避免灾难性遗忘，提升结构鲁棒性。

## 摘要（原文）

> Monocular depth foundation models achieve remarkable generalization by learning large-scale semantic priors, but this creates a critical vulnerability: they hallucinate illusory 3D structures from geometrically planar but perceptually ambiguous inputs. We term this failure the 3D Mirage. This paper introduces the first end-to-end framework to probe, quantify, and tame this unquantified safety risk. To probe, we present 3D-Mirage, the first benchmark of real-world illusions (e.g., street art) with precise planar-region annotations and context-restricted crops. To quantify, we propose a Laplacian-based evaluation framework with two metrics: the Deviation Composite Score (DCS) for spurious non-planarity and the Confusion Composite Score (CCS) for contextual instability. To tame this failure, we introduce Grounded Self-Distillation, a parameter-efficient strategy that surgically enforces planarity on illusion ROIs while using a frozen teacher to preserve background knowledge, thus avoiding catastrophic forgetting. Our work provides the essential tools to diagnose and mitigate this phenomenon, urging a necessary shift in MDE evaluation from pixel-wise accuracy to structural and contextual robustness. Our code and benchmark will be publicly available to foster this exciting research direction.

