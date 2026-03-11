---
layout: default
title: MA-EgoQA: Question Answering over Egocentric Videos from Multiple Embodied Agents
---

# MA-EgoQA: Question Answering over Egocentric Videos from Multiple Embodied Agents
**arXiv**：[2603.09827v1](https://arxiv.org/abs/2603.09827) · [PDF](https://arxiv.org/pdf/2603.09827.pdf)  
**作者**：Kangsan Kim, Yanlai Yang, Suji Kim, Woongyeong Yeo, Youngwan Lee, Mengye Ren, Sung Ju Hwang  

**一句话要点**：提出MA-EgoQA基准与EgoMAS基线模型，以解决多智能体第一人称视频问答问题。

**关键词**：多智能体系统, 第一人称视频问答, 长视频理解, 共享记忆, 动态检索, 基准评估

## 3 点简述
- 核心问题：定义多智能体长时第一人称视频理解新问题，需并行处理多视频流并聚合系统级记忆。
- 方法要点：引入MA-EgoQA基准，包含五类问题；提出EgoMAS基线，利用共享记忆和动态检索。
- 实验或效果：评估显示现有方法难以有效处理多视频流，突显未来需系统级理解进展。

## 摘要（原文）

> As embodied models become powerful, humans will collaborate with multiple embodied AI agents at their workplace or home in the future. To ensure better communication between human users and the multi-agent system, it is crucial to interpret incoming information from agents in parallel and refer to the appropriate context for each query. Existing challenges include effectively compressing and communicating high volumes of individual sensory inputs in the form of video and correctly aggregating multiple egocentric videos to construct system-level memory. In this work, we first formally define a novel problem of understanding multiple long-horizon egocentric videos simultaneously collected from embodied agents. To facilitate research in this direction, we introduce MultiAgent-EgoQA (MA-EgoQA), a benchmark designed to systemically evaluate existing models in our scenario. MA-EgoQA provides 1.7k questions unique to multiple egocentric streams, spanning five categories: social interaction, task coordination, theory-of-mind, temporal reasoning, and environmental interaction. We further propose a simple baseline model for MA-EgoQA named EgoMAS, which leverages shared memory across embodied agents and agent-wise dynamic retrieval. Through comprehensive evaluation across diverse baselines and EgoMAS on MA-EgoQA, we find that current approaches are unable to effectively handle multiple egocentric streams, highlighting the need for future advances in system-level understanding across the agents. The code and benchmark are available at https://ma-egoqa.github.io.

