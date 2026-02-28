---
layout: default
title: MovieTeller: Tool-augmented Movie Synopsis with ID Consistent Progressive Abstraction
---

# MovieTeller: Tool-augmented Movie Synopsis with ID Consistent Progressive Abstraction
**arXiv**：[2602.23228v1](https://arxiv.org/abs/2602.23228) · [PDF](https://arxiv.org/pdf/2602.23228.pdf)  
**作者**：Yizhi Li, Xiaohan Chen, Miao Jiang, Wentao Tang, Gaoang Wang  

**一句话要点**：提出MovieTeller框架，通过工具增强的渐进抽象生成电影摘要，解决长视频摘要中角色识别一致性和叙事连贯性问题。

**关键词**：长视频摘要, 工具增强生成, 角色识别一致性, 渐进抽象, 视觉语言模型

## 3 点简述
- 核心问题：现有视觉语言模型在长视频摘要中缺乏角色识别一致性和叙事连贯性。
- 方法要点：使用训练免费的工具增强方法，结合人脸识别模型提供事实基础，并采用渐进抽象流程分解摘要任务。
- 实验或效果：相比端到端基线，在事实准确性、角色一致性和叙事连贯性方面有显著提升。

## 摘要（原文）

> With the explosive growth of digital entertainment, automated video summarization has become indispensable for applications such as content indexing, personalized recommendation, and efficient media archiving. Automatic synopsis generation for long-form videos, such as movies and TV series, presents a significant challenge for existing Vision-Language Models (VLMs). While proficient at single-image captioning, these general-purpose models often exhibit critical failures in long-duration contexts, primarily a lack of ID-consistent character identification and a fractured narrative coherence. To overcome these limitations, we propose MovieTeller, a novel framework for generating movie synopses via tool-augmented progressive abstraction. Our core contribution is a training-free, tool-augmented, fact-grounded generation process. Instead of requiring costly model fine-tuning, our framework directly leverages off-the-shelf models in a plug-and-play manner. We first invoke a specialized face recognition model as an external "tool" to establish Factual Groundings--precise character identities and their corresponding bounding boxes. These groundings are then injected into the prompt to steer the VLM's reasoning, ensuring the generated scene descriptions are anchored to verifiable facts. Furthermore, our progressive abstraction pipeline decomposes the summarization of a full-length movie into a multi-stage process, effectively mitigating the context length limitations of current VLMs. Experiments demonstrate that our approach yields significant improvements in factual accuracy, character consistency, and overall narrative coherence compared to end-to-end baselines.

