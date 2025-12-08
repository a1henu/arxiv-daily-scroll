---
layout: default
title: FieldSeer I: Physics-Guided World Models for Long-Horizon Electromagnetic Dynamics under Partial Observability
---

# FieldSeer I: Physics-Guided World Models for Long-Horizon Electromagnetic Dynamics under Partial Observability
**arXiv**：[2512.05361v1](https://arxiv.org/abs/2512.05361) · [PDF](https://arxiv.org/pdf/2512.05361.pdf)  
**作者**：Ziheng Guo, Fang Wu, Maoxiong Zhao, Chaoqun Fang, Yang Bu  

**一句话要点**：提出FieldSeer I，一种几何感知世界模型，用于在部分可观测条件下预测二维TE波导中的电磁场长时程动力学。

**关键词**：电磁场预测, 世界模型, 部分可观测性, 几何感知, 数字孪生, 长时程动力学

## 3 点简述
- 核心问题：在部分可观测条件下，如何准确预测电磁场在二维TE波导中的长时程动力学，并支持几何编辑。
- 方法要点：模型基于短前缀观测场、标量源动作和结构/材料图，在物理域中生成闭环推演，训练时使用对称对数域确保数值稳定性。
- 实验或效果：在可复现的FDTD基准测试中，FieldSeer I在三种实际设置下均优于GRU和确定性基线，并支持无需重新同化的前缀后几何修改。

## 摘要（原文）

> We introduce FieldSeer I, a geometry-aware world model that forecasts electromagnetic field dynamics from partial observations in 2-D TE waveguides. The model assimilates a short prefix of observed fields, conditions on a scalar source action and structure/material map, and generates closed-loop rollouts in the physical domain. Training in a symmetric-log domain ensures numerical stability. Evaluated on a reproducible FDTD benchmark (200 unique simulations, structure-wise split), FieldSeer I achieves higher suffix fidelity than GRU and deterministic baselines across three practical settings: (i) software-in-the-loop filtering (64x64, P=80->Q=80), (ii) offline single-file rollouts (80x140, P=240->Q=40), and (iii) offline multi-structure rollouts (80x140, P=180->Q=100). Crucially, it enables edit-after-prefix geometry modifications without re-assimilation. Results demonstrate that geometry-conditioned world models provide a practical path toward interactive digital twins for photonic design.

