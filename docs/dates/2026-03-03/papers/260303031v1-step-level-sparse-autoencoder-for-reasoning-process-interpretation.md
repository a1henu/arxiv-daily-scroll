---
layout: default
title: Step-Level Sparse Autoencoder for Reasoning Process Interpretation
---

# Step-Level Sparse Autoencoder for Reasoning Process Interpretation
**arXiv**：[2603.03031v1](https://arxiv.org/abs/2603.03031) · [PDF](https://arxiv.org/pdf/2603.03031.pdf)  
**作者**：Xuan Yang, Jiayu Liu, Yuhang Lai, Hao Xu, Zhenya Huang, Ning Miao  

**一句话要点**：提出步级稀疏自编码器以解析大语言模型的推理过程

**关键词**：稀疏自编码器, 推理过程解析, 大语言模型, 步级特征, 信息瓶颈, 线性探测

## 3 点简述
- 问题：现有稀疏自编码器在词元级别操作，难以捕捉推理步骤的关键信息如方向和语义转换。
- 方法：通过控制步级特征的稀疏性，形成信息瓶颈，分离增量与背景信息为稀疏激活维度。
- 实验：在多个模型和任务中验证特征有效性，线性探测可预测生成长度、正确性等属性。

## 摘要（原文）

> Large Language Models (LLMs) have achieved strong complex reasoning capabilities through Chain-of-Thought (CoT) reasoning. However, their reasoning patterns remain too complicated to analyze. While Sparse Autoencoders (SAEs) have emerged as a powerful tool for interpretability, existing approaches predominantly operate at the token level, creating a granularity mismatch when capturing more critical step-level information, such as reasoning direction and semantic transitions. In this work, we propose step-level sparse autoencoder (SSAE), which serves as an analytical tool to disentangle different aspects of LLMs' reasoning steps into sparse features. Specifically, by precisely controlling the sparsity of a step feature conditioned on its context, we form an information bottleneck in step reconstruction, which splits incremental information from background information and disentangles it into several sparsely activated dimensions. Experiments on multiple base models and reasoning tasks show the effectiveness of the extracted features. By linear probing, we can easily predict surface-level information, such as generation length and first token distribution, as well as more complicated properties, such as the correctness and logicality of the step. These observations indicate that LLMs should already at least partly know about these properties during generation, which provides the foundation for the self-verification ability of LLMs. The code is available at https://github.com/Miaow-Lab/SSAE

