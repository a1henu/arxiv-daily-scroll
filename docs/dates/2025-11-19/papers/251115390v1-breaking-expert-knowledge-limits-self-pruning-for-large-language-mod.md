---
layout: default
title: Breaking Expert Knowledge Limits: Self-Pruning for Large Language Models
---

# Breaking Expert Knowledge Limits: Self-Pruning for Large Language Models
**arXiv**：[2511.15390v1](https://arxiv.org/abs/2511.15390) · [PDF](https://arxiv.org/pdf/2511.15390.pdf)  
**作者**：Haidong Kang, Lihong Lin, Enneng Yang, Hongning Dai, Hao Wang  

**一句话要点**：提出AutoPrune方法，使大语言模型自动设计剪枝算法以解决专家依赖和性能下降问题

**关键词**：大语言模型剪枝, 自动算法设计, 图驱动思维链, 动态稀疏分配, 离群值问题

## 3 点简述
- 核心问题：大语言模型剪枝依赖专家知识，且高剪枝比下因离群值问题导致性能下降
- 方法要点：利用图驱动思维链优化提示，使模型自动生成剪枝算法，并引入偏态感知动态稀疏分配
- 实验或效果：在主流基准测试中表现优于现有方法，代码已开源

## 摘要（原文）

> Large language models (LLMs) have achieved remarkable performance on a wide range of tasks, hindering real-world deployment due to their massive size. Existing pruning methods (e.g., Wanda) tailored for LLMs rely heavily on manual design pruning algorithms, thereby leading to \textit{huge labor costs} and \textit{requires expert knowledge}. Furthermore, we are the first to identify the serious \textit{outlier value issue} behind dramatic performance degradation under high pruning ratios that are caused by uniform sparsity, raising an additional concern about how to design adaptive pruning sparsity ideal for LLMs. Can LLMs prune by themselves? In this work, we introduce an affirmative answer by proposing a novel pruning method called \textbf{AutoPrune}, which first overcomes expert knowledge limits by leveraging LLMs to design optimal pruning algorithms for themselves automatically without any expert knowledge. Specifically, to mitigate the black-box nature of LLMs, we propose a Graph-driven Chain-of-Thought (GCoT) to optimize prompts, significantly enhancing the reasoning process in learning the pruning algorithm and enabling us to generate pruning algorithms with superior performance and interpretability in the next generation. Finally, grounded in insights of outlier value issue, we introduce Skew-aware Dynamic Sparsity Allocation (SDSA) to overcome the outlier value issue, mitigating performance degradation under high pruning ratios. We conduct extensive experiments on mainstream LLMs benchmarks, demonstrating the superiority of AutoPrune, which consistently excels state-of-the-art competitors. The code is available at: https://anonymous.4open.science/r/AutoPrune.

