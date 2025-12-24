---
layout: default
title: FaithLens: Detecting and Explaining Faithfulness Hallucination
---

# FaithLens: Detecting and Explaining Faithfulness Hallucination
**arXiv**：[2512.20182v1](https://arxiv.org/abs/2512.20182) · [PDF](https://arxiv.org/pdf/2512.20182.pdf)  
**作者**：Shuzheng Si, Qingyi Wang, Haozhe Zhao, Yuzhuo Bai, Guanqiao Chen, Kangyang Luo, Gang Chen, Fanchao Qi, Minjia Zhang, Baobao Chang, Maosong Sun  

**一句话要点**：提出FaithLens模型以检测和解释大语言模型输出中的忠实性幻觉，提升可信度。

**关键词**：忠实性幻觉检测, 大语言模型可信度, 数据合成与过滤, 强化学习优化, 解释生成

## 3 点简述
- 核心问题：检测大语言模型输出中的忠实性幻觉，对检索增强生成和摘要等应用至关重要。
- 方法要点：通过合成数据、数据过滤和基于规则的强化学习，联合提供预测和解释。
- 实验或效果：在12个任务上，8B参数FaithLens优于GPT-4.1等模型，平衡可信度、效率和效果。

## 摘要（原文）

> Recognizing whether outputs from large language models (LLMs) contain faithfulness hallucination is crucial for real-world applications, e.g., retrieval-augmented generation and summarization. In this paper, we introduce FaithLens, a cost-efficient and effective faithfulness hallucination detection model that can jointly provide binary predictions and corresponding explanations to improve trustworthiness. To achieve this, we first synthesize training data with explanations via advanced LLMs and apply a well-defined data filtering strategy to ensure label correctness, explanation quality, and data diversity. Subsequently, we fine-tune the model on these well-curated training data as a cold start and further optimize it with rule-based reinforcement learning, using rewards for both prediction correctness and explanation quality. Results on 12 diverse tasks show that the 8B-parameter FaithLens outperforms advanced models such as GPT-4.1 and o3. Also, FaithLens can produce high-quality explanations, delivering a distinctive balance of trustworthiness, efficiency, and effectiveness.

