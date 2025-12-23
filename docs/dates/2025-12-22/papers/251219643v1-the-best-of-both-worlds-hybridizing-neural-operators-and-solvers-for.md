---
layout: default
title: The Best of Both Worlds: Hybridizing Neural Operators and Solvers for Stable Long-Horizon Inference
---

# The Best of Both Worlds: Hybridizing Neural Operators and Solvers for Stable Long-Horizon Inference
**arXiv**：[2512.19643v1](https://arxiv.org/abs/2512.19643) · [PDF](https://arxiv.org/pdf/2512.19643.pdf)  
**作者**：Rajyasri Roy, Dibyajyoti Nayak, Somdatta Goswami  

**一句话要点**：提出ANCHOR框架，通过混合神经算子与数值求解器实现稳定长时程PDE预测

**关键词**：神经算子, 偏微分方程求解, 长时程预测, 自适应校正, 混合模型, 误差控制

## 3 点简述
- 核心问题：神经算子在长时程预测中易受累积误差影响，缺乏在线监控与校正机制
- 方法要点：基于物理残差误差估计器，自适应触发数值求解器干预以控制误差
- 实验或效果：在多个PDE上验证，能有效限制误差增长，提升鲁棒性并保持高效

## 摘要（原文）

> Numerical simulation of time-dependent partial differential equations (PDEs) is central to scientific and engineering applications, but high-fidelity solvers are often prohibitively expensive for long-horizon or time-critical settings. Neural operator (NO) surrogates offer fast inference across parametric and functional inputs; however, most autoregressive NO frameworks remain vulnerable to compounding errors, and ensemble-averaged metrics provide limited guarantees for individual inference trajectories. In practice, error accumulation can become unacceptable beyond the training horizon, and existing methods lack mechanisms for online monitoring or correction. To address this gap, we propose ANCHOR (Adaptive Numerical Correction for High-fidelity Operator Rollouts), an online, instance-aware hybrid inference framework for stable long-horizon prediction of nonlinear, time-dependent PDEs. ANCHOR treats a pretrained NO as the primary inference engine and adaptively couples it with a classical numerical solver using a physics-informed, residual-based error estimator. Inspired by adaptive time-stepping in numerical analysis, ANCHOR monitors an exponential moving average (EMA) of the normalized PDE residual to detect accumulating error and trigger corrective solver interventions without requiring access to ground-truth solutions. We show that the EMA-based estimator correlates strongly with the true relative L2 error, enabling data-free, instance-aware error control during inference. Evaluations on four canonical PDEs: 1D and 2D Burgers', 2D Allen-Cahn, and 3D heat conduction, demonstrate that ANCHOR reliably bounds long-horizon error growth, stabilizes extrapolative rollouts, and significantly improves robustness over standalone neural operators, while remaining substantially more efficient than high-fidelity numerical solvers.

