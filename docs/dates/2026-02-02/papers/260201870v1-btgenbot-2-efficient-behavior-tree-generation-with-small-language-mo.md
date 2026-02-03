---
layout: default
title: BTGenBot-2: Efficient Behavior Tree Generation with Small Language Models
---

# BTGenBot-2: Efficient Behavior Tree Generation with Small Language Models
**arXiv**：[2602.01870v1](https://arxiv.org/abs/2602.01870) · [PDF](https://arxiv.org/pdf/2602.01870.pdf)  
**作者**：Riccardo Andrea Izzo, Gianluca Bardaro, Matteo Matteucci  

**一句话要点**：提出BTGenBot-2，一种轻量级开源小语言模型，用于从自然语言生成可执行行为树，以解决机器人任务规划中的部署和标准化挑战。

**关键词**：行为树生成, 小语言模型, 机器人任务规划, 零样本学习, 开源模型, 轻量级部署

## 3 点简述
- 核心问题：现有LLM任务规划方法常闭源或计算密集，缺乏适用于真实机器人的即插即用表示。
- 方法要点：开发1B参数模型，支持零样本生成XML行为树，具备推理和运行时错误恢复能力。
- 实验或效果：在标准化基准测试中，零样本成功率90.38%，推理速度比前代快16倍，优于GPT-5等模型。

## 摘要（原文）

> Recent advances in robot learning increasingly rely on LLM-based task planning, leveraging their ability to bridge natural language with executable actions. While prior works showcased great performances, the widespread adoption of these models in robotics has been challenging as 1) existing methods are often closed-source or computationally intensive, neglecting the actual deployment on real-world physical systems, and 2) there is no universally accepted, plug-and-play representation for robotic task generation. Addressing these challenges, we propose BTGenBot-2, a 1B-parameter open-source small language model that directly converts natural language task descriptions and a list of robot action primitives into executable behavior trees in XML. Unlike prior approaches, BTGenBot-2 enables zero-shot BT generation, error recovery at inference and runtime, while remaining lightweight enough for resource-constrained robots. We further introduce the first standardized benchmark for LLM-based BT generation, covering 52 navigation and manipulation tasks in NVIDIA Isaac Sim. Extensive evaluations demonstrate that BTGenBot-2 consistently outperforms GPT-5, Claude Opus 4.1, and larger open-source models across both functional and non-functional metrics, achieving average success rates of 90.38% in zero-shot and 98.07% in one-shot, while delivering up to 16x faster inference compared to the previous BTGenBot.

