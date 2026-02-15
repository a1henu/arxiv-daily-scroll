---
layout: default
title: It's TIME: Towards the Next Generation of Time Series Forecasting Benchmarks
---

# It's TIME: Towards the Next Generation of Time Series Forecasting Benchmarks
**arXiv**：[2602.12147v1](https://arxiv.org/abs/2602.12147) · [PDF](https://arxiv.org/pdf/2602.12147.pdf)  
**作者**：Zhongzheng Qiao, Sheng Pan, Anni Wang, Viktoriya Zhukova, Yong Liu, Xudong Jiang, Qingsong Wen, Mingsheng Long, Ming Jin, Chenghao Liu  

**一句话要点**：提出TIME基准以解决时间序列预测基准在数据、任务和评估方面的局限性

**关键词**：时间序列预测基准, 零样本评估, 模式级评估, 人机协同管道, 多粒度排行榜

## 3 点简述
- 现有基准存在数据陈旧、质量不足、任务脱离实际和评估视角僵化等问题
- TIME包含50个新数据集和98个任务，采用人机协同管道确保数据完整性，并基于真实需求定义任务
- 提出模式级评估视角，评估12个模型并建立多粒度排行榜，提供可泛化的模型能力分析

## 摘要（原文）

> Time series foundation models (TSFMs) are revolutionizing the forecasting landscape from specific dataset modeling to generalizable task evaluation. However, we contend that existing benchmarks exhibit common limitations in four dimensions: constrained data composition dominated by reused legacy sources, compromised data integrity lacking rigorous quality assurance, misaligned task formulations detached from real-world contexts, and rigid analysis perspectives that obscure generalizable insights. To bridge these gaps, we introduce TIME, a next-generation task-centric benchmark comprising 50 fresh datasets and 98 forecasting tasks, tailored for strict zero-shot TSFM evaluation free from data leakage. Integrating large language models and human expertise, we establish a rigorous human-in-the-loop benchmark construction pipeline to ensure high data integrity and redefine task formulation by aligning forecasting configurations with real-world operational requirements and variate predictability. Furthermore, we propose a novel pattern-level evaluation perspective that moves beyond traditional dataset-level evaluations based on static meta labels. By leveraging structural time series features to characterize intrinsic temporal properties, this approach offers generalizable insights into model capabilities across diverse patterns. We evaluate 12 representative TSFMs and establish a multi-granular leaderboard to facilitate in-depth analysis and visualized inspection. The leaderboard is available at https://huggingface.co/spaces/Real-TSF/TIME-leaderboard.

