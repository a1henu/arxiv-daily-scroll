---
layout: default
title: A Hybrid Supervised-LLM Pipeline for Actionable Suggestion Mining in Unstructured Customer Reviews
---

# A Hybrid Supervised-LLM Pipeline for Actionable Suggestion Mining in Unstructured Customer Reviews
**arXiv**：[2601.19214v1](https://arxiv.org/abs/2601.19214) · [PDF](https://arxiv.org/pdf/2601.19214.pdf)  
**作者**：Aakash Trivedi, Aniket Upadhyay, Pratik Narang, Dhruv Kumar, Praveen Kumar  

**一句话要点**：提出混合监督-LLM管道，从非结构化客户评论中提取可操作建议，提升提取准确性和聚类一致性。

**关键词**：可操作建议挖掘, 混合监督学习, 大型语言模型, 客户评论分析, 文本分类, 聚类摘要

## 3 点简述
- 核心问题：现有方法难以从混合意图的非结构化文本中精确提取企业所需的改进指令。
- 方法要点：结合高召回RoBERTa分类器和指令调优LLM，进行建议提取、分类、聚类和摘要。
- 实验或效果：在真实酒店和食品数据集上，混合系统在提取准确性和聚类一致性上优于基线，人类评估确认结果清晰可靠。

## 摘要（原文）

> Extracting actionable suggestions from customer reviews is essential for operational decision-making, yet these directives are often embedded within mixed-intent, unstructured text. Existing approaches either classify suggestion-bearing sentences or generate high-level summaries, but rarely isolate the precise improvement instructions businesses need. We evaluate a hybrid pipeline combining a high-recall RoBERTa classifier trained with a precision-recall surrogate to reduce unrecoverable false negatives with a controlled, instruction-tuned LLM for suggestion extraction, categorization, clustering, and summarization. Across real-world hospitality and food datasets, the hybrid system outperforms prompt-only, rule-based, and classifier-only baselines in extraction accuracy and cluster coherence. Human evaluations further confirm that the resulting suggestions and summaries are clear, faithful, and interpretable. Overall, our results show that hybrid reasoning architectures achieve meaningful improvements fine-grained actionable suggestion mining while highlighting challenges in domain adaptation and efficient local deployment.

