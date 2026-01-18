---
layout: default
title: MathDoc: Benchmarking Structured Extraction and Active Refusal on Noisy Mathematics Exam Papers
---

# MathDoc: Benchmarking Structured Extraction and Active Refusal on Noisy Mathematics Exam Papers
**arXiv**：[2601.10104v1](https://arxiv.org/abs/2601.10104) · [PDF](https://arxiv.org/pdf/2601.10104.pdf)  
**作者**：Chenyue Zhou, Jiayi Tuo, Shitong Qin, Wei Dai, Mingxuan Wang, Ziwei Zhao, Duoyang Li, Shiyang Su, Yanxi Lu, Yanbiao Ma  

**一句话要点**：提出MathDoc基准以解决真实数学试卷结构化提取和主动拒绝能力评估问题

**关键词**：文档级信息提取, 数学试卷基准, 主动拒绝能力, 视觉噪声, 多模态大语言模型, 结构化问题提取

## 3 点简述
- 核心问题：真实数学试卷因视觉噪声导致结构化提取困难，现有基准忽略结构完整性和主动拒绝能力
- 方法要点：构建首个包含真实噪声和不可识别样本的文档级数学试卷基准，提出多维度评估框架
- 实验或效果：SOTA模型提取性能强但无法拒绝不可读输入，揭示模型可靠性差距

## 摘要（原文）

> The automated extraction of structured questions from paper-based mathematics exams is fundamental to intelligent education, yet remains challenging in real-world settings due to severe visual noise. Existing benchmarks mainly focus on clean documents or generic layout analysis, overlooking both the structural integrity of mathematical problems and the ability of models to actively reject incomplete inputs. We introduce MathDoc, the first benchmark for document-level information extraction from authentic high school mathematics exam papers. MathDoc contains \textbf{3,609} carefully curated questions with real-world artifacts and explicitly includes unrecognizable samples to evaluate active refusal behavior. We propose a multi-dimensional evaluation framework covering stem accuracy, visual similarity, and refusal capability. Experiments on SOTA MLLMs, including Qwen3-VL and Gemini-2.5-Pro, show that although end-to-end models achieve strong extraction performance, they consistently fail to refuse illegible inputs, instead producing confident but invalid outputs. These results highlight a critical gap in current MLLMs and establish MathDoc as a benchmark for assessing model reliability under degraded document conditions. Our project repository is available at \href{https://github.com/winnk123/papers/tree/master}{GitHub repository}

