---
layout: default
title: SAGE: Steerable Agentic Data Generation for Deep Search with Execution Feedback
---

# SAGE: Steerable Agentic Data Generation for Deep Search with Execution Feedback
**arXiv**：[2601.18202v1](https://arxiv.org/abs/2601.18202) · [PDF](https://arxiv.org/pdf/2601.18202.pdf)  
**作者**：Fangyuan Xu, Rujun Han, Yanfei Chen, Zifeng Wang, I-Hung Hsu, Jun Yan, Vishy Tirumalashetty, Eunsol Choi, Tomas Pfister, Chen-Yu Lee  

**一句话要点**：提出SAGE以自动生成高质量、难度可控的深度搜索问答对，用于训练深度搜索代理。

**关键词**：深度搜索代理, 数据生成, 问答对生成, 执行反馈, 难度控制, 合成数据训练

## 3 点简述
- 核心问题：深度搜索代理训练需昂贵人工标注，因探索轨迹长且复杂。
- 方法要点：SAGE通过数据生成器和搜索代理多轮交互，迭代优化问答对至目标难度。
- 实验或效果：合成数据训练代理在基准测试中提升性能达23%，并能适应不同检索环境。

## 摘要（原文）

> Deep search agents, which aim to answer complex questions requiring reasoning across multiple documents, can significantly speed up the information-seeking process. Collecting human annotations for this application is prohibitively expensive due to long and complex exploration trajectories. We propose an agentic pipeline that automatically generates high quality, difficulty-controlled deep search question-answer pairs for a given corpus and a target difficulty level. Our pipeline, SAGE, consists of a data generator which proposes QA pairs and a search agent which attempts to solve the generated question and provide execution feedback for the data generator. The two components interact over multiple rounds to iteratively refine the question-answer pairs until they satisfy the target difficulty level. Our intrinsic evaluation shows SAGE generates questions that require diverse reasoning strategies, while significantly increases the correctness and difficulty of the generated data. Our extrinsic evaluation demonstrates up to 23% relative performance gain on popular deep search benchmarks by training deep search agents with our synthetic data. Additional experiments show that agents trained on our data can adapt from fixed-corpus retrieval to Google Search at inference time, without further training.

