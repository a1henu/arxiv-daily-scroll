---
layout: default
title: RPO-RAG: Aligning Small LLMs with Relation-aware Preference Optimization for Knowledge Graph Question Answering
---

# RPO-RAG: Aligning Small LLMs with Relation-aware Preference Optimization for Knowledge Graph Question Answering
**arXiv**：[2601.19225v1](https://arxiv.org/abs/2601.19225) · [PDF](https://arxiv.org/pdf/2601.19225.pdf)  
**作者**：Kaehyun Um, KyuHwan Yeom, Haerim Yang, Minyoung Choi, Hyeongjun Yang, Kyong-Ho Lee  

**一句话要点**：提出RPO-RAG框架，通过关系感知偏好优化提升小语言模型在知识图谱问答中的性能。

**关键词**：知识图谱问答, 检索增强生成, 小语言模型, 关系感知优化, 偏好优化, 推理能力提升

## 3 点简述
- 现有基于知识图谱的检索增强生成方法存在语义无关路径采样和弱对齐问题，限制小模型推理能力。
- RPO-RAG引入查询路径语义采样、关系感知偏好优化和答案中心提示设计，增强小模型知识利用。
- 在WebQSP和CWQ数据集上实验显示，RPO-RAG显著提升小模型性能，在8B参数以下模型达到新SOTA。

## 摘要（原文）

> Large Language Models (LLMs) have recently demonstrated remarkable reasoning abilities, yet hallucinate on knowledge-intensive tasks. Retrieval-augmented generation (RAG) mitigates this issue by grounding answers in external sources, e.g., knowledge graphs (KGs). However, existing KG-based RAG approaches rely on semantics-unaware path sampling and are weakly aligned with KG reasoning objectives, which limits further accuracy gains. They also feed retrieved paths directly into the reasoner without organizing them into answer-centered reasoning paths, hindering small LLMs' ability to leverage the retrieved knowledge. Furthermore, prior works predominantly rely on large LLMs (e.g., ChatGPT/GPT-4) or assume backbones above 7B parameters, leaving sub-7B models underexplored. We address this gap with RPO-RAG, the first KG-based RAG framework specifically designed for small LLMs, to the best of our knowledge. RPO-RAG introduces three key innovations: (1) a query-path semantic sampling strategy that provides informative supervisory signals; (2) a relation-aware preference optimization that aligns training with intermediate KG reasoning signals (e.g., relation); and (3) an answer-centered prompt design that organizes entities and reasoning paths in an interpretable format. Extensive experiments on two benchmark Knowledge Graph Question Answering (KGQA) datasets, WebQSP and CWQ, demonstrate that RPO-RAG effectively bridges the performance gap between small and large language models. On WebQSP, it improves F1 by up to 8.8%, reflecting enhanced answer precision, while on CWQ it achieves new state-of-the-art results among models under 8B parameters in both Hit and F1. Overall, RPO-RAG substantially improves the reasoning capability of small LLMs, even under 3B parameters-highlighting their potential for resource-efficient and practical on-device KGQA applications.

