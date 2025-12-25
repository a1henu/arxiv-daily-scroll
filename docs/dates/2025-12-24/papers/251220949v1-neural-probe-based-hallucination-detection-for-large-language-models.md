---
layout: default
title: Neural Probe-Based Hallucination Detection for Large Language Models
---

# Neural Probe-Based Hallucination Detection for Large Language Models
**arXiv**：[2512.20949v1](https://arxiv.org/abs/2512.20949) · [PDF](https://arxiv.org/pdf/2512.20949.pdf)  
**作者**：Shize Liang, Hongzhi Wang  

**一句话要点**：提出基于神经探针的幻觉检测框架，以提升大语言模型在低误报下的检测性能。

**关键词**：幻觉检测, 大语言模型, 神经探针, 非线性建模, 贝叶斯优化, 轻量检测

## 3 点简述
- 大语言模型易产生幻觉内容，现有方法在置信度高时仍出错或依赖外部知识。
- 采用轻量MLP探针对隐藏状态进行非线性建模，结合多目标损失和贝叶斯优化自动搜索最优层。
- 在LongFact等数据集上，MLP探针在准确率、召回率和低误报检测能力上显著优于现有方法。

## 摘要（原文）

> Large language models(LLMs) excel at text generation and knowledge question-answering tasks, but they are prone to generating hallucinated content, severely limiting their application in high-risk domains. Current hallucination detection methods based on uncertainty estimation and external knowledge retrieval suffer from the limitation that they still produce erroneous content at high confidence levels and rely heavily on retrieval efficiency and knowledge coverage. In contrast, probe methods that leverage the model's hidden-layer states offer real-time and lightweight advantages. However, traditional linear probes struggle to capture nonlinear structures in deep semantic spaces.To overcome these limitations, we propose a neural network-based framework for token-level hallucination detection. By freezing language model parameters, we employ lightweight MLP probes to perform nonlinear modeling of high-level hidden states. A multi-objective joint loss function is designed to enhance detection stability and semantic disambiguity. Additionally, we establish a layer position-probe performance response model, using Bayesian optimization to automatically search for optimal probe insertion layers and achieve superior training results.Experimental results on LongFact, HealthBench, and TriviaQA demonstrate that MLP probes significantly outperform state-of-the-art methods in accuracy, recall, and detection capability under low false-positive conditions.

