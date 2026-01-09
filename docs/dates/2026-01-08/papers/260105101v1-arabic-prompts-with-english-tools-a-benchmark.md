---
layout: default
title: Arabic Prompts with English Tools: A Benchmark
---

# Arabic Prompts with English Tools: A Benchmark
**arXiv**：[2601.05101v1](https://arxiv.org/abs/2601.05101) · [PDF](https://arxiv.org/pdf/2601.05101.pdf)  
**作者**：Konstantin Kubrak, Ahmed El-Moselhy, Ammar Alsulami, Remaz Altuwaim, Hassan Ismail Fawaz, Faisal Alsaby  

**一句话要点**：提出首个阿拉伯语工具调用基准，揭示阿拉伯语提示下LLM性能下降5-10%。

**关键词**：阿拉伯语大语言模型, 工具调用基准, 代理能力评估, 多语言AI, 功能准确性, 语言公平性

## 3 点简述
- 核心问题：阿拉伯语LLM工具调用评估缺乏基准，现有框架多聚焦英语。
- 方法要点：构建标准化框架，评估阿拉伯语代理工作流的功能准确性和鲁棒性。
- 实验或效果：发现阿拉伯语交互时工具调用准确率平均下降5-10%，与工具描述语言无关。

## 摘要（原文）

> Large Language Models (LLMs) are now integral to numerous industries, increasingly serving as the core reasoning engine for autonomous agents that perform complex tasks through tool-use. While the development of Arabic-native LLMs is accelerating, the benchmarks for evaluating their capabilities lag behind, with most existing frameworks focusing on English. A critical and overlooked area is tool-calling, where the performance of models prompted in non-English languages like Arabic is poorly understood, especially since these models are often pretrained on predominantly English data. This paper addresses this critical gap by introducing the first dedicated benchmark for evaluating the tool-calling and agentic capabilities of LLMs in the Arabic language. Our work provides a standardized framework to measure the functional accuracy and robustness of models in Arabic agentic workflows. Our findings reveal a huge performance gap: when users interact in Arabic, tool-calling accuracy drops by an average of 5-10\%, regardless of whether the tool descriptions themselves are in Arabic or English. By shedding light on these critical challenges, this benchmark aims to foster the development of more reliable and linguistically equitable AI agents for Arabic-speaking users.

