---
layout: default
title: IRIS: Implicit Reward-Guided Internal Sifting for Mitigating Multimodal Hallucination
---

# IRIS: Implicit Reward-Guided Internal Sifting for Mitigating Multimodal Hallucination
**arXiv**：[2602.01769v1](https://arxiv.org/abs/2602.01769) · [PDF](https://arxiv.org/pdf/2602.01769.pdf)  
**作者**：Yuanshuai Li, Yuping Yan, Jirui Han, Fei Ming, Lingjuan Lv, Yaochu Jin  

**一句话要点**：提出IRIS方法，利用隐式奖励引导内部筛选以缓解多模态大语言模型的幻觉问题

**关键词**：多模态大语言模型, 幻觉缓解, 隐式奖励, 策略内优化, 模态竞争

## 3 点简述
- 核心问题：多模态大语言模型存在幻觉，现有方法依赖外部评估器导致学习间隙和离散化损失
- 方法要点：通过连续隐式奖励在概率空间捕获模态竞争，使用自生成偏好对进行策略内优化
- 实验或效果：在关键幻觉基准上仅用5.7k样本实现竞争性能，无需外部反馈

## 摘要（原文）

> Hallucination remains a fundamental challenge for Multimodal Large Language Models (MLLMs). While Direct Preference Optimization (DPO) is a key alignment framework, existing approaches often rely heavily on costly external evaluators for scoring or rewriting, incurring off-policy learnability gaps and discretization loss. Due to the lack of access to internal states, such feedback overlooks the fine-grained conflicts between different modalities that lead to hallucinations during generation.
>   To address this issue, we propose IRIS (Implicit Reward-Guided Internal Sifting), which leverages continuous implicit rewards in the native log-probability space to preserve full information density and capture internal modal competition. This on-policy paradigm eliminates learnability gaps by utilizing self-generated preference pairs. By sifting these pairs based on multimodal implicit rewards, IRIS ensures that optimization is driven by signals that directly resolve modal conflicts. Extensive experiments demonstrate that IRIS achieves highly competitive performance on key hallucination benchmarks using only 5.7k samples, without requiring any external feedback during preference alignment. These results confirm that IRIS provides an efficient and principled paradigm for mitigating MLLM hallucinations.

