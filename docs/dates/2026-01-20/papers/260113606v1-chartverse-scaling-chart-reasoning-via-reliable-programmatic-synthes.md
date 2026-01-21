---
layout: default
title: ChartVerse: Scaling Chart Reasoning via Reliable Programmatic Synthesis from Scratch
---

# ChartVerse: Scaling Chart Reasoning via Reliable Programmatic Synthesis from Scratch
**arXiv**：[2601.13606v1](https://arxiv.org/abs/2601.13606) · [PDF](https://arxiv.org/pdf/2601.13606.pdf)  
**作者**：Zheng Liu, Honglin Lin, Chonghan Qin, Xiaoyang Wang, Xin Gao, Yu Li, Mengzhang Cai, Yun Zhu, Zhanping Zhong, Qizhi Pei, Zhuoshi Pan, Xiaoran Shang, Bin Cui, Conghui He, Wentao Zhang, Lijun Wu  

**一句话要点**：提出ChartVerse框架，通过程序化合成复杂图表和可靠推理数据以解决图表推理训练数据不足问题。

**关键词**：图表推理, 程序化合成, 视觉语言模型, 数据生成, 复杂度量化, 问答对验证

## 3 点简述
- 核心问题：开源视觉语言模型缺乏高质量图表推理训练数据，现有数据集图表简单且问答对易产生幻觉。
- 方法要点：引入Rollout Posterior Entropy量化图表复杂度，开发复杂度感知图表编码器合成高复杂度图表；采用答案优先范式生成可靠问答对，并进行一致性验证。
- 实验或效果：ChartVerse-8B在实验中达到最先进性能，超越其教师模型并媲美更强模型。

## 摘要（原文）

> Chart reasoning is a critical capability for Vision Language Models (VLMs). However, the development of open-source models is severely hindered by the lack of high-quality training data. Existing datasets suffer from a dual challenge: synthetic charts are often simplistic and repetitive, while the associated QA pairs are prone to hallucinations and lack the reasoning depth required for complex tasks. To bridge this gap, we propose ChartVerse, a scalable framework designed to synthesize complex charts and reliable reasoning data from scratch. (1) To address the bottleneck of simple patterns, we first introduce Rollout Posterior Entropy (RPE), a novel metric that quantifies chart complexity. Guided by RPE, we develop complexity-aware chart coder to autonomously synthesize diverse, high-complexity charts via executable programs. (2) To guarantee reasoning rigor, we develop truth-anchored inverse QA synthesis. Diverging from standard generation, we adopt an answer-first paradigm: we extract deterministic answers directly from the source code, generate questions conditional on these anchors, and enforce strict consistency verification. To further elevate difficulty and reasoning depth, we filter samples based on model fail-rate and distill high-quality Chain-of-Thought (CoT) reasoning. We curate ChartVerse-SFT-600K and ChartVerse-RL-40K using Qwen3-VL-30B-A3B-Thinking as the teacher. Experimental results demonstrate that ChartVerse-8B achieves state-of-the-art performance, notably surpassing its teacher and rivaling the stronger Qwen3-VL-32B-Thinking.

