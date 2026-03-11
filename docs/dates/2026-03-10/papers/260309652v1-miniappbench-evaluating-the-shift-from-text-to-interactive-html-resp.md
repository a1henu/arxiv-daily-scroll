---
layout: default
title: MiniAppBench: Evaluating the Shift from Text to Interactive HTML Responses in LLM-Powered Assistants
---

# MiniAppBench: Evaluating the Shift from Text to Interactive HTML Responses in LLM-Powered Assistants
**arXiv**：[2603.09652v1](https://arxiv.org/abs/2603.09652) · [PDF](https://arxiv.org/pdf/2603.09652.pdf)  
**作者**：Zuhao Zhang, Chengyue Yu, Yuante Li, Chenyi Zhuang, Linjian Mo, Shuai Li  

**一句话要点**：提出MiniAppBench基准以评估LLM从文本转向交互式HTML应用生成的能力

**关键词**：交互式应用生成, 大语言模型评估, HTML代码生成, 浏览器自动化测试, 基准构建

## 3 点简述
- 核心问题：现有基准无法评估LLM生成原则驱动交互应用的能力
- 方法要点：构建包含500任务的基准，并开发基于浏览器自动化的评估框架MiniAppEval
- 实验或效果：实验显示当前LLM生成高质量MiniApp仍面临挑战，MiniAppEval与人类判断高度一致

## 摘要（原文）

> With the rapid advancement of Large Language Models (LLMs) in code generation, human-AI interaction is evolving from static text responses to dynamic, interactive HTML-based applications, which we term MiniApps. These applications require models to not only render visual interfaces but also construct customized interaction logic that adheres to real-world principles. However, existing benchmarks primarily focus on algorithmic correctness or static layout reconstruction, failing to capture the capabilities required for this new paradigm. To address this gap, we introduce MiniAppBench, the first comprehensive benchmark designed to evaluate principle-driven, interactive application generation. Sourced from a real-world application with 10M+ generations, MiniAppBench distills 500 tasks across six domains (e.g., Games, Science, and Tools). Furthermore, to tackle the challenge of evaluating open-ended interactions where no single ground truth exists, we propose MiniAppEval, an agentic evaluation framework. Leveraging browser automation, it performs human-like exploratory testing to systematically assess applications across three dimensions: Intention, Static, and Dynamic. Our experiments reveal that current LLMs still face significant challenges in generating high-quality MiniApps, while MiniAppEval demonstrates high alignment with human judgment, establishing a reliable standard for future research. Our code is available in github.com/MiniAppBench.

