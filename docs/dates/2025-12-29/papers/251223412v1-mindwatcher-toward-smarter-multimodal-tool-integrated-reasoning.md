---
layout: default
title: MindWatcher: Toward Smarter Multimodal Tool-Integrated Reasoning
---

# MindWatcher: Toward Smarter Multimodal Tool-Integrated Reasoning
**arXiv**：[2512.23412v1](https://arxiv.org/abs/2512.23412) · [PDF](https://arxiv.org/pdf/2512.23412.pdf)  
**作者**：Jiawei Chen, Xintian Shen, Lihao Zheng, Zhenwei Shao, Hongyuan Zhang, Pengfei Yu, Xudong Rao, Ning Mao, Xiaobo Liu, Lian Wen, Chaoqun Du, Feng Gu, Wei He, Qizhen Li, Shanshan Li, Zide Liu, Jing Luo, Lifu Mu, Xuhao Pan, Chang Ren, Haoyi Sun, Qian Wang, Wei Wang, Hongfu Yang, Jiqing Zhan, Chunpeng Zhou, Zheng Zhou, Hao Ma, Tao Wei, Pan Zhou, Wei Chen  

**一句话要点**：提出MindWatcher，一种集成交错思维与多模态链式推理的工具集成推理代理，以解决复杂决策任务中工具调用的自主性问题。

**关键词**：工具集成推理, 交错思维, 多模态链式推理, 自主工具调用, 代理训练, 图像检索

## 3 点简述
- 传统基于工作流的代理在需要工具调用的现实问题中智能有限，工具集成推理代理成为处理复杂决策任务的有力方法。
- MindWatcher采用交错思维范式，可在推理中随时切换思考与工具调用，并具备多模态链式推理能力，支持图像操作以提升搜索精度。
- 实验表明，MindWatcher通过高效工具调用，性能匹配或超越更大或更新的模型，并揭示了代理训练中的遗传继承现象等关键见解。

## 摘要（原文）

> Traditional workflow-based agents exhibit limited intelligence when addressing real-world problems requiring tool invocation. Tool-integrated reasoning (TIR) agents capable of autonomous reasoning and tool invocation are rapidly emerging as a powerful approach for complex decision-making tasks involving multi-step interactions with external environments. In this work, we introduce MindWatcher, a TIR agent integrating interleaved thinking and multimodal chain-of-thought (CoT) reasoning. MindWatcher can autonomously decide whether and how to invoke diverse tools and coordinate their use, without relying on human prompts or workflows. The interleaved thinking paradigm enables the model to switch between thinking and tool calling at any intermediate stage, while its multimodal CoT capability allows manipulation of images during reasoning to yield more precise search results. We implement automated data auditing and evaluation pipelines, complemented by manually curated high-quality datasets for training, and we construct a benchmark, called MindWatcher-Evaluate Bench (MWE-Bench), to evaluate its performance. MindWatcher is equipped with a comprehensive suite of auxiliary reasoning tools, enabling it to address broad-domain multimodal problems. A large-scale, high-quality local image retrieval database, covering eight categories including cars, animals, and plants, endows model with robust object recognition despite its small size. Finally, we design a more efficient training infrastructure for MindWatcher, enhancing training speed and hardware utilization. Experiments not only demonstrate that MindWatcher matches or exceeds the performance of larger or more recent models through superior tool invocation, but also uncover critical insights for agent training, such as the genetic inheritance phenomenon in agentic RL.

