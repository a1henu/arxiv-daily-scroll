---
layout: default
title: T3D: Few-Step Diffusion Language Models via Trajectory Self-Distillation with Direct Discriminative Optimization
---

# T3D: Few-Step Diffusion Language Models via Trajectory Self-Distillation with Direct Discriminative Optimization
**arXiv**：[2602.12262v1](https://arxiv.org/abs/2602.12262) · [PDF](https://arxiv.org/pdf/2602.12262.pdf)  
**作者**：Tunyu Zhang, Xinxi Zhang, Ligong Han, Haizhou Shi, Xiaoxiao He, Zhuowei Li, Hao Wang, Kai Xu, Akash Srivastava, Hao Wang, Vladimir Pavlovic, Dimitris N. Metaxas  

**一句话要点**：提出轨迹自蒸馏框架T3D，结合直接判别优化，提升扩散大语言模型的少步解码效率与质量。

**关键词**：扩散大语言模型, 少步解码, 轨迹自蒸馏, 直接判别优化, 文本生成

## 3 点简述
- 扩散大语言模型少步解码时，生成质量因步数减少而显著下降，影响推理效率。
- 通过轨迹自蒸馏框架，利用模型自身生成轨迹进行蒸馏，并引入直接判别优化以聚焦高概率模式。
- 在严格步数限制下，该方法优于现有少步基线，显著缩小与全步解码的差距。

## 摘要（原文）

> Diffusion large language models (DLLMs) have the potential to enable fast text generation by decoding multiple tokens in parallel. However, in practice, their inference efficiency is constrained by the need for many refinement steps, while aggressively reducing the number of steps leads to a substantial degradation in generation quality. To alleviate this, we propose a trajectory self-distillation framework that improves few-step decoding by distilling the model's own generative trajectories. We incorporate Direct Discriminative Optimization (DDO), a reverse-KL objective that promotes mode-seeking distillation and encourages the student to concentrate on high-probability teacher modes. Across benchmarks, our approach consistently outperforms strong few-step baselines and standard training under tight step budgets. Although full-step decoding remains superior, we substantially narrow the gap, establishing a strong foundation towards practical few-step DLLMs. The source code is available at https://github.com/Tyrion58/T3D.

