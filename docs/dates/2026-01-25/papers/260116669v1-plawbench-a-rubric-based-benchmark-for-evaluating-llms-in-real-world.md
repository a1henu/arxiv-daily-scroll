---
layout: default
title: PLawBench: A Rubric-Based Benchmark for Evaluating LLMs in Real-World Legal Practice
---

# PLawBench: A Rubric-Based Benchmark for Evaluating LLMs in Real-World Legal Practice
**arXiv**：[2601.16669v1](https://arxiv.org/abs/2601.16669) · [PDF](https://arxiv.org/pdf/2601.16669.pdf)  
**作者**：Yuzhen Shi, Huanghai Liu, Yiran Hu, Gaojie Song, Xinran Xu, Yubo Ma, Tianyi Tang, Li Zhang, Qingjing Chen, Di Feng, Wenbo Lv, Weiheng Wu, Kexin Yang, Sen Yang, Wei Wang, Rongyao Shi, Yuanyang Qiu, Yuemeng Qi, Jingwen Zhang, Xiaoyu Sui, Yifan Chen, Yi Zhang, An Yang, Bowen Yu, Dayiheng Liu, Junyang Lin, Weixing Shen, Bing Zhao, Charles L. A. Clarke, Hu Wei  

**一句话要点**：提出PLawBench基准以评估大语言模型在真实法律实践中的能力

**关键词**：法律大语言模型评估, 真实法律实践基准, 细粒度法律推理, 专家评估细则, 大语言模型评测

## 3 点简述
- 现有法律基准任务简化，无法反映真实法律实践的模糊性和复杂性
- PLawBench基于真实法律工作流，包含三类任务和专家设计的评估细则
- 实验评估10个先进大语言模型，显示其在细粒度法律推理方面存在显著局限

## 摘要（原文）

> As large language models (LLMs) are increasingly applied to legal domain-specific tasks, evaluating their ability to perform legal work in real-world settings has become essential. However, existing legal benchmarks rely on simplified and highly standardized tasks, failing to capture the ambiguity, complexity, and reasoning demands of real legal practice. Moreover, prior evaluations often adopt coarse, single-dimensional metrics and do not explicitly assess fine-grained legal reasoning. To address these limitations, we introduce PLawBench, a Practical Law Benchmark designed to evaluate LLMs in realistic legal practice scenarios. Grounded in real-world legal workflows, PLawBench models the core processes of legal practitioners through three task categories: public legal consultation, practical case analysis, and legal document generation. These tasks assess a model's ability to identify legal issues and key facts, perform structured legal reasoning, and generate legally coherent documents. PLawBench comprises 850 questions across 13 practical legal scenarios, with each question accompanied by expert-designed evaluation rubrics, resulting in approximately 12,500 rubric items for fine-grained assessment. Using an LLM-based evaluator aligned with human expert judgments, we evaluate 10 state-of-the-art LLMs. Experimental results show that none achieves strong performance on PLawBench, revealing substantial limitations in the fine-grained legal reasoning capabilities of current LLMs and highlighting important directions for future evaluation and development of legal LLMs. Data is available at: https://github.com/skylenage/PLawbench.

