---
layout: default
title: Rethinking the Practicality of Vision-language-action Model: A Comprehensive Benchmark and An Improved Baseline
---

# Rethinking the Practicality of Vision-language-action Model: A Comprehensive Benchmark and An Improved Baseline
**arXiv**：[2602.22663v1](https://arxiv.org/abs/2602.22663) · [PDF](https://arxiv.org/pdf/2602.22663.pdf)  
**作者**：Wenxuan Song, Jiayi Chen, Xiaoquan Sun, Huashuo Lei, Yikai Qin, Wei Zhao, Pengxiang Ding, Han Zhao, Tongxin Wang, Pengxu Hou, Zhide Zhong, Haodong Yan, Donglin Wang, Jun Ma, Haoang Li  

**一句话要点**：提出CEBench基准与LLaVA-VLA模型以提升视觉-语言-动作模型的实用性

**关键词**：视觉-语言-动作模型, 机器人基准, 轻量模型, 移动操作, 仿真训练, 端到端学习

## 3 点简述
- 现有VLA模型参数规模大、预训练成本高且适用性有限，阻碍实际部署
- 引入CEBench基准，涵盖仿真与真实世界多样化场景，支持训练与评估
- 设计LLaVA-VLA模型，采用轻量架构与两阶段训练，实现移动操作任务

## 摘要（原文）

> Vision-Language-Action (VLA) models have emerged as a generalist robotic agent. However, existing VLAs are hindered by excessive parameter scales, prohibitive pre-training requirements, and limited applicability to diverse embodiments. To improve the practicality of VLAs, we propose a comprehensive benchmark and an improved baseline. First, we propose CEBench, a new benchmark spanning diverse embodiments in both simulation and the real world with consideration of domain randomization. We collect 14.4k simulated trajectories and 1.6k real-world expert-curated trajectories to support training on CEBench. Second, using CEBench as our testbed, we study three critical aspects of VLAs' practicality and offer several key findings. Informed by these findings, we introduce LLaVA-VLA, a lightweight yet powerful VLA designed for practical deployment on consumer-grade GPUs. Architecturally, it integrates a compact VLM backbone with multi-view perception, proprioceptive tokenization, and action chunking. To eliminate reliance on costly pre-training, LLaVA-VLA adopts a two-stage training paradigm including post-training and fine-tuning. Furthermore, LLaVA-VLA extends the action space to unify navigation and manipulation. Experiments across embodiments demonstrate the capabilities of generalization and versatility of LLaVA-VLA , while real-world mobile manipulation experiments establish it as the first end-to-end VLA model for mobile manipulation. We will open-source all datasets, codes, and checkpoints upon acceptance to foster reproducibility and future research.

