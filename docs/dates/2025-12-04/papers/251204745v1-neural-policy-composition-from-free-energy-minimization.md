---
layout: default
title: Neural Policy Composition from Free Energy Minimization
---

# Neural Policy Composition from Free Energy Minimization
**arXiv**：[2512.04745v1](https://arxiv.org/abs/2512.04745) · [PDF](https://arxiv.org/pdf/2512.04745.pdf)  
**作者**：Francesca Rossi, Veronica Centorrino, Francesco Bullo, Giovanni Russo  

**一句话要点**：提出GateMod模型，基于自由能最小化解释神经策略门控机制

**关键词**：神经策略门控, 自由能最小化, 计算模型, 神经环路, 多智能体系统, 决策任务

## 3 点简述
- 核心问题：任务结构如何影响神经策略门控及其神经环路实现机制未知
- 方法要点：建立GateFrame规范框架，将策略门控建模为自由能最小化问题
- 实验或效果：在集体行为和人类决策任务中，GateMod提供可解释机制并匹配或超越现有模型

## 摘要（原文）

> The ability to compose acquired skills to plan and execute behaviors is a hallmark of natural intelligence. Yet, despite remarkable cross-disciplinary efforts, a principled account of how task structure shapes gating and how such computations could be delivered in neural circuits, remains elusive. Here we introduce GateMod, an interpretable theoretically grounded computational model linking the emergence of gating to the underlying decision-making task, and to a neural circuit architecture. We first develop GateFrame, a normative framework casting policy gating into the minimization of the free energy. This framework, relating gating rules to task, applies broadly across neuroscience, cognitive and computational sciences. We then derive GateFlow, a continuous-time energy based dynamics that provably converges to GateFrame optimal solution. Convergence, exponential and global, follows from a contractivity property that also yields robustness and other desirable properties. Finally, we derive a neural circuit from GateFlow, GateNet. This is a soft-competitive recurrent circuit whose components perform local and contextual computations consistent with known dendritic and neural processing motifs. We evaluate GateMod across two different settings: collective behaviors in multi-agent systems and human decision-making in multi-armed bandits. In all settings, GateMod provides interpretable mechanistic explanations of gating and quantitatively matches or outperforms established models. GateMod offers a unifying framework for neural policy gating, linking task objectives, dynamical computation, and circuit-level mechanisms. It provides a framework to understand gating in natural agents beyond current explanations and to equip machines with this ability.

