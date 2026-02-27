---
layout: default
title: Test-Time Scaling with Diffusion Language Models via Reward-Guided Stitching
---

# Test-Time Scaling with Diffusion Language Models via Reward-Guided Stitching
**arXiv**：[2602.22871v1](https://arxiv.org/abs/2602.22871) · [PDF](https://arxiv.org/pdf/2602.22871.pdf)  
**作者**：Roy Miles, Aysim Toker, Andreea-Maria Oncescu, Songcen Xu, Jiankang Deng, Ismail Elezi  

**一句话要点**：提出基于奖励引导拼接的扩散语言模型测试时缩放方法，以提升数学推理性能。

**关键词**：扩散语言模型, 推理聚合, 过程奖励模型, 测试时缩放, 数学推理, 自一致性框架

## 3 点简述
- 核心问题：现有聚合策略丢弃部分或接近正确推理轨迹中的有用中间步骤，限制推理效率。
- 方法要点：使用掩码扩散语言模型采样多样推理轨迹，通过过程奖励模型评分步骤，拼接高质量步骤形成复合推理。
- 实验或效果：在数学和编码任务上平均准确率提升达23.8%，延迟降低达1.8倍，无需训练。

## 摘要（原文）

> Reasoning with large language models often benefits from generating multiple chains-of-thought, but existing aggregation strategies are typically trajectory-level (e.g., selecting the best trace or voting on the final answer), discarding useful intermediate work from partial or "nearly correct" attempts. We propose Stitching Noisy Diffusion Thoughts, a self-consistency framework that turns cheap diffusion-sampled reasoning into a reusable pool of step-level candidates. Given a problem, we (i) sample many diverse, low-cost reasoning trajectories using a masked diffusion language model, (ii) score every intermediate step with an off-the-shelf process reward model (PRM), and (iii) stitch these highest-quality steps across trajectories into a composite rationale. This rationale then conditions an autoregressive (AR) model (solver) to recompute only the final answer. This modular pipeline separates exploration (diffusion) from evaluation and solution synthesis, avoiding monolithic unified hybrids while preserving broad search. Across math reasoning benchmarks, we find that step-level recombination is most beneficial on harder problems, and ablations highlight the importance of the final AR solver in converting stitched but imperfect rationales into accurate answers. Using low-confidence diffusion sampling with parallel, independent rollouts, our training-free framework improves average accuracy by up to 23.8% across six math and coding tasks. At the same time, it achieves up to a 1.8x latency reduction relative to both traditional diffusion models (e.g., Dream, LLaDA) and unified architectures (e.g., TiDAR). Code is available at https://github.com/roymiles/diffusion-stitching.

