---
layout: default
title: A Systematic Study of Code Obfuscation Against LLM-based Vulnerability Detection
---

# A Systematic Study of Code Obfuscation Against LLM-based Vulnerability Detection
**arXiv**：[2512.16538v1](https://arxiv.org/abs/2512.16538) · [PDF](https://arxiv.org/pdf/2512.16538.pdf)  
**作者**：Xiao Li, Yue Li, Hao Wu, Yue Zhang, Yechao Zhang, Fengyuan Xu, Sheng Zhong  

**一句话要点**：系统研究代码混淆对基于LLM的漏洞检测的影响，评估其正负效应

**关键词**：代码混淆, 漏洞检测, 大语言模型, 系统评估, 编程语言

## 3 点简述
- 核心问题：LLM在漏洞检测中的可靠性受代码混淆影响，缺乏系统评估。
- 方法要点：将混淆技术分为布局、数据流、控制流三类，统一框架实现于四种编程语言。
- 实验或效果：评估15个LLM和两个编码代理，揭示混淆导致性能提升或下降的条件。

## 摘要（原文）

> As large language models (LLMs) are increasingly adopted for code vulnerability detection, their reliability and robustness across diverse vulnerability types have become a pressing concern. In traditional adversarial settings, code obfuscation has long been used as a general strategy to bypass auditing tools, preserving exploitability without tampering with the tools themselves. Numerous efforts have explored obfuscation methods and tools, yet their capabilities differ in terms of supported techniques, granularity, and programming languages, making it difficult to systematically assess their impact on LLM-based vulnerability detection. To address this gap, we provide a structured systematization of obfuscation techniques and evaluate them under a unified framework. Specifically, we categorize existing obfuscation methods into three major classes (layout, data flow, and control flow) covering 11 subcategories and 19 concrete techniques. We implement these techniques across four programming languages (Solidity, C, C++, and Python) using a consistent LLM-driven approach, and evaluate their effects on 15 LLMs spanning four model families (DeepSeek, OpenAI, Qwen, and LLaMA), as well as on two coding agents (GitHub Copilot and Codex). Our findings reveal both positive and negative impacts of code obfuscation on LLM-based vulnerability detection, highlighting conditions under which obfuscation leads to performance improvements or degradations. We further analyze these outcomes with respect to vulnerability characteristics, code properties, and model attributes. Finally, we outline several open problems and propose future directions to enhance the robustness of LLMs for real-world vulnerability detection.

