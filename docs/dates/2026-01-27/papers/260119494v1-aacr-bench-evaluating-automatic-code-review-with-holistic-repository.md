---
layout: default
title: AACR-Bench: Evaluating Automatic Code Review with Holistic Repository-Level Context
---

# AACR-Bench: Evaluating Automatic Code Review with Holistic Repository-Level Context
**arXiv**：[2601.19494v1](https://arxiv.org/abs/2601.19494) · [PDF](https://arxiv.org/pdf/2601.19494.pdf)  
**作者**：Lei Zhang, Yongda Yu, Minghui Yu, Xinxin Guo, Zhengqi Zhuang, Guoping Rong, Dong Shao, Haifeng Shen, Hongyu Kuang, Zhengfeng Li, Boge Wang, Guoan Zhang, Bangyu Xiang, Xiaobing Xu  

**一句话要点**：提出AACR-Bench基准以解决自动代码评审评估中多语言支持不足和标注噪声问题

**关键词**：自动代码评审, 大语言模型评估, 多语言基准, 仓库级上下文, 缺陷检测, AI辅助标注

## 3 点简述
- 现有自动代码评审基准缺乏多语言仓库级上下文，且依赖原始PR评论的噪声标注
- 采用AI辅助专家验证的标注流程，发现更多潜在缺陷，缺陷覆盖率提升285%
- 评估发现上下文粒度、检索方法选择对LLM性能影响显著，且因模型、语言和架构而异

## 摘要（原文）

> High-quality evaluation benchmarks are pivotal for deploying Large Language Models (LLMs) in Automated Code Review (ACR). However, existing benchmarks suffer from two critical limitations: first, the lack of multi-language support in repository-level contexts, which restricts the generalizability of evaluation results; second, the reliance on noisy, incomplete ground truth derived from raw Pull Request (PR) comments, which constrains the scope of issue detection. To address these challenges, we introduce AACR-Bench a comprehensive benchmark that provides full cross-file context across multiple programming languages. Unlike traditional datasets, AACR-Bench employs an "AI-assisted, Expert-verified" annotation pipeline to uncover latent defects often overlooked in original PRs, resulting in a 285\% increase in defect coverage. Extensive evaluations of mainstream LLMs on AACR-Bench reveal that previous assessments may have either misjudged or only partially captured model capabilities due to data limitations. Our work establishes a more rigorous standard for ACR evaluation and offers new insights on LLM based ACR, i.e., the granularity/level of context and the choice of retrieval methods significantly impact ACR performance, and this influence varies depending on the LLM, programming language, and the LLM usage paradigm e.g., whether an Agent architecture is employed. The code, data, and other artifacts of our evaluation set are available at https://github.com/alibaba/aacr-bench .

