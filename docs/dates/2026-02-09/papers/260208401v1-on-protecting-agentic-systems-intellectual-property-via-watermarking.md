---
layout: default
title: On Protecting Agentic Systems' Intellectual Property via Watermarking
---

# On Protecting Agentic Systems' Intellectual Property via Watermarking
**arXiv**：[2602.08401v1](https://arxiv.org/abs/2602.08401) · [PDF](https://arxiv.org/pdf/2602.08401.pdf)  
**作者**：Liwen Wang, Zongjie Li, Yuchong Xie, Shuai Wang, Dongdong She, Wei Wang, Juergen Rahmel  

**一句话要点**：提出AGENTWM水印框架以保护智能体系统知识产权免受模仿攻击

**关键词**：智能体系统, 知识产权保护, 水印技术, 模仿攻击, 动作序列, 统计假设检验

## 3 点简述
- 核心问题：智能体系统易受模仿攻击，现有LLM水印技术因内部推理痕迹隐藏而失效
- 方法要点：利用动作序列语义等价性，通过偏置功能相同工具执行路径分布注入水印
- 实验或效果：在三个复杂领域评估，实现高检测精度且对智能体性能影响可忽略

## 摘要（原文）

> The evolution of Large Language Models (LLMs) into agentic systems that perform autonomous reasoning and tool use has created significant intellectual property (IP) value. We demonstrate that these systems are highly vulnerable to imitation attacks, where adversaries steal proprietary capabilities by training imitation models on victim outputs. Crucially, existing LLM watermarking techniques fail in this domain because real-world agentic systems often operate as grey boxes, concealing the internal reasoning traces required for verification. This paper presents AGENTWM, the first watermarking framework designed specifically for agentic models. AGENTWM exploits the semantic equivalence of action sequences, injecting watermarks by subtly biasing the distribution of functionally identical tool execution paths. This mechanism allows AGENTWM to embed verifiable signals directly into the visible action trajectory while remaining indistinguishable to users. We develop an automated pipeline to generate robust watermark schemes and a rigorous statistical hypothesis testing procedure for verification. Extensive evaluations across three complex domains demonstrate that AGENTWM achieves high detection accuracy with negligible impact on agent performance. Our results confirm that AGENTWM effectively protects agentic IP against adaptive adversaries, who cannot remove the watermarks without severely degrading the stolen model's utility.

