---
layout: default
title: VulnLLM-R: Specialized Reasoning LLM with Agent Scaffold for Vulnerability Detection
---

# VulnLLM-R: Specialized Reasoning LLM with Agent Scaffold for Vulnerability Detection
**arXiv**：[2512.07533v1](https://arxiv.org/abs/2512.07533) · [PDF](https://arxiv.org/pdf/2512.07533.pdf)  
**作者**：Yuzhou Nie, Hongwei Li, Chengquan Guo, Ruizhe Jiang, Zhun Wang, Bo Li, Dawn Song, Wenbo Guo  

**一句话要点**：提出VulnLLM-R，首个专用于漏洞检测的推理大模型，结合代理框架提升实际项目检测能力。

**关键词**：漏洞检测, 推理大模型, 程序状态分析, 代理框架, 零日漏洞, 静态分析

## 3 点简述
- 核心问题：现有推理大模型在漏洞检测中性能有限，或规模过大、闭源，难以泛化。
- 方法要点：通过专门数据选择、生成、过滤与校正，训练70亿参数模型，实现程序状态推理而非简单模式匹配。
- 实验或效果：在Python、C/C++、Java数据集上优于静态分析工具及开源/商业大模型，代理框架在真实项目中超越CodeQL和AFL++，发现零日漏洞。

## 摘要（原文）

> We propose VulnLLM-R, the~\emph{first specialized reasoning LLM} for vulnerability detection. Our key insight is that LLMs can reason about program states and analyze the potential vulnerabilities, rather than simple pattern matching. This can improve the model's generalizability and prevent learning shortcuts. However, SOTA reasoning LLMs are typically ultra-large, closed-source, or have limited performance in vulnerability detection. To address this, we propose a novel training recipe with specialized data selection, reasoning data generation, reasoning data filtering and correction, and testing-phase optimization. Using our proposed methodology, we train a reasoning model with seven billion parameters. Through extensive experiments on SOTA datasets across Python, C/C++, and Java, we show that VulnLLM-R has superior effectiveness and efficiency than SOTA static analysis tools and both open-source and commercial large reasoning models. We further conduct a detailed ablation study to validate the key designs in our training recipe. Finally, we construct an agent scaffold around our model and show that it outperforms CodeQL and AFL++ in real-world projects. Our agent further discovers a set of zero-day vulnerabilities in actively maintained repositories. This work represents a pioneering effort to enable real-world, project-level vulnerability detection using AI agents powered by specialized reasoning models. The code is available at~\href{https://github.com/ucsb-mlsec/VulnLLM-R}{github}.

