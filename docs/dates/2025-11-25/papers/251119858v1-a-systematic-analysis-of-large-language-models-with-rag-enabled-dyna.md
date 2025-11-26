---
layout: default
title: A Systematic Analysis of Large Language Models with RAG-enabled Dynamic Prompting for Medical Error Detection and Correction
---

# A Systematic Analysis of Large Language Models with RAG-enabled Dynamic Prompting for Medical Error Detection and Correction
**arXiv**：[2511.19858v1](https://arxiv.org/abs/2511.19858) · [PDF](https://arxiv.org/pdf/2511.19858.pdf)  
**作者**：Farzad Ahmed, Joniel Augustine Jerome, Meliha Yetisgen, Özlem Uzuner  

**一句话要点**：提出检索增强动态提示方法以提升医学错误检测与纠正性能

**关键词**：医学错误检测, 检索增强生成, 动态提示, 大型语言模型, 临床文档处理

## 3 点简述
- 临床文档存在事实、诊断和管理错误，可能危害患者安全。
- 比较零样本提示、静态提示和检索增强动态提示在医学错误处理任务中的表现。
- 检索增强动态提示降低假阳性率，提高召回率，生成更准确纠正。

## 摘要（原文）

> Objective: Clinical documentation contains factual, diagnostic, and management errors that can compromise patient safety. Large language models (LLMs) may help detect and correct such errors, but their behavior under different prompting strategies remains unclear. We evaluate zero-shot prompting, static prompting with random exemplars (SPR), and retrieval-augmented dynamic prompting (RDP) for three subtasks of medical error processing: error flag detection, error sentence detection, and error correction.
>   Methods: Using the MEDEC dataset, we evaluated nine instruction-tuned LLMs (GPT, Claude, Gemini, and OpenAI o-series models). We measured performance using accuracy, recall, false-positive rate (FPR), and an aggregate score of ROUGE-1, BLEURT, and BERTScore for error correction. We also analyzed example outputs to identify failure modes and differences between LLM and clinician reasoning.
>   Results: Zero-shot prompting showed low recall in both detection tasks, often missing abbreviation-heavy or atypical errors. SPR improved recall but increased FPR. Across all nine LLMs, RDP reduced FPR by about 15 percent, improved recall by 5 to 10 percent in error sentence detection, and generated more contextually accurate corrections.
>   Conclusion: Across diverse LLMs, RDP outperforms zero-shot and SPR prompting. Using retrieved exemplars improves detection accuracy, reduces false positives, and enhances the reliability of medical error correction.

