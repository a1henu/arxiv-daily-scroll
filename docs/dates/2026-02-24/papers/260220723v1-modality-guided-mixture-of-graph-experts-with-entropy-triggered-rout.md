---
layout: default
title: Modality-Guided Mixture of Graph Experts with Entropy-Triggered Routing for Multimodal Recommendation
---

# Modality-Guided Mixture of Graph Experts with Entropy-Triggered Routing for Multimodal Recommendation
**arXiv**：[2602.20723v1](https://arxiv.org/abs/2602.20723) · [PDF](https://arxiv.org/pdf/2602.20723.pdf)  
**作者**：Ji Dai, Quan Fang, Dengsheng Cai  

**一句话要点**：提出MAGNET以解决多模态推荐中信号异质与融合不平衡问题

**关键词**：多模态推荐, 图神经网络, 专家混合, 熵触发路由, 长尾分布, 可解释性

## 3 点简述
- 核心问题：多模态信号异质且可能冲突，现有方法易导致表示纠缠与模态不平衡
- 方法要点：采用模态引导的图专家混合网络，结合熵触发路由和双视图图学习，增强融合可控性与可解释性
- 实验或效果：在公开基准上实验显示优于强基线，提升推荐性能

## 摘要（原文）

> Multimodal recommendation enhances ranking by integrating user-item interactions with item content, which is particularly effective under sparse feedback and long-tail distributions. However, multimodal signals are inherently heterogeneous and can conflict in specific contexts, making effective fusion both crucial and challenging. Existing approaches often rely on shared fusion pathways, leading to entangled representations and modality imbalance. To address these issues, we propose \textbf{MAGNET}, a \textbf{M}odality-Guided Mixture of \textbf{A}daptive \textbf{G}raph Experts \textbf{N}etwork with Progressive \textbf{E}ntropy-\textbf{T}riggered Routing for Multimodal Recommendation, designed to enhance controllability, stability, and interpretability in multimodal fusion. MAGNET couples interaction-conditioned expert routing with structure-aware graph augmentation, so that both \emph{what} to fuse and \emph{how} to fuse are explicitly controlled and interpretable. At the representation level, a dual-view graph learning module augments the interaction graph with content-induced edges, improving coverage for sparse and long-tail items while preserving collaborative structure via parallel encoding and lightweight fusion. At the fusion level, MAGNET employs structured experts with explicit modality roles -- dominant, balanced, and complementary -- enabling a more interpretable and adaptive combination of behavioral, visual, and textual cues. To further stabilize sparse routing and prevent expert collapse, we introduce a two-stage entropy-weighting mechanism that monitors routing entropy. This mechanism automatically transitions training from an early coverage-oriented regime to a later specialization-oriented regime, progressively balancing expert utilization and routing confidence. Extensive experiments on public benchmarks demonstrate consistent improvements over strong baselines.

