---
layout: default
title: FocalOrder: Focal Preference Optimization for Reading Order Detection
---

# FocalOrder: Focal Preference Optimization for Reading Order Detection
**arXiv**：[2601.07483v1](https://arxiv.org/abs/2601.07483) · [PDF](https://arxiv.org/pdf/2601.07483.pdf)  
**作者**：Fuyuan Liu, Dianyu Yu, He Ren, Nayu Liu, Xiaomian Kang, Delai Qiu, Fa Zhang, Genpeng Zhen, Shengping Liu, Jiaen Liang, Wei Huang, Yining Wang, Junnan Zhu  

**一句话要点**：提出FocalOrder框架，通过焦点偏好优化解决文档阅读顺序检测中的位置差异问题。

**关键词**：文档理解, 阅读顺序检测, 焦点偏好优化, 位置差异, 自适应难度发现, 成对排序目标

## 3 点简述
- 核心问题：现有方法假设布局区域难度均匀，但存在位置差异，模型在复杂中间区域性能崩溃。
- 方法要点：采用自适应难度发现和指数移动平均机制动态识别难学过渡，引入难度校准的成对排序目标确保全局逻辑一致性。
- 实验或效果：在OmniDocBench v1.0和Comp-HRDoc上取得新SOTA，紧凑模型超越专业基线和大型通用视觉语言模型。

## 摘要（原文）

> Reading order detection is the foundation of document understanding. Most existing methods rely on uniform supervision, implicitly assuming a constant difficulty distribution across layout regions. In this work, we challenge this assumption by revealing a critical flaw: \textbf{Positional Disparity}, a phenomenon where models demonstrate mastery over the deterministic start and end regions but suffer a performance collapse in the complex intermediate sections. This degradation arises because standard training allows the massive volume of easy patterns to drown out the learning signals from difficult layouts. To address this, we propose \textbf{FocalOrder}, a framework driven by \textbf{Focal Preference Optimization (FPO)}. Specifically, FocalOrder employs adaptive difficulty discovery with exponential moving average mechanism to dynamically pinpoint hard-to-learn transitions, while introducing a difficulty-calibrated pairwise ranking objective to enforce global logical consistency. Extensive experiments demonstrate that FocalOrder establishes new state-of-the-art results on OmniDocBench v1.0 and Comp-HRDoc. Our compact model not only outperforms competitive specialized baselines but also significantly surpasses large-scale general VLMs. These results demonstrate that aligning the optimization with intrinsic structural ambiguity of documents is critical for mastering complex document structures.

