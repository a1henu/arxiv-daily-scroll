---
layout: default
title: Neural Policy Composition from Free Energy Minimization
---

# Neural Policy Composition from Free Energy Minimization
**arXiv**：[2512.04745v1](https://arxiv.org/abs/2512.04745) · [PDF](https://arxiv.org/pdf/2512.04745.pdf)  
**作者**：Francesca Rossi, Veronica Centorrino, Francesco Bullo, Giovanni Russo  

**一句话要点**：提出GateMod模型，基于自由能最小化统一神经策略门控，应用于多智能体系统和人类决策。

**关键词**：自由能最小化, 神经策略门控, 多智能体系统, 多臂赌博机, 可解释模型, 神经电路建模

## 3 点简述
- 核心问题：任务结构如何塑造神经策略门控，缺乏统一的理论和神经电路解释。
- 方法要点：通过GateFrame框架将门控建模为自由能最小化，并推导GateFlow动力学和GateNet神经电路。
- 实验或效果：在多智能体系统和多臂赌博机任务中，GateMod提供可解释机制，性能匹配或优于现有模型。

## 摘要（原文）

> The ability to compose acquired skills to plan and execute behaviors is a hallmark of natural intelligence. Yet, despite remarkable cross-disciplinary efforts, a principled account of how task structure shapes gating and how such computations could be delivered in neural circuits, remains elusive. Here we introduce GateMod, an interpretable theoretically grounded computational model linking the emergence of gating to the underlying decision-making task, and to a neural circuit architecture. We first develop GateFrame, a normative framework casting policy gating into the minimization of the free energy. This framework, relating gating rules to task, applies broadly across neuroscience, cognitive and computational sciences. We then derive GateFlow, a continuous-time energy based dynamics that provably converges to GateFrame optimal solution. Convergence, exponential and global, follows from a contractivity property that also yields robustness and other desirable properties. Finally, we derive a neural circuit from GateFlow, GateNet. This is a soft-competitive recurrent circuit whose components perform local and contextual computations consistent with known dendritic and neural processing motifs. We evaluate GateMod across two different settings: collective behaviors in multi-agent systems and human decision-making in multi-armed bandits. In all settings, GateMod provides interpretable mechanistic explanations of gating and quantitatively matches or outperforms established models. GateMod offers a unifying framework for neural policy gating, linking task objectives, dynamical computation, and circuit-level mechanisms. It provides a framework to understand gating in natural agents beyond current explanations and to equip machines with this ability.

