---
layout: default
title: Safety Beyond the Training Data: Robust Out-of-Distribution MPC via Conformalized System Level Synthesis
---

# Safety Beyond the Training Data: Robust Out-of-Distribution MPC via Conformalized System Level Synthesis
**arXiv**：[2602.12047v1](https://arxiv.org/abs/2602.12047) · [PDF](https://arxiv.org/pdf/2602.12047.pdf)  
**作者**：Anutam Srinivasan, Antoine Leeman, Glen Chou  

**一句话要点**：提出基于保形预测与系统级合成的鲁棒分布外MPC框架，以解决学习动力学模型在训练数据外确保安全性的挑战。

**关键词**：保形预测, 系统级合成, 鲁棒模型预测控制, 分布外泛化, 安全规划, 非线性系统

## 3 点简述
- 核心问题：学习动力学模型在分布外场景下难以保证安全与鲁棒性。
- 方法要点：使用加权保形预测推导高置信模型误差界，并集成到基于系统级合成的鲁棒非线性MPC中。
- 实验或效果：在非线性系统（如4D汽车和12D四旋翼）上验证，相比基线提升安全性与鲁棒性。

## 摘要（原文）

> We present a novel framework for robust out-of-distribution planning and control using conformal prediction (CP) and system level synthesis (SLS), addressing the challenge of ensuring safety and robustness when using learned dynamics models beyond the training data distribution. We first derive high-confidence model error bounds using weighted CP with a learned, state-control-dependent covariance model. These bounds are integrated into an SLS-based robust nonlinear model predictive control (MPC) formulation, which performs constraint tightening over the prediction horizon via volume-optimized forward reachable sets. We provide theoretical guarantees on coverage and robustness under distributional drift, and analyze the impact of data density and trajectory tube size on prediction coverage. Empirically, we demonstrate our method on nonlinear systems of increasing complexity, including a 4D car and a {12D} quadcopter, improving safety and robustness compared to fixed-bound and non-robust baselines, especially outside of the data distribution.

