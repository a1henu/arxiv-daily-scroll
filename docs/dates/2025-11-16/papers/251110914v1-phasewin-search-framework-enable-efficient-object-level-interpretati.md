---
layout: default
title: PhaseWin Search Framework Enable Efficient Object-Level Interpretation
---

# PhaseWin Search Framework Enable Efficient Object-Level Interpretation
**arXiv**：[2511.10914v1](https://arxiv.org/abs/2511.10914) · [PDF](https://arxiv.org/pdf/2511.10914.pdf)  
**作者**：Zihan Gu, Ruoyu Chen, Junchi Zhang, Yue Hu, Hua Zhang, Xiaochun Cao  

**一句话要点**：提出PhaseWin搜索框架以高效实现对象级基础模型的忠实归因

**关键词**：对象级归因, 子模优化, 高效搜索算法, 视觉基础模型, 计算效率提升

## 3 点简述
- 核心问题：现有子模子集选择方法忠实度高但效率低，阻碍实际部署。
- 方法要点：采用分阶段粗到细搜索，结合自适应剪枝和窗口选择，近似贪婪行为。
- 实验或效果：计算预算仅20%时达到95%以上贪婪忠实度，在检测和视觉定位任务中领先。

## 摘要（原文）

> Attribution is essential for interpreting object-level foundation models. Recent methods based on submodular subset selection have achieved high faithfulness, but their efficiency limitations hinder practical deployment in real-world scenarios. To address this, we propose PhaseWin, a novel phase-window search algorithm that enables faithful region attribution with near-linear complexity. PhaseWin replaces traditional quadratic-cost greedy selection with a phased coarse-to-fine search, combining adaptive pruning, windowed fine-grained selection, and dynamic supervision mechanisms to closely approximate greedy behavior while dramatically reducing model evaluations. Theoretically, PhaseWin retains near-greedy approximation guarantees under mild monotone submodular assumptions. Empirically, PhaseWin achieves over 95% of greedy attribution faithfulness using only 20% of the computational budget, and consistently outperforms other attribution baselines across object detection and visual grounding tasks with Grounding DINO and Florence-2. PhaseWin establishes a new state of the art in scalable, high-faithfulness attribution for object-level multimodal models.

