---
layout: default
title: Brain4FMs: A Benchmark of Foundation Models for Electrical Brain Signal
---

# Brain4FMs: A Benchmark of Foundation Models for Electrical Brain Signal
**arXiv**：[2602.11558v1](https://arxiv.org/abs/2602.11558) · [PDF](https://arxiv.org/pdf/2602.11558.pdf)  
**作者**：Fanqi Shen, Enhong Yang, Jiahe Li, Junru Hong, Xiaoran Pan, Zhizhang Yuan, Meng Li, Yang Yang  

**一句话要点**：提出Brain4FMs基准平台以解决脑基础模型缺乏统一评估框架的问题

**关键词**：脑基础模型, 自监督学习, 脑电图, 基准评估, 神经信号处理

## 3 点简述
- 核心问题：脑基础模型领域缺乏方法论统一理解和标准化评估框架
- 方法要点：基于自监督学习分类组织模型，并汇总下游任务与公共数据集
- 实验或效果：集成15个代表性模型和18个数据集，支持标准化比较与分析

## 摘要（原文）

> Brain Foundation Models (BFMs) are transforming neuroscience by enabling scalable and transferable learning from neural signals, advancing both clinical diagnostics and cutting-edge neuroscience exploration. Their emergence is powered by large-scale clinical recordings, particularly electroencephalography (EEG) and intracranial EEG, which provide rich temporal and spatial representations of brain dynamics. However, despite their rapid proliferation, the field lacks a unified understanding of existing methodologies and a standardized evaluation framework. To fill this gap, we map the benchmark design space along two axes: (i) from the model perspective, we organize BFMs under a self-supervised learning (SSL) taxonomy; and (ii) from the dataset perspective, we summarize common downstream tasks and curate representative public datasets across clinical and human-centric neurotechnology applications. Building on this consolidation, we introduce Brain4FMs, an open evaluation platform with plug-and-play interfaces that integrates 15 representative BFMs and 18 public datasets. It enables standardized comparisons and analysis of how pretraining data, SSL strategies, and architectures affect generalization and downstream performance, guiding more accurate and transferable BFMs. The code is available at https://anonymous.4open.science/r/Brain4FMs-85B8.

