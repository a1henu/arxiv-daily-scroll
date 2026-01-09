---
layout: default
title: DVD: A Robust Method for Detecting Variant Contamination in Large Language Model Evaluation
---

# DVD: A Robust Method for Detecting Variant Contamination in Large Language Model Evaluation
**arXiv**：[2601.04895v1](https://arxiv.org/abs/2601.04895) · [PDF](https://arxiv.org/pdf/2601.04895.pdf)  
**作者**：Renzhao Liang, Jingru Chen, Bo Jia, Bo Deng, Chenggang Xie, Yidong Wang, Ke Jin, Xin Wang, Linfeng Zhang, Cunxiang Wang  

**一句话要点**：提出DVD方法以检测大语言模型评估中的变体污染问题

**关键词**：大语言模型评估, 变体污染检测, 生成分布方差, 温度采样, 基准构建, 鲁棒性分析

## 3 点简述
- 核心问题：变体污染导致评估分数虚高，现有检测方法难以识别语义等效但词汇或句法变化的测试项
- 方法要点：基于温度采样建模局部输出分布方差，利用记忆状态与扰动漂移状态的交替作为检测指纹
- 实验或效果：在Omni-MATH和SuperGPQA基准上优于多种基线方法，展现强鲁棒性

## 摘要（原文）

> Evaluating large language models (LLMs) is increasingly confounded by \emph{variant contamination}: the training corpus contains semantically equivalent yet lexically or syntactically altered versions of test items. Unlike verbatim leakage, these paraphrased or structurally transformed variants evade existing detectors based on sampling consistency or perplexity, thereby inflating benchmark scores via memorization rather than genuine reasoning. We formalize this problem and introduce \textbf{DVD} (\textbf{D}etection via \textbf{V}ariance of generation \textbf{D}istribution), a single-sample detector that models the local output distribution induced by temperature sampling. Our key insight is that contaminated items trigger alternation between a \emph{memory-adherence} state and a \emph{perturbation-drift} state, yielding abnormally high variance in the synthetic difficulty of low-probability tokens; uncontaminated items remain in drift with comparatively smooth variance. We construct the first benchmark for variant contamination across two domains Omni-MATH and SuperGPQA by generating and filtering semantically equivalent variants, and simulate contamination via fine-tuning models of different scales and architectures (Qwen2.5 and Llama3.1). Across datasets and models, \textbf{DVD} consistently outperforms perplexity-based, Min-$k$\%++, edit-distance (CDD), and embedding-similarity baselines, while exhibiting strong robustness to hyperparameters. Our results establish variance of the generation distribution as a principled and practical fingerprint for detecting variant contamination in LLM evaluation.

