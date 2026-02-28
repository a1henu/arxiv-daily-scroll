---
layout: default
title: A Mathematical Theory of Agency and Intelligence
---

# A Mathematical Theory of Agency and Intelligence
**arXiv**：[2602.22519v1](https://arxiv.org/abs/2602.22519) · [PDF](https://arxiv.org/pdf/2602.22519.pdf)  
**作者**：Wael Hafez, Chenan Wei, Rodrigo Felipe, Amir Nazeri, Cameron Reid  

**一句话要点**：提出双可预测性理论以量化系统交互中的共享信息，区分代理与智能。

**关键词**：双可预测性, 代理与智能, 信息共享度量, 系统交互分析, 实时监控架构

## 3 点简述
- 核心问题：现有AI系统缺乏衡量观察、行动与结果间共享信息的原理性度量。
- 方法要点：从第一性原理推导双可预测性P，证明其在量子与经典系统中的严格界限。
- 实验或效果：在物理系统、强化学习代理和LLM对话中验证界限，并展示实时监控架构。

## 摘要（原文）

> To operate reliably under changing conditions, complex systems require feedback on how effectively they use resources, not just whether objectives are met. Current AI systems process vast information to produce sophisticated predictions, yet predictions can appear successful while the underlying interaction with the environment degrades. What is missing is a principled measure of how much of the total information a system deploys is actually shared between its observations, actions, and outcomes. We prove this shared fraction, which we term bipredictability, P, is intrinsic to any interaction, derivable from first principles, and strictly bounded: P can reach unity in quantum systems, P equal to, or smaller than 0.5 in classical systems, and lower once agency (action selection) is introduced. We confirm these bounds in a physical system (double pendulum), reinforcement learning agents, and multi turn LLM conversations. These results distinguish agency from intelligence: agency is the capacity to act on predictions, whereas intelligence additionally requires learning from interaction, self-monitoring of its learning effectiveness, and adapting the scope of observations, actions, and outcomes to restore effective learning. By this definition, current AI systems achieve agency but not intelligence. Inspired by thalamocortical regulation in biological systems, we demonstrate a feedback architecture that monitors P in real time, establishing a prerequisite for adaptive, resilient AI.

