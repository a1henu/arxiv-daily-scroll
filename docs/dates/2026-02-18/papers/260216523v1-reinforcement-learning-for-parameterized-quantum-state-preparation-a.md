---
layout: default
title: Reinforcement Learning for Parameterized Quantum State Preparation: A Comparative Study
---

# Reinforcement Learning for Parameterized Quantum State Preparation: A Comparative Study
**arXiv**：[2602.16523v1](https://arxiv.org/abs/2602.16523) · [PDF](https://arxiv.org/pdf/2602.16523.pdf)  
**作者**：Gerhard Stenzel, Isabella Debelic, Michael Kölle, Tobias Rohe, Leo Sünkel, Julian Hager, Claudia Linnhoff-Popien  

**一句话要点**：提出强化学习参数化量子态制备方法，比较单阶段与两阶段训练策略。

**关键词**：强化学习, 量子态制备, 参数化量子电路, PPO算法, 可扩展性分析

## 3 点简述
- 扩展DQCS至连续旋转参数化量子态制备，解决离散门选择局限。
- 比较单阶段联合决策与两阶段先离散后优化策略，评估PPO与A2C性能。
- 实验显示PPO在稳定超参数下成功，但可扩展性在λ约3-4时饱和。

## 摘要（原文）

> We extend directed quantum circuit synthesis (DQCS) with reinforcement learning from purely discrete gate selection to parameterized quantum state preparation with continuous single-qubit rotations \(R_x\), \(R_y\), and \(R_z\). We compare two training regimes: a one-stage agent that jointly selects the gate type, the affected qubit(s), and the rotation angle; and a two-stage variant that first proposes a discrete circuit and subsequently optimizes the rotation angles with Adam using parameter-shift gradients. Using Gymnasium and PennyLane, we evaluate Proximal Policy Optimization (PPO) and Advantage Actor--Critic (A2C) on systems comprising two to ten qubits and on targets of increasing complexity with \(λ\) ranging from one to five. Whereas A2C does not learn effective policies in this setting, PPO succeeds under stable hyperparameters (one-stage: learning rate approximately \(5\times10^{-4}\) with a self-fidelity-error threshold of 0.01; two-stage: learning rate approximately \(10^{-4}\)). Both approaches reliably reconstruct computational basis states (between 83\% and 99\% success) and Bell states (between 61\% and 77\% success). However, scalability saturates for \(λ\) of approximately three to four and does not extend to ten-qubit targets even at \(λ=2\). The two-stage method offers only marginal accuracy gains while requiring around three times the runtime. For practicality under a fixed compute budget, we therefore recommend the one-stage PPO policy, provide explicit synthesized circuits, and contrast with a classical variational baseline to outline avenues for improved scalability.

