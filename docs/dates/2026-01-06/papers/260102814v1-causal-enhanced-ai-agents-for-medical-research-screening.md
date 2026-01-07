---
layout: default
title: Causal-Enhanced AI Agents for Medical Research Screening
---

# Causal-Enhanced AI Agents for Medical Research Screening
**arXiv**：[2601.02814v1](https://arxiv.org/abs/2601.02814) · [PDF](https://arxiv.org/pdf/2601.02814.pdf)  
**作者**：Duc Ngo, Arya Rahgoza  

**一句话要点**：提出因果图增强的检索增强生成系统，以解决医学系统综述中AI幻觉问题

**关键词**：因果推理, 检索增强生成, 医学系统综述, 知识图谱, AI幻觉, 可解释AI

## 3 点简述
- 核心问题：医学系统综述中AI模型存在幻觉，错误率影响患者护理，需高可靠性方法
- 方法要点：集成因果推理与双层知识图，实施证据优先协议，自动生成干预-结果路径图
- 实验或效果：在234篇痴呆运动摘要评估中，准确率达95%，检索成功率100%，零幻觉

## 摘要（原文）

> Systematic reviews are essential for evidence-based medicine, but reviewing 1.5 million+ annual publications manually is infeasible. Current AI approaches suffer from hallucinations in systematic review tasks, with studies reporting rates ranging from 28--40% for earlier models to 2--15% for modern implementations which is unacceptable when errors impact patient care.
>   We present a causal graph-enhanced retrieval-augmented generation system integrating explicit causal reasoning with dual-level knowledge graphs. Our approach enforces evidence-first protocols where every causal claim traces to retrieved literature and automatically generates directed acyclic graphs visualizing intervention-outcome pathways.
>   Evaluation on 234 dementia exercise abstracts shows CausalAgent achieves 95% accuracy, 100% retrieval success, and zero hallucinations versus 34% accuracy and 10% hallucinations for baseline AI. Automatic causal graphs enable explicit mechanism modeling, visual synthesis, and enhanced interpretability. While this proof-of-concept evaluation used ten questions focused on dementia exercise research, the architectural approach demonstrates transferable principles for trustworthy medical AI and causal reasoning's potential for high-stakes healthcare.

