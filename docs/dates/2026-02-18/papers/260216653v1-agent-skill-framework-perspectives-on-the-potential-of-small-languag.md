---
layout: default
title: Agent Skill Framework: Perspectives on the Potential of Small Language Models in Industrial Environments
---

# Agent Skill Framework: Perspectives on the Potential of Small Language Models in Industrial Environments
**arXiv**：[2602.16653v1](https://arxiv.org/abs/2602.16653) · [PDF](https://arxiv.org/pdf/2602.16653.pdf)  
**作者**：Yangjie Xu, Lujun Li, Lama Sleem, Niccolo Gentile, Yewei Song, Yiqun Wang, Siming Ji, Wenbo Wu, Radu State  

**一句话要点**：评估Agent Skill框架在小型语言模型工业部署中的潜力，提升任务准确性与效率

**关键词**：Agent Skill框架, 小型语言模型, 工业部署, 任务准确性, GPU效率, 代码专用模型

## 3 点简述
- 核心问题：在数据安全和预算限制的工业场景中，小型语言模型泛化能力有限，依赖公共API不可行。
- 方法要点：提出Agent Skill过程的数学定义，系统评估不同规模模型在开源任务和保险数据集上的表现。
- 实验或效果：中等规模SLM（约12B-30B参数）显著受益，80B参数代码专用变体性能接近闭源基线且GPU效率提升。

## 摘要（原文）

> Agent Skill framework, now widely and officially supported by major players such as GitHub Copilot, LangChain, and OpenAI, performs especially well with proprietary models by improving context engineering, reducing hallucinations, and boosting task accuracy. Based on these observations, an investigation is conducted to determine whether the Agent Skill paradigm provides similar benefits to small language models (SLMs). This question matters in industrial scenarios where continuous reliance on public APIs is infeasible due to data-security and budget constraints requirements, and where SLMs often show limited generalization in highly customized scenarios. This work introduces a formal mathematical definition of the Agent Skill process, followed by a systematic evaluation of language models of varying sizes across multiple use cases. The evaluation encompasses two open-source tasks and a real-world insurance claims data set. The results show that tiny models struggle with reliable skill selection, while moderately sized SLMs (approximately 12B - 30B) parameters) benefit substantially from the Agent Skill approach. Moreover, code-specialized variants at around 80B parameters achieve performance comparable to closed-source baselines while improving GPU efficiency. Collectively, these findings provide a comprehensive and nuanced characterization of the capabilities and constraints of the framework, while providing actionable insights for the effective deployment of Agent Skills in SLM-centered environments.

