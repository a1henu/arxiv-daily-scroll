---
layout: default
title: Electrostatics-Inspired Surface Reconstruction (EISR): Recovering 3D Shapes as a Superposition of Poisson's PDE Solutions
---

# Electrostatics-Inspired Surface Reconstruction (EISR): Recovering 3D Shapes as a Superposition of Poisson's PDE Solutions
**arXiv**：[2602.11642v1](https://arxiv.org/abs/2602.11642) · [PDF](https://arxiv.org/pdf/2602.11642.pdf)  
**作者**：Diego Patiño, Knut Peterson, Kostas Daniilidis, David K. Han  

**一句话要点**：提出基于泊松方程的表面重建方法，通过叠加解恢复3D形状细节

**关键词**：表面重建, 泊松方程, 隐式形状表示, 格林函数, 高频细节恢复

## 3 点简述
- 核心问题：传统隐式形状表示依赖Eikonal方程，难以高效捕捉高频细节。
- 方法要点：将表面重建编码为泊松方程解，利用格林函数和线性叠加原理构建参数化表达。
- 实验或效果：在少量形状先验下，该方法在近似高频细节方面表现更优。

## 摘要（原文）

> Implicit shape representation, such as SDFs, is a popular approach to recover the surface of a 3D shape as the level sets of a scalar field. Several methods approximate SDFs using machine learning strategies that exploit the knowledge that SDFs are solutions of the Eikonal partial differential equation (PDEs). In this work, we present a novel approach to surface reconstruction by encoding it as a solution to a proxy PDE, namely Poisson's equation. Then, we explore the connection between Poisson's equation and physics, e.g., the electrostatic potential due to a positive charge density. We employ Green's functions to obtain a closed-form parametric expression for the PDE's solution, and leverage the linearity of our proxy PDE to find the target shape's implicit field as a superposition of solutions. Our method shows improved results in approximating high-frequency details, even with a small number of shape priors.

