---
layout: default
title: AMap: Distilling Future Priors for Ahead-Aware Online HD Map Construction
---

# AMap: Distilling Future Priors for Ahead-Aware Online HD Map Construction
**arXiv**：[2512.19150v1](https://arxiv.org/abs/2512.19150) · [PDF](https://arxiv.org/pdf/2512.19150.pdf)  
**作者**：Ruikai Li, Xinrun Li, Mengwei Xie, Hao Shan, Shoumeng Qiu, Xinyuan Chang, Yizhe Fan, Feng Xiong, Han Jiang, Yilong Ren, Haiyang Yu, Mu Xu, Yang Long, Varun Ojha, Zhiyong Cui  

**一句话要点**：提出AMap框架，通过蒸馏未来先验实现前瞻感知的在线高精地图构建

**关键词**：在线高精地图构建, 前瞻感知, 知识蒸馏, 时序融合, 自动驾驶感知

## 3 点简述
- 核心问题：现有在线高精地图构建方法依赖历史时序融合，导致对前方未观测道路感知不足，存在安全隐患
- 方法要点：采用“从未来蒸馏”范式，用特权访问未来上下文的教师模型指导仅使用当前帧的轻量学生模型
- 实验或效果：在nuScenes和Argoverse 2基准测试中，AMap显著提升当前帧感知，在前向关键区域优于先进时序模型

## 摘要（原文）

> Online High-Definition (HD) map construction is pivotal for autonomous driving. While recent approaches leverage historical temporal fusion to improve performance, we identify a critical safety flaw in this paradigm: it is inherently ``spatially backward-looking." These methods predominantly enhance map reconstruction in traversed areas, offering minimal improvement for the unseen road ahead. Crucially, our analysis of downstream planning tasks reveals a severe asymmetry: while rearward perception errors are often tolerable, inaccuracies in the forward region directly precipitate hazardous driving maneuvers. To bridge this safety gap, we propose AMap, a novel framework for Ahead-aware online HD Mapping. We pioneer a ``distill-from-future" paradigm, where a teacher model with privileged access to future temporal contexts guides a lightweight student model restricted to the current frame. This process implicitly compresses prospective knowledge into the student model, endowing it with ``look-ahead" capabilities at zero inference-time cost. Technically, we introduce a Multi-Level BEV Distillation strategy with spatial masking and an Asymmetric Query Adaptation module to effectively transfer future-aware representations to the student's static queries. Extensive experiments on the nuScenes and Argoverse 2 benchmark demonstrate that AMap significantly enhances current-frame perception. Most notably, it outperforms state-of-the-art temporal models in critical forward regions while maintaining the efficiency of single current frame inference.

