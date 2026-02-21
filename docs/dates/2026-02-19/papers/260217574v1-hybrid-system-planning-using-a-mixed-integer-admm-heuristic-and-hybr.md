---
layout: default
title: Hybrid System Planning using a Mixed-Integer ADMM Heuristic and Hybrid Zonotopes
---

# Hybrid System Planning using a Mixed-Integer ADMM Heuristic and Hybrid Zonotopes
**arXiv**：[2602.17574v1](https://arxiv.org/abs/2602.17574) · [PDF](https://arxiv.org/pdf/2602.17574.pdf)  
**作者**：Joshua A. Robbins, Andrew F. Thompson, Jonah J. Glunt, Herschel C. Pangborn  

**一句话要点**：提出混合整数ADMM启发式与混合Zonotopes框架，用于嵌入式混合系统运动规划

**关键词**：混合系统规划, 混合整数规划, ADMM启发式, 混合Zonotopes, 嵌入式优化, 自动驾驶规划

## 3 点简述
- 核心问题：混合系统规划中混合整数规划计算密集且对数值公式敏感
- 方法要点：结合混合Zonotopes集合表示与ADMM启发式，降低内存复杂度并提升收敛率
- 实验或效果：在自动驾驶行为与运动规划场景中验证，相比现有启发式收敛更快

## 摘要（原文）

> Embedded optimization-based planning for hybrid systems is challenging due to the use of mixed-integer programming, which is computationally intensive and often sensitive to the specific numerical formulation. To address that challenge, this article proposes a framework for motion planning of hybrid systems that pairs hybrid zonotopes - an advanced set representation - with a new alternating direction method of multipliers (ADMM) mixed-integer programming heuristic. A general treatment of piecewise affine (PWA) system reachability analysis using hybrid zonotopes is presented and extended to formulate optimal planning problems. Sets produced using the proposed identities have lower memory complexity and tighter convex relaxations than equivalent sets produced from preexisting techniques. The proposed ADMM heuristic makes efficient use of the hybrid zonotope structure. For planning problems formulated as hybrid zonotopes, the proposed heuristic achieves improved convergence rates as compared to state-of-the-art mixed-integer programming heuristics. The proposed methods for hybrid system planning on embedded hardware are experimentally applied in a combined behavior and motion planning scenario for autonomous driving.

