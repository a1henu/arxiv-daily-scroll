---
layout: default
title: RENEW: Risk- and Energy-Aware Navigation in Dynamic Waterways
---

# RENEW: Risk- and Energy-Aware Navigation in Dynamic Waterways
**arXiv**：[2601.16424v1](https://arxiv.org/abs/2601.16424) · [PDF](https://arxiv.org/pdf/2601.16424.pdf)  
**作者**：Mingi Jeong, Alberto Quattrini Li  

**一句话要点**：提出RENEW框架，为动态水域中的自主水面艇提供风险与能量感知的全局路径规划。

**关键词**：自主水面艇, 路径规划, 动态环境, 风险感知, 能量优化, 海事导航

## 3 点简述
- 核心问题：在动态水域中，自主水面艇需应对水流等外部扰动，确保安全导航。
- 方法要点：采用分层架构，结合高层约束三角剖分以增加路径拓扑多样性，并在安全走廊内进行低层轨迹优化。
- 实验或效果：使用真实海洋数据验证，首次联合处理自适应不可导航区域和拓扑路径多样性，提升鲁棒性。

## 摘要（原文）

> We present RENEW, a global path planner for Autonomous Surface Vehicle (ASV) in dynamic environments with external disturbances (e.g., water currents). RENEW introduces a unified risk- and energy-aware strategy that ensures safety by dynamically identifying non-navigable regions and enforcing adaptive safety constraints. Inspired by maritime contingency planning, it employs a best-effort strategy to maintain control under adverse conditions. The hierarchical architecture combines high-level constrained triangulation for topological diversity with low-level trajectory optimization within safe corridors. Validated with real-world ocean data, RENEW is the first framework to jointly address adaptive non-navigability and topological path diversity for robust maritime navigation.

