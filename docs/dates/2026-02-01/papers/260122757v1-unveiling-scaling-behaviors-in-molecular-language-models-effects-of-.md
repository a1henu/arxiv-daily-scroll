---
layout: default
title: Unveiling Scaling Behaviors in Molecular Language Models: Effects of Model Size, Data, and Representation
---

# Unveiling Scaling Behaviors in Molecular Language Models: Effects of Model Size, Data, and Representation
**arXiv**：[2601.22757v1](https://arxiv.org/abs/2601.22757) · [PDF](https://arxiv.org/pdf/2601.22757.pdf)  
**作者**：Dong Xu, Qihua Pan, Sisi Yuan, Jianqiang Li, Zexuan Zhu, Junkai Ji  

**一句话要点**：揭示分子语言模型的缩放规律，分析模型大小、数据和表示的影响

**关键词**：分子语言模型, 缩放规律, 分子表示, 预训练, 下游任务, 计算预算

## 3 点简述
- 核心问题：分子语言模型在固定计算预算下是否遵循可预测的缩放规律
- 方法要点：通过训练300个模型，独立控制模型大小、训练标记数和分子表示
- 实验或效果：发现分子表示对性能有显著影响，并公开最大模型库

## 摘要（原文）

> Molecular generative models, often employing GPT-style language modeling on molecular string representations, have shown promising capabilities when scaled to large datasets and model sizes. However, it remains unclear and subject to debate whether these models adhere to predictable scaling laws under fixed computational budgets, which is a crucial understanding for optimally allocating resources between model size, data volume, and molecular representation. In this study, we systematically investigate the scaling behavior of molecular language models across both pretraining and downstream tasks. We train 300 models and conduct over 10,000 experiments, rigorously controlling compute budgets while independently varying model size, number of training tokens, and molecular representation. Our results demonstrate clear scaling laws in molecular models for both pretraining and downstream transfer, reveal the substantial impact of molecular representation on performance, and explain previously observed inconsistencies in scaling behavior for molecular generation. Additionally, we publicly release the largest library of molecular language models to date to facilitate future research and development. Code and models are available at https://github.com/SZU-ADDG/MLM-Scaling.

