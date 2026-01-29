---
layout: default
title: LLM-AutoDP: Automatic Data Processing via LLM Agents for Model Fine-tuning
---

# LLM-AutoDP: Automatic Data Processing via LLM Agents for Model Fine-tuning
**arXiv**：[2601.20375v1](https://arxiv.org/abs/2601.20375) · [PDF](https://arxiv.org/pdf/2601.20375.pdf)  
**作者**：Wei Huang, Anda Cheng, Yinggui Wang, Lei Wang, Tao Wei  

**一句话要点**：提出LLM-AutoDP框架，利用LLM代理自动生成和优化数据处理策略，以解决领域特定数据微调中的低质量样本问题。

**关键词**：LLM代理, 自动数据处理, 模型微调, 策略优化, 隐私保护, 加速技术

## 3 点简述
- 核心问题：领域特定数据常含低质量样本，手动处理成本高且可能引发隐私风险。
- 方法要点：基于LLM代理迭代生成和优化策略，引入分布保持采样、处理目标选择和缓存重用技术加速搜索。
- 实验或效果：处理后的数据训练模型胜率超80%，相比基于LLM的AutoML基线胜率约65%，搜索时间减少达10倍。

## 摘要（原文）

> Large Language Models (LLMs) can be fine-tuned on domain-specific data to enhance their performance in specialized fields. However, such data often contains numerous low-quality samples, necessitating effective data processing (DP). In practice, DP strategies are typically developed through iterative manual analysis and trial-and-error adjustment. These processes inevitably incur high labor costs and may lead to privacy issues in high-privacy domains like healthcare due to direct human access to sensitive data. Thus, achieving automated data processing without exposing the raw data has become a critical challenge. To address this challenge, we propose LLM-AutoDP, a novel framework that leverages LLMs as agents to automatically generate and optimize data processing strategies. Our method generates multiple candidate strategies and iteratively refines them using feedback signals and comparative evaluations. This iterative in-context learning mechanism enables the agent to converge toward high-quality processing pipelines without requiring direct human intervention or access to the underlying data. To further accelerate strategy search, we introduce three key techniques: Distribution Preserving Sampling, which reduces data volume while maintaining distributional integrity; Processing Target Selection, which uses a binary classifier to identify low-quality samples for focused processing; Cache-and-Reuse Mechanism}, which minimizes redundant computations by reusing prior processing results. Results show that models trained on data processed by our framework achieve over 80% win rates against models trained on unprocessed data. Compared to AutoML baselines based on LLM agents, LLM-AutoDP achieves approximately a 65% win rate. Moreover, our acceleration techniques reduce the total searching time by up to 10 times, demonstrating both effectiveness and efficiency.

