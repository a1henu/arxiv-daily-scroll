---
layout: default
title: Yo'City: Personalized and Boundless 3D Realistic City Scene Generation via Self-Critic Expansion
---

# Yo'City: Personalized and Boundless 3D Realistic City Scene Generation via Self-Critic Expansion
**arXiv**：[2511.18734v1](https://arxiv.org/abs/2511.18734) · [PDF](https://arxiv.org/pdf/2511.18734.pdf)  
**作者**：Keyang Lu, Sifan Zhou, Hongbin Xu, Gang Xu, Zhifei Yang, Yikai Wang, Zhen Xiao, Jieyi Long, Ming Li  

**一句话要点**：提出Yo'City框架，实现个性化无限扩展的3D城市场景生成

**关键词**：3D城市生成, 个性化场景, 无限扩展, 分层规划, 图像合成, 场景图优化

## 3 点简述
- 现有方法依赖单一扩散模型，难以生成个性化无限城市场景
- 采用分层规划与图像合成循环，结合场景图优化实现城市扩展
- 构建多维度评估基准，实验显示在语义、几何等方面优于现有方法

## 摘要（原文）

> Realistic 3D city generation is fundamental to a wide range of applications, including virtual reality and digital twins. However, most existing methods rely on training a single diffusion model, which limits their ability to generate personalized and boundless city-scale scenes. In this paper, we present Yo'City, a novel agentic framework that enables user-customized and infinitely expandable 3D city generation by leveraging the reasoning and compositional capabilities of off-the-shelf large models. Specifically, Yo'City first conceptualize the city through a top-down planning strategy that defines a hierarchical "City-District-Grid" structure. The Global Planner determines the overall layout and potential functional districts, while the Local Designer further refines each district with detailed grid-level descriptions. Subsequently, the grid-level 3D generation is achieved through a "produce-refine-evaluate" isometric image synthesis loop, followed by image-to-3D generation. To simulate continuous city evolution, Yo'City further introduces a user-interactive, relationship-guided expansion mechanism, which performs scene graph-based distance- and semantics-aware layout optimization, ensuring spatially coherent city growth. To comprehensively evaluate our method, we construct a diverse benchmark dataset and design six multi-dimensional metrics that assess generation quality from the perspectives of semantics, geometry, texture, and layout. Extensive experiments demonstrate that Yo'City consistently outperforms existing state-of-the-art methods across all evaluation aspects.

