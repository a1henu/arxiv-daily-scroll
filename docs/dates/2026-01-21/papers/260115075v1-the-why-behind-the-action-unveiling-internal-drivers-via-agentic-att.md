---
layout: default
title: The Why Behind the Action: Unveiling Internal Drivers via Agentic Attribution
---

# The Why Behind the Action: Unveiling Internal Drivers via Agentic Attribution
**arXiv**：[2601.15075v1](https://arxiv.org/abs/2601.15075) · [PDF](https://arxiv.org/pdf/2601.15075.pdf)  
**作者**：Chen Qian, Peng Wang, Dongrui Liu, Junyao Yang, Dadi Guo, Ling Tang, Jilin Mei, Qihan Ren, Shuai Shao, Yong Liu, Jie Fu, Jing Shao, Xia Hu  

**一句话要点**：提出通用智能体归因框架以解释LLM智能体行为的内在驱动因素

**关键词**：智能体归因, LLM智能体, 行为解释, 时序分析, 扰动分析, 可靠性风险

## 3 点简述
- 核心问题：现有研究聚焦失败归因，不足以解释智能体行为背后的推理过程
- 方法要点：采用分层框架，结合时序似然动态和基于扰动的分析来定位关键内部因素
- 实验或效果：在多样化智能体场景中验证，能可靠识别行为背后的关键历史事件和文本证据

## 摘要（原文）

> Large Language Model (LLM)-based agents are widely used in real-world applications such as customer service, web navigation, and software engineering. As these systems become more autonomous and are deployed at scale, understanding why an agent takes a particular action becomes increasingly important for accountability and governance. However, existing research predominantly focuses on \textit{failure attribution} to localize explicit errors in unsuccessful trajectories, which is insufficient for explaining the reasoning behind agent behaviors. To bridge this gap, we propose a novel framework for \textbf{general agentic attribution}, designed to identify the internal factors driving agent actions regardless of the task outcome. Our framework operates hierarchically to manage the complexity of agent interactions. Specifically, at the \textit{component level}, we employ temporal likelihood dynamics to identify critical interaction steps; then at the \textit{sentence level}, we refine this localization using perturbation-based analysis to isolate the specific textual evidence. We validate our framework across a diverse suite of agentic scenarios, including standard tool use and subtle reliability risks like memory-induced bias. Experimental results demonstrate that the proposed framework reliably pinpoints pivotal historical events and sentences behind the agent behavior, offering a critical step toward safer and more accountable agentic systems.

