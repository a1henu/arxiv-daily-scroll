---
layout: default
title: GraphPilot: Grounded Scene Graph Conditioning for Language-Based Autonomous Driving
---

# GraphPilot: Grounded Scene Graph Conditioning for Language-Based Autonomous Driving
**arXiv**：[2511.11266v1](https://arxiv.org/abs/2511.11266) · [PDF](https://arxiv.org/pdf/2511.11266.pdf)  
**作者**：Fabian Schmidt, Markus Enzweiler, Abhinav Valada  

**一句话要点**：提出GraphPilot方法，通过场景图条件化提升语言模型在自动驾驶中的规划性能

**关键词**：自动驾驶规划, 场景图条件化, 视觉语言模型, 多模态推理, 结构化提示

## 3 点简述
- 现有视觉语言模型缺乏显式关系依赖监督，限制从多模态输入推理交通实体交互的能力
- 采用模型无关方法，将不同抽象层级的场景图序列化并融入模型提示模板
- 在LangAuto基准测试中，LMDrive和BEVDriver的驾驶分数分别提升15.6%和17.5%

## 摘要（原文）

> Vision-language models have recently emerged as promising planners for autonomous driving, where success hinges on topology-aware reasoning over spatial structure and dynamic interactions from multimodal input. However, existing models are typically trained without supervision that explicitly encodes these relational dependencies, limiting their ability to infer how agents and other traffic entities influence one another from raw sensor data. In this work, we bridge this gap with a novel model-agnostic method that conditions language-based driving models on structured relational context in the form of traffic scene graphs. We serialize scene graphs at various abstraction levels and formats, and incorporate them into the models via structured prompt templates, enabling a systematic analysis of when and how relational supervision is most beneficial. Extensive evaluations on the public LangAuto benchmark show that scene graph conditioning of state-of-the-art approaches yields large and persistent improvement in driving performance. Notably, we observe up to a 15.6\% increase in driving score for LMDrive and 17.5\% for BEVDriver, indicating that models can better internalize and ground relational priors through scene graph-conditioned training, even without requiring scene graph input at test-time. Code, fine-tuned models, and our scene graph dataset are publicly available at https://github.com/iis-esslingen/GraphPilot.

