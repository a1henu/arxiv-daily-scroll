---
layout: default
title: ShipTraj-R1: Reinforcing Ship Trajectory Prediction in Large Language Models via Group Relative Policy Optimization
---

# ShipTraj-R1: Reinforcing Ship Trajectory Prediction in Large Language Models via Group Relative Policy Optimization
**arXiv**：[2603.02939v1](https://arxiv.org/abs/2603.02939) · [PDF](https://arxiv.org/pdf/2603.02939.pdf)  
**作者**：Yang Zhan, Yunhao Li, Zhang Chao, Yuxu Lu, Yan Li  

**一句话要点**：提出ShipTraj-R1框架，通过GRPO强化大语言模型在船舶轨迹预测中的应用。

**关键词**：船舶轨迹预测, 大语言模型, 强化微调, GRPO, 文本生成, 海事数据分析

## 3 点简述
- 核心问题：将船舶轨迹预测作为文本生成任务，利用大语言模型解决该领域未充分探索的问题。
- 方法要点：设计动态提示和基于规则的奖励机制，结合GRPO进行强化微调，提升模型推理和预测准确性。
- 实验或效果：在真实海事数据集上验证，相比现有深度学习和LLM基线，ShipTraj-R1实现了最小误差。

## 摘要（原文）

> Recent advancements in reinforcement fine-tuning have significantly improved the reasoning ability of large language models (LLMs). In particular, methods such as group relative policy optimization (GRPO) have demonstrated strong capabilities across various fields. However, applying LLMs to ship trajectory prediction remains largely unexplored. In this paper, we propose ShipTraj-R1, a novel LLM-based framework that reformulates ship trajectory prediction as a text-to-text generation problem. (1) We design a dynamic prompt containing trajectory information about conflicting ships to guide the model to achieve adaptive chain-of-thought (CoT) reasoning. (2) We introduce a comprehensive rule-based reward mechanism to incentivize the reasoning format and prediction accuracy of the model. (3) Our ShipTraj-R1 is reinforced through the GRPO mechanism guided by domain-specific prompts and rewards, and utilizes the Qwen3 as the model backbone. Extensive experimental results on two complex and real-world maritime datasets show that the proposed ShipTraj-R1 achieves the least error compared with state-of-the-art deep learning and LLM-based baselines.

