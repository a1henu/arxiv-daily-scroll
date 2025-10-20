---
layout: default
title: Paper2Web: Let's Make Your Paper Alive!
---

# Paper2Web: Let's Make Your Paper Alive!
**arXiv**：[2510.15842v1](https://arxiv.org/abs/2510.15842) · [PDF](https://arxiv.org/pdf/2510.15842.pdf)  
**作者**：Yuhang Chen, Tianpeng Lv, Siyi Zhang, Yixiang Yin, Yao Wan, Philip S. Yu, Dongping Chen  

**一句话要点**：提出Paper2Web基准和PWAgent管道，以生成交互式学术网页。

**关键词**：学术网页生成, 基准评估, 交互式设计, LLM评估, 自主代理

## 3 点简述
- 当前学术网页生成方法难以实现布局感知和交互，缺乏全面评估框架。
- 引入基准数据集和多维评估，包括规则指标和LLM-as-a-Judge。
- PWAgent通过迭代优化内容和布局，在实验中显著优于基线方法。

## 摘要（原文）

> Academic project websites can more effectively disseminate research when they
> clearly present core content and enable intuitive navigation and interaction.
> However, current approaches such as direct Large Language Model (LLM)
> generation, templates, or direct HTML conversion struggle to produce
> layout-aware, interactive sites, and a comprehensive evaluation suite for this
> task has been lacking. In this paper, we introduce Paper2Web, a benchmark
> dataset and multi-dimensional evaluation framework for assessing academic
> webpage generation. It incorporates rule-based metrics like Connectivity,
> Completeness and human-verified LLM-as-a-Judge (covering interactivity,
> aesthetics, and informativeness), and PaperQuiz, which measures paper-level
> knowledge retention. We further present PWAgent, an autonomous pipeline that
> converts scientific papers into interactive and multimedia-rich academic
> homepages. The agent iteratively refines both content and layout through MCP
> tools that enhance emphasis, balance, and presentation quality. Our experiments
> show that PWAgent consistently outperforms end-to-end baselines like
> template-based webpages and arXiv/alphaXiv versions by a large margin while
> maintaining low cost, achieving the Pareto-front in academic webpage
> generation.

