---
layout: default
title: OralGPT-Plus: Learning to Use Visual Tools via Reinforcement Learning for Panoramic X-ray Analysis
---

# OralGPT-Plus: Learning to Use Visual Tools via Reinforcement Learning for Panoramic X-ray Analysis
**arXiv**：[2603.06366v1](https://arxiv.org/abs/2603.06366) · [PDF](https://arxiv.org/pdf/2603.06366.pdf)  
**作者**：Yuxuan Fan, Jing Hao, Hong Chen, Jiahao Bao, Yihua Shao, Yuci Liang, Kuo Feng Hung, Hao Tang  

**一句话要点**：提出OralGPT-Plus，通过强化学习实现全景牙科X光片的交互式对称感知诊断推理

**关键词**：全景牙科X光分析, 视觉语言模型, 强化学习, 对称感知推理, 临床诊断基准

## 3 点简述
- 核心问题：现有视觉语言模型静态单次推理限制全景牙科X光片临床可靠性，需细粒度空间推理和对称理解。
- 方法要点：构建DentalProbe数据集和Reinspection-driven强化学习框架，支持迭代检查和对称比较。
- 实验或效果：在MMOral-X基准上优于基线，验证交互式对称推理的有效性。

## 摘要（原文）

> Panoramic dental radiographs require fine-grained spatial reasoning, bilateral symmetry understanding, and multi-step diagnostic verification, yet existing vision-language models operate under a static single-pass paradigm that limits their clinical reliability. In this paper, we introduce OralGPT-Plus, an agentic vision-language model designed to perform iterative and symmetry-aware diagnostic reasoning for panoramic dental radiograph analysis. To support this paradigm, we construct DentalProbe, a five-thousand-image dataset with expert-curated diagnostic trajectories that provide structured supervision for localized inspection and contralateral comparison. We further develop a Reinspection-driven reinforcement learning framework that encourages clinically meaningful re-examination and stabilizes long-horizon reasoning with rubric-based reward and conditioned diagnostic-driven reward. In parallel, we present MMOral-X, the first benchmark for holistic panoramic diagnosis, containing 300 open-ended questions and region-level annotations across multiple difficulty levels. OralGPT-Plus demonstrates consistent and reliable improvements over strong baselines on MMOral-X and established panoramic benchmarks, indicating the effectiveness of interactive and symmetry-informed reasoning. Our work highlights the value of agentic modeling for dental imaging and provides a foundation for future research in clinically aligned panoramic radiograph analysis.

