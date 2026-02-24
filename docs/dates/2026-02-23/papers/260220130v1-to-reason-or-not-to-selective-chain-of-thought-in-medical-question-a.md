---
layout: default
title: To Reason or Not to: Selective Chain-of-Thought in Medical Question Answering
---

# To Reason or Not to: Selective Chain-of-Thought in Medical Question Answering
**arXiv**：[2602.20130v1](https://arxiv.org/abs/2602.20130) · [PDF](https://arxiv.org/pdf/2602.20130.pdf)  
**作者**：Zaifu Zhan, Min Zeng, Shuang Zhou, Yiran Song, Xiaoyi Chen, Yu Hou, Yifan Wu, Yang Ruan, Rui Zhang  

**一句话要点**：提出选择性思维链以优化医疗问答效率，通过动态判断推理需求减少冗余计算。

**关键词**：医疗问答, 选择性思维链, 推理效率, 大语言模型, 生物医学基准

## 3 点简述
- 核心问题：医疗问答中LLMs推理效率低，常对无需推理的回忆型问题生成冗余解释。
- 方法要点：选择性思维链在推理时预测问题是否需要推理，仅必要时生成解释，平衡效率与准确性。
- 实验效果：在四个生物医学基准上，减少推理时间13-45%和令牌使用8-47%，准确率损失≤4%。

## 摘要（原文）

> Objective: To improve the efficiency of medical question answering (MedQA) with large language models (LLMs) by avoiding unnecessary reasoning while maintaining accuracy.
>   Methods: We propose Selective Chain-of-Thought (Selective CoT), an inference-time strategy that first predicts whether a question requires reasoning and generates a rationale only when needed. Two open-source LLMs (Llama-3.1-8B and Qwen-2.5-7B) were evaluated on four biomedical QA benchmarks-HeadQA, MedQA-USMLE, MedMCQA, and PubMedQA. Metrics included accuracy, total generated tokens, and inference time.
>   Results: Selective CoT reduced inference time by 13-45% and token usage by 8-47% with minimal accuracy loss ($\leq$4\%). In some model-task pairs, it achieved both higher accuracy and greater efficiency than standard CoT. Compared with fixed-length CoT, Selective CoT reached similar or superior accuracy at substantially lower computational cost.
>   Discussion: Selective CoT dynamically balances reasoning depth and efficiency by invoking explicit reasoning only when beneficial, reducing redundancy on recall-type questions while preserving interpretability.
>   Conclusion: Selective CoT provides a simple, model-agnostic, and cost-effective approach for medical QA, aligning reasoning effort with question complexity to enhance real-world deployability of LLM-based clinical systems.

