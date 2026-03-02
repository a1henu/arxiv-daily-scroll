---
layout: default
title: AudioCapBench: Quick Evaluation on Audio Captioning across Sound, Music, and Speech
---

# AudioCapBench: Quick Evaluation on Audio Captioning across Sound, Music, and Speech
**arXiv**：[2602.23649v1](https://arxiv.org/abs/2602.23649) · [PDF](https://arxiv.org/pdf/2602.23649.pdf)  
**作者**：Jielin Qiu, Jianguo Zhang, Zixiang Chen, Liangwei Yang, Ming Zhu, Juntao Tan, Haolin Chen, Wenting Zhao, Rithesh Murthy, Roshan Ram, Akshara Prabhakar, Shelby Heinecke, Caiming, Xiong, Silvio Savarese, Huan Wang  

**一句话要点**：提出AudioCapBench基准，用于评估大模型在环境声、音乐和语音三个音频领域的字幕生成能力。

**关键词**：音频字幕生成, 多模态基准, LLM评估, 跨领域评估, 大模型评测

## 3 点简述
- 核心问题：缺乏统一基准评估大模型在音频字幕生成中的跨领域表现。
- 方法要点：构建包含1000个样本的基准，结合基于参考的指标和LLM-as-Judge框架进行多维度评估。
- 实验或效果：Gemini模型整体表现更优，所有模型在语音字幕生成上表现最佳，音乐上最差。

## 摘要（原文）

> We introduce AudioCapBench, a benchmark for evaluating audio captioning capabilities of large multimodal models. \method covers three distinct audio domains, including environmental sound, music, and speech, with 1,000 curated evaluation samples drawn from established datasets. We evaluate 13 models across two providers (OpenAI, Google Gemini) using both reference-based metrics (METEOR, BLEU, ROUGE-L) and an LLM-as-Judge framework that scores predictions on three orthogonal dimensions: \textit{accuracy} (semantic correctness), \textit{completeness} (coverage of reference content), and \textit{hallucination} (absence of fabricated content). Our results reveal that Gemini models generally outperform OpenAI models on overall captioning quality, with Gemini~3~Pro achieving the highest overall score (6.00/10), while OpenAI models exhibit lower hallucination rates. All models perform best on speech captioning and worst on music captioning. We release the benchmark as well as evaluation code to facilitate reproducible audio understanding research.

