---
layout: default
title: Learning to Generate and Extract: A Multi-Agent Collaboration Framework For Zero-shot Document-level Event Arguments Extraction
---

# Learning to Generate and Extract: A Multi-Agent Collaboration Framework For Zero-shot Document-level Event Arguments Extraction
**arXiv**：[2603.02909v1](https://arxiv.org/abs/2603.02909) · [PDF](https://arxiv.org/pdf/2603.02909.pdf)  
**作者**：Guangjun Zhang, Hu Zhang, Yazhou Han, Yue Fan, Yuhang Shao, Ru Li, Hongye Tan  

**一句话要点**：提出多智能体协作框架以解决零样本文档级事件论元提取中合成数据质量与提取性能的挑战

**关键词**：零样本学习, 文档级事件论元提取, 多智能体协作, 强化学习, 合成数据生成, 语义一致性评估

## 3 点简述
- 核心问题：零样本DEAE中，仅基于事件类型提示生成的合成数据难以准确捕捉未见事件的上下文和结构关系，且缺乏质量评估机制。
- 方法要点：设计生成与评估智能体，模拟“提出-评估-修订”协作过程，通过强化学习迭代优化，提升数据生成质量和论元提取性能。
- 实验或效果：在RAMS和WikiEvents数据集构建的三个零样本场景中，方法在数据生成质量和论元提取性能上均取得提升，并增强其他DEAE模型的零样本性能。

## 摘要（原文）

> Document-level event argument extraction (DEAE) is essential for knowledge acquisition, aiming to extract participants of events from documents.In the zero-shot setting, existing methods employ LLMs to generate synthetic data to address the challenge posed by the scarcity of annotated data. However, relying solely on Event-type-only prompts makes it difficult for the generated content to accurately capture the contextual and structural relationships of unseen events. Moreover, ensuring the reliability and usability of synthetic data remains a significant challenge due to the absence of quality evaluation mechanisms. To this end, we introduce a multi-agent collaboration framework for zero-shot document-level event argument extraction (ZS-DEAE), which simulates the human collaborative cognitive process of "Propose-Evaluate-Revise." Specifically, the framework comprises a generation agent and an evaluation agent. The generation agent synthesizes data for unseen events by leveraging knowledge from seen events, while the evaluation agent extracts arguments from the synthetic data and assesses their semantic consistency with the context. The evaluation results are subsequently converted into reward signals, with event structure constraints incorporated into the reward design to enable iterative optimization of both agents via reinforcement learning.In three zero-shot scenarios constructed from the RAMS and WikiEvents datasets, our method achieves improvements both in data generation quality and argument extraction performance, while the generated data also effectively enhances the zero-shot performance of other DEAE models.

