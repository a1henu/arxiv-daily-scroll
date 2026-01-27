---
layout: default
title: DEEPMED: Building a Medical DeepResearch Agent via Multi-hop Med-Search Data and Turn-Controlled Agentic Training & Inference
---

# DEEPMED: Building a Medical DeepResearch Agent via Multi-hop Med-Search Data and Turn-Controlled Agentic Training & Inference
**arXiv**：[2601.18496v1](https://arxiv.org/abs/2601.18496) · [PDF](https://arxiv.org/pdf/2601.18496.pdf)  
**作者**：Zihan wang, Hao Wang, Shi Feng, Xiaocui Yang, Daling Wang, Yiqun Zhang, Jinghao Lin, Haihua Yang, Xiaozhong Ji  

**一句话要点**：提出DeepMed，通过多跳医学搜索数据与轮次控制训练推理，提升医学深度研究代理性能。

**关键词**：医学深度研究, 多跳搜索数据, 轮次控制训练, 医学推理, 工具调用优化, 基准测试

## 3 点简述
- 医学推理模型受限于参数知识，易遗忘和幻觉，直接迁移深度研究模型效果有限。
- 构建多跳医学搜索QA数据，支持模型在临床上下文中解释证据，避免盲目工具调用。
- 在七个医学基准上，DeepMed平均提升基础模型9.79%，优于更大模型。

## 摘要（原文）

> Medical reasoning models remain constrained by parametric knowledge and are thus susceptible to forgetting and hallucinations. DeepResearch (DR) models ground outputs in verifiable evidence from tools and perform strongly in general domains, but their direct transfer to medical field yields relatively limited gains. We attribute this to two gaps: task characteristic and tool-use scaling. Medical questions require evidence interpretation in a knowledge-intensive clinical context; while general DR models can retrieve information, they often lack clinical-context reasoning and thus "find it but fail to use it," leaving performance limited by medical abilities. Moreover, in medical scenarios, blindly scaling tool-call can inject noisy context, derailing sensitive medical reasoning and prompting repetitive evidence-seeking along incorrect paths. Therefore, we propose DeepMed. For data, we deploy a multi-hop med-search QA synthesis method supporting the model to apply the DR paradigm in medical contexts. For training, we introduce a difficulty-aware turn-penalty to suppress excessive tool-call growth. For inference, we bring a monitor to help validate hypotheses within a controlled number of steps and avoid context rot. Overall, on seven medical benchmarks, DeepMed improves its base model by 9.79\% on average and outperforms larger medical reasoning and DR models.

