---
layout: default
title: Generative Giants, Retrieval Weaklings: Why do Multimodal Large Language Models Fail at Multimodal Retrieval?
---

# Generative Giants, Retrieval Weaklings: Why do Multimodal Large Language Models Fail at Multimodal Retrieval?
**arXiv**：[2512.19115v1](https://arxiv.org/abs/2512.19115) · [PDF](https://arxiv.org/pdf/2512.19115.pdf)  
**作者**：Hengyi Feng, Zeang Sheng, Meiyi Qiang, Wentao Zhang  

**一句话要点**：揭示多模态大语言模型在零样本检索中表现不佳的机制，并提出改进方向。

**关键词**：多模态大语言模型, 零样本检索, 稀疏自编码器, 表示空间分析, 多模态检索

## 3 点简述
- 核心问题：多模态大语言模型在生成任务中成功，但在零样本多模态检索中表现不佳。
- 方法要点：使用稀疏自编码器分解模型输出表示，分析语义概念以探究内在行为。
- 实验或效果：发现表示空间以文本语义为主，视觉信息占比小，且相似度计算中的关键特征成分会降低检索性能。

## 摘要（原文）

> Despite the remarkable success of multimodal large language models (MLLMs) in generative tasks, we observe that they exhibit a counterintuitive deficiency in the zero-shot multimodal retrieval task. In this work, we investigate the underlying mechanisms that hinder MLLMs from serving as effective retrievers. With the help of sparse autoencoders (SAEs), we decompose MLLM output representations into interpretable semantic concepts to probe their intrinsic behavior. Our analysis reveals that the representation space of MLLMs is overwhelmingly dominated by textual semantics; the visual information essential for multimodal retrieval only constitutes a small portion. This imbalance is compounded by the heavy focus of MLLMs on bridging image-text modalities, which facilitates generation but homogenizes embeddings and finally diminishes the discriminative power required for multimodal retrieval. We further discover that the specific feature components that contribute most to the similarity computations for MLLMs are in fact distractors that actively degrade retrieval performance. Overall, our work provides the first in-depth interpretability analysis of MLLM representations in the context of multimodal retrieval and offers possible directions for enhancing the multimodal retrieval capabilities of MLLMs.

