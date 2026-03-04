---
layout: default
title: PathSpace: Rapid continuous map approximation for efficient SLAM using B-Splines in constrained environments
---

# PathSpace: Rapid continuous map approximation for efficient SLAM using B-Splines in constrained environments
**arXiv**：[2603.02538v1](https://arxiv.org/abs/2603.02538) · [PDF](https://arxiv.org/pdf/2603.02538.pdf)  
**作者**：Aduen Benjumea, Andrew Bradley, Alexander Rast, Matthias Rolf  

**一句话要点**：提出PathSpace框架，使用B样条紧凑表示环境以提升约束环境中SLAM效率

**关键词**：语义SLAM, B样条表示, 环境建模, 自主导航, 概率推理

## 3 点简述
- 当前语义SLAM依赖密集几何表示，限制基于上下文约束的应用
- PathSpace利用B样条连续表示环境，支持概率推理并减少资源使用
- 在自主赛车场景测试，实现高精度且显著降低表示复杂度

## 摘要（原文）

> Simultaneous Localization and Mapping (SLAM) plays a crucial role in enabling autonomous vehicles to navigate previously unknown environments.
>   Semantic SLAM mostly extends visual SLAM, leveraging the higher density information available to reason about the environment in a more human-like manner. This allows for better decision making by exploiting prior structural knowledge of the environment, usually in the form of labels. Current semantic SLAM techniques still mostly rely on a dense geometric representation of the environment, limiting their ability to apply constraints based on context. We propose PathSpace, a novel semantic SLAM framework that uses continuous B-splines to represent the environment in a compact manner, while also maintaining and reasoning through the continuous probability density functions required for probabilistic reasoning. This system applies the multiple strengths of B-splines in the context of SLAM to interpolate and fit otherwise discrete sparse environments. We test this framework in the context of autonomous racing, where we exploit pre-specified track characteristics to produce significantly reduced representations at comparable levels of accuracy to traditional landmark based methods and demonstrate its potential in limiting the resources used by a system with minimal accuracy loss.

