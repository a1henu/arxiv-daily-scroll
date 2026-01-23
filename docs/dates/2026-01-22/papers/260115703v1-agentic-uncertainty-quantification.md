---
layout: default
title: Agentic Uncertainty Quantification
---

# Agentic Uncertainty Quantification
**arXiv**：[2601.15703v1](https://arxiv.org/abs/2601.15703) · [PDF](https://arxiv.org/pdf/2601.15703.pdf)  
**作者**：Jiaxin Zhang, Prafulla Kumar Choubey, Kung-Hsiang Huang, Caiming Xiong, Chien-Sheng Wu  

**一句话要点**：提出双过程代理不确定性量化框架以解决AI代理在长程推理中的可靠性问题

**关键词**：不确定性量化, AI代理, 长程推理, 双过程框架, 轨迹校准

## 3 点简述
- 核心问题：AI代理在长程推理中因早期认知错误传播导致可靠性下降，现有方法存在被动诊断或无效修正的局限。
- 方法要点：设计双过程框架，将言语化不确定性转化为主动控制信号，包括隐式传播信心的系统1和触发定向推理的系统2。
- 实验或效果：在闭环基准和开放深度研究任务中，无需训练的方法实现了优越性能和轨迹级校准。

## 摘要（原文）

> Although AI agents have demonstrated impressive capabilities in long-horizon reasoning, their reliability is severely hampered by the ``Spiral of Hallucination,'' where early epistemic errors propagate irreversibly. Existing methods face a dilemma: uncertainty quantification (UQ) methods typically act as passive sensors, only diagnosing risks without addressing them, while self-reflection mechanisms suffer from continuous or aimless corrections. To bridge this gap, we propose a unified Dual-Process Agentic UQ (AUQ) framework that transforms verbalized uncertainty into active, bi-directional control signals. Our architecture comprises two complementary mechanisms: System 1 (Uncertainty-Aware Memory, UAM), which implicitly propagates verbalized confidence and semantic explanations to prevent blind decision-making; and System 2 (Uncertainty-Aware Reflection, UAR), which utilizes these explanations as rational cues to trigger targeted inference-time resolution only when necessary. This enables the agent to balance efficient execution and deep deliberation dynamically. Extensive experiments on closed-loop benchmarks and open-ended deep research tasks demonstrate that our training-free approach achieves superior performance and trajectory-level calibration. We believe this principled framework AUQ represents a significant step towards reliable agents.

