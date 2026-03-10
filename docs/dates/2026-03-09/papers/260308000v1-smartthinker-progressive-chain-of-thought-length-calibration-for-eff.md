---
layout: default
title: SmartThinker: Progressive Chain-of-Thought Length Calibration for Efficient Large Language Model Reasoning
---

# SmartThinker: Progressive Chain-of-Thought Length Calibration for Efficient Large Language Model Reasoning
**arXiv**：[2603.08000v1](https://arxiv.org/abs/2603.08000) · [PDF](https://arxiv.org/pdf/2603.08000.pdf)  
**作者**：Chenzhi Hu, Qinzhe Hu, Yuhang Xu, Junyi Chen, Ruijie Wang, Shengzhong Liu, Jianxin Li, Fan Wu, Guihai Chen  

**一句话要点**：提出SmartThinker方法，通过渐进式思维链长度校准优化大型推理模型效率

**关键词**：大型推理模型, 思维链优化, 渐进式校准, 长度压缩, GRPO方法, 效率提升

## 3 点简述
- 核心问题：大型推理模型思维链冗长导致冗余和过度思考，现有静态长度奖励设计无法动态适应问题难度和响应分布，造成过度压缩和精度损失。
- 方法要点：基于GRPO，动态估计训练中最佳长度以引导过长响应，并动态调整长度奖励系数避免惩罚正确推理路径。
- 实验或效果：在AIME25等基准上实现最高52.5%平均长度压缩和16.6%精度提升，代码开源。

## 摘要（原文）

> Large reasoning models (LRMs) like OpenAI o1 and DeepSeek-R1 achieve high accuracy on complex tasks by adopting long chain-of-thought (CoT) reasoning paths. However, the inherent verbosity of these processes frequently results in redundancy and overthinking. To address this issue, existing works leverage Group Relative Policy Optimization (GRPO) to reduce LRM output length, but their static length reward design cannot dynamically adapt according to the relative problem difficulty and response length distribution, causing over-compression and compromised accuracy. Therefore, we propose SmartThinker, a novel GRPO-based efficient reasoning method with progressive CoT length calibration. SmartThinker makes a two-fold contribution: First, it dynamically estimates the optimal length with peak accuracy during training and guides overlong responses toward it to reduce response length while sustaining accuracy. Second, it dynamically modulates the length reward coefficient to avoid the unwarranted penalization of correct reasoning paths. Extensive experiment results show that SmartThinker achieves up to 52.5% average length compression with improved accuracy, and achieves up to 16.6% accuracy improvement on challenging benchmarks like AIME25. The source code can be found at https://github.com/SJTU-RTEAS/SmartThinker.

