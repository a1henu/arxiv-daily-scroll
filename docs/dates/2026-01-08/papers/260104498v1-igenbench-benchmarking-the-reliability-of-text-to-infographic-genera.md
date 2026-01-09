---
layout: default
title: IGenBench: Benchmarking the Reliability of Text-to-Infographic Generation
---

# IGenBench: Benchmarking the Reliability of Text-to-Infographic Generation
**arXiv**：[2601.04498v1](https://arxiv.org/abs/2601.04498) · [PDF](https://arxiv.org/pdf/2601.04498.pdf)  
**作者**：Yinghao Tang, Xueding Liu, Boyuan Zhang, Tingfeng Lan, Yupeng Xie, Jiale Lao, Yiyao Wang, Haoxuan Li, Tingting Gao, Bo Pan, Luoxuan Weng, Xiuqi Huang, Minfeng Zhu, Yingchaojie Feng, Yuyu Luo, Wei Chen  

**一句话要点**：提出IGenBench基准以评估文本到信息图生成的可靠性

**关键词**：文本到信息图生成, 可靠性基准, 多模态评估, 自动化验证, 数据可视化

## 3 点简述
- 核心问题：文本到图像模型生成信息图时存在可靠性问题，如数据编码失真或文本错误
- 方法要点：设计自动化评估框架，将可靠性验证分解为基于10类问题的原子是/否问题，使用多模态大语言模型进行验证
- 实验或效果：评估10个先进模型，揭示性能分层、数据相关维度为瓶颈，以及端到端正确性挑战

## 摘要（原文）

> Infographics are composite visual artifacts that combine data visualizations with textual and illustrative elements to communicate information. While recent text-to-image (T2I) models can generate aesthetically appealing images, their reliability in generating infographics remains unclear. Generated infographics may appear correct at first glance but contain easily overlooked issues, such as distorted data encoding or incorrect textual content. We present IGENBENCH, the first benchmark for evaluating the reliability of text-to-infographic generation, comprising 600 curated test cases spanning 30 infographic types. We design an automated evaluation framework that decomposes reliability verification into atomic yes/no questions based on a taxonomy of 10 question types. We employ multimodal large language models (MLLMs) to verify each question, yielding question-level accuracy (Q-ACC) and infographic-level accuracy (I-ACC). We comprehensively evaluate 10 state-of-the-art T2I models on IGENBENCH. Our systematic analysis reveals key insights for future model development: (i) a three-tier performance hierarchy with the top model achieving Q-ACC of 0.90 but I-ACC of only 0.49; (ii) data-related dimensions emerging as universal bottlenecks (e.g., Data Completeness: 0.21); and (iii) the challenge of achieving end-to-end correctness across all models. We release IGENBENCH at https://igen-bench.vercel.app/.

