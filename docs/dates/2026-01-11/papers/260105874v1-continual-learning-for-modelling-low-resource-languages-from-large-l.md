---
layout: default
title: Continual-learning for Modelling Low-Resource Languages from Large Language Models
---

# Continual-learning for Modelling Low-Resource Languages from Large Language Models
**arXiv**：[2601.05874v1](https://arxiv.org/abs/2601.05874) · [PDF](https://arxiv.org/pdf/2601.05874.pdf)  
**作者**：Santosh Srinath K, Mudit Somani, Varun Reddy Padala, Prajna Devi Upadhyay, Abhijit Das  

**一句话要点**：提出基于词性代码切换与回放适配器的持续学习策略，以缓解低资源语言建模中的灾难性遗忘问题。

**关键词**：持续学习, 低资源语言建模, 灾难性遗忘, 代码切换, 视觉语言任务, 回放适配器

## 3 点简述
- 核心问题：从大语言模型适应构建低资源语言小模型时，灾难性遗忘是主要挑战。
- 方法要点：采用基于词性的代码切换和回放适配器策略，实现持续学习以减轻遗忘。
- 实验或效果：在视觉问答和语言建模任务上验证了架构的有效性。

## 摘要（原文）

> Modelling a language model for a multi-lingual scenario includes several potential challenges, among which catastrophic forgetting is the major challenge. For example, small language models (SLM) built for low-resource languages by adapting large language models (LLMs) pose the challenge of catastrophic forgetting. This work proposes to employ a continual learning strategy using parts-of-speech (POS)-based code-switching along with a replay adapter strategy to mitigate the identified gap of catastrophic forgetting while training SLM from LLM. Experiments conducted on vision language tasks such as visual question answering and language modelling task exhibits the success of the proposed architecture.

