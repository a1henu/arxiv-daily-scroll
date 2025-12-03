---
layout: default
title: Cross-Lingual Prompt Steerability: Towards Accurate and Robust LLM Behavior across Languages
---

# Cross-Lingual Prompt Steerability: Towards Accurate and Robust LLM Behavior across Languages
**arXiv**：[2512.02841v1](https://arxiv.org/abs/2512.02841) · [PDF](https://arxiv.org/pdf/2512.02841.pdf)  
**作者**：Lechen Zhang, Yusheng Zhou, Tolga Ergen, Lajanugen Logeswaran, Moontae Lee, David Jurgens  

**一句话要点**：提出跨语言提示优化框架以提升多语言LLM的准确性和鲁棒性

**关键词**：跨语言提示引导, 多语言LLM评估, 提示优化框架, 系统提示, 推理模式分析, 语言切换减少

## 3 点简述
- 研究系统提示在多语言环境中如何引导LLM行为，聚焦跨语言可靠性的核心问题
- 开发统一四维评估框架和提示优化方法，自动发现提升性能的提示
- 通过大规模实验验证优化提示能改善指标5-10%，并分析推理模式变化

## 摘要（原文）

> System prompts provide a lightweight yet powerful mechanism for conditioning large language models (LLMs) at inference time. While prior work has focused on English-only settings, real-world deployments benefit from having a single prompt to operate reliably across languages. This paper presents a comprehensive study of how different system prompts steer models toward accurate and robust cross-lingual behavior. We propose a unified four-dimensional evaluation framework to assess system prompts in multilingual environments. Through large-scale experiments on five languages, three LLMs, and three benchmarks, we uncover that certain prompt components, such as CoT, emotion, and scenario, correlate with robust multilingual behavior. We develop a prompt optimization framework for multilingual settings and show it can automatically discover prompts that improve all metrics by 5-10%. Finally, we analyze over 10 million reasoning units and find that more performant system prompts induce more structured and consistent reasoning patterns, while reducing unnecessary language-switching. Together, we highlight system prompt optimization as a scalable path to accurate and robust multilingual LLM behavior.

