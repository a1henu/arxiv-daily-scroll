---
layout: default
title: Architectural Proprioception in State Space Models: Thermodynamic Training Induces Anticipatory Halt Detection
---

# Architectural Proprioception in State Space Models: Thermodynamic Training Induces Anticipatory Halt Detection
**arXiv**：[2603.04180v1](https://arxiv.org/abs/2603.04180) · [PDF](https://arxiv.org/pdf/2603.04180.pdf)  
**作者**：Jay Noon  

**一句话要点**：提出概率导航架构框架，通过热力学训练诱导状态空间模型产生架构本体感知，实现计算自意识。

**关键词**：状态空间模型, 热力学训练, 架构本体感知, 计算自意识, 概率导航架构, 停止检测

## 3 点简述
- 核心问题：神经计算中如何实现计算自意识和成本感知，以优化推理过程。
- 方法要点：引入热力学损失函数，结合交叉熵惩罚计算浪费，训练状态空间模型和Transformer。
- 实验或效果：热力学训练的状态空间模型展现出架构本体感知，形成通用停止签名，而Transformer无此现象。

## 摘要（原文）

> We introduce the Probability Navigation Architecture (PNA) framework, which treats neural computation as navigation through a probability manifold governed by thermodynamic principles. We train State Space Models (SSMs) and Transformers with a novel thermodynamic loss function that penalizes computational waste alongside standard cross-entropy. Across 19 experimental phases, we discover that thermodynamically-trained SSMs develop architectural proprioception: a strong anticipatory coupling between recurrent state entropy and halt confidence (r = -0.836, p < 0.001) in which the halt signal leads state entropy collapse by exactly two tokens (tau = -2.0). This Universal Stopping Signature (USS) reproduces to four decimal places across random seeds and generalizes to a structurally distinct sorting task. Critically, Transformers trained identically show no such coupling (r = -0.07), demonstrating that the phenomenon is architecture-dependent. Cross-task transfer experiments confirm that SSM halt detection reflects genuine meta-cognition (zero-shot transfer F1: SSMs 64.2% vs. Transformers 69.3%; post-adaptation: SSMs 94.5% vs. Transformers 86.4%), while Transformer halt detection relies on syntactic pattern matching. A 2D hyperparameter sweep over energy penalty (alpha) and halt supervision (beta) reveals that the anticipatory coupling is continuously controllable through training, with thermodynamic pressure serving as the primary induction mechanism and explicit halt supervision as an amplifier. Our results establish that SSMs are thermodynamically native architectures whose fixed-size recurrent states naturally support the Markovian compression that enables computational self-awareness, with implications for cost-aware inference, dynamic token budgets, and confidence-based routing in production systems.

