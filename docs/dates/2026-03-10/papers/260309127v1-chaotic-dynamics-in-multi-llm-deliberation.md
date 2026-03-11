---
layout: default
title: Chaotic Dynamics in Multi-LLM Deliberation
---

# Chaotic Dynamics in Multi-LLM Deliberation
**arXiv**：[2603.09127v1](https://arxiv.org/abs/2603.09127) · [PDF](https://arxiv.org/pdf/2603.09127.pdf)  
**作者**：Hajime Shimao, Warut Khern-am-nuai, Sung Joo Kim  

**一句话要点**：提出多LLM审议混沌动力学模型，量化稳定性并识别两种不稳定路径

**关键词**：多LLM审议, 混沌动力学, 李雅普诺夫指数, 稳定性审计, 随机动力系统, 委员会建模

## 3 点简述
- 核心问题：多LLM审议系统在重复执行中的稳定性未充分表征，实践中常误以为确定性行为
- 方法要点：将五智能体LLM委员会建模为随机动力系统，使用经验李雅普诺夫指数量化轨迹发散
- 实验或效果：在12个政策场景中，识别角色分化和模型异质性为不稳定路径，并验证协议变体可降低发散

## 摘要（原文）

> Collective AI systems increasingly rely on multi-LLM deliberation, but their stability under repeated execution remains poorly characterized. We model five-agent LLM committees as random dynamical systems and quantify inter-run sensitivity using an empirical Lyapunov exponent ($\hatλ$) derived from trajectory divergence in committee mean preferences. Across 12 policy scenarios, a factorial design at $T=0$ identifies two independent routes to instability: role differentiation in homogeneous committees and model heterogeneity in no-role committees. Critically, these effects appear even in the $T=0$ regime where practitioners often expect deterministic behavior. In the HL-01 benchmark, both routes produce elevated divergence ($\hatλ=0.0541$ and $0.0947$, respectively), while homogeneous no-role committees also remain in a positive-divergence regime ($\hatλ=0.0221$). The combined mixed+roles condition is less unstable than mixed+no-role ($\hatλ=0.0519$ vs $0.0947$), showing non-additive interaction. Mechanistically, Chair-role ablation reduces $\hatλ$ most strongly, and targeted protocol variants that shorten memory windows further attenuate divergence. These results support stability auditing as a core design requirement for multi-LLM governance systems.

