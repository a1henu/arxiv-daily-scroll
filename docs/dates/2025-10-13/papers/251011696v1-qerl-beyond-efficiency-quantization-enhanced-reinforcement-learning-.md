---
layout: default
title: QeRL: Beyond Efficiency -- Quantization-enhanced Reinforcement Learning for LLMs
---

# QeRL: Beyond Efficiency -- Quantization-enhanced Reinforcement Learning for LLMs
**arXiv**：[2510.11696v1](https://arxiv.org/abs/2510.11696) · [PDF](https://arxiv.org/pdf/2510.11696.pdf)  
**作者**：Wei Huang, Yi Ge, Shuai Yang, Yicheng Xiao, Huizi Mao, Yujun Lin, Hanrong Ye, Sifei Liu, Ka Chun Cheung, Hongxu Yin, Yao Lu, Xiaojuan Qi, Song Han, Yukang Chen  

**一句话要点**：提出QeRL框架，结合量化与强化学习，提升大语言模型训练效率与探索能力。

**关键词**：量化强化学习, 大语言模型训练, 低秩适应, 自适应噪声, GPU效率优化, 数学推理基准

## 3 点简述
- 核心问题：强化学习在大语言模型中资源密集，需高GPU内存和长训练时间。
- 方法要点：结合NVFP4量化和LoRA，引入自适应量化噪声机制，加速训练并增强探索。
- 实验效果：在7B模型上实现1.5倍加速，单GPU训练32B模型，数学基准性能媲美全参数微调。

## 摘要（原文）

> We propose QeRL, a Quantization-enhanced Reinforcement Learning framework for
> large language models (LLMs). While RL is essential for LLMs' reasoning
> capabilities, it is resource-intensive, requiring substantial GPU memory and
> long rollout durations. QeRL addresses these issues by combining NVFP4
> quantization with Low-Rank Adaptation (LoRA), accelerating rollout phase of RL
> while reducing memory overhead. Beyond efficiency, our findings show that
> quantization noise increases policy entropy, enhancing exploration, and
> enabling the discovery of better strategies during RL. To further optimize
> exploration, QeRL introduces an Adaptive Quantization Noise (AQN) mechanism,
> which dynamically adjusts noise during training. Experiments demonstrate that
> QeRL delivers over 1.5 times speedup in the rollout phase. Moreover, this is
> the first framework to enable RL training of a 32B LLM on a single H100 80GB
> GPU, while delivering overall speedups for RL training. It also achieves faster
> reward growth and higher final accuracy than 16-bit LoRA and QLoRA, while
> matching the performance of full-parameter fine-tuning on mathematical
> benchmarks such as GSM8K (90.8%) and MATH 500 (77.4%) in the 7B model. These
> results establish QeRL as an efficient and effective framework for RL training
> in LLMs.

