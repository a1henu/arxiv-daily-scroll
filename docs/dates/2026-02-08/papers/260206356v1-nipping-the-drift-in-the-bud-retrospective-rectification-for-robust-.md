---
layout: default
title: Nipping the Drift in the Bud: Retrospective Rectification for Robust Vision-Language Navigation
---

# Nipping the Drift in the Bud: Retrospective Rectification for Robust Vision-Language Navigation
**arXiv**：[2602.06356v1](https://arxiv.org/abs/2602.06356) · [PDF](https://arxiv.org/pdf/2602.06356.pdf)  
**作者**：Gang He, Zhenyang Liu, Kepeng Xu, Li Xu, Tong Qiao, Wenxin Yu, Chang Wu, Weiying Xie  

**一句话要点**：提出BudVLN框架，通过回顾性矫正解决视觉语言导航中的指令-状态错位问题。

**关键词**：视觉语言导航, 模仿学习, 暴露偏差, 在线学习, 反事实推理, 轨迹合成

## 3 点简述
- 核心问题：模仿学习存在暴露偏差，导致推理时微小偏差累积为错误，且传统纠错方法可能引发指令-状态语义冲突。
- 方法要点：采用在线框架，通过反事实重锚和决策条件监督合成，利用测地线预言机生成语义一致的矫正轨迹。
- 实验或效果：在R2R-CE和RxR-CE基准测试中，有效缓解分布偏移，在成功率和SPL指标上达到最优性能。

## 摘要（原文）

> Vision-Language Navigation (VLN) requires embodied agents to interpret natural language instructions and navigate through complex continuous 3D environments. However, the dominant imitation learning paradigm suffers from exposure bias, where minor deviations during inference lead to compounding errors. While DAgger-style approaches attempt to mitigate this by correcting error states, we identify a critical limitation: Instruction-State Misalignment. Forcing an agent to learn recovery actions from off-track states often creates supervision signals that semantically conflict with the original instruction. In response to these challenges, we introduce BudVLN, an online framework that learns from on-policy rollouts by constructing supervision to match the current state distribution. BudVLN performs retrospective rectification via counterfactual re-anchoring and decision-conditioned supervision synthesis, using a geodesic oracle to synthesize corrective trajectories that originate from valid historical states, ensuring semantic consistency. Experiments on the standard R2R-CE and RxR-CE benchmarks demonstrate that BudVLN consistently mitigates distribution shift and achieves state-of-the-art performance in both Success Rate and SPL.

