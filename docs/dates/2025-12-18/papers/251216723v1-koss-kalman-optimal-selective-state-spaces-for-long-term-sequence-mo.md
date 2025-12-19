---
layout: default
title: KOSS: Kalman-Optimal Selective State Spaces for Long-Term Sequence Modeling
---

# KOSS: Kalman-Optimal Selective State Spaces for Long-Term Sequence Modeling
**arXiv**：[2512.16723v1](https://arxiv.org/abs/2512.16723) · [PDF](https://arxiv.org/pdf/2512.16723.pdf)  
**作者**：Lei Wang, Xin Tan, Mingwei Wang, Ying Zhang  

**一句话要点**：提出KOSS模型以解决选择性状态空间模型缺乏理论依据和上下文感知选择的问题

**关键词**：选择性状态空间模型, 卡尔曼滤波, 长序列建模, 上下文感知选择, 理论推导, 实时应用

## 3 点简述
- 现有选择性状态空间模型如Mamba缺乏理论支持，无法实现基于上下文的选择
- KOSS基于估计理论，通过卡尔曼增益实现闭环、上下文感知的选择机制
- 在选择性复制任务和长期预测基准测试中，KOSS显著优于现有模型

## 摘要（原文）

> Recent selective state space models (SSMs), such as Mamba and Mamba-2, have demonstrated strong performance in sequence modeling owing to input-dependent selection mechanisms. However, these mechanisms lack theoretical grounding and cannot support context-aware selection from latent state dynamics. To address these limitations, we propose KOSS, a Kalman-optimal Selective State Space model that formulates selection as latent state uncertainty minimization. Derived from estimation theory, KOSS adopts a continuous-time latent update driven by a Kalman gain that dynamically modulates information propagation based on content and context, enabling a closed-loop, context-aware selectivity mechanism. To ensure stable computation and near-linear scalability, KOSS employs global spectral differentiation for frequency-domain derivative estimation, along with a segment-wise scan for hardware-efficient processing. On a selective copying task with distractors, KOSS achieves over 79\% accuracy while baselines drop below 20\%, demonstrating robust context-aware selection. Furthermore, across nine long-term forecasting benchmarks, KOSS reduces MSE by 2.92--36.23\% and consistently outperforms state-of-the-art models in both accuracy and stability. To assess real-world applicability, a case study on secondary surveillance radar (SSR) tracking confirms KOSS's robustness under irregular intervals and noisy conditions and demonstrates its effectiveness in real-world applications. Finally, supplementary experiments verify Kalman gain convergence and the frequency response of spectral differentiation, providing theoretical support for the proposed closed-loop design.

