---
layout: default
title: Modality-Balanced Collaborative Distillation for Multi-Modal Domain Generalization
---

# Modality-Balanced Collaborative Distillation for Multi-Modal Domain Generalization
**arXiv**：[2511.20258v1](https://arxiv.org/abs/2511.20258) · [PDF](https://arxiv.org/pdf/2511.20258.pdf)  
**作者**：Xiaohan Wang, Zhangtao Cheng, Ting Zhong, Leiting Chen, Fan Zhou  

**一句话要点**：提出MBCD以解决多模态域泛化中权重平均导致的模态不平衡问题

**关键词**：多模态域泛化, 权重平均, 模态不平衡, 协作蒸馏, 梯度一致性, 跨模态交互

## 3 点简述
- 核心问题：权重平均在多模态域泛化中因模态优化速度差异导致偏向快速模态，抑制互补模态融合
- 方法要点：采用自适应模态丢弃、梯度一致性约束和基于权重平均的跨模态蒸馏来平衡模态学习
- 实验或效果：在MMDG基准测试中，MBCD优于现有方法，提升未见域的准确性和鲁棒性

## 摘要（原文）

> Weight Averaging (WA) has emerged as a powerful technique for enhancing generalization by promoting convergence to a flat loss landscape, which correlates with stronger out-of-distribution performance. However, applying WA directly to multi-modal domain generalization (MMDG) is challenging: differences in optimization speed across modalities lead WA to overfit to faster-converging ones in early stages, suppressing the contribution of slower yet complementary modalities, thereby hindering effective modality fusion and skewing the loss surface toward sharper, less generalizable minima. To address this issue, we propose MBCD, a unified collaborative distillation framework that retains WA's flatness-inducing advantages while overcoming its shortcomings in multi-modal contexts. MBCD begins with adaptive modality dropout in the student model to curb early-stage bias toward dominant modalities. A gradient consistency constraint then aligns learning signals between uni-modal branches and the fused representation, encouraging coordinated and smoother optimization. Finally, a WA-based teacher conducts cross-modal distillation by transferring fused knowledge to each uni-modal branch, which strengthens cross-modal interactions and steer convergence toward flatter solutions. Extensive experiments on MMDG benchmarks show that MBCD consistently outperforms existing methods, achieving superior accuracy and robustness across diverse unseen domains.

