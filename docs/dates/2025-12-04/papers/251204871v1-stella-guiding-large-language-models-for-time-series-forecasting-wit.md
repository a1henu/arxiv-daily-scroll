---
layout: default
title: STELLA: Guiding Large Language Models for Time Series Forecasting with Semantic Abstractions
---

# STELLA: Guiding Large Language Models for Time Series Forecasting with Semantic Abstractions
**arXiv**：[2512.04871v1](https://arxiv.org/abs/2512.04871) · [PDF](https://arxiv.org/pdf/2512.04871.pdf)  
**作者**：Junjie Fan, Hongye Zhao, Linduo Wei, Jiayu Rao, Guijia Li, Jiaxin Yuan, Wenqi Xu, Yong Qi  

**一句话要点**：提出STELLA框架，通过语义抽象引导大语言模型进行时间序列预测。

**关键词**：时间序列预测, 大语言模型, 语义抽象, 动态分解, 层次化提示, 零样本学习

## 3 点简述
- 问题：现有方法依赖静态相关性，缺乏动态行为生成解释和全局/实例上下文。
- 方法：动态语义抽象机制分解序列为趋势、季节性和残差，生成层次化语义锚点作为前缀提示。
- 效果：在八个基准数据集上超越先进方法，零样本和少样本泛化能力优越。

## 摘要（原文）

> Recent adaptations of Large Language Models (LLMs) for time series forecasting often fail to effectively enhance information for raw series, leaving LLM reasoning capabilities underutilized. Existing prompting strategies rely on static correlations rather than generative interpretations of dynamic behavior, lacking critical global and instance-specific context. To address this, we propose STELLA (Semantic-Temporal Alignment with Language Abstractions), a framework that systematically mines and injects structured supplementary and complementary information. STELLA employs a dynamic semantic abstraction mechanism that decouples input series into trend, seasonality, and residual components. It then translates intrinsic behavioral features of these components into Hierarchical Semantic Anchors: a Corpus-level Semantic Prior (CSP) for global context and a Fine-grained Behavioral Prompt (FBP) for instance-level patterns. Using these anchors as prefix-prompts, STELLA guides the LLM to model intrinsic dynamics. Experiments on eight benchmark datasets demonstrate that STELLA outperforms state-of-the-art methods in long- and short-term forecasting, showing superior generalization in zero-shot and few-shot settings. Ablation studies further validate the effectiveness of our dynamically generated semantic anchors.

