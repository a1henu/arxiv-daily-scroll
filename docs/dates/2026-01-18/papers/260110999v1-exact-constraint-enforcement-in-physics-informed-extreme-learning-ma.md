---
layout: default
title: Exact Constraint Enforcement in Physics-Informed Extreme Learning Machines using Null-Space Projection Framework
---

# Exact Constraint Enforcement in Physics-Informed Extreme Learning Machines using Null-Space Projection Framework
**arXiv**：[2601.10999v1](https://arxiv.org/abs/2601.10999) · [PDF](https://arxiv.org/pdf/2601.10999.pdf)  
**作者**：Rishi Mishra, Smriti, Balaji Srinivasan, Sundararajan Natarajan, Ganapathy Krishnamurthi  

**一句话要点**：提出零空间投影框架NP-PIELM，在物理信息极限学习机中实现精确约束执行。

**关键词**：物理信息极限学习机, 精确约束执行, 零空间投影, 边界条件, 单次训练, 数值模拟

## 3 点简述
- PIELMs传统方法通过惩罚项近似满足边界条件，易受权重影响并传播误差。
- NP-PIELM利用边界算子的零空间进行代数投影，将约束问题转化为无约束最小二乘。
- 数值实验在椭圆和抛物问题中验证了框架，消除了惩罚系数并保持单次训练效率。

## 摘要（原文）

> Physics-informed extreme learning machines (PIELMs) typically impose boundary and initial conditions through penalty terms, yielding only approximate satisfaction that is sensitive to user-specified weights and can propagate errors into the interior solution. This work introduces Null-Space Projected PIELM (NP-PIELM), achieving exact constraint enforcement through algebraic projection in coefficient space. The method exploits the geometric structure of the admissible coefficient manifold, recognizing that it admits a decomposition through the null space of the boundary operator. By characterizing this manifold via a translation-invariant representation and projecting onto the kernel component, optimization is restricted to constraint-preserving directions, transforming the constrained problem into unconstrained least-squares where boundary conditions are satisfied exactly at discrete collocation points. This eliminates penalty coefficients, dual variables, and problem-specific constructions while preserving single-shot training efficiency. Numerical experiments on elliptic and parabolic problems including complex geometries and mixed boundary conditions validate the framework.

