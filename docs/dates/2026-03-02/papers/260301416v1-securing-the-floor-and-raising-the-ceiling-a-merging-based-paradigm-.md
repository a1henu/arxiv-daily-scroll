---
layout: default
title: Securing the Floor and Raising the Ceiling: A Merging-based Paradigm for Multi-modal Search Agents
---

# Securing the Floor and Raising the Ceiling: A Merging-based Paradigm for Multi-modal Search Agents
**arXiv**：[2603.01416v1](https://arxiv.org/abs/2603.01416) · [PDF](https://arxiv.org/pdf/2603.01416.pdf)  
**作者**：Zhixiang Wang, Jingxuan Xu, Dajun Chen, Yunfang Wu, Wei Jiang, Yong Li  

**一句话要点**：提出基于模型合并的无训练范式，通过OBM算法提升多模态搜索代理性能

**关键词**：多模态搜索代理, 模型合并, 最优大脑合并, 零样本学习, 跨模态集成

## 3 点简述
- 现有方法依赖大规模监督轨迹或强化学习，导致高成本和不稳定性
- 采用跨模态模型合并，无需额外多模态训练数据即可组合搜索能力
- OBM算法基于校准样本识别关键参数，在基准测试中实现零样本和热启动优势

## 摘要（原文）

> Recent advances in Vision-Language Models (VLMs) have motivated the development of multi-modal search agents that can actively invoke external search tools and integrate retrieved evidence through multi-step reasoning. While promising, existing approaches typically rely on large-scale supervised trajectories or expensive reinforcement learning (RL), leading to high training cost, instability, and a severe cold-start problem for standard VLMs. We propose a training-free paradigm to empower VLMs with autonomous search capabilities via cross-modal model merging. By fusing a text-based search agent with a base VLM, we show that multi-modal search capabilities can be effectively composed without any additional multi-modal training data. To mitigate parameter interference during cross-modal integration, we introduce Optimal Brain Merging (OBM), a saliency-aware merging algorithm that identifies task-critical parameters based on their impact on model loss using only a small set of calibration samples. Extensive experiments on search-intensive benchmarks (e.g., InfoSeek, MMSearch) reveal that: (1) Model merging secures a reasonable performance floor as a zero-shot agent, with OBM achieving superior search rates; (2) OBM significantly raises the performance ceiling as a warm-start strategy, achieving faster convergence and higher peak accuracy than standard VLM initialization.

