---
layout: default
title: TCM-DiffRAG: Personalized Syndrome Differentiation Reasoning Method for Traditional Chinese Medicine based on Knowledge Graph and Chain of Thought
---

# TCM-DiffRAG: Personalized Syndrome Differentiation Reasoning Method for Traditional Chinese Medicine based on Knowledge Graph and Chain of Thought
**arXiv**：[2602.22828v1](https://arxiv.org/abs/2602.22828) · [PDF](https://arxiv.org/pdf/2602.22828.pdf)  
**作者**：Jianmin Li, Ying Chang, Su-Kit Tang, Yujia Liu, Yanwen Wang, Shuyuan Lin, Binkai Ou  

**一句话要点**：提出TCM-DiffRAG框架，结合知识图谱与思维链，提升中医个性化辨证推理性能

**关键词**：检索增强生成, 知识图谱, 思维链, 中医辨证, 个性化推理, 大语言模型

## 3 点简述
- 传统RAG方法在中医复杂推理和个体差异场景中表现不佳
- TCM-DiffRAG集成知识图谱与思维链，优化推理过程
- 实验显示在三个数据集上显著优于原生LLM、微调模型及其他RAG基准

## 摘要（原文）

> Background: Retrieval augmented generation (RAG) technology can empower large language models (LLMs) to generate more accurate, professional, and timely responses without fine tuning. However, due to the complex reasoning processes and substantial individual differences involved in traditional Chinese medicine (TCM) clinical diagnosis and treatment, traditional RAG methods often exhibit poor performance in this domain. Objective: To address the limitations of conventional RAG approaches in TCM applications, this study aims to develop an improved RAG framework tailored to the characteristics of TCM reasoning. Methods: We developed TCM-DiffRAG, an innovative RAG framework that integrates knowledge graphs (KG) with chains of thought (CoT). TCM-DiffRAG was evaluated on three distinctive TCM test datasets. Results: The experimental results demonstrated that TCM-DiffRAG achieved significant performance improvements over native LLMs. For example, the qwen-plus model achieved scores of 0.927, 0.361, and 0.038, which were significantly enhanced to 0.952, 0.788, and 0.356 with TCM-DiffRAG. The improvements were even more pronounced for non-Chinese LLMs. Additionally, TCM-DiffRAG outperformed directly supervised fine-tuned (SFT) LLMs and other benchmark RAG methods. Conclusions: TCM-DiffRAG shows that integrating structured TCM knowledge graphs with Chain of Thought based reasoning substantially improves performance in individualized diagnostic tasks. The joint use of universal and personalized knowledge graphs enables effective alignment between general knowledge and clinical reasoning. These results highlight the potential of reasoning-aware RAG frameworks for advancing LLM applications in traditional Chinese medicine.

