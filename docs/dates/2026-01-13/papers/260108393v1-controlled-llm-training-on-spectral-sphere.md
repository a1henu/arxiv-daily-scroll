---
layout: default
title: Controlled LLM Training on Spectral Sphere
---

# Controlled LLM Training on Spectral Sphere
**arXiv**：[2601.08393v1](https://arxiv.org/abs/2601.08393) · [PDF](https://arxiv.org/pdf/2601.08393.pdf)  
**作者**：Tian Xie, Haoming Luo, Haoyu Tang, Yiwen Hu, Jason Klein Liu, Qingnan Ren, Yang Wang, Wayne Xin Zhao, Rui Yan, Bing Su, Chong Luo, Baining Guo  

**一句话要点**：提出谱球优化器以解决大模型训练中权重漂移问题，实现严格谱约束优化。

**关键词**：大模型训练, 谱约束优化, 稳定性控制, 优化算法, 并行计算, 混合专家模型

## 3 点简述
- 核心问题：现有优化器如Muon仅部分对齐μP理论，允许权重漂移，影响训练稳定性。
- 方法要点：引入谱球优化器，在谱球上推导最速下降方向，对权重和更新施加严格模块级谱约束。
- 实验或效果：在多种架构上预训练，SSO优于AdamW和Muon，提升MoE路由器负载平衡并抑制异常值。

## 摘要（原文）

> Scaling large models requires optimization strategies that ensure rapid convergence grounded in stability. Maximal Update Parametrization ($\boldsymbolμ$P) provides a theoretical safeguard for width-invariant $Θ(1)$ activation control, whereas emerging optimizers like Muon are only ``half-aligned'' with these constraints: they control updates but allow weights to drift. To address this limitation, we introduce the \textbf{Spectral Sphere Optimizer (SSO)}, which enforces strict module-wise spectral constraints on both weights and their updates. By deriving the steepest descent direction on the spectral sphere, SSO realizes a fully $\boldsymbolμ$P-aligned optimization process. To enable large-scale training, we implement SSO as an efficient parallel algorithm within Megatron. Through extensive pretraining on diverse architectures, including Dense 1.7B, MoE 8B-A1B, and 200-layer DeepNet models, SSO consistently outperforms AdamW and Muon. Furthermore, we observe significant practical stability benefits, including improved MoE router load balancing, suppressed outliers, and strictly bounded activations.

