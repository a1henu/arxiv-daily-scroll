---
layout: default
title: Video-Thinker: Sparking "Thinking with Videos" via Reinforcement Learning
---

# Video-Thinker: Sparking "Thinking with Videos" via Reinforcement Learning
**arXiv**：[2510.23473v1](https://arxiv.org/abs/2510.23473) · [PDF](https://arxiv.org/pdf/2510.23473.pdf)  
**作者**：Shijian Wang, Jiarui Jin, Xingjian Wang, Linxin Song, Runhao Fu, Hecheng Wang, Zongyuan Ge, Yuan Lu, Xuelian Cheng  

**一句话要点**：提出Video-Thinker，通过强化学习实现多模态大语言模型在视频推理中自主思考

**关键词**：视频推理, 多模态大语言模型, 强化学习, 自主工具使用, 链式思维推理

## 3 点简述
- 核心问题：视频推理中缺乏动态推理范式，无法自主利用模型能力生成推理线索
- 方法要点：构建Video-Thinker-10K数据集，结合监督微调和GRPO强化训练，实现自主工具使用
- 实验或效果：在多个视频推理基准上显著超越基线，7B模型达到最优性能

## 摘要（原文）

> Recent advances in image reasoning methods, particularly "Thinking with
> Images", have demonstrated remarkable success in Multimodal Large Language
> Models (MLLMs); however, this dynamic reasoning paradigm has not yet been
> extended to video reasoning tasks. In this paper, we propose Video-Thinker,
> which empowers MLLMs to think with videos by autonomously leveraging their
> intrinsic "grounding" and "captioning" capabilities to generate reasoning clues
> throughout the inference process. To spark this capability, we construct
> Video-Thinker-10K, a curated dataset featuring autonomous tool usage within
> chain-of-thought reasoning sequences. Our training strategy begins with
> Supervised Fine-Tuning (SFT) to learn the reasoning format, followed by Group
> Relative Policy Optimization (GRPO) to strengthen this reasoning capability.
> Through this approach, Video-Thinker enables MLLMs to autonomously navigate
> grounding and captioning tasks for video reasoning, eliminating the need for
> constructing and calling external tools. Extensive experiments demonstrate that
> Video-Thinker achieves significant performance gains on both in-domain tasks
> and challenging out-of-domain video reasoning benchmarks, including
> Video-Holmes, CG-Bench-Reasoning, and VRBench. Our Video-Thinker-7B
> substantially outperforms existing baselines such as Video-R1 and establishes
> state-of-the-art performance among 7B-sized MLLMs.

