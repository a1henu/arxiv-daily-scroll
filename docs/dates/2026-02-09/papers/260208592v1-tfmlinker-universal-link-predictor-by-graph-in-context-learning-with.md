---
layout: default
title: TFMLinker: Universal Link Predictor by Graph In-Context Learning with Tabular Foundation Models
---

# TFMLinker: Universal Link Predictor by Graph In-Context Learning with Tabular Foundation Models
**arXiv**：[2602.08592v1](https://arxiv.org/abs/2602.08592) · [PDF](https://arxiv.org/pdf/2602.08592.pdf)  
**作者**：Tianyin Liao, Chunyu Hu, Yicheng Sui, Xingxuan Zhang, Peng Cui, Jianxin Li, Ziwei Zhang  

**一句话要点**：提出TFMLinker，利用表格基础模型的上下文学习能力实现跨图通用链接预测

**关键词**：链接预测, 表格基础模型, 上下文学习, 图机器学习, 通用预测

## 3 点简述
- 核心问题：现有图基础模型在通用链接预测中存在预训练规模有限或过度依赖文本信息的局限
- 方法要点：设计原型增强的局部-全局上下文模块和通用拓扑感知链接编码器，以捕获图特定和跨图可转移模式
- 实验或效果：在6个跨领域图基准测试中优于最先进基线，无需数据集特定微调

## 摘要（原文）

> Link prediction is a fundamental task in graph machine learning with widespread applications such as recommendation systems, drug discovery, knowledge graphs, etc. In the foundation model era, how to develop universal link prediction methods across datasets and domains becomes a key problem, with some initial attempts adopting Graph Foundation Models utilizing Graph Neural Networks and Large Language Models. However, the existing methods face notable limitations, including limited pre-training scale or heavy reliance on textual information. Motivated by the success of tabular foundation models (TFMs) in achieving universal prediction across diverse tabular datasets, we explore an alternative approach by TFMs, which are pre-trained on diverse synthetic datasets sampled from structural causal models and support strong in-context learning independent of textual attributes. Nevertheless, adapting TFMs for link prediction faces severe technical challenges such as how to obtain the necessary context and capture link-centric topological information. To solve these challenges, we propose TFMLinker (Tabular Foundation Model for Link Predictor), aiming to leverage the in-context learning capabilities of TFMs to perform link prediction across diverse graphs without requiring dataset-specific fine-tuning. Specifically, we first develop a prototype-augmented local-global context module to construct context that captures both graph-specific and cross-graph transferable patterns. Next, we design a universal topology-aware link encoder to capture link-centric topological information and generate link representations as inputs for the TFM. Finally, we employ the TFM to predict link existence through in-context learning. Experiments on 6 graph benchmarks across diverse domains demonstrate the superiority of our method over state-of-the-art baselines without requiring dataset-specific finetuning.

