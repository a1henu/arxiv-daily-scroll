---
layout: default
title: Generation of Programmatic Rules for Document Forgery Detection Using Large Language Models
---

# Generation of Programmatic Rules for Document Forgery Detection Using Large Language Models
**arXiv**：[2512.19228v1](https://arxiv.org/abs/2512.19228) · [PDF](https://arxiv.org/pdf/2512.19228.pdf)  
**作者**：Valentin Schmidberger, Manuel Eberhardinger, Setareh Maghsudi, Johannes Maucher  

**一句话要点**：提出基于大语言模型微调生成文档伪造检测规则，以自动化规则创建并适应受限硬件。

**关键词**：文档伪造检测, 大语言模型微调, 规则生成, 自动化验证, 受限硬件

## 3 点简述
- 核心问题：文档伪造检测中手动实现规则耗时，需自动化方法。
- 方法要点：微调开源大语言模型于领域特定代码数据，生成可执行规则。
- 实验或效果：模型能生成有效验证程序，支持安全敏感场景的决策。

## 摘要（原文）

> Document forgery poses a growing threat to legal, economic, and governmental processes, requiring increasingly sophisticated verification mechanisms. One approach involves the use of plausibility checks, rule-based procedures that assess the correctness and internal consistency of data, to detect anomalies or signs of manipulation. Although these verification procedures are essential for ensuring data integrity, existing plausibility checks are manually implemented by software engineers, which is time-consuming. Recent advances in code generation with large language models (LLMs) offer new potential for automating and scaling the generation of these checks. However, adapting LLMs to the specific requirements of an unknown domain remains a significant challenge. This work investigates the extent to which LLMs, adapted on domain-specific code and data through different fine-tuning strategies, can generate rule-based plausibility checks for forgery detection on constrained hardware resources. We fine-tune open-source LLMs, Llama 3.1 8B and OpenCoder 8B, on structured datasets derived from real-world application scenarios and evaluate the generated plausibility checks on previously unseen forgery patterns. The results demonstrate that the models are capable of generating executable and effective verification procedures. This also highlights the potential of LLMs as scalable tools to support human decision-making in security-sensitive contexts where comprehensibility is required.

