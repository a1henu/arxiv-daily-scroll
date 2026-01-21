---
layout: default
title: SWE-Tester: Training Open-Source LLMs for Issue Reproduction in Real-World Repositories
---

# SWE-Tester: Training Open-Source LLMs for Issue Reproduction in Real-World Repositories
**arXiv**：[2601.13713v1](https://arxiv.org/abs/2601.13713) · [PDF](https://arxiv.org/pdf/2601.13713.pdf)  
**作者**：Aditya Bharat Soni, Rajat Ghosh, Vaishnavi Bhargava, Valerie Chen, Debojyoti Dutta  

**一句话要点**：提出SWE-Tester框架，训练开源大语言模型生成软件问题复现测试

**关键词**：软件测试自动化, 问题复现测试生成, 开源大语言模型训练, 数据集构建, 模型微调, 性能评估

## 3 点简述
- 核心问题：现有方法依赖闭源大语言模型，开源模型在软件问题复现测试生成中探索有限
- 方法要点：构建高质量训练数据集，训练不同规模和家族的开源大语言模型
- 实验或效果：在SWT-Bench Verified上，成功率和变更覆盖率分别提升最高10%和21%

## 摘要（原文）

> Software testing is crucial for ensuring the correctness and reliability of software systems. Automated generation of issue reproduction tests from natural language issue descriptions enhances developer productivity by simplifying root cause analysis, promotes test-driven development -- "test first, write code later", and can be used for improving the effectiveness of automated issue resolution systems like coding agents. Existing methods proposed for this task predominantly rely on closed-source LLMs, with limited exploration of open models. To address this, we propose SWE-Tester -- a novel pipeline for training open-source LLMs to generate issue reproduction tests. First, we curate a high-quality training dataset of 41K instances from 2.6K open-source GitHub repositories and use it to train LLMs of varying sizes and families. The fine-tuned models achieve absolute improvements of up to 10\% in success rate and 21\% in change coverage on SWT-Bench Verified. Further analysis shows consistent improvements with increased inference-time compute, more data, and larger models. These results highlight the effectiveness of our framework for advancing open-source LLMs in this domain.

