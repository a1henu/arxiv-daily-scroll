---
layout: default
title: PHAST: Port-Hamiltonian Architecture for Structured Temporal Dynamics Forecasting
---

# PHAST: Port-Hamiltonian Architecture for Structured Temporal Dynamics Forecasting
**arXiv**：[2602.17998v1](https://arxiv.org/abs/2602.17998) · [PDF](https://arxiv.org/pdf/2602.17998.pdf)  
**作者**：Shubham Bhardwaj, Chandrajit Bajaj  

**一句话要点**：提出PHAST架构以解决仅基于位置观测的物理系统长期稳定预测与参数恢复问题

**关键词**：端口哈密顿系统, 时间序列预测, 物理信息机器学习, 参数恢复, 耗散系统, 长期稳定性

## 3 点简述
- 核心问题：从部分观测（仅位置）预测耗散物理系统的动态，需保证长期稳定性和物理参数可恢复性
- 方法要点：基于端口哈密顿框架，分解哈密顿量为势能、质量和阻尼，采用低秩参数化和Strang分裂推进动态
- 实验或效果：在13个基准测试中实现最佳长期预测，并在有足够锚点时恢复物理参数，评估分离预测稳定性和可识别性

## 摘要（原文）

> Real physical systems are dissipative -- a pendulum slows, a circuit loses charge to heat -- and forecasting their dynamics from partial observations is a central challenge in scientific machine learning. We address the \emph{position-only} (q-only) problem: given only generalized positions~$q_t$ at discrete times (momenta~$p_t$ latent), learn a structured model that (a)~produces stable long-horizon forecasts and (b)~recovers physically meaningful parameters when sufficient structure is provided. The port-Hamiltonian framework makes the conservative-dissipative split explicit via $\dot{x}=(J-R)\nabla H(x)$, guaranteeing $dH/dt\le 0$ when $R\succeq 0$. We introduce \textbf{PHAST} (Port-Hamiltonian Architecture for Structured Temporal dynamics), which decomposes the Hamiltonian into potential~$V(q)$, mass~$M(q)$, and damping~$D(q)$ across three knowledge regimes (KNOWN, PARTIAL, UNKNOWN), uses efficient low-rank PSD/SPD parameterizations, and advances dynamics with Strang splitting. Across thirteen q-only benchmarks spanning mechanical, electrical, molecular, thermal, gravitational, and ecological systems, PHAST achieves the best long-horizon forecasting among competitive baselines and enables physically meaningful parameter recovery when the regime provides sufficient anchors. We show that identification is fundamentally ill-posed without such anchors (gauge freedom), motivating a two-axis evaluation that separates forecasting stability from identifiability.

