---
layout: default
title: Automatic Replication of LLM Mistakes in Medical Conversations
---

# Automatic Replication of LLM Mistakes in Medical Conversations
**arXiv**：[2512.20983v1](https://arxiv.org/abs/2512.20983) · [PDF](https://arxiv.org/pdf/2512.20983.pdf)  
**作者**：Oleksii Proniakin, Diego Fajardo, Ruslan Nazarenko, Razvan Marinescu  

**一句话要点**：提出MedMistake自动管道以复制LLM在医疗对话中的错误并构建基准

**关键词**：医疗对话评估, 错误复制, 基准构建, LLM自动管道, 单次QA对

## 3 点简述
- 核心问题：LLM在临床评估中错误难以跨模型自动复制，需手动处理。
- 方法要点：通过LLM模拟医患对话，多维度评估提取错误，转化为单次QA对基准。
- 实验或效果：发布包含3390个QA对的数据集，验证12个前沿LLM，GPT、Claude和Grok表现最佳。

## 摘要（原文）

> Large language models (LLMs) are increasingly evaluated in clinical settings using multi-dimensional rubrics which quantify reasoning quality, safety, and patient-centeredness. Yet, replicating specific mistakes in other LLM models is not straightforward and often requires manual effort. We introduce MedMistake, an automatic pipeline that extracts mistakes LLMs make in patient-doctor conversations and converts them into a benchmark of single-shot QA pairs. Our pipeline (1) creates complex, conversational data between an LLM patient and LLM doctor, (2) runs an evaluation with a committee of 2 LLM judges across a variety of dimensions and (3) creates simplified single-shot QA scenarios from those mistakes. We release MedMistake-All, a dataset of 3,390 single-shot QA pairs where GPT-5 and Gemini 2.5 Pro are currently failing to answer correctly, as judged by two LLM judges. We used medical experts to validate a subset of 211/3390 questions (MedMistake-Bench), which we used to run a final evaluation of 12 frontier LLMs: Claude Opus 4.5, Claude Sonnet 4.5, DeepSeek-Chat, Gemini 2.5 Pro, Gemini 3 Pro, GPT-4o, GPT-5, GPT-5.1, GPT-5.2, Grok 4, Grok 4.1, Mistral Large. We found that GPT models, Claude and Grok obtained the best performance on MedMistake-Bench. We release both the doctor-validated benchmark (MedMistake-Bench), as well as the full dataset (MedMistake-All) at https://huggingface.co/datasets/TheLumos/MedicalMistakeBenchmark.

