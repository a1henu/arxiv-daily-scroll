---
layout: default
title: TorchLean: Formalizing Neural Networks in Lean
---

# TorchLean: Formalizing Neural Networks in Lean
**arXiv**：[2602.22631v1](https://arxiv.org/abs/2602.22631) · [PDF](https://arxiv.org/pdf/2602.22631.pdf)  
**作者**：Robert Joseph George, Jennifer Cruden, Xiangru Zhong, Huan Zhang, Anima Anandkumar  

**一句话要点**：提出TorchLean框架，以统一执行与验证的精确语义，解决神经网络在安全关键系统中语义鸿沟问题。

**关键词**：形式化验证, 神经网络语义, 定理证明, 安全关键系统, 浮点运算, 边界传播

## 3 点简述
- 核心问题：神经网络执行与验证分离导致语义鸿沟，影响安全关键系统可靠性。
- 方法要点：在Lean 4中构建PyTorch风格API，集成IEEE-754浮点语义和IBP/CROWN/LiRPA验证方法。
- 实验或效果：验证了认证鲁棒性、PINNs物理约束和神经控制器稳定性，并实现通用逼近定理机械化证明。

## 摘要（原文）

> Neural networks are increasingly deployed in safety- and mission-critical pipelines, yet many verification and analysis results are produced outside the programming environment that defines and runs the model. This separation creates a semantic gap between the executed network and the analyzed artifact, so guarantees can hinge on implicit conventions such as operator semantics, tensor layouts, preprocessing, and floating-point corner cases. We introduce TorchLean, a framework in the Lean 4 theorem prover that treats learned models as first-class mathematical objects with a single, precise semantics shared by execution and verification. TorchLean unifies (1) a PyTorch-style verified API with eager and compiled modes that lower to a shared op-tagged SSA/DAG computation-graph IR, (2) explicit Float32 semantics via an executable IEEE-754 binary32 kernel and proof-relevant rounding models, and (3) verification via IBP and CROWN/LiRPA-style bound propagation with certificate checking. We validate TorchLean end-to-end on certified robustness, physics-informed residual bounds for PINNs, and Lyapunov-style neural controller verification, alongside mechanized theoretical results including a universal approximation theorem. These results demonstrate a semantics-first infrastructure for fully formal, end-to-end verification of learning-enabled systems.

