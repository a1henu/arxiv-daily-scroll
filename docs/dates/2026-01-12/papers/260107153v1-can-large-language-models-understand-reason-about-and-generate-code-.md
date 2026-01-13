---
layout: default
title: Can Large Language Models Understand, Reason About, and Generate Code-Switched Text?
---

# Can Large Language Models Understand, Reason About, and Generate Code-Switched Text?
**arXiv**：[2601.07153v1](https://arxiv.org/abs/2601.07153) · [PDF](https://arxiv.org/pdf/2601.07153.pdf)  
**作者**：Genta Indra Winata, David Anugraha, Patrick Amadeus Irawan, Anirban Das, Haneul Yoo, Paresh Dashore, Shreyas Kulkarni, Ruochen Zhang, Haruki Sakajo, Frederikus Hudi, Anaelia Ovalle, Syrielle Montariol, Felix Gaschi, Michael Anugraha, Rutuj Ravindra Puranik, Zawad Hayat Ahmed, Adril Putra Merin, Emmanuele Chersoni  

**一句话要点**：提出CodeMixQA基准以评估大语言模型在代码切换文本中的理解、推理与生成能力

**关键词**：代码切换, 大语言模型评估, 多语言基准, 文本生成, 推理分析

## 3 点简述
- 核心问题：大语言模型在多语言代码切换环境下的鲁棒性未知
- 方法要点：构建包含16种语言对变体的高质量人工标注基准CodeMixQA
- 实验或效果：分析模型推理行为并评估生成文本的自然度与语义保真度

## 摘要（原文）

> Code-switching is a pervasive phenomenon in multilingual communication, yet the robustness of large language models (LLMs) in mixed-language settings remains insufficiently understood. In this work, we present a comprehensive evaluation of LLM capabilities in understanding, reasoning over, and generating code-switched text. We introduce CodeMixQA a novel benchmark with high-quality human annotations, comprising 16 diverse parallel code-switched language-pair variants that span multiple geographic regions and code-switching patterns, and include both original scripts and their transliterated forms. Using this benchmark, we analyze the reasoning behavior of LLMs on code-switched question-answering tasks, shedding light on how models process and reason over mixed-language inputs. We further conduct a systematic evaluation of LLM-generated synthetic code-switched text, focusing on both naturalness and semantic fidelity, and uncover key limitations in current generation capabilities. Our findings reveal persistent challenges in both reasoning and generation under code-switching conditions and provide actionable insights for building more robust multilingual LLMs. We release the dataset and code as open source.

