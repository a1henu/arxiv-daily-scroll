---
layout: default
title: When Wording Steers the Evaluation: Framing Bias in LLM judges
---

# When Wording Steers the Evaluation: Framing Bias in LLM judges
**arXiv**：[2601.13537v1](https://arxiv.org/abs/2601.13537) · [PDF](https://arxiv.org/pdf/2601.13537.pdf)  
**作者**：Yerin Hwang, Dongryeol Lee, Taegwan Kang, Minwoo Lee, Kyomin Jung  

**一句话要点**：揭示大语言模型评估中的框架偏差，通过对称提示设计展示其结构性影响

**关键词**：大语言模型评估, 框架偏差, 提示工程, 心理学框架效应, 对称提示设计, 模型稳定性

## 3 点简述
- 核心问题：大语言模型评估易受提示措辞影响，导致判断不稳定，框架偏差未充分研究
- 方法要点：基于心理学框架效应，设计谓词-正/负对称提示，系统分析模型判断偏差
- 实验或效果：在14个LLM法官上测试四个高风险任务，发现显著偏差，模型家族呈现不同倾向

## 摘要（原文）

> Large language models (LLMs) are known to produce varying responses depending on prompt phrasing, indicating that subtle guidance in phrasing can steer their answers. However, the impact of this framing bias on LLM-based evaluation, where models are expected to make stable and impartial judgments, remains largely underexplored. Drawing inspiration from the framing effect in psychology, we systematically investigate how deliberate prompt framing skews model judgments across four high-stakes evaluation tasks. We design symmetric prompts using predicate-positive and predicate-negative constructions and demonstrate that such framing induces significant discrepancies in model outputs. Across 14 LLM judges, we observe clear susceptibility to framing, with model families showing distinct tendencies toward agreement or rejection. These findings suggest that framing bias is a structural property of current LLM-based evaluation systems, underscoring the need for framing-aware protocols.

