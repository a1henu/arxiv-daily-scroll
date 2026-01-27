---
layout: default
title: QualiRAG: Retrieval-Augmented Generation for Visual Quality Understanding
---

# QualiRAG: Retrieval-Augmented Generation for Visual Quality Understanding
**arXiv**：[2601.18195v1](https://arxiv.org/abs/2601.18195) · [PDF](https://arxiv.org/pdf/2601.18195.pdf)  
**作者**：Linhan Cao, Wei Sun, Weixia Zhang, Xiangyang Zhu, Kaiwei Zhang, Jun Jia, Dandan Zhu, Guangtao Zhai, Xiongkuo Min  

**一句话要点**：提出QualiRAG框架，通过检索增强生成实现免训练的视觉质量理解

**关键词**：检索增强生成, 视觉质量评估, 大模型应用, 免训练框架, 多模态理解

## 3 点简述
- 视觉质量评估转向可解释理解，需细粒度感知与上下文信息，现有方法依赖标注数据易有偏差
- QualiRAG利用大模型潜知识，动态生成四类辅助知识源，进行相关性检索以支持证据推理
- 实验显示在质量理解任务上优于开源及微调模型，质量比较任务表现竞争性，无需特定训练

## 摘要（原文）

> Visual quality assessment (VQA) is increasingly shifting from scalar score prediction toward interpretable quality understanding -- a paradigm that demands \textit{fine-grained spatiotemporal perception} and \textit{auxiliary contextual information}. Current approaches rely on supervised fine-tuning or reinforcement learning on curated instruction datasets, which involve labor-intensive annotation and are prone to dataset-specific biases. To address these challenges, we propose \textbf{QualiRAG}, a \textit{training-free} \textbf{R}etrieval-\textbf{A}ugmented \textbf{G}eneration \textbf{(RAG)} framework that systematically leverages the latent perceptual knowledge of large multimodal models (LMMs) for visual quality perception. Unlike conventional RAG that retrieves from static corpora, QualiRAG dynamically generates auxiliary knowledge by decomposing questions into structured requests and constructing four complementary knowledge sources: \textit{visual metadata}, \textit{subject localization}, \textit{global quality summaries}, and \textit{local quality descriptions}, followed by relevance-aware retrieval for evidence-grounded reasoning. Extensive experiments show that QualiRAG achieves substantial improvements over open-source general-purpose LMMs and VQA-finetuned LMMs on visual quality understanding tasks, and delivers competitive performance on visual quality comparison tasks, demonstrating robust quality assessment capabilities without any task-specific training. The code will be publicly available at https://github.com/clh124/QualiRAG.

