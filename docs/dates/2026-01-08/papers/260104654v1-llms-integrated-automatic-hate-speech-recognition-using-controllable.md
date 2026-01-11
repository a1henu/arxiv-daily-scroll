---
layout: default
title: LLMs-Integrated Automatic Hate Speech Recognition Using Controllable Text Generation Models
---

# LLMs-Integrated Automatic Hate Speech Recognition Using Controllable Text Generation Models
**arXiv**：[2601.04654v1](https://arxiv.org/abs/2601.04654) · [PDF](https://arxiv.org/pdf/2601.04654.pdf)  
**作者**：Ryutaro Oshima, Yuya Hosoda, Youji Iiguni  

**一句话要点**：提出集成LLM的自动语音识别模型，用于仇恨语音转录与审查，通过可控文本生成优化训练数据。

**关键词**：仇恨语音识别, 大型语言模型集成, 可控文本生成, 课程学习, 语音转录审查

## 3 点简述
- 核心问题：仇恨语音数据集有限，影响LLM指令调优和审查性能。
- 方法要点：使用CoT提示生成文本，经TTS转换后过滤非仇恨样本，通过阈值控制仇恨级别进行课程学习。
- 实验或效果：模型在仇恨相关词屏蔽准确率达58.6%，超越基线，课程训练提升转录与审查效率。

## 摘要（原文）

> This paper proposes an automatic speech recognition (ASR) model for hate speech using large language models (LLMs). The proposed method integrates the encoder of the ASR model with the decoder of the LLMs, enabling simultaneous transcription and censorship tasks to prevent the exposure of harmful content. Instruction tuning of the LLM to mask hate-related words with specific tokens requires an annotated hate speech dataset, which is limited. We generate text samples using an LLM with the Chain-of-Thought (CoT) prompting technique guided by cultural context and examples and then convert them into speech samples using a text-to-speech (TTS) system. However, some of them contain non-hate speech samples with hate-related words, which degrades the censorship performance. This paper filters the samples which text classification models correctly label as hate content. By adjusting the threshold for the number of correct answer models, we can control the level of hate in the generated dataset, allowing us to train the LLMs through curriculum learning in a gradual manner. Experimental results show that the proposed method achieves a masking accuracy of 58.6\% for hate-related words, surpassing previous baselines. We also confirm that the curriculum training contributes to the efficiency of both transcription and censorship tasks.

