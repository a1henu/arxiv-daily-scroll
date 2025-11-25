---
layout: default
title: GContextFormer: A global context-aware hybrid multi-head attention approach with scaled additive aggregation for multimodal trajectory prediction
---

# GContextFormer: A global context-aware hybrid multi-head attention approach with scaled additive aggregation for multimodal trajectory prediction
**arXiv**：[2511.18874v1](https://arxiv.org/abs/2511.18874) · [PDF](https://arxiv.org/pdf/2511.18874.pdf)  
**作者**：Yuzhi Chen, Yuanchang Xie, Lei Zhao, Pan Liu, Yajie Zou, Chen Wang  

**一句话要点**：提出GContextFormer以解决无地图多模态轨迹预测中的全局上下文缺失问题

**关键词**：轨迹预测, 多模态学习, 注意力机制, 全局上下文, 意图对齐, 无地图预测

## 3 点简述
- 核心问题：无地图方法缺乏全局上下文，注意力机制放大直线模式抑制过渡模式，导致运动意图错位
- 方法要点：采用全局上下文感知混合注意力和缩放加法聚合，实现意图对齐的多模态预测
- 实验或效果：在TOD-VT数据集上超越现有方法，在高曲率和过渡区表现更稳健

## 摘要（原文）

> Multimodal trajectory prediction generates multiple plausible future trajectories to address vehicle motion uncertainty from intention ambiguity and execution variability. However, HD map-dependent models suffer from costly data acquisition, delayed updates, and vulnerability to corrupted inputs, causing prediction failures. Map-free approaches lack global context, with pairwise attention over-amplifying straight patterns while suppressing transitional patterns, resulting in motion-intention misalignment. This paper proposes GContextFormer, a plug-and-play encoder-decoder architecture with global context-aware hybrid attention and scaled additive aggregation achieving intention-aligned multimodal prediction without map reliance. The Motion-Aware Encoder builds scene-level intention prior via bounded scaled additive aggregation over mode-embedded trajectory tokens and refines per-mode representations under shared global context, mitigating inter-mode suppression and promoting intention alignment. The Hierarchical Interaction Decoder decomposes social reasoning into dual-pathway cross-attention: a standard pathway ensures uniform geometric coverage over agent-mode pairs while a neighbor-context-enhanced pathway emphasizes salient interactions, with gating module mediating their contributions to maintain coverage-focus balance. Experiments on eight highway-ramp scenarios from TOD-VT dataset show GContextFormer outperforms state-of-the-art baselines. Compared to existing transformer models, GContextFormer achieves greater robustness and concentrated improvements in high-curvature and transition zones via spatial distributions. Interpretability is achieved through motion mode distinctions and neighbor context modulation exposing reasoning attribution. The modular architecture supports extensibility toward cross-domain multimodal reasoning tasks. Source: https://fenghy-chen.github.io/sources/.

