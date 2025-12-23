---
layout: default
title: Activations as Features: Probing LLMs for Generalizable Essay Scoring Representations
---

# Activations as Features: Probing LLMs for Generalizable Essay Scoring Representations
**arXiv**：[2512.19456v1](https://arxiv.org/abs/2512.19456) · [PDF](https://arxiv.org/pdf/2512.19456.pdf)  
**作者**：Jinwei Chi, Ke Wang, Yu Chen, Xuanye Lin, Qiang Xu  

**一句话要点**：提出利用LLM中间层激活作为特征，以解决跨提示自动作文评分中的评分标准多样性问题。

**关键词**：自动作文评分, 大语言模型, 激活特征, 跨提示评估, 判别力分析

## 3 点简述
- 核心问题：跨提示自动作文评分因评分标准多样而具挑战性，传统方法多关注LLM输出。
- 方法要点：评估LLM中间层激活的判别力，通过拟合探针分析模型和输入内容的影响。
- 实验或效果：激活在评估作文质量上具强判别力，LLM能适应不同特质和作文类型，有效处理评分标准多样性。

## 摘要（原文）

> Automated essay scoring (AES) is a challenging task in cross-prompt settings due to the diversity of scoring criteria. While previous studies have focused on the output of large language models (LLMs) to improve scoring accuracy, we believe activations from intermediate layers may also provide valuable information. To explore this possibility, we evaluated the discriminative power of LLMs' activations in cross-prompt essay scoring task. Specifically, we used activations to fit probes and further analyzed the effects of different models and input content of LLMs on this discriminative power. By computing the directions of essays across various trait dimensions under different prompts, we analyzed the variation in evaluation perspectives of large language models concerning essay types and traits. Results show that the activations possess strong discriminative power in evaluating essay quality and that LLMs can adapt their evaluation perspectives to different traits and essay types, effectively handling the diversity of scoring criteria in cross-prompt settings.

