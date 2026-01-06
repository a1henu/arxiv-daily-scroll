---
layout: default
title: pdfQA: Diverse, Challenging, and Realistic Question Answering over PDFs
---

# pdfQA: Diverse, Challenging, and Realistic Question Answering over PDFs
**arXiv**：[2601.02285v1](https://arxiv.org/abs/2601.02285) · [PDF](https://arxiv.org/pdf/2601.02285.pdf)  
**作者**：Tobias Schimanski, Imene Kolli, Jingwei Ni, Yu Fan, Ario Saeid Vaghefi, Elliott Ash, Markus Leippold  

**一句话要点**：提出pdfQA数据集以解决PDF文档问答中缺乏多样性和挑战性的问题

**关键词**：PDF问答, 多领域数据集, 复杂度维度, 端到端评估, 开源LLM, 信息检索

## 3 点简述
- 核心问题：现有QA数据集多基于文本源或特定领域，PDF作为互联网第二大文档类型缺乏多样化问答评估基准。
- 方法要点：构建包含真实和合成数据的多领域数据集，通过十个复杂度维度标注，并应用质量和难度过滤器。
- 实验或效果：使用开源LLM回答问题，揭示复杂度维度与挑战的相关性，为端到端QA管道评估提供基础。

## 摘要（原文）

> PDFs are the second-most used document type on the internet (after HTML). Yet, existing QA datasets commonly start from text sources or only address specific domains. In this paper, we present pdfQA, a multi-domain 2K human-annotated (real-pdfQA) and 2K synthetic dataset (syn-pdfQA) differentiating QA pairs in ten complexity dimensions (e.g., file type, source modality, source position, answer type). We apply and evaluate quality and difficulty filters on both datasets, obtaining valid and challenging QA pairs. We answer the questions with open-source LLMs, revealing existing challenges that correlate with our complexity dimensions. pdfQA presents a basis for end-to-end QA pipeline evaluation, testing diverse skill sets and local optimizations (e.g., in information retrieval or parsing).

