---
layout: default
title: QEDBENCH: Quantifying the Alignment Gap in Automated Evaluation of University-Level Mathematical Proofs
---

# QEDBENCH: Quantifying the Alignment Gap in Automated Evaluation of University-Level Mathematical Proofs
**arXiv**：[2602.20629v1](https://arxiv.org/abs/2602.20629) · [PDF](https://arxiv.org/pdf/2602.20629.pdf)  
**作者**：Santiago Gonzalez, Alireza Amiri Bavandpour, Peter Ye, Edward Zhang, Ruslans Aleksejevs, Todor Antić, Polina Baron, Sujeet Bhalerao, Shubhrajit Bhattacharya, Zachary Burton, John Byrne, Hyungjun Choi, Nujhat Ahmed Disha, Koppany István Encz, Yuchen Fang, Robert Joseph George, Ebrahim Ghorbani, Alan Goldfarb, Jing Guo, Meghal Gupta, Stefano Huber, Annika Kanckos, Minjung Kang, Hyun Jong Kim, Dino Lorenzini, Levi Lorenzo, Tianyi Mao, Giovanni Marzenta, Ariane M. Masuda, Lukas Mauth, Ana Mickovic, Andres Miniguano-Trujillo, Antoine Moulin, Wenqi Ni, Tomos Parry, Kevin Ren, Hossein Roodbarani, Mathieu Rundström, Manjil Saikia, Detchat Samart, Rebecca Steiner, Connor Stewart, Dhara Thakkar, Jeffrey Tse, Vasiliki Velona, Yunhai Xiang, Sibel Yalçın, Jun Yan, Ji Zeng, Arman Cohan, Quanquan C. Liu  

**一句话要点**：提出QEDBench基准以量化大学数学证明自动评估中的对齐差距

**关键词**：自动评估对齐, 数学证明评估, LLM评判者, 双标准基准, 离散数学推理

## 3 点简述
- 核心问题：LLM作为评判者在大学数学证明评估中存在系统性对齐差距
- 方法要点：引入双标准对齐基准，对比课程特定标准与专家常识标准
- 实验或效果：揭示前沿评估模型存在显著正偏差，并发现离散领域推理差距

## 摘要（原文）

> As Large Language Models (LLMs) saturate elementary benchmarks, the research frontier has shifted from generation to the reliability of automated evaluation. We demonstrate that standard "LLM-as-a-Judge" protocols suffer from a systematic Alignment Gap when applied to upper-undergraduate to early graduate level mathematics. To quantify this, we introduce QEDBench, the first large-scale dual-rubric alignment benchmark to systematically measure alignment with human experts on university-level math proofs by contrasting course-specific rubrics against expert common knowledge criteria. By deploying a dual-evaluation matrix (7 judges x 5 solvers) against 1,000+ hours of human evaluation, we reveal that certain frontier evaluators like Claude Opus 4.5, DeepSeek-V3, Qwen 2.5 Max, and Llama 4 Maverick exhibit significant positive bias (up to +0.18, +0.20, +0.30, +0.36 mean score inflation, respectively). Furthermore, we uncover a critical reasoning gap in the discrete domain: while Gemini 3.0 Pro achieves state-of-the-art performance (0.91 average human evaluation score), other reasoning models like GPT-5 Pro and Claude Sonnet 4.5 see their performance significantly degrade in discrete domains. Specifically, their average human evaluation scores drop to 0.72 and 0.63 in Discrete Math, and to 0.74 and 0.50 in Graph Theory. In addition to these research results, we also release QEDBench as a public benchmark for evaluating and improving AI judges. Our benchmark is publicly published at https://github.com/qqliu/Yale-QEDBench.

