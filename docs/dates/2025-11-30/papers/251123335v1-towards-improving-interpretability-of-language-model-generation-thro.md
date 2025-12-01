---
layout: default
title: Towards Improving Interpretability of Language Model Generation through a Structured Knowledge Discovery Approach
---

# Towards Improving Interpretability of Language Model Generation through a Structured Knowledge Discovery Approach
**arXiv**：[2511.23335v1](https://arxiv.org/abs/2511.23335) · [PDF](https://arxiv.org/pdf/2511.23335.pdf)  
**作者**：Shuqi Liu, Han Wu, Guanzhi Deng, Jianshu Chen, Xiaoyang Wang, Linqi Song  

**一句话要点**：提出任务无关的结构化知识发现方法，以提升语言模型生成的可解释性

**关键词**：知识增强文本生成, 可解释性, 结构化知识发现, 任务无关模型, 分层指针网络

## 3 点简述
- 核心问题：知识增强文本生成中，语言模型缺乏可解释性，影响实际应用可靠性。
- 方法要点：利用结构化知识的两层架构，设计本地-全局交互表示学习和分层指针网络，选择相关知识和实体。
- 实验或效果：在RotoWireFG和KdConv数据集上验证，模型优于现有方法，提升生成质量和可解释性。

## 摘要（原文）

> Knowledge-enhanced text generation aims to enhance the quality of generated text by utilizing internal or external knowledge sources. While language models have demonstrated impressive capabilities in generating coherent and fluent text, the lack of interpretability presents a substantial obstacle. The limited interpretability of generated text significantly impacts its practical usability, particularly in knowledge-enhanced text generation tasks that necessitate reliability and explainability. Existing methods often employ domain-specific knowledge retrievers that are tailored to specific data characteristics, limiting their generalizability to diverse data types and tasks. To overcome this limitation, we directly leverage the two-tier architecture of structured knowledge, consisting of high-level entities and low-level knowledge triples, to design our task-agnostic structured knowledge hunter. Specifically, we employ a local-global interaction scheme for structured knowledge representation learning and a hierarchical transformer-based pointer network as the backbone for selecting relevant knowledge triples and entities. By combining the strong generative ability of language models with the high faithfulness of the knowledge hunter, our model achieves high interpretability, enabling users to comprehend the model output generation process. Furthermore, we empirically demonstrate the effectiveness of our model in both internal knowledge-enhanced table-to-text generation on the RotoWireFG dataset and external knowledge-enhanced dialogue response generation on the KdConv dataset. Our task-agnostic model outperforms state-of-the-art methods and corresponding language models, setting new standards on the benchmark.

