---
layout: default
title: Whitespaces Don't Lie: Feature-Driven and Embedding-Based Approaches for Detecting Machine-Generated Code
---

# Whitespaces Don't Lie: Feature-Driven and Embedding-Based Approaches for Detecting Machine-Generated Code
**arXiv**：[2601.19264v1](https://arxiv.org/abs/2601.19264) · [PDF](https://arxiv.org/pdf/2601.19264.pdf)  
**作者**：Syed Mehedi Hasan Nirob, Shamim Ehsan, Moqsadur Rahman, Summit Haque  

**一句话要点**：提出基于特征和嵌入的方法，以检测机器生成代码，应对学术诚信和AI责任风险。

**关键词**：代码检测, 特征驱动方法, 嵌入驱动方法, 学术诚信, 大语言模型, 代码风格分析

## 3 点简述
- 核心问题：大语言模型生成代码易引发学术诚信和作者归属问题，需区分人写与机器生成代码。
- 方法要点：比较特征驱动方法（基于代码风格和结构特征）和嵌入驱动方法（利用预训练编码器）。
- 实验或效果：在60万样本数据集上，特征方法ROC-AUC达0.995，嵌入方法ROC-AUC达0.994，显示高检测性能。

## 摘要（原文）

> Large language models (LLMs) have made it remarkably easy to synthesize plausible source code from natural language prompts. While this accelerates software development and supports learning, it also raises new risks for academic integrity, authorship attribution, and responsible AI use. This paper investigates the problem of distinguishing human-written from machine-generated code by comparing two complementary approaches: feature-based detectors built from lightweight, interpretable stylometric and structural properties of code, and embedding-based detectors leveraging pretrained code encoders. Using a recent large-scale benchmark dataset of 600k human-written and AI-generated code samples, we find that feature-based models achieve strong performance (ROC-AUC 0.995, PR-AUC 0.995, F1 0.971), while embedding-based models with CodeBERT embeddings are also very competitive (ROC-AUC 0.994, PR-AUC 0.994, F1 0.965). Analysis shows that features tied to indentation and whitespace provide particularly discriminative cues, whereas embeddings capture deeper semantic patterns and yield slightly higher precision. These findings underscore the trade-offs between interpretability and generalization, offering practical guidance for deploying robust code-origin detection in academic and industrial contexts.

