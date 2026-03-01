---
layout: default
title: ContextRL: Enhancing MLLM's Knowledge Discovery Efficiency with Context-Augmented RL
---

# ContextRL: Enhancing MLLM's Knowledge Discovery Efficiency with Context-Augmented RL
**arXiv**：[2602.22623v1](https://arxiv.org/abs/2602.22623) · [PDF](https://arxiv.org/pdf/2602.22623.pdf)  
**作者**：Xingyu Lu, Jinpeng Wang, YiFan Zhang, Shijie Ma, Xiao Hu, Tianke Zhang, Haonan fan, Kaiyu Jiang, Changyi Liu, Kaiyu Tang, Bin Wen, Fan Yang, Tingting Gao, Han Li, Chun Yuan  

**一句话要点**：提出ContextRL框架，通过上下文增强强化学习提升多模态大语言模型的知识发现效率

**关键词**：上下文增强强化学习, 多模态大语言模型, 知识发现效率, 奖励模型优化, 奖励黑客缓解, 多轮采样策略

## 3 点简述
- 核心问题：多模态大语言模型在知识发现中面临可识别性和可达性瓶颈，导致奖励模型准确度低和奖励黑客问题
- 方法要点：引入上下文增强，提供完整参考解决方案以改进可识别性，并采用多轮采样策略生成错误报告以提升可达性
- 实验或效果：在11个感知与推理基准上显著提升效率，使Qwen3-VL-8B模型性能媲美32B模型，大幅超越标准RLVR基线

## 摘要（原文）

> We propose ContextRL, a novel framework that leverages context augmentation to overcome these bottlenecks. Specifically, to enhance Identifiability, we provide the reward model with full reference solutions as context, enabling fine-grained process verification to filter out false positives (samples with the right answer but low-quality reasoning process). To improve Reachability, we introduce a multi-turn sampling strategy where the reward model generates mistake reports for failed attempts, guiding the policy to "recover" correct responses from previously all-negative groups. Experimental results on 11 perception and reasoning benchmarks show that ContextRL significantly improves knowledge discovery efficiency. Notably, ContextRL enables the Qwen3-VL-8B model to achieve performance comparable to the 32B model, outperforming standard RLVR baselines by a large margin while effectively mitigating reward hacking. Our in-depth analysis reveals the significant potential of contextual information for improving reward model accuracy and document the widespread occurrence of reward hacking, offering valuable insights for future RLVR research.

