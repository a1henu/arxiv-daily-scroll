---
layout: default
title: A Unified Understanding of Offline Data Selection and Online Self-refining Generation for Post-training LLMs
---

# A Unified Understanding of Offline Data Selection and Online Self-refining Generation for Post-training LLMs
**arXiv**：[2511.21056v1](https://arxiv.org/abs/2511.21056) · [PDF](https://arxiv.org/pdf/2511.21056.pdf)  
**作者**：Quan Xiao, Tianyi Chen  

**一句话要点**：提出双层数据选择与在线自优化生成框架，以提升后训练大语言模型在下游任务中的性能。

**关键词**：大语言模型后训练, 离线数据选择, 在线自优化生成, 双层优化, 模型微调, 数据权重学习

## 3 点简述
- 核心问题：离线数据选择和在线自优化生成如何统一优化以提升大语言模型在下游任务的数据质量。
- 方法要点：采用双层数据选择优化离线数据，并将在线自优化视为模型适应步骤，学习数据权重。
- 实验或效果：在质量增强和安全感知微调实验中验证了性能提升，优于未过滤基线。

## 摘要（原文）

> Offline data selection and online self-refining generation, which enhance the data quality, are crucial steps in adapting large language models (LLMs) to specific downstream tasks. We tackle offline data selection and online self-refining generations through an optimization perspective. Specifically, bilevel data selection is used for offline data selection with respect to the validation dataset, and we treat online self-refining generation as a model adaptation step of selecting the model trained on current responses that best fits the validation data. Our framework offers a unified understanding of offline data selection and self-refining generation by assigning a learned data weight to each question and response, either explicitly or implicitly. For the first time, we theoretically demonstrate the effectiveness of the bilevel data selection framework and demonstrate its performance gains over unfiltered direct mixing baselines. By combining offline data with validation-weighted online generations, our method enhances fine-tuning performance. Experiments on quality enhancement and safety-aware LLM fine-tuning validate its effectiveness.

