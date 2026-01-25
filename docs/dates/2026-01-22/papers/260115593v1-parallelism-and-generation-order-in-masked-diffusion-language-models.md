---
layout: default
title: Parallelism and Generation Order in Masked Diffusion Language Models: Limits Today, Potential Tomorrow
---

# Parallelism and Generation Order in Masked Diffusion Language Models: Limits Today, Potential Tomorrow
**arXiv**：[2601.15593v1](https://arxiv.org/abs/2601.15593) · [PDF](https://arxiv.org/pdf/2601.15593.pdf)  
**作者**：Yangyang Zhong, Yanmei Gu, Zhengqing Zang, Xiaomeng Li, Yuqi Ding, Xibei Jia, Yuting Shen, Zhenzhong Lan, Liwang Zhu, Weiping Liu, Junlin Zhou, Haisheng Liu, Zhong Xin Yu, Pengxin Luo, Donglian Qi, Yunfeng Yan, Junbo Zhao  

**一句话要点**：评估掩码扩散语言模型的并行生成与顺序能力，提出生成-编辑范式以提升性能

**关键词**：掩码扩散语言模型, 并行生成, 生成顺序, 自适应解码, 生成-编辑范式

## 3 点简述
- 核心问题：掩码扩散语言模型在并行生成和任意顺序解码方面的实际能力尚不明确
- 方法要点：使用平均最终化并行度和肯德尔τ系数量化模型的并行强度和生成顺序
- 实验或效果：在58个基准测试中，模型表现落后于自回归模型，但展示任务自适应性

## 摘要（原文）

> Masked Diffusion Language Models (MDLMs) promise parallel token generation and arbitrary-order decoding, yet it remains unclear to what extent current models truly realize these capabilities. We characterize MDLM behavior along two dimensions -- parallelism strength and generation order -- using Average Finalization Parallelism (AFP) and Kendall's tau. We evaluate eight mainstream MDLMs (up to 100B parameters) on 58 benchmarks spanning knowledge, reasoning, and programming. The results show that MDLMs still lag behind comparably sized autoregressive models, mainly because parallel probabilistic modeling weakens inter-token dependencies. Meanwhile, MDLMs exhibit adaptive decoding behavior: their parallelism and generation order vary significantly with the task domain, the stage of reasoning, and whether the output is correct. On tasks that require "backward information" (e.g., Sudoku), MDLMs adopt a solution order that tends to fill easier Sudoku blanks first, highlighting their advantages. Finally, we provide theoretical motivation and design insights supporting a Generate-then-Edit paradigm, which mitigates dependency loss while retaining the efficiency of parallel decoding.

