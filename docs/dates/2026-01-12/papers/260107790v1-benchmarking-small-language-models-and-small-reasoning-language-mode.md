---
layout: default
title: Benchmarking Small Language Models and Small Reasoning Language Models on System Log Severity Classification
---

# Benchmarking Small Language Models and Small Reasoning Language Models on System Log Severity Classification
**arXiv**：[2601.07790v1](https://arxiv.org/abs/2601.07790) · [PDF](https://arxiv.org/pdf/2601.07790.pdf)  
**作者**：Yahya Masri, Emily Ma, Zifu Wang, Joseph Rogers, Chaowei Yang  

**一句话要点**：提出系统日志严重性分类作为基准，评估小型语言模型在实时部署中的理解能力与效率。

**关键词**：系统日志分类, 小型语言模型, 检索增强生成, 实时部署, 数字孪生系统

## 3 点简述
- 核心问题：系统日志规模大且复杂，严重性分类作为独立任务价值有限，需作为模型理解能力的基准。
- 方法要点：使用真实Linux日志数据，在零样本、少样本和检索增强生成提示下评估九种小型语言模型。
- 实验或效果：Qwen3-4B在RAG下准确率最高达95.64%，而某些推理模型与RAG结合时性能下降，效率差异显著。

## 摘要（原文）

> System logs are crucial for monitoring and diagnosing modern computing infrastructure, but their scale and complexity require reliable and efficient automated interpretation. Since severity levels are predefined metadata in system log messages, having a model merely classify them offers limited standalone practical value, revealing little about its underlying ability to interpret system logs. We argue that severity classification is more informative when treated as a benchmark for probing runtime log comprehension rather than as an end task. Using real-world journalctl data from Linux production servers, we evaluate nine small language models (SLMs) and small reasoning language models (SRLMs) under zero-shot, few-shot, and retrieval-augmented generation (RAG) prompting. The results reveal strong stratification. Qwen3-4B achieves the highest accuracy at 95.64% with RAG, while Gemma3-1B improves from 20.25% under few-shot prompting to 85.28% with RAG. Notably, the tiny Qwen3-0.6B reaches 88.12% accuracy despite weak performance without retrieval. In contrast, several SRLMs, including Qwen3-1.7B and DeepSeek-R1-Distill-Qwen-1.5B, degrade substantially when paired with RAG. Efficiency measurements further separate models: most Gemma and Llama variants complete inference in under 1.2 seconds per log, whereas Phi-4-Mini-Reasoning exceeds 228 seconds per log while achieving <10% accuracy. These findings suggest that (1) architectural design, (2) training objectives, and (3) the ability to integrate retrieved context under strict output constraints jointly determine performance. By emphasizing small, deployable models, this benchmark aligns with real-time requirements of digital twin (DT) systems and shows that severity classification serves as a lens for evaluating model competence and real-time deployability, with implications for root cause analysis (RCA) and broader DT integration.

