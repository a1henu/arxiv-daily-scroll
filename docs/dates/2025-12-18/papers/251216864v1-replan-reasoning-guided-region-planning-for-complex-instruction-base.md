---
layout: default
title: RePlan: Reasoning-guided Region Planning for Complex Instruction-based Image Editing
---

# RePlan: Reasoning-guided Region Planning for Complex Instruction-based Image Editing
**arXiv**：[2512.16864v1](https://arxiv.org/abs/2512.16864) · [PDF](https://arxiv.org/pdf/2512.16864.pdf)  
**作者**：Tianyuan Qu, Lei Ke, Xiaohang Zhan, Longxiang Tang, Yuqi Liu, Bohao Peng, Bei Yu, Dong Yu, Jiaya Jia  

**一句话要点**：提出RePlan框架，通过推理引导的区域规划解决复杂指令图像编辑中的视觉-指令复杂度问题。

**关键词**：指令图像编辑, 视觉-指令复杂度, 区域规划, 扩散模型, 强化学习, 注意力注入

## 3 点简述
- 核心问题：现有模型在复杂指令与杂乱场景结合时，编辑精度和保真度不足。
- 方法要点：采用规划-执行框架，先分解指令并定位区域，再通过注意力注入机制进行并行编辑。
- 实验或效果：在IV-Edit基准上优于强基线，提升区域精度和整体保真度，无需大规模训练数据。

## 摘要（原文）

> Instruction-based image editing enables natural-language control over visual modifications, yet existing models falter under Instruction-Visual Complexity (IV-Complexity), where intricate instructions meet cluttered or ambiguous scenes. We introduce RePlan (Region-aligned Planning), a plan-then-execute framework that couples a vision-language planner with a diffusion editor. The planner decomposes instructions via step-by-step reasoning and explicitly grounds them to target regions; the editor then applies changes using a training-free attention-region injection mechanism, enabling precise, parallel multi-region edits without iterative inpainting. To strengthen planning, we apply GRPO-based reinforcement learning using 1K instruction-only examples, yielding substantial gains in reasoning fidelity and format reliability. We further present IV-Edit, a benchmark focused on fine-grained grounding and knowledge-intensive edits. Across IV-Complex settings, RePlan consistently outperforms strong baselines trained on far larger datasets, improving regional precision and overall fidelity. Our project page: https://replan-iv-edit.github.io

