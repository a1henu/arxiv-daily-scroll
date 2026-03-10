---
layout: default
title: In-Context Reinforcement Learning for Tool Use in Large Language Models
---

# In-Context Reinforcement Learning for Tool Use in Large Language Models
**arXiv**：[2603.08068v1](https://arxiv.org/abs/2603.08068) · [PDF](https://arxiv.org/pdf/2603.08068.pdf)  
**作者**：Yaoqi Ye, Yiran Zhao, Keyu Duan, Zeyu Zheng, Kenji Kawaguchi, Cihang Xie, Michael Qizhe Shieh  

**一句话要点**：提出上下文强化学习框架以解决大语言模型工具使用中的数据效率问题

**关键词**：大语言模型, 工具使用, 强化学习, 上下文学习, 数据效率, 零样本学习

## 3 点简述
- 核心问题：大语言模型使用外部工具时依赖监督微调，数据标注成本高。
- 方法要点：通过上下文示例在强化学习阶段引导模型调用工具，逐步减少示例至零样本。
- 实验或效果：在推理和工具使用基准测试中达到先进性能，证明其可扩展性和数据效率。

## 摘要（原文）

> While large language models (LLMs) exhibit strong reasoning abilities, their performance on complex tasks is often constrained by the limitations of their internal knowledge. A compelling approach to overcome this challenge is to augment these models with external tools -- such as Python interpreters for mathematical computations or search engines for retrieving factual information. However, enabling models to use these tools effectively remains a significant challenge. Existing methods typically rely on cold-start pipelines that begin with supervised fine-tuning (SFT), followed by reinforcement learning (RL). These approaches often require substantial amounts of labeled data for SFT, which is expensive to annotate or synthesize. In this work, we propose In-Context Reinforcement Learning (ICRL), an RL-only framework that eliminates the need for SFT by leveraging few-shot prompting during the rollout stage of RL. Specifically, ICRL introduces in-context examples within the rollout prompts to teach the model how to invoke external tools. Furthermore, as training progresses, the number of in-context examples is gradually reduced, eventually reaching a zero-shot setting where the model learns to call tools independently. We conduct extensive experiments across a range of reasoning and tool-use benchmarks. Results show that ICRL achieves state-of-the-art performance, demonstrating its effectiveness as a scalable, data-efficient alternative to traditional SFT-based pipelines.

