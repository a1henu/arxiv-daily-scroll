---
layout: default
title: Thinking with Images as Continuous Actions: Numerical Visual Chain-of-Thought
---

# Thinking with Images as Continuous Actions: Numerical Visual Chain-of-Thought
**arXiv**：[2602.23959v1](https://arxiv.org/abs/2602.23959) · [PDF](https://arxiv.org/pdf/2602.23959.pdf)  
**作者**：Kesen Zhao, Beier Zhu, Junbao Zhou, Xingyu Zhu, Zhongqi Yue, Hanwang Zhang  

**一句话要点**：提出数值视觉思维链以解决多模态大语言模型中视觉推理的模态不匹配和区域定位精度问题。

**关键词**：多模态大语言模型, 视觉推理, 连续动作空间, 边界框坐标, 强化学习, 监督微调

## 3 点简述
- 现有视觉思维链方法存在模态不匹配或区域选择精度限制，影响多模态大语言模型的视觉推理能力。
- NV-CoT通过将动作空间扩展到连续欧几里得空间，使模型能直接生成边界框坐标，仅需最小架构修改。
- 实验表明，该方法在三个基准测试中显著提升定位精度和答案准确性，并加速训练收敛。

## 摘要（原文）

> Recent multimodal large language models (MLLMs) increasingly rely on visual chain-of-thought to perform region-grounded reasoning over images. However, existing approaches ground regions via either textified coordinates-causing modality mismatch and semantic fragmentation or fixed-granularity patches that both limit precise region selection and often require non-trivial architectural changes. In this paper, we propose Numerical Visual Chain-of-Thought (NV-CoT), a framework that enables MLLMs to reason over images using continuous numerical coordinates. NV-CoT expands the MLLM action space from discrete vocabulary tokens to a continuous Euclidean space, allowing models to directly generate bounding-box coordinates as actions with only minimal architectural modification. The framework supports both supervised fine-tuning and reinforcement learning. In particular, we replace categorical token policies with a Gaussian (or Laplace) policy over coordinates and introduce stochasticity via reparameterized sampling, making NV-CoT fully compatible with GRPO-style policy optimization. Extensive experiments on three benchmarks against eight representative visual reasoning baselines demonstrate that NV-CoT significantly improves localization precision and final answer accuracy, while also accelerating training convergence, validating the effectiveness of continuous-action visual reasoning in MLLMs. The code is available in https://github.com/kesenzhao/NV-CoT.

