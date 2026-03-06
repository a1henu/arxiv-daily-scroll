---
layout: default
title: Med-V1: Small Language Models for Zero-shot and Scalable Biomedical Evidence Attribution
---

# Med-V1: Small Language Models for Zero-shot and Scalable Biomedical Evidence Attribution
**arXiv**：[2603.05308v1](https://arxiv.org/abs/2603.05308) · [PDF](https://arxiv.org/pdf/2603.05308.pdf)  
**作者**：Qiao Jin, Yin Fang, Lauren He, Yifan Yang, Guangzhi Xiong, Zhizheng Wang, Nicholas Wan, Joey Chan, Donald C. Comeau, Robert Leaman, Charalampos S. Floudas, Aidong Zhang, Michael F. Chiang, Yifan Peng, Zhiyong Lu  

**一句话要点**：提出Med-V1小语言模型，用于高效且可扩展的生物医学证据归因与验证任务。

**关键词**：生物医学证据归因, 小语言模型, 幻觉检测, 声明验证, 合成数据训练, 临床指南分析

## 3 点简述
- 核心问题：评估文章是否支持断言对幻觉检测和声明验证至关重要，但现有大型语言模型部署成本高。
- 方法要点：开发仅30亿参数的Med-V1模型，基于高质量合成数据训练，统一五个生物医学基准为验证格式。
- 实验或效果：Med-V1在基准上显著超越基础模型，性能媲美前沿LLMs，并应用于量化幻觉和识别临床指南误归因。

## 摘要（原文）

> Assessing whether an article supports an assertion is essential for hallucination detection and claim verification. While large language models (LLMs) have the potential to automate this task, achieving strong performance requires frontier models such as GPT-5 that are prohibitively expensive to deploy at scale. To efficiently perform biomedical evidence attribution, we present Med-V1, a family of small language models with only three billion parameters. Trained on high-quality synthetic data newly developed in this study, Med-V1 substantially outperforms (+27.0% to +71.3%) its base models on five biomedical benchmarks unified into a verification format. Despite its smaller size, Med-V1 performs comparably to frontier LLMs such as GPT-5, along with high-quality explanations for its predictions. We use Med-V1 to conduct a first-of-its-kind use case study that quantifies hallucinations in LLM-generated answers under different citation instructions. Results show that the format instruction strongly affects citation validity and hallucination, with GPT-5 generating more claims but exhibiting hallucination rates similar to GPT-4o. Additionally, we present a second use case showing that Med-V1 can automatically identify high-stakes evidence misattributions in clinical practice guidelines, revealing potentially negative public health impacts that are otherwise challenging to identify at scale. Overall, Med-V1 provides an efficient and accurate lightweight alternative to frontier LLMs for practical and real-world applications in biomedical evidence attribution and verification tasks. Med-V1 is available at https://github.com/ncbi-nlp/Med-V1.

