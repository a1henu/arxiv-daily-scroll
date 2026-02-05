---
layout: default
title: Steering LLMs via Scalable Interactive Oversight
---

# Steering LLMs via Scalable Interactive Oversight
**arXiv**：[2602.04210v1](https://arxiv.org/abs/2602.04210) · [PDF](https://arxiv.org/pdf/2602.04210.pdf)  
**作者**：Enyu Zhou, Zhiheng Xi, Long Ma, Zhihao Zhang, Shihan Dou, Zhikai Lei, Guoteng Wang, Rui Zheng, Hang Yan, Tao Gui, Qi Zhang, Xuanjing Huang  

**一句话要点**：提出可扩展交互式监督框架，通过递归分解意图以解决复杂任务中人类监督不足的问题。

**关键词**：可扩展监督, 交互式反馈, 意图分解, 强化学习, 复杂任务指导, 人类控制

## 3 点简述
- 核心问题：大型语言模型在复杂长程任务中，人类因专业知识不足、意图表达困难和输出验证不可靠而难以有效指导。
- 方法要点：将复杂意图递归分解为可管理决策树，在节点收集低负担反馈并聚合为全局指导，避免开放式提示。
- 实验或效果：在网页开发任务中验证，非专家可生成专家级产品需求文档，对齐度提升54%，且框架可通过在线用户反馈强化学习优化。

## 摘要（原文）

> As Large Language Models increasingly automate complex, long-horizon tasks such as \emph{vibe coding}, a supervision gap has emerged. While models excel at execution, users often struggle to guide them effectively due to insufficient domain expertise, the difficulty of articulating precise intent, and the inability to reliably validate complex outputs. It presents a critical challenge in scalable oversight: enabling humans to responsibly steer AI systems on tasks that surpass their own ability to specify or verify. To tackle this, we propose Scalable Interactive Oversight, a framework that decomposes complex intent into a recursive tree of manageable decisions to amplify human supervision. Rather than relying on open-ended prompting, our system elicits low-burden feedback at each node and recursively aggregates these signals into precise global guidance. Validated in web development task, our framework enables non-experts to produce expert-level Product Requirement Documents, achieving a 54\% improvement in alignment. Crucially, we demonstrate that this framework can be optimized via Reinforcement Learning using only online user feedback, offering a practical pathway for maintaining human control as AI scales.

