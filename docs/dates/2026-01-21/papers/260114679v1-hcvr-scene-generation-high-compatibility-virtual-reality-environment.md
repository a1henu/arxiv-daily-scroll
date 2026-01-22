---
layout: default
title: HCVR Scene Generation: High Compatibility Virtual Reality Environment Generation for Extended Redirected Walking
---

# HCVR Scene Generation: High Compatibility Virtual Reality Environment Generation for Extended Redirected Walking
**arXiv**：[2601.14679v1](https://arxiv.org/abs/2601.14679) · [PDF](https://arxiv.org/pdf/2601.14679.pdf)  
**作者**：Yiran Zhang, Xingpeng Sun, Aniket Bera  

**一句话要点**：提出HCVR框架以生成高兼容性虚拟场景，优化重定向行走效果

**关键词**：虚拟现实场景生成, 重定向行走, 兼容性度量, 布局优化, LLM资产检索

## 3 点简述
- 核心问题：物理与虚拟环境几何差异大时，重定向行走易导致碰撞，现有场景生成方法忽视兼容性。
- 方法要点：引入ENI++度量评估兼容性，结合LLM检索资产并调整布局以覆盖不兼容区域。
- 实验或效果：用户研究表明，HCVR减少22.78倍物理碰撞，ENI++得分降低35.89%，布局设计评分提高12.5%。

## 摘要（原文）

> Natural walking enhances immersion in virtual environments (VEs), but physical space limitations and obstacles hinder exploration, especially in large virtual scenes. Redirected Walking (RDW) techniques mitigate this by subtly manipulating the virtual camera to guide users away from physical collisions within pre-defined VEs. However, RDW efficacy diminishes significantly when substantial geometric divergence exists between the physical and virtual environments, leading to unavoidable collisions. Existing scene generation methods primarily focus on object relationships or layout aesthetics, often neglecting the crucial aspect of physical compatibility required for effective RDW. To address this, we introduce HCVR (High Compatibility Virtual Reality Environment Generation), a novel framework that generates virtual scenes inherently optimized for alignment-based RDW controllers. HCVR first employs ENI++, a novel, boundary-sensitive metric to evaluate the incompatibility between physical and virtual spaces by comparing rotation-sensitive visibility polygons. Guided by the ENI++ compatibility map and user prompts, HCVR utilizes a Large Language Model (LLM) for context-aware 3D asset retrieval and initial layout generation. The framework then strategically adjusts object selection, scaling, and placement to maximize coverage of virtually incompatible regions, effectively guiding users towards RDW-feasible paths. User studies evaluating physical collisions and layout quality demonstrate HCVR's effectiveness with HCVR-generated scenes, resulting in 22.78 times fewer physical collisions and received 35.89\% less on ENI++ score compared to LLM-based generation with RDW, while also receiving 12.5\% higher scores on user feedback to layout design.

