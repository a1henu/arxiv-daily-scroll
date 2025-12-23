---
layout: default
title: Efficient Jailbreak Mitigation Using Semantic Linear Classification in a Multi-Staged Pipeline
---

# Efficient Jailbreak Mitigation Using Semantic Linear Classification in a Multi-Staged Pipeline
**arXiv**：[2512.19011v1](https://arxiv.org/abs/2512.19011) · [PDF](https://arxiv.org/pdf/2512.19011.pdf)  
**作者**：Akshaj Prashanth Rao, Advait Singh, Saumya Kumaar Saksena, Dhruv Kumar  

**一句话要点**：提出基于语义线性分类的多阶段防御架构，以高效缓解LLM的提示注入与越狱攻击。

**关键词**：提示注入防御, 越狱攻击缓解, 线性SVM分类, 多阶段管道, 语义过滤, LLM安全

## 3 点简述
- 核心问题：提示注入和越狱攻击对LLM系统构成持续安全威胁，需高效防御。
- 方法要点：采用轻量级多阶段管道，核心为基于文本归一化、TF-IDF和线性SVM的语义过滤器。
- 实验或效果：在超过30,000个标记提示上评估，准确率达93.4%，延迟降低10倍以上。

## 摘要（原文）

> Prompt injection and jailbreaking attacks pose persistent security challenges to large language model (LLM)-based systems. We present an efficient and systematically evaluated defense architecture that mitigates these threats through a lightweight, multi-stage pipeline. Its core component is a semantic filter based on text normalization, TF-IDF representations, and a Linear SVM classifier. Despite its simplicity, this module achieves 93.4% accuracy and 96.5% specificity on held-out data, substantially reducing attack throughput while incurring negligible computational overhead.
>   Building on this efficient foundation, the full pipeline integrates complementary detection and mitigation mechanisms that operate at successive stages, providing strong robustness with minimal latency. In comparative experiments, our SVM-based configuration improves overall accuracy from 35.1% to 93.4% while reducing average time to completion from approximately 450s to 47s, yielding over 10 times lower latency than ShieldGemma. These results demonstrate that the proposed design simultaneously advances defensive precision and efficiency, addressing a core limitation of current model-based moderators.
>   Evaluation across a curated corpus of over 30,000 labeled prompts, including benign, jailbreak, and application-layer injections, confirms that staged, resource-efficient defenses can robustly secure modern LLM-driven applications.

