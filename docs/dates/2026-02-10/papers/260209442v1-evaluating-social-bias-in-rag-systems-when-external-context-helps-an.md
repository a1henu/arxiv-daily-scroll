---
layout: default
title: Evaluating Social Bias in RAG Systems: When External Context Helps and Reasoning Hurts
---

# Evaluating Social Bias in RAG Systems: When External Context Helps and Reasoning Hurts
**arXiv**：[2602.09442v1](https://arxiv.org/abs/2602.09442) · [PDF](https://arxiv.org/pdf/2602.09442.pdf)  
**作者**：Shweta Parihar, Lu Cheng  

**一句话要点**：评估RAG系统的社会偏见：外部上下文缓解偏见而推理增加偏见

**关键词**：检索增强生成, 社会偏见评估, 链式思维提示, 公平性分析, 外部知识检索

## 3 点简述
- 研究RAG架构中社会偏见的评估与影响，覆盖13种以上偏见类型
- 实验发现外部上下文可减少偏见，但CoT推理增加偏见，揭示公平性权衡
- 通过多数据集和模型实验，分析偏见在检索与推理过程中的动态变化

## 摘要（原文）

> Social biases inherent in large language models (LLMs) raise significant fairness concerns. Retrieval-Augmented Generation (RAG) architectures, which retrieve external knowledge sources to enhance the generative capabilities of LLMs, remain susceptible to the same bias-related challenges. This work focuses on evaluating and understanding the social bias implications of RAG. Through extensive experiments across various retrieval corpora, LLMs, and bias evaluation datasets, encompassing more than 13 different bias types, we surprisingly observe a reduction in bias in RAG. This suggests that the inclusion of external context can help counteract stereotype-driven predictions, potentially improving fairness by diversifying the contextual grounding of the model's outputs. To better understand this phenomenon, we then explore the model's reasoning process by integrating Chain-of-Thought (CoT) prompting into RAG while assessing the faithfulness of the model's CoT. Our experiments reveal that the model's bias inclinations shift between stereotype and anti-stereotype responses as more contextual information is incorporated from the retrieved documents. Interestingly, we find that while CoT enhances accuracy, contrary to the bias reduction observed with RAG, it increases overall bias across datasets, highlighting the need for bias-aware reasoning frameworks that can mitigate this trade-off.

