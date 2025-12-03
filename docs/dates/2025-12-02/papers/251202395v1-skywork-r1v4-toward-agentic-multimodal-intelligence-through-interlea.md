---
layout: default
title: Skywork-R1V4: Toward Agentic Multimodal Intelligence through Interleaved Thinking with Images and DeepResearch
---

# Skywork-R1V4: Toward Agentic Multimodal Intelligence through Interleaved Thinking with Images and DeepResearch
**arXiv**：[2512.02395v1](https://arxiv.org/abs/2512.02395) · [PDF](https://arxiv.org/pdf/2512.02395.pdf)  
**作者**：Yifan Zhang, Liang Hu, Haofeng Sun, Peiyu Wang, Yichen Wei, Shukang Yin, Jiangbo Pei, Wei Shen, Peng Xia, Yi Peng, Tianyidan Xie, Eric Li, Yang Liu, Xuchen Song, Yahui Zhou  

**一句话要点**：提出Skywork-R1V4，通过图像与深度搜索的交错推理实现代理式多模态智能

**关键词**：多模态代理系统, 交错推理, 监督微调, 图像操作, 深度搜索, 长时程规划

## 3 点简述
- 现有方法将图像操作与网络搜索分离，依赖强化学习且缺乏基于工具执行轨迹的规划
- Skywork-R1V4统一多模态规划、主动图像操作和深度搜索，通过监督微调训练
- 在MMSearch和FVQA基准上取得最优结果，无需强化学习即可实现长时程推理

## 摘要（原文）

> Despite recent progress in multimodal agentic systems, existing approaches often treat image manipulation and web search as disjoint capabilities, rely heavily on costly reinforcement learning, and lack planning grounded in real tool-execution traces. To address these limitations, we present Skywork-R1V4, a 30B (A3B) parameter multimodal agentic model that unifies multimodal planning, active image manipulation ("thinking with images"), deep multimodal search, and, most critically, interleaved reasoning that dynamically alternates between visual operations and external knowledge retrieval. Trained solely via supervised fine-tuning on fewer than 30,000 high-quality, planning-execution-consistent trajectories and validated through stepwise consistency filtering, Skywork-R1V4 achieves state-of-the-art results across perception and multimodal search benchmarks: it scores 66.1 on MMSearch and 67.2 on FVQA, surpassing Gemini 2.5 Flash on all 11 metrics. Skywork-R1V4 exhibits emergent long-horizon reasoning at inference time, successfully orchestrating more than 10 tool calls to solve complex, multi-step tasks. Our results demonstrate that sophisticated agentic multimodal intelligence can be achieved through carefully curated supervised learning alone, without any reliance on reinforcement learning.

