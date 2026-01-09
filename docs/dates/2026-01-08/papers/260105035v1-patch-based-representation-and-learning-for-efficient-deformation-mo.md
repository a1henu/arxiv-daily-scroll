---
layout: default
title: Patch-based Representation and Learning for Efficient Deformation Modeling
---

# Patch-based Representation and Learning for Efficient Deformation Modeling
**arXiv**：[2601.05035v1](https://arxiv.org/abs/2601.05035) · [PDF](https://arxiv.org/pdf/2601.05035.pdf)  
**作者**：Ruochen Chen, Thuy Tran, Shaifali Parashar  

**一句话要点**：提出基于局部面片拟合的PolyFit表示，用于高效表面变形建模

**关键词**：表面表示, 变形建模, 局部拟合, 监督学习, 计算机视觉, 图形学

## 3 点简述
- 核心问题：传统表面变形方法计算成本高，难以泛化到不同表面类型。
- 方法要点：通过局部拟合jet函数构建面片表示，支持监督学习以更新紧凑系数实现变形。
- 实验或效果：在形状模板和服装悬垂应用中，实现快速推理和竞争性精度，优于基线方法。

## 摘要（原文）

> In this paper, we present a patch-based representation of surfaces, PolyFit, which is obtained by fitting jet functions locally on surface patches. Such a representation can be learned efficiently in a supervised fashion from both analytic functions and real data. Once learned, it can be generalized to various types of surfaces. Using PolyFit, the surfaces can be efficiently deformed by updating a compact set of jet coefficients rather than optimizing per-vertex degrees of freedom for many downstream tasks in computer vision and graphics. We demonstrate the capabilities of our proposed methodologies with two applications: 1) Shape-from-template (SfT): where the goal is to deform the input 3D template of an object as seen in image/video. Using PolyFit, we adopt test-time optimization that delivers competitive accuracy while being markedly faster than offline physics-based solvers, and outperforms recent physics-guided neural simulators in accuracy at modest additional runtime. 2) Garment draping. We train a self-supervised, mesh- and garment-agnostic model that generalizes across resolutions and garment types, delivering up to an order-of-magnitude faster inference than strong baselines.

