---
layout: default
title: Personalized Federated Fine-Tuning of Vision Foundation Models for Healthcare
---

# Personalized Federated Fine-Tuning of Vision Foundation Models for Healthcare
**arXiv**：[2510.12741v1](https://arxiv.org/abs/2510.12741) · [PDF](https://arxiv.org/pdf/2510.12741.pdf)  
**作者**：Adam Tupper, Christian Gagné  

**一句话要点**：提出个性化联邦微调方法，利用正交LoRA适配器解决医疗数据隐私下的模型适应问题

**关键词**：联邦学习, 基础模型微调, LoRA适配器, 医疗成像, 个性化学习, 数据隐私

## 3 点简述
- 核心问题：医疗数据隐私限制共享，导致基础模型微调数据不足
- 方法要点：通过联邦学习学习正交LoRA适配器，分离通用与客户端特定知识
- 实验或效果：在真实联邦医疗成像任务中，与现有方法竞争性表现

## 摘要（原文）

> Foundation models open up new possibilities for the use of AI in healthcare.
> However, even when pre-trained on health data, they still need to be fine-tuned
> for specific downstream tasks. Furthermore, although foundation models reduce
> the amount of training data required to achieve good performance, obtaining
> sufficient data is still a challenge. This is due, in part, to restrictions on
> sharing and aggregating data from different sources to protect patients'
> privacy. One possible solution to this is to fine-tune foundation models via
> federated learning across multiple participating clients (i.e., hospitals,
> clinics, etc.). In this work, we propose a new personalized federated
> fine-tuning method that learns orthogonal LoRA adapters to disentangle general
> and client-specific knowledge, enabling each client to fully exploit both their
> own data and the data of others. Our preliminary results on real-world
> federated medical imaging tasks demonstrate that our approach is competitive
> against current federated fine-tuning methods.

