---
layout: default
title: On the use of LLMs to generate a dataset of Neural Networks
---

# On the use of LLMs to generate a dataset of Neural Networks
**arXiv**：[2602.04388v1](https://arxiv.org/abs/2602.04388) · [PDF](https://arxiv.org/pdf/2602.04388.pdf)  
**作者**：Nadia Daoudi, Jordi Cabot  

**一句话要点**：提出利用LLMs生成神经网络数据集以解决验证工具评估缺乏基准的问题

**关键词**：神经网络验证, 数据集生成, 大型语言模型, 静态分析, 符号追踪

## 3 点简述
- 核心问题：缺乏公开多样的神经网络数据集，难以系统评估验证工具的有效性。
- 方法要点：利用大型语言模型自动生成涵盖多样架构和任务的神经网络数据集。
- 实验或效果：生成608个样本，通过静态分析和符号追踪验证正确性，并公开数据集。

## 摘要（原文）

> Neural networks are increasingly used to support decision-making. To verify their reliability and adaptability, researchers and practitioners have proposed a variety of tools and methods for tasks such as NN code verification, refactoring, and migration. These tools play a crucial role in guaranteeing both the correctness and maintainability of neural network architectures, helping to prevent implementation errors, simplify model updates, and ensure that complex networks can be reliably extended and reused. Yet, assessing their effectiveness remains challenging due to the lack of publicly diverse datasets of neural networks that would allow systematic evaluation. To address this gap, we leverage large language models (LLMs) to automatically generate a dataset of neural networks that can serve as a benchmark for validation. The dataset is designed to cover diverse architectural components and to handle multiple input data types and tasks. In total, 608 samples are generated, each conforming to a set of precise design choices. To further ensure their consistency, we validate the correctness of the generated networks using static analysis and symbolic tracing. We make the dataset publicly available to support the community in advancing research on neural network reliability and adaptability.

