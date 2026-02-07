---
layout: default
title: Detecting Misbehaviors of Large Vision-Language Models by Evidential Uncertainty Quantification
---

# Detecting Misbehaviors of Large Vision-Language Models by Evidential Uncertainty Quantification
**arXiv**：[2602.05535v1](https://arxiv.org/abs/2602.05535) · [PDF](https://arxiv.org/pdf/2602.05535.pdf)  
**作者**：Tao Huang, Rui Wang, Xiaofei Liu, Yi Qin, Li Duan, Liping Jing  

**一句话要点**：提出证据不确定性量化方法以检测大型视觉语言模型的不当行为

**关键词**：大型视觉语言模型, 不确定性量化, 证据理论, 模型不当行为检测, 幻觉检测, 对抗鲁棒性

## 3 点简述
- 核心问题：大型视觉语言模型面对不完整或对抗输入时产生幻觉等不当行为，源于认知不确定性。
- 方法要点：基于证据理论，从模型输出特征量化内部冲突和知识缺失，实现细粒度不确定性评估。
- 实验或效果：在幻觉、越狱等四类不当行为检测中优于基线，并分析层间不确定性动态以解释内部表示演化。

## 摘要（原文）

> Large vision-language models (LVLMs) have shown substantial advances in multimodal understanding and generation. However, when presented with incompetent or adversarial inputs, they frequently produce unreliable or even harmful content, such as fact hallucinations or dangerous instructions. This misalignment with human expectations, referred to as \emph{misbehaviors} of LVLMs, raises serious concerns for deployment in critical applications. These misbehaviors are found to stem from epistemic uncertainty, specifically either conflicting internal knowledge or the absence of supporting information. However, existing uncertainty quantification methods, which typically capture only overall epistemic uncertainty, have shown limited effectiveness in identifying such issues. To address this gap, we propose Evidential Uncertainty Quantification (EUQ), a fine-grained method that captures both information conflict and ignorance for effective detection of LVLM misbehaviors. In particular, we interpret features from the model output head as either supporting (positive) or opposing (negative) evidence. Leveraging Evidence Theory, we model and aggregate this evidence to quantify internal conflict and knowledge gaps within a single forward pass. We extensively evaluate our method across four categories of misbehavior, including hallucinations, jailbreaks, adversarial vulnerabilities, and out-of-distribution (OOD) failures, using state-of-the-art LVLMs, and find that EUQ consistently outperforms strong baselines, showing that hallucinations correspond to high internal conflict and OOD failures to high ignorance. Furthermore, layer-wise evidential uncertainty dynamics analysis helps interpret the evolution of internal representations from a new perspective. The source code is available at https://github.com/HT86159/EUQ.

