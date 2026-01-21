---
layout: default
title: CauScientist: Teaching LLMs to Respect Data for Causal Discovery
---

# CauScientist: Teaching LLMs to Respect Data for Causal Discovery
**arXiv**：[2601.13614v1](https://arxiv.org/abs/2601.13614) · [PDF](https://arxiv.org/pdf/2601.13614.pdf)  
**作者**：Bo Peng, Sirui Chen, Lei Xu, Chaochao Lu  

**一句话要点**：提出CauScientist框架，结合LLM与统计验证以提升因果发现准确性

**关键词**：因果发现, 大语言模型, 统计验证, 混合初始化, 迭代优化

## 3 点简述
- 核心问题：现有因果发现方法存在统计不可区分性或依赖未经验证先验，导致结果不可靠。
- 方法要点：采用混合初始化选择起始图，通过LLM生成假设并由统计标准验证，迭代优化结构并维护错误记忆。
- 实验效果：在实验中显著超越纯数据驱动基线，F1分数提升达53.8%，结构汉明距离减少44.0%。

## 摘要（原文）

> Causal discovery is fundamental to scientific understanding and reliable decision-making. Existing approaches face critical limitations: purely data-driven methods suffer from statistical indistinguishability and modeling assumptions, while recent LLM-based methods either ignore statistical evidence or incorporate unverified priors that can mislead result. To this end, we propose CauScientist, a collaborative framework that synergizes LLMs as hypothesis-generating "data scientists" with probabilistic statistics as rigorous "verifiers". CauScientist employs hybrid initialization to select superior starting graphs, iteratively refines structures through LLM-proposed modifications validated by statistical criteria, and maintains error memory to guide efficient search space. Experiments demonstrate that CauScientist substantially outperforms purely data-driven baselines, achieving up to 53.8% F1 score improvement and enhancing recall from 35.0% to 100.0%. Notably, while standalone LLM performance degrades with graph complexity, CauScientist reduces structural hamming distance (SHD) by 44.0% compared to Qwen3-32B on 37-node graphs. Our project page is at https://github.com/OpenCausaLab/CauScientist.

