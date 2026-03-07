---
layout: default
title: MedCoRAG: Interpretable Hepatology Diagnosis via Hybrid Evidence Retrieval and Multispecialty Consensus
---

# MedCoRAG: Interpretable Hepatology Diagnosis via Hybrid Evidence Retrieval and Multispecialty Consensus
**arXiv**：[2603.05129v1](https://arxiv.org/abs/2603.05129) · [PDF](https://arxiv.org/pdf/2603.05129.pdf)  
**作者**：Zheng Li, Jiayi Xu, Zhikai Hu, Hechang Chen, Lele Cong, Yunyun Wang, Shuchao Pang  

**一句话要点**：提出MedCoRAG框架，通过混合证据检索和多专家协作提升肝病诊断的准确性与可解释性。

**关键词**：肝病诊断, 检索增强生成, 多智能体协作, 可解释AI, 临床决策支持, 知识图谱

## 3 点简述
- 核心问题：现有AI临床诊断方法缺乏透明度、结构化推理和可部署性，尤其在肝病诊断中。
- 方法要点：结合UMLS知识图谱和临床指南进行证据检索与剪枝，采用多智能体协作推理模拟多学科会诊。
- 实验或效果：在MIMIC-IV肝病案例上，MedCoRAG在诊断性能和推理可解释性上优于现有方法和闭源模型。

## 摘要（原文）

> Diagnosing hepatic diseases accurately and interpretably is critical, yet it remains challenging in real-world clinical settings. Existing AI approaches for clinical diagnosis often lack transparency, structured reasoning, and deployability. Recent efforts have leveraged large language models (LLMs), retrieval-augmented generation (RAG), and multi-agent collaboration. However, these approaches typically retrieve evidence from a single source and fail to support iterative, role-specialized deliberation grounded in structured clinical data. To address this, we propose MedCoRAG (i.e., Medical Collaborative RAG), an end-to-end framework that generates diagnostic hypotheses from standardized abnormal findings and constructs a patient-specific evidence package by jointly retrieving and pruning UMLS knowledge graph paths and clinical guidelines. It then performs Multi-Agent Collaborative Reasoning: a Router Agent dynamically dispatches Specialist Agents based on case complexity; these agents iteratively reason over the evidence and trigger targeted re-retrievals when needed, while a Generalist Agent synthesizes all deliberations into a traceable consensus diagnosis that emulates multidisciplinary consultation. Experimental results on hepatic disease cases from MIMIC-IV show that MedCoRAG outperforms existing methods and closed-source models in both diagnostic performance and reasoning interpretability.

