---
layout: default
title: Reasoning-Style Poisoning of LLM Agents via Stealthy Style Transfer: Process-Level Attacks and Runtime Monitoring in RSV Space
---

# Reasoning-Style Poisoning of LLM Agents via Stealthy Style Transfer: Process-Level Attacks and Runtime Monitoring in RSV Space
**arXiv**：[2512.14448v1](https://arxiv.org/abs/2512.14448) · [PDF](https://arxiv.org/pdf/2512.14448.pdf)  
**作者**：Xingfu Zhou, Pengfei Wang  

**一句话要点**：提出推理风格投毒攻击与监控方法，针对依赖检索的LLM代理进行过程级安全防护。

**关键词**：推理风格投毒, 过程级攻击, 风格向量监控, LLM代理安全, 检索增强生成

## 3 点简述
- 识别LLM代理推理风格为新型攻击面，通过风格注入操纵信息处理方式。
- 开发推理风格向量量化攻击效果，实验显示性能显著下降且绕过内容过滤器。
- 提出轻量级运行时监控器实时检测推理风格异常，触发安全警报。

## 摘要（原文）

> Large Language Model (LLM) agents relying on external retrieval are increasingly deployed in high-stakes environments. While existing adversarial attacks primarily focus on content falsification or instruction injection, we identify a novel, process-oriented attack surface: the agent's reasoning style. We propose Reasoning-Style Poisoning (RSP), a paradigm that manipulates how agents process information rather than what they process. We introduce Generative Style Injection (GSI), an attack method that rewrites retrieved documents into pathological tones--specifically "analysis paralysis" or "cognitive haste"--without altering underlying facts or using explicit triggers. To quantify these shifts, we develop the Reasoning Style Vector (RSV), a metric tracking Verification depth, Self-confidence, and Attention focus. Experiments on HotpotQA and FEVER using ReAct, Reflection, and Tree of Thoughts (ToT) architectures reveal that GSI significantly degrades performance. It increases reasoning steps by up to 4.4 times or induces premature errors, successfully bypassing state-of-the-art content filters. Finally, we propose RSP-M, a lightweight runtime monitor that calculates RSV metrics in real-time and triggers alerts when values exceed safety thresholds. Our work demonstrates that reasoning style is a distinct, exploitable vulnerability, necessitating process-level defenses beyond static content analysis.

