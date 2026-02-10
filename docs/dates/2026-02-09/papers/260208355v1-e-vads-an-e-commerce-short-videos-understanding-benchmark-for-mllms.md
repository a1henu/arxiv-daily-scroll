---
layout: default
title: E-VAds: An E-commerce Short Videos Understanding Benchmark for MLLMs
---

# E-VAds: An E-commerce Short Videos Understanding Benchmark for MLLMs
**arXiv**：[2602.08355v1](https://arxiv.org/abs/2602.08355) · [PDF](https://arxiv.org/pdf/2602.08355.pdf)  
**作者**：Xianjie Liu, Yiman Hu, Liang Wu, Ping Hu, Yixiong Zou, Jian Xu, Bo Zheng  

**一句话要点**：提出E-VAds基准和E-VAds-R1模型以解决电商短视频理解中商业意图推理的挑战

**关键词**：电商短视频理解, 多模态基准, 商业意图推理, 强化学习模型, 多粒度奖励设计

## 3 点简述
- 核心问题：现有基准忽视电商短视频的高密度多模态信号和商业意图推理，导致模型性能不足
- 方法要点：引入多模态信息密度评估框架量化复杂度，并构建E-VAds基准包含感知与认知推理任务
- 实验或效果：E-VAds-R1模型通过MG-GRPO奖励设计，在少量样本下实现商业意图推理性能提升109.2%

## 摘要（原文）

> E-commerce short videos represent a high-revenue segment of the online video industry characterized by a goal-driven format and dense multi-modal signals. Current models often struggle with these videos because existing benchmarks focus primarily on general-purpose tasks and neglect the reasoning of commercial intent. In this work, we first propose a \textbf{multi-modal information density assessment framework} to quantify the complexity of this domain. Our evaluation reveals that e-commerce content exhibits substantially higher density across visual, audio, and textual modalities compared to mainstream datasets, establishing a more challenging frontier for video understanding. To address this gap, we introduce \textbf{E-commerce Video Ads Benchmark (E-VAds)}, which is the first benchmark specifically designed for e-commerce short video understanding. We curated 3,961 high-quality videos from Taobao covering a wide range of product categories and used a multi-agent system to generate 19,785 open-ended Q&A pairs. These questions are organized into two primary dimensions, namely Perception and Cognition and Reasoning, which consist of five distinct tasks. Finally, we develop \textbf{E-VAds-R1}, an RL-based reasoning model featuring a multi-grained reward design called \textbf{MG-GRPO}. This strategy provides smooth guidance for early exploration while creating a non-linear incentive for expert-level precision. Experimental results demonstrate that E-VAds-R1 achieves a 109.2% performance gain in commercial intent reasoning with only a few hundred training samples.

