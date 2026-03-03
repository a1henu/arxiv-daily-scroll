---
layout: default
title: SafeSci: Safety Evaluation of Large Language Models in Science Domains and Beyond
---

# SafeSci: Safety Evaluation of Large Language Models in Science Domains and Beyond
**arXiv**：[2603.01589v1](https://arxiv.org/abs/2603.01589) · [PDF](https://arxiv.org/pdf/2603.01589.pdf)  
**作者**：Xiangyang Zhu, Yuan Tian, Qi Jia, Kaiwei Zhang, Zicheng Zhang, Chunyi Li, Kaiyuan Ji, Dongrui Liu, Zijian Chen, Lu Sun, Renrui Zhang, Yan Teng, Jing Shao, Wei Sun, Xia Hu, Yu Qiao, Guangtao Zhai  

**一句话要点**：提出SafeSci框架以评估和增强科学领域大语言模型的安全性

**关键词**：大语言模型安全评估, 科学领域安全基准, 安全对齐增强, 客观评估指标, 多学科数据集

## 3 点简述
- 现有科学安全基准风险覆盖有限且依赖主观评估，存在不足
- SafeSci包含多学科基准SafeSciBench和大规模训练集SafeSciTrain，采用客观指标
- 评估24个先进模型揭示漏洞，微调SafeSciTrain显著提升安全对齐

## 摘要（原文）

> The success of large language models (LLMs) in scientific domains has heightened safety concerns, prompting numerous benchmarks to evaluate their scientific safety. Existing benchmarks often suffer from limited risk coverage and a reliance on subjective evaluation. To address these problems, we introduce SafeSci, a comprehensive framework for safety evaluation and enhancement in scientific contexts. SafeSci comprises SafeSciBench, a multi-disciplinary benchmark with 0.25M samples, and SafeSciTrain, a large-scale dataset containing 1.5M samples for safety enhancement. SafeSciBench distinguishes between safety knowledge and risk to cover extensive scopes and employs objective metrics such as deterministically answerable questions to mitigate evaluation bias. We evaluate 24 advanced LLMs, revealing critical vulnerabilities in current models. We also observe that LLMs exhibit varying degrees of excessive refusal behaviors on safety-related issues. For safety enhancement, we demonstrate that fine-tuning on SafeSciTrain significantly enhances the safety alignment of models. Finally, we argue that knowledge is a double-edged sword, and determining the safety of a scientific question should depend on specific context, rather than universally categorizing it as safe or unsafe. Our work provides both a diagnostic tool and a practical resource for building safer scientific AI systems.

